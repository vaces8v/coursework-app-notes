import os
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile
from PyQt5.QtCore import QUrl

class FullscreenWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Записная книжка')
        self.setWindowIcon(QIcon('icon.png'))
        self.browser = QWebEngineView()

        self.profile = QWebEngineProfile.defaultProfile()
        self.browser.setUrl(QUrl("http://83.222.24.22:3000/"))

        self.setCentralWidget(self.browser)
        self.setMinimumSize(875, 600)
        self.resize(1000, 700)

        self.profile.cookieStore().deleteAllCookies()


if __name__ == "__main__":
    os.environ["QTWEBENGINE_ENABLE_HARDWARE_ACCELERATION"] = "1"
    app = QApplication(sys.argv)
    window = FullscreenWindow()
    window.show()
    sys.exit(app.exec_())
