import os
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEngineDownloadItem
from PyQt5.QtCore import QUrl


class FullscreenWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Записная книжка')
        self.setWindowIcon(QIcon('icon.png'))
        self.browser = QWebEngineView()
        self.profile = QWebEngineProfile.defaultProfile()

        # Задаём URL сайта
        self.browser.setUrl(QUrl("https://cwnotes.ru/"))

        self.setCentralWidget(self.browser)
        self.setMinimumSize(875, 600)
        self.resize(1000, 700)
        self.profile.downloadRequested.connect(self.handle_download)
        self.profile.cookieStore().deleteAllCookies()

    def handle_download(self, download: QWebEngineDownloadItem):
        # Устанавливаем имя файла и расширение по умолчанию
        default_filename = "notes.xlsx"
        save_path, _ = QFileDialog.getSaveFileName(
            self,
            "Сохранить файл",
            os.path.expanduser(f"~/") + default_filename,
        )
        if save_path:
            download.setPath(save_path)
            download.finished.connect(lambda: self.on_download_finished(download))
            download.accept()
        else:
            QMessageBox.warning(self, "Загрузка отменена", "Загрузка была отменена.")

    def on_download_finished(self, download):
        if download.isFinished():
            QMessageBox.information(self, "Загрузка завершена", f"Файл сохранен в: {download.path()}")
        else:
            QMessageBox.critical(self, "Ошибка", "Загрузка не завершена успешно.")

if __name__ == "__main__":
    os.environ["QTWEBENGINE_ENABLE_HARDWARE_ACCELERATION"] = "1"
    app = QApplication(sys.argv)
    window = FullscreenWindow()
    window.show()
    sys.exit(app.exec_())
