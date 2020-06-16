"""

Copyright 2020 Taoidle

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

"""
import sys, ui

from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QMainWindow, QGridLayout, QVBoxLayout, QAction


class MainWindow(QMainWindow):
    vid_status = False

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.video_wid = QVideoWidget()
        self.video_wid.setMinimumSize(640, 480)

        self.video_console = ui.VideoConsole()
        self.video_console.pause_button.clicked.connect(self.video_status)

        self.gbox = QGridLayout()
        self.gbox.addWidget(self.video_wid, 1, 1)
        self.gbox.addWidget(self.video_console, 2, 1)

        self.main_wid = QWidget()
        self.main_wid.setLayout(self.gbox)
        self.setCentralWidget(self.main_wid)

        self.statusBar()
        open_vid = QAction('打开视频', self)
        open_vid.triggered.connect(self.open_video)
        open_vid.setShortcut('Ctrl+O')

        # 添加File菜单&子菜单
        file_menubar = self.menuBar()
        file_menu = file_menubar.addMenu('文件')
        file_menu.addAction(open_vid)

        self.show()

    def open_video(self):
        # 调用存储文件
        file_name, tmp = QFileDialog.getOpenFileName(self, '打开视频', 'video.mp4', '*.mp4')
        if file_name == '':
            return
        self.play_video(file_name)

    def play_video(self, url):
        self.vid_player = QMediaPlayer()
        self.vid_player.setVideoOutput(self.video_wid)
        self.vid_player.setMedia(QMediaContent(QUrl.fromLocalFile(url)))
        self.vid_status = True
        self.vid_player.play()

    def video_status(self):
        if self.vid_status is True:
            self.vid_player.pause()
            self.vid_status = False
        else:
            self.vid_player.play()
            self.vid_status = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())
