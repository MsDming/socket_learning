from PyQt5 import QtCore
from PyQt5.QtCore import QFileInfo, QUrl, QFile, QIODevice, QByteArray, \
    QBuffer
from PyQt5.QtGui import QImage, QImageReader, QTextDocumentFragment
from PyQt5.QtWidgets import QTextEdit

from datetime import datetime


class TextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

    def canInsertFromMimeData(self, source: QtCore.QMimeData) -> bool:
        return source.hasImage() or source.hasUrls() or \
            super(TextEdit, self).canInsertFromMimeData(source)

    def insertFromMimeData(self, source: QtCore.QMimeData) -> None:
        if source.hasImage():
            self.insert_image(source.imageData())
        elif source.hasUrls():
            for url in source.urls():
                file_info = QFileInfo(url.toLocalFile())
                ext = file_info.suffix().lower()
                if ext in QImageReader.supportedImageFormats():
                    self.insert_image(QImage(file_info.filePath()), ext)
                else:
                    self.insert_file(url)
        else:
            super(TextEdit, self).insertFromMimeData(source)

    def insert_image(self, image: QImage, fmt: str = "png"):
        """插入图片"""
        data = QByteArray()
        buffer = QBuffer(data)
        image.save(buffer, fmt)
        base64_data = str(data.toBase64())[2:-1]
        data = f'<img src="data:image/{fmt};base64,{base64_data}" />'
        fragment = QTextDocumentFragment.fromHtml(data)
        self.textCursor().insertFragment(fragment)

    def insert_file(self, url: QUrl):
        """插入文件"""
        file = None
        # noinspection PyBroadException
        try:
            file = QFile(url.toLocalFile())
            if not file.open(QIODevice.ReadOnly or QIODevice.Text):
                return
            file_data = file.readAll()
            # noinspection PyBroadException
            try:
                self.textCursor().insertHtml(str(file_data, encoding="utf8"))
            except Exception:
                self.textCursor().insertHtml(str(file_data))
        except Exception:
            if file:
                file.close()

    @staticmethod
    def get_time_str():
        return datetime.now().strftime("%Y%#m%#d_%H%M%S")
