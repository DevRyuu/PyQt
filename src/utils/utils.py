import os
import platform
import cv2 as cv
import numpy as np
import shutil
from openpyxl import Workbook

PLATFORM = platform.system()

from PySide6.QtCore import Qt, QPointF
from PySide6.QtWidgets import QMessageBox, QFileDialog, QProgressDialog
from PySide6.QtGui import QImage

from superpoint_superglue_deployment import Matcher
from loguru import logger

bands = ['청색광', '녹색광', '적색광', '적변광', '근적외선']
image_path = None
band_list = []
sorted_band_list = []

def check_directory(dir):
    imageDir = os.path.join(dir, "image")
    tempDir = os.path.join(dir, "temp")
    resultDir = os.path.join(dir, "result")

    dir_list = [imageDir, tempDir, resultDir]
    
    for directory in dir_list:
        if not os.path.exists(directory):
            os.makedirs(directory)

    return imageDir, tempDir, resultDir

def check_project_directory(idir, rdir):
    for root, dirs, files in os.walk(idir):
        for dirname in list(dirs):
            full_dir_path = os.path.join(root, dirname)
            if not os.listdir(full_dir_path):
                os.rmdir(full_dir_path)

    for root, dirs, files in os.walk(rdir):
        for dirname in list(dirs):
            full_dir_path = os.path.join(root, dirname)
            if not os.listdir(full_dir_path):
                os.rmdir(full_dir_path)

    subdirs = [name for name in os.listdir(idir) if os.path.isdir(os.path.join(idir, name))]

    if not subdirs:
        max_dir = "0000"
    else:
        max_dir = max(subdirs)

    new_dir_number = str(int(max_dir) + 1).zfill(4)
    
    inputDir = os.path.join(idir, new_dir_number)
    outputDir = os.path.join(rdir, new_dir_number)
    if not os.path.exists(inputDir):
        os.mkdir(inputDir)
    if not os.path.exists(outputDir):
        os.mkdir(outputDir)

    return inputDir, outputDir

