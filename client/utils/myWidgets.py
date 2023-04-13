import base64

from PyQt5.QtWidgets import QApplication, QTextEdit
from PyQt5.QtGui import QImage, QPixmap, QDragEnterEvent, QDropEvent, QMouseEvent, QKeyEvent
from PyQt5.QtCore import Qt, QMimeData, QByteArray, QBuffer


class MyTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasImage():
            event.acceptProposedAction()

    def dragMoveEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasImage():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasImage():
            image = QImage(event.mimeData().imageData())
            self.insertImage(image)
            event.acceptProposedAction()

    def insertFromMimeData(self, source: QMimeData):
        if source.hasImage():
            image = QImage(source.imageData())
            self.insertImage(image)
        else:
            super().insertFromMimeData(source)

    def insertImage(self, image: QImage):
        cursor = self.textCursor()
        data = QByteArray()
        buffer = QBuffer(data)
        image.save(buffer)
        base = str(data.toBase64())
        print(base)
        cursor.insertHtml('<img src="data:image/png;base64,{0}"/>'.format(base))
