import os

from utils.utils import numpy_to_qimage, get_color_image

from PySide6.QtCore import Qt, Signal, QPointF, QLineF, QRectF, QSize
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsRectItem, QGraphicsPolygonItem, QGraphicsTextItem
from PySide6.QtGui import QImage, QPixmap, QPen, QColor, QBrush, QFont, QPolygonF, QPainter

class DraggablePixmapItem(QGraphicsPixmapItem):
    def __init__(self, pixmap, parent=None):
        super().__init__(pixmap, parent)
        self.beforeMovingPos = self.pos()
        self.afterMovingRect = self.boundingRect()

class ImageViewer(QGraphicsView):
    updateRoi = Signal(list)
    updateRect = Signal(object)

    def __init__(self, ui):
        super(ImageViewer, self).__init__()
        self.view = ui.graphicsView
        self.source = ui.label_view

        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)
        self.view.setMouseTracking(True)

        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)
        self.view.setMouseTracking(True)

        self.path = None
        self.image = None
        self.pixmapitem = None

        self.drawing = ''
        self.drawing_mode = 'zoom'
        self.roipoints = []
        self.rectitem = []
        self.start_rectangle = None
        self.start_free = None
        self.rectangle_count = 0
        self.temp_polygon_point =[]
        self.temp_free_point = []
        self.scalepixmapitem = 1

        self.scene.mousePressEvent = self.scene_mousePressEvent
        self.scene.mouseMoveEvent = self.scene_mouseMoveEvent
        self.scene.mouseReleaseEvent = self.scene_mouseReleaseEvent
        self.scene.wheelEvent = self.scene_wheelEvent

    def get_image(self):
        self.image = get_color_image(self.path[0])

    def get_pixmapitem(self):
        self.original_height, self.original_width, qimage = numpy_to_qimage(self.image)
        pixmap = QPixmap.fromImage(qimage)
        self.pixmapitem = QGraphicsPixmapItem(pixmap)

    def set_image(self):
        self.scene.clear()
        self.scene.addItem(self.pixmapitem)
        
        center_x = self.view.width() / 2
        center_y = self.view.height() / 2

        scale_x = self.original_width / self.view.viewport().width()
        scale_y = self.original_height / self.view.viewport().height()

        scale = max(scale_x, scale_y)

        scene_width = self.original_width / scale
        scene_height = self.original_height / scale

        self.scene.setSceneRect(center_x, center_y, scene_width, scene_height)

        self.pixmapitem.setScale(1 / scale)
        self.pixmapitem.setPos(center_x, center_y)

    def update_image(self):
        self.get_image()
        self.get_pixmapitem()
        self.set_image()
        if len(self.scene.items()) > 1:
            self.redraw_allrect()
            
    def set_event(self, mode):
        self.drawing = mode.split('_')[-2]
        self.drawing_mode = mode.split('_')[-1]
        print('drawing mode: ', self.drawing)
        print('drawing rect: ', self.drawing_mode)

    def clear_rect(self):
        for item in self.scene.items():
            if not isinstance(item, QGraphicsPixmapItem):
                self.scene.removeItem(item)
    
    def clear_temp_rectangle(self):
        self.scene.removeItem(self.scene.items()[0])

    def clear_items_on_scene(self):
        items = self.scene.items()
        for item in items:
            if not isinstance(item, QGraphicsPixmapItem):
                self.scene.removeItem(item)

    def draw_text(self, text, point):
        item = QGraphicsTextItem(text)
        item.setX(point.x())
        item.setY(point.y())
        current_scale = self.pixmapitem.scale()
        size = int(15 * current_scale)
        item.setFont(QFont("Arial", size))
        item.setDefaultTextColor(QColor(Qt.GlobalColor.white))
        self.scene.addItem(item)

    def redraw_allrect(self):
        self.clear_items_on_scene()
        self.updateRect.emit(self.rectitem)
        for i, rect in enumerate(self.rectitem):
            if isinstance(rect, QPointF):
                p = self.draw_point(rect)
                self.draw_text(f'관심영역{i+1}', p)
                # self.draw_text(f'ROA{i+1}', p)
            elif isinstance(rect, list) and len(rect) == 2 and all(isinstance(p, QPointF) for p in rect):
                p = self.draw_rectangle(rect[0], rect[1])
                self.draw_text(f'관심영역{i+1}', p)
                # self.draw_text(f'ROA{i+1}', p)
                self.rectangle_count = 0
            elif isinstance(rect, list) and len(rect) > 2 and all(isinstance(p, QPointF) for p in rect):
                p = self.draw_polygon(rect)
                self.draw_text(f'관심영역{i+1}', p)
                # self.draw_text(f'ROA{i+1}', p)
            else:
                print('도형 구조를 확인하세요!!')

    def draw_point(self, qpoint):
        current_scale = self.pixmapitem.scale()
        current_pos = self.pixmapitem.pos()
        qpoint1 = QPointF((current_scale * qpoint.x()) + current_pos.x(), (current_scale * qpoint.y()) + current_pos.y())
        point = QGraphicsEllipseItem(qpoint1.x() - 1.5, qpoint1.y() - 1.5, 3, 3)
        point.setBrush(QBrush(Qt.GlobalColor.white))
        point.setPen(QPen(Qt.GlobalColor.white))
        self.scene.addItem(point)
        return qpoint1

    def draw_rectangle(self, qp1, qp2):
        current_scale = self.pixmapitem.scale()
        current_pos = self.pixmapitem.pos()
        qpoint1 = QPointF((current_scale * qp1.x()) + current_pos.x(), (current_scale * qp1.y()) + current_pos.y())
        qpoint2 = QPointF((current_scale * qp2.x()) + current_pos.x(), (current_scale * qp2.y()) + current_pos.y())
        line = QLineF(qpoint1, qpoint2)
        distance = line.length()
        if distance < 2:
            pass
            return None
        else:
            if self.rectangle_count == 0:
                self.rectangle_count += 1
            else:
                self.rectangle_count += 1
                self.clear_temp_rectangle()
            rectangle = QRectF(qpoint1, qpoint2)
            rectangle_item = QGraphicsRectItem(rectangle)
            rectangle_item.setPen(QPen(Qt.GlobalColor.white, 2))
            rectangle_item.setBrush(QColor(Qt.GlobalColor.transparent))
            self.scene.addItem(rectangle_item)
            return qpoint2

    def draw_polygon_point(self, qp1):
        current_scale = self.pixmapitem.scale()
        current_pos = self.pixmapitem.pos()
        qpoint = QPointF((current_scale * qp1.x()) + current_pos.x(), (current_scale * qp1.y()) + current_pos.y())
        point = QGraphicsEllipseItem(qpoint.x() - 1, qpoint.y() - 1, 2, 2)
        point.setBrush(QBrush(Qt.GlobalColor.red))
        point.setPen(QPen(Qt.GlobalColor.red))
        self.scene.addItem(point)

    def draw_polygon_line(self, qp1, qp2):
        current_scale = self.pixmapitem.scale()
        current_pos = self.pixmapitem.pos()
        qpoint1 = QPointF((current_scale * qp1.x()) + current_pos.x(),(current_scale * qp1.y()) + current_pos.y())
        qpoint2 = QPointF((current_scale * qp2.x()) + current_pos.x(),(current_scale * qp2.y()) + current_pos.y())
        line = QGraphicsLineItem(qpoint1.x(), qpoint1.y(), qpoint2.x(), qpoint2.y())
        line.setPen(QPen(Qt.GlobalColor.red, 2))
        self.scene.addItem(line)

    def draw_polygon(self, qpoints):
        if len(qpoints) >= 3:
            newRect = []
            current_scale = self.pixmapitem.scale()
            current_pos = self.pixmapitem.pos()
            for qp1 in qpoints:
                qpoint1 = QPointF((current_scale * qp1.x()) + current_pos.x(),
                                  (current_scale * qp1.y()) + current_pos.y())
                newRect.append(qpoint1)
            polygon = QPolygonF(newRect)
            polygon_item = QGraphicsPolygonItem(polygon)
            polygon_item.setPen(QPen(Qt.GlobalColor.white, 2))
            polygon_item.setBrush(QColor(Qt.GlobalColor.transparent))
            self.scene.addItem(polygon_item)
            return newRect[-1]

    def scene_mousePressEvent(self, event):
        scenepos = event.scenePos()
        if event.button() == Qt.MouseButton.LeftButton:
            qpoint = self.pixmapitem.mapFromScene(scenepos)
            if self.drawing_mode == "zoom":
                ### when clicked on image.
                ### moving and zooming processing.
                self.pixmapitem.beforeMovingPos = self.pixmapitem.pos()
                if event.button() == Qt.MouseButton.LeftButton:
                    self.pixmapitem.setCursor(Qt.CursorShape.ClosedHandCursor)
                    self.pixmapitem.setFlag(self.pixmapitem.GraphicsItemFlag.ItemIsMovable, enabled=True)
                    
            elif self.drawing_mode == 'point':
                self.rectitem.append(qpoint)
                print(f'{self.drawing_mode} item updated.')
                print(self.rectitem)
                self.updateRect.emit(self.rectitem)
                p = self.draw_point(qpoint)
                self.draw_text(f'관심영역{len(self.rectitem)}', p)
                # self.draw_text(f'ROA{len(self.rectitem)}', p)
                self.drawing_mode = 'zoom'

            elif self.drawing_mode == 'rectangle':
                self.start_rectangle = qpoint

            elif self.drawing_mode == 'polygon':
                if len(self.temp_polygon_point) == 0:
                    self.start_polygon = qpoint
                    self.temp_polygon_point.append(qpoint)
                    self.draw_polygon_point(qpoint)
                elif len(self.temp_polygon_point) == 1:
                    self.temp_polygon_point.append(qpoint)
                    self.draw_polygon_line(self.start_polygon, qpoint)
                else:
                    line = QLineF(self.temp_polygon_point[0], qpoint)
                    distance = line.length()
                    if distance < 5:
                        if self.drawing == 'roi':
                            self.updateRoi.emit(self.temp_polygon_point)
                            self.clear_items_on_scene()
                        elif self.drawing == 'roa':
                            self.rectitem.append(self.temp_polygon_point)
                            p = self.draw_polygon(self.temp_polygon_point)
                            print(f'{self.drawing_mode} item updated.')
                            print(self.rectitem)
                            self.updateRect.emit(self.rectitem)
                            self.draw_text(f'관심영역{len(self.rectitem)}', p)
                            # self.draw_text(f'ROA{len(self.rectitem)}', p)
                        self.start_polygon = None
                        self.temp_polygon_point = []
                        self.drawing_mode = 'zoom'
                    else:
                        self.temp_polygon_point.append(qpoint)
                        self.draw_polygon_line(self.temp_polygon_point[-2], self.temp_polygon_point[-1])

            elif self.drawing_mode == 'freedraw':
                if len(self.temp_free_point) == 0:
                    self.start_free = qpoint
                    self.temp_free_point.append(qpoint)
                    self.draw_polygon_point(qpoint)
                else:
                    pass

            # elif self.drawing_mode == 'zoom':
            #     self.pixmapitem.beforeMovingPos = self.pixmapitem.pos()
            #     self.pixmapitem.setFlag(self.pixmapitem.GraphicsItemFlag.ItemIsMovable, enabled=True)

            else:
                pass

        elif event.button() == Qt.MouseButton.RightButton:
            if self.drawing_mode in ('point', 'rectangle', 'polygon', 'free') and self.drawing == 'roa':
                self.rectitem.pop()
                print(f'{self.drawing_mode} item updated.')
                print(self.rectitem)
                self.updateRect.emit(self.rectitem)
                self.clear_rect()
                self.redraw_allrect()
            elif self.drawing_mode == "zoom":
                ### if right click outside the image. (when image zoomed out), the clickedItem should return None
                try:
                    clickedItem = self.scene.items(scenepos)[0] ### take the first (in front) item only.
                except:
                    clickedItem = None
                if isinstance(clickedItem, QGraphicsTextItem):
                    ### remove rect/point/polygon
                    ### and remove text, too.
                    text = clickedItem.toPlainText()
                    idx = int(text.strip()[-1]) - 1
                    self.rectitem.pop(idx)
                    print(f'{self.drawing_mode} item deleted.')
                    self.updateRect.emit(self.rectitem)

                else:
                    ### reset image size when right click on zoom mode
                    center_x = self.view.width() / 2
                    center_y = self.view.height() / 2
                    scale_x = self.original_width / self.view.viewport().width()
                    scale_y = self.original_height / self.view.viewport().height()
                    scale = max(scale_x, scale_y)
                    scene_width = self.original_width / scale
                    scene_height = self.original_height / scale
                    self.scene.setSceneRect(center_x, center_y, scene_width, scene_height)
                    self.pixmapitem.setScale(1 / scale)
                    self.pixmapitem.setPos(center_x, center_y)
                self.redraw_allrect()
        else:
            pass

    def scene_mouseMoveEvent(self, event):
        if self.pixmapitem is not None:
            scenepos = event.scenePos()
            qpoint = self.pixmapitem.mapFromScene(scenepos)
            if self.drawing_mode == 'rectangle':
                if self.start_rectangle is not None:
                    # event.accept()
                    self.draw_rectangle(self.start_rectangle, qpoint)
                else:
                    pass

            elif self.drawing_mode == 'freedraw':
                if self.start_free is not None:
                    event.accept()
                    self.temp_free_point.append(qpoint)
                    if len(self.temp_free_point) > 1:
                        self.draw_polygon_line(self.temp_free_point[-2], self.temp_free_point[-1])

            elif self.drawing_mode == 'zoom':
                ### image dragging event handler.
                if self.pixmapitem.cursor().shape() == Qt.CursorShape.ClosedHandCursor:
                    deltaPos = event.scenePos() - event.buttonDownScenePos(Qt.MouseButton.LeftButton)
                    newPosX = self.pixmapitem.beforeMovingPos.x() + deltaPos.x()
                    newPosY = self.pixmapitem.beforeMovingPos.y() + deltaPos.y()
                    self.pixmapitem.setPos(newPosX, newPosY)
                    self.redraw_allrect()
            else:
                pass

    def scene_mouseReleaseEvent(self, event):
        scenepos = event.scenePos()

        self.pixmapitem.setCursor(Qt.CursorShape.ArrowCursor)
        self.pixmapitem.setFlag(self.pixmapitem.GraphicsItemFlag.ItemIsMovable, enabled=False)

        if event.button() == Qt.MouseButton.LeftButton:
            qpoint = self.pixmapitem.mapFromScene(scenepos)
            if self.drawing_mode == 'rectangle':
                self.rectitem.append([self.start_rectangle, qpoint])
                p = self.draw_rectangle(self.start_rectangle, qpoint)
                print(f'{self.drawing_mode} item updated.')
                self.updateRect.emit(self.rectitem)
                self.draw_text(f'관심영역{len(self.rectitem)}', p)
                # self.draw_text(f'ROA{len(self.rectitem)}', p)
                self.start_rectangle = None
                self.rectangle_count = 0
                self.drawing_mode = 'zoom'

            elif self.drawing_mode == 'freedraw':
                if self.drawing == 'roi':
                    self.updateRoi.emit(self.temp_free_point)
                    self.clear_items_on_scene()
                elif self.drawing == 'roa':
                    self.rectitem.append(self.temp_free_point)
                    p = self.draw_polygon(self.temp_free_point)
                    print(f'{self.drawing_mode} item updated.')
                    self.updateRect.emit(self.rectitem)
                    self.draw_text(f'관심영역{len(self.rectitem)}', p)
                    # self.draw_text(f'ROA{len(self.rectitem)}', p)
                else:
                    pass
                self.start_free = None
                self.temp_free_point = []
                self.drawing_mode = 'zoom'
                
            # elif self.drawing_mode == 'zoom':
            #     self.pixmapitem.beforeMovingPos = qpoint
            else:
                pass
        else:
            pass

    def scene_wheelEvent(self, event):
        if self.pixmapitem is None:
            return
        if self.drawing_mode == 'zoom':
            zoomStep = 0.1
            currentScale = self.pixmapitem.scale()
            if event.delta() > 0:
                direction = 1
            else:
                direction = -1
            newScale = currentScale + (zoomStep * direction)
            if newScale > 5: newScale = 5
            if newScale < 0.3: newScale = 0.3
            self.pixmapitem.setScale(newScale)
            event.accept()
            self.pixmapitem.wheelEvent(event)
            self.redraw_allrect()

    def copysource(self):
        image = QImage(self.scene.width(), self.scene.height(), QImage.Format.Format_ARGB32)
        image.fill(Qt.GlobalColor.white)
        painter = QPainter(image)
        self.scene.render(painter)
        painter.end()
        self.source.setPixmap(QPixmap.fromImage(image))
        self.source.setMinimumSize(QSize(self.scene.width(), self.source.height()))
        self.source.adjustSize()

    def save_present_image(self):
        self.count = 1
        image = QImage(self.scene.width(), self.scene.height(), QImage.Format.Format_ARGB32)
        image.fill(Qt.GlobalColor.white)
        painter = QPainter(image)
        self.scene.render(painter)
        painter.end()
        filename = f'{self.count:4d}_saved.png'
        image.save(os.path.join(self.dir, filename))

    def save_image(self, type):
        self.count = 1
        if type == 'band':
            pass # copy from imageDir
        elif type == 'color':
            pass # copy from imageDir
        elif type == 'rgb':
            pass # copy from imageDir
        else:
            image = QImage(self.scene.width(), self.scene.height(), QImage.Format.Format_ARGB32)
            image.fill(Qt.GlobalColor.white)
            painter = QPainter(image)
            self.scene.render(painter)
            painter.end()
            project_num = self.dir.split("\\")
            if type in self.vindex:
                filename = f'INDEX_{project_num}_{type.upper()}.png'
            else:
                filename = f'INDEX_{project_num}_{type.upper()}_Boost.png'
            image.save(os.path.join(self.dir, filename))