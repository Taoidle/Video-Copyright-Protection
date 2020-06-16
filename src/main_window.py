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

import sys, ui, cv2
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaMetaData
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QMainWindow, QGridLayout, QVBoxLayout, QAction


class MainWindow(QMainWindow):
    vid_status = False

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.video_wid = QVideoWidget()
        self.video_wid.setMinimumSize(360, 240)
        self.vid_player = QMediaPlayer()

        self.video_console = ui.VideoConsole()
        self.video_console.pause_button.clicked.connect(self.video_status)
        self.video_console.pause_button.setShortcut('space')
        self.video_console.stop_button.clicked.connect(self.video_stop)

        self.video_info = ui.VideoInfo()

        self.gbox = QGridLayout()
        self.gbox.addWidget(self.video_wid, 1, 1, 1, 2)
        self.gbox.addWidget(self.video_console, 2, 1)
        self.gbox.addWidget(self.video_info, 2, 2)

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
        self.vid_reader = cv2.VideoCapture(url)
        ret_tmp, tmp = self.vid_reader.read()
        tmp_height, tmp_width, tmp_channel = tmp.shape
        vid_time_sum = self.vid_reader.get(cv2.CAP_PROP_FRAME_COUNT) / self.vid_reader.get(
            cv2.CAP_PROP_FPS) / 60
        vid_time_min = self.vid_reader.get(cv2.CAP_PROP_FRAME_COUNT) / self.vid_reader.get(
            cv2.CAP_PROP_FPS) // 60
        vid_time_sec = (vid_time_sum - vid_time_min) * 60
        self.video_info.vid_time_len_show_label.setText(str(int(vid_time_min)) + '分' + str(int(vid_time_sec)) + '秒')
        self.video_info.vid_resolution_show_label.setText(str(tmp_width) + ' x ' + str(tmp_height))
        self.video_info.vid_fps_show_label.setText(str(round(self.vid_reader.get(cv2.CAP_PROP_FPS), 2)))
        self.video_wid.setMinimumSize(tmp_width, tmp_height)
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

    def video_stop(self):
        self.vid_player.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())