def clear_temp_directory(temp_dir):
    for file in os.listdir(temp_dir):
        try:
            file_path = os.path.join(temp_dir, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Error deleting {file}: {str(e)}")

def clear_empty_directory(dir):
    for root, dirs, files in os.walk(dir):
        for dirname in list(dirs):
            full_dir_path = os.path.join(root, dirname)
            if not os.listdir(full_dir_path):
                os.rmdir(full_dir_path)

    subdirs = [name for name in os.listdir(dir) if os.path.isdir(os.path.join(dir, name))]

    if not subdirs:
        max_dir = "0000"
    else:
        max_dir = max(subdirs)

    inputDir = os.path.join(dir, max_dir)
    outputDir = os.path.join(inputDir.replace("image", "result"))

    return inputDir, outputDir

def simple_alert(app, title, content):
    msg_box = QMessageBox(app)
    msg_box.setWindowTitle(title)
    msg_box.setText(content)
    msg_box.setIcon(QMessageBox.Icon.Information)
    msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
    current_size = msg_box.size()
    new_size = current_size * 4
    msg_box.setFixedSize(new_size)
    msg_box.move(app.geometry().center() - msg_box.rect().center())
    msg_box.setWindowModality(Qt.WindowModality.ApplicationModal)

    msg_box.exec()

def yesorno_alert(app, title, content):
    msg_box = QMessageBox(app)
    msg_box.setWindowTitle(title)
    msg_box.setText(content)
    msg_box.setIcon(QMessageBox.Icon.Information)
    current_size = msg_box.size()
    new_size = current_size * 4
    msg_box.setFixedSize(new_size)
    msg_box.move(app.geometry().center() - msg_box.rect().center())
    msg_box.setWindowModality(Qt.WindowModality.ApplicationModal)

    # 기능 버튼 추가 (추가종류 DestructiveRole, ActionRole, ApplyRole, ResetRole)
    button_1 = msg_box.addButton('아니요', QMessageBox.ButtonRole.ActionRole)
    button_2 = msg_box.addButton('예', QMessageBox.ButtonRole.ActionRole)
    
    msg_box.exec()

    clicked_button = msg_box.clickedButton()
    if clicked_button == button_1:
        return 'no'
    elif clicked_button == button_2:
        return 'yes'
    else:
        return None

def get_path(dir):
    global image_path
    dialog = QFileDialog()
    dialog.setDirectory(dir)
    dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
    dialog.setNameFilter('Image Files (*.png *.jpg *.jpeg *.tif *.tiff *.raw)')
    if dialog.exec() == QFileDialog.DialogCode.Accepted:
        paths = dialog.selectedFiles()
        if paths:
            full = paths[0]
            dir_name, file_all = os.path.split(full)
            file, extension = os.path.splitext(file_all)

    return full, dir_name, file, extension

def get_color_image(path):
    arr = np.fromfile(path, np.uint8)
    image = cv.imdecode(arr, cv.IMREAD_COLOR)
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    return image

def numpy_to_qimage(image):
    height, width = image.shape[:2]

    # BufferError: memoryview: underlying buffer is not C-contiguou
    image = np.ascontiguousarray(image)

    bytes_per_line = image.strides[0]
    if image.ndim == 3:  # 컬러 이미지
        if image.shape[2] == 3:  # BGR 채널 순서
            qimage = QImage(image.data, width, height, bytes_per_line, QImage.Format.Format_RGB888)
        elif image.shape[2] == 4:  # BGRA 채널 순서
            qimage = QImage(image.data, width, height, bytes_per_line, QImage.Format.Format_RGBA8888)
        else:
            raise ValueError("지원하지 않는 이미지 형식입니다.")
    elif image.ndim == 2:  # 흑백 이미지
        qimage = QImage(image.data, width, height, bytes_per_line, QImage.Format.Format_Grayscale8)
    else:
        raise ValueError("지원하지 않는 이미지 형식입니다.")

    return height, width, qimage

def calculate_distribution(image):
    image = image[image > 0]
    mean = np.around(np.mean(image), decimals=3)
    median = int(np.median(np.sort(image)))
    hist, _ = np.histogram(image, bins=256, range=[0, 256])
    bins = [i for i in range(0, 256)]
    mode = np.argmax(hist)
    ymax = np.max(hist)

    return bins, hist, ymax, mean, median, mode
    
def calculate_bintensity(image_list, rectitem):
    intensities = []
    for rect in rectitem:
        band_intensity = []
        if isinstance(rect, QPointF):
            for image in image_list:
                x, y = rect.x(), rect.y()
                intensity = image[int(y), int(x)]
                band_intensity.append(intensity)
            intensities.append(band_intensity)
        elif isinstance(rect, list):
            if len(rect) == 2:
                for image in image_list:
                    x1, y1, x2, y2 = rect[0].x(), rect[0].y(), rect[1].x(), rect[1].y()
                    area = image[int(y1):int(y2), int(x1):int(x2)]
                    intensity = np.mean(area)
                    band_intensity.append(intensity)
                intensities.append(band_intensity)
            else:
                for image in image_list:
                    points = [(int(qpoint.x()), int(qpoint.y())) for qpoint in rect]
                    polygon = cv.convexHull(np.array(points))
                    intensity = np.mean(image[polygon])
                    band_intensity.append(intensity)
                intensities.append(band_intensity)
        else:
            pass
    return intensities


def calculate_intensity(image, rectitem):
    intensities = []
    for rect in rectitem:
        if isinstance(rect, QPointF):
            x, y = rect.x(), rect.y()
            intensity = image[int(y), int(x)]
            print(intensity)
            intensities.append(intensity)
        elif isinstance(rect, list):
            if len(rect) == 2:
                x1, y1, x2, y2 = rect[0].x(), rect[0].y(), rect[1].x(), rect[1].y()
                area = image[int(y1):int(y2), int(x1):int(x2)]
                intensity = np.mean(area)
                print(intensity)
                intensities.append(intensity)
            else:
                points = [(int(qpoint.x()), int(qpoint.y())) for qpoint in rect]
                polygon = cv.convexHull(np.array(points))
                intensity = np.mean(image[polygon])
                print(intensity)
                intensities.append(intensity)
        else:
            pass
    return intensities

def match_image(app, referece_img, image_list):
    if referece_img.ndim == 3:
        referece_img = cv.cvtColor(referece_img, cv.COLOR_RGB2GRAY)
    else:
        pass
    superglue_matcher = Matcher(
{
    "superpoint": {
        "descriptor_dim": 256,
        "nms_radius": 4,
        "keypoint_threshold": 0.001,
        "max_keypoints": -1,
        "remove_borders": 4,
        "input_shape": (-1, -1),
    },
    "superglue": {
        "descriptor_dim": 256,
        "weights": "outdoor",
        "keypoint_encoder": [32, 64, 128, 256],
        "GNN_layers": ["self", "cross"] * 9,
        "sinkhorn_iterations": 500,
        "match_threshold": 0.5,
    },
    "use_gpu": True,
})

    aligned_bImages = []

    progress = QProgressDialog("영상 정렬중...", "중지", 0, len(image_list))

    progress.setStyleSheet("QPushButton { background: #0B661F; max-width: 120px; max-height: 32px; color: #FFF; font-family: Cabin; font-size: 12px; font-style: normal; font-weight: 700; line-height: normal; }""\n""QLabel {text-align: center; font-family: Cabin; font-size: 20px; font-style: normal; font-weight: 700; line-height: normal; }")
    current_size = progress.size()
    new_size = current_size * 4
    progress.setFixedSize(new_size)
    progress.move(app.geometry().center() - progress.rect().center())
    progress.setWindowModality(Qt.WindowModality.ApplicationModal)
    for i in range(len(image_list)):
        progress.setValue(i)
        ref_image = referece_img
        query_image = image_list[i]

        query_kpts, ref_kpts, _, _, matches = superglue_matcher.match(query_image, ref_image)
        M, mask = cv.findHomography(
            np.float64([query_kpts[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2),
            np.float64([ref_kpts[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2),
            method=cv.USAC_MAGSAC,
            ransacReprojThreshold=5.0,
            maxIters=100,
            confidence=0.95,
        )
        matches = np.array(matches)[np.all(mask > 0, axis=1)]
        matches = sorted(matches, key=lambda match: match.distance)
        logger.info(f"number of inliers: {mask.sum()}")
        aligned_bImage = cv.warpPerspective(query_image, M, (ref_image.shape[1], ref_image.shape[0]))
        # cv.imwrite(f'{i}.tiff', aligned_bImage)
        aligned_bImages.append(aligned_bImage)

    progress.setValue(len(image_list))

    return aligned_bImages

def make_RGB(image_list):
    rgb = cv.merge((image_list[0], image_list[1], image_list[2]))
    rgb = cv.cvtColor(rgb, cv.COLOR_RGB2BGR)
    cv.imwrite("rgb.png", rgb)
    return rgb

def qpoint2point(list):
    new_list = []
    for i in range(len(list)):
        x, y = list[i].x(), list[i].y()
        new_list.append((x, y))
    return new_list

def make_mask(image, qpoints, val=255):
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    points = [(int(qpoint.x()), int(qpoint.y())) for qpoint in qpoints]
    pts = np.array(points, dtype=np.int32)
    cv.fillPoly(mask, [pts], val)

    return mask, pts

def remove_background(list, mask):
    image_list = []
    for image in list:
        image = cv.bitwise_and(image, mask)
        image_list.append(image)
        
    return image_list

def make_vegetation_index(images, type):
    if type == "ndvi":
        index_image = (images[4].astype(float) - images[2].astype(float)) / (images[4].astype(float) + images[2].astype(float) + 1e-9)
    elif type == "ndre":
        index_image = (images[4].astype(float) - images[3].astype(float)) / (images[4].astype(float) + images[3].astype(float) + 1e-9)
    elif type == "gndvi":
        index_image = (images[4].astype(float) - images[1].astype(float)) / (images[4].astype(float) + images[1].astype(float) + 1e-9)
    elif type == "evi":
        index_image = 2.5*((images[4].astype(float) - images[2].astype(float)) /((images[4].astype(float) + 6 * images[2].astype(float) - 7.5 * images[0].astype(float) + 1e-9) + 1))
    elif type == "avi":
        index_image = (images[4].astype(float) * (1-images[2]).astype(float) * (images[4].astype(float)-images[2].astype(float)  + 1e-9) + 1e-9)/3
    elif type == "savi":
        index_image = ((images[4].astype(float) - images[2].astype(float)) / (images[4].astype(float) + images[2].astype(float) + 0.5  + 1e-9)) * (1 + 0.5)
    elif type == "g":
        index_image = images[2].astype(float) / (images[3].astype(float) + 1e-9)
    elif type == "cire":
        index_image = images[4].astype(float) / (images[3].astype(float) + 1e-9)
    elif type == "ndgi":
        index_image = (images[4].astype(float) - images[1].astype(float)) / ( images[4].astype(float) + images[1].astype(float) + 1e-9)
    elif type == "arvi":
        index_image = (images[4].astype(float) - (2 * images[2].astype(float)) + images[0].astype(float)) / (images[4].astype(float) + (2 * images[2].astype(float) + 1e-9) + images[0].astype(float) + 1e-9)
    elif type == "sipi":
        index_image = (images[4].astype(float) - images[0].astype(float)) /(images[4].astype(float) - images[2].astype(float) + 1e-9) 
    elif type == "vari":
        index_image = (images[1].astype(float) - images[2].astype(float)) / (images[1].astype(float) + images[2].astype(float) - images[0].astype(float) + 1e-9)
    # elif type == "lci":
    #     index_image = (images[4].astype(float) - images[3].astype(float)) / (images[4].astype(float) + images[2].astype(float) + 1e-9)
    # elif type == "ndwi":
    #     index_image = (images[1].astype(float) - images[4].astype(float)) / (images[1].astype(float) + images[4].astype(float) + 1e-9)
    # elif type == "cvi":
    #     index_image = (images[4].astype(float) * images[2].astype(float)) / (images[1].astype(float) * images[1].astype(float) + 1e-9)
    else:
        print(f'no vegetation_index: {type}')

    return index_image

def get_colorbar(dir):
    colorbar = cv.imread(os.path.join(dir, 'icons/main', 'colorbar.png'))
    # colorbar = cv.cvtColor(colorbar, cv.COLOR_BGR2RGB)
    return colorbar

def apply_colormap(image, colorbar):
    min_value = np.min(image)
    max_value = np.max(image)
    normalized_image = (image - min_value) / (max_value - min_value)
    colormap = cv.applyColorMap((normalized_image * 255).astype(np.uint8), cv.COLORMAP_JET)

    colormap_height, colormap_width, _ = colormap.shape
    colorbar_height, colorbar_width, _ = colorbar.shape
    index_image_height = max(colormap_height, colorbar_height)
    index_image_width = colormap_width + colorbar_width

    colorbar = cv.resize(colorbar, (colorbar_width, index_image_height))

    index_image = np.zeros((index_image_height, index_image_width, 3), dtype=np.uint8)

    index_image[:, :colormap_width, :] = colormap
    index_image[:, colormap_width:, :] = colorbar

    index_image = cv.cvtColor(index_image, cv.COLOR_RGB2BGR)

    return index_image



def process_index(dir, image, index_name):
    """
    image: ndarray
    index_name: str

    Returns:
    index: ndarray
    """
    min_value = np.min(image)
    max_value = np.max(image)
    normalized_image = (image - min_value) / (max_value - min_value)
    colormap = cv.applyColorMap((normalized_image * 255).astype(np.uint8), cv.COLORMAP_JET)
    colorbar = cv.imread(os.path.join(dir, 'icons/colorbar.png'))

    colormap_height, colormap_width, _ = colormap.shape
    colorbar_height, colorbar_width, _ = colorbar.shape
    index_image_height = max(colormap_height, colorbar_height)
    index_image_width = colormap_width + colorbar_width

    colorbar = cv.resize(colorbar, (colorbar_width, index_image_height))

    index_image = np.zeros((index_image_height, index_image_width, 3), dtype=np.uint8)

    index_image[:, :colormap_width, :] = colormap
    index_image[:, colormap_width:, :] = colorbar

    index_bgr = cv.cvtColor(index_image, cv.COLOR_RGB2BGR)
    cv.imwrite(os.path.join(dir, 'temp', f'index_{index_name}.png'), index_bgr)

    return index_image

def get_normalize(image, pixels):
    if type(pixels) == 'numpy.ndarray':
        mask = np.zeros_like(image, dtype=np.uint8)
        cv.fillPoly(mask, [pixels], color=255)
        pixel_coordinates = cv.findNonZero(mask)

        values = image[pixel_coordinates[:, 0, 1], pixel_coordinates[:, 0, 0]]
        min_value = np.min(values)
        max_value = np.max(values)

        normalized_image = np.zeros_like(image, dtype=np.float64)
        normalized_image[pixel_coordinates[:, 0, 1], pixel_coordinates[:, 0, 0]] = (values - min_value) / (max_value - min_value)

        normalized_values = normalized_image[pixel_coordinates[:, 0, 1], pixel_coordinates[:, 0, 0]]
        normalized_min_value = np.min(normalized_values)
        normalized_max_value = np.max(normalized_values)
        normalized_mean_value = np.mean(normalized_values)

    else:
        min_value = np.min(image)
        max_value = np.max(image)
        normalized_image = (image - min_value) / (max_value - min_value)

        normalized_min_value = np.min(normalized_image)
        normalized_max_value = np.max(normalized_image)
        normalized_mean_value = np.mean(normalized_image)

    return normalized_image, normalized_min_value, normalized_max_value, normalized_mean_value

def advance_index(image, pixels):
    values = image[pixels[:, 1], pixels[:, 0]]
    mean_value = np.mean(values)

    advanced_image = np.zeros_like(image, dtype=np.float64)

    lower_values = values[values < mean_value]
    upper_values = values[values > mean_value]

    lower_percentile = np.percentile(lower_values, 10) if len(lower_values) > 0 else 0.0
    upper_percentile = np.percentile(upper_values, 90) if len(upper_values) > 0 else 1.0

    advanced_values = np.where(values < mean_value,
                               999 ** (values - mean_value) + mean_value - 1,
                               -999 ** (-values + mean_value) + mean_value + 1)
    
    # advanced_image[advanced_image < lower_percentile] = lower_percentile
    # advanced_image[advanced_image > upper_percentile] = upper_percentile
    advanced_image[pixels[:, 1], pixels[:, 0]] = np.clip(advanced_values, lower_percentile, upper_percentile)

    advanced_min_value = np.min(advanced_values)
    advanced_max_value = np.max(advanced_values)
    advanced_mean_value = np.mean(advanced_values)

    return advanced_image, advanced_min_value, advanced_max_value, advanced_mean_value

def get_renormalize(image, pixels):
    valid_pixels = pixels[(pixels[:, 0] < image.shape[1]) & (pixels[:, 1] < image.shape[0])]
    values = image[valid_pixels[:, 1], valid_pixels[:, 0]]
    mean_value = np.mean(values)

    normalized_image = np.zeros_like(image, dtype=np.float64)

    lower_values = values[values < mean_value]
    upper_values = values[values > mean_value]

    lower_min = np.min(lower_values) if len(lower_values) > 0 else 0.0
    lower_max = np.max(lower_values) if len(lower_values) > 0 else mean_value
    upper_min = np.min(upper_values) if len(upper_values) > 0 else mean_value
    upper_max = np.max(upper_values) if len(upper_values) > 0 else 1.0

    lower_normalized = (lower_values - lower_min) / (lower_max - lower_min)
    upper_normalized = (upper_values - upper_min) / (upper_max - upper_min)

    normalized_image[valid_pixels[values < mean_value][:, 1], valid_pixels[values < mean_value][:, 0]] = lower_normalized
    normalized_image[valid_pixels[values > mean_value][:, 1], valid_pixels[values > mean_value][:, 0]] = upper_normalized

    normalized_values = normalized_image[valid_pixels[:, 1], valid_pixels[:, 0]]
    normalized_min_value = np.min(normalized_values)
    normalized_max_value = np.max(normalized_values)
    normalized_mean_value = np.mean(normalized_values)

    return normalized_image, normalized_min_value, normalized_max_value, normalized_mean_value

def update_index(dir, image, index_name, mask):
    """
    image: ndarray (float64)
    """
    inside_pixels = np.argwhere(mask == 255)
    # 1. normalize
    normalized_index, normalized_min, normalized_max, normalized_mean = get_normalize(image, inside_pixels)

    # 2. advanced
    advanced_index, advanced_min, advanced_max, advanced_mean = advance_index(normalized_index, inside_pixels)

    # 3. renormalize
    renormalized_index, renormalized_min, renormalized_max, renormalized_mean = get_renormalize(advanced_index, inside_pixels)

    colormap = cv.applyColorMap((renormalized_index * 255).astype(np.uint8), cv.COLORMAP_JET)
    colorbar = cv.imread(os.path.join(dir, 'icons/colorbar.png'))

    colormap_height, colormap_width, _ = colormap.shape
    colorbar_height, colorbar_width, _ = colorbar.shape
    index_image_height = max(colormap_height, colorbar_height)
    index_image_width = colormap_width + colorbar_width

    colorbar = cv.resize(colorbar, (colorbar_width, index_image_height))

    index_image = np.zeros((index_image_height, index_image_width, 3), dtype=np.uint8)

    index_image[:, :colormap_width, :] = colormap
    index_image[:, colormap_width:, :] = colorbar

    index_bgr = cv.cvtColor(index_image, cv.COLOR_RGB2BGR)

    cv.imwrite(os.path.join(dir, 'temp', f'index_{index_name}.png'), index_bgr)

    return index_image

def print_index(dir, image, name):
    workbook = Workbook()
    sheet = workbook.active
    for i in range(image.shape[1]):
        for j in range(image.shape[0]):

            cell_value = image[j, i]
            sheet.cell(row=j+1, column=i+1, value=cell_value)

    workbook.save(os.path.join(dir, f'{name}_original.xlsx'))

"""
    get the mask, from the polygon formed using points (QPointF)
    on the image
"""
def get_mask(image, points, val = 1):
    import cv2
    mask = np.zeros(image.shape[:2], dtype=np.uint8) ### only take the width, height not the color dim
    tuple_point = [(p.x(),p.y()) for p in points]
    polygon = [np.array(tuple_point, dtype=np.int32)]
    cv2.fillPoly(mask,polygon, val)
    return mask