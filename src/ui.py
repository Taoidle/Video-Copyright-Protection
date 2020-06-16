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

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QSlider, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtCore import Qt


class VideoConsole(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('视频控制')
        self.play_slider = QSlider(Qt.Horizontal)
        self.retreat_button = QPushButton('快退')
        self.back_pic_button = QPushButton('上一帧')
        self.pause_button = QPushButton('暂停/开始')
        self.stop_button = QPushButton('停止')
        self.next_pic_button = QPushButton('下一帧')
        self.fast_button = QPushButton('快进')
        self.full_screen_button = QPushButton('全屏')
        self.max_screen_button = QPushButton('最大化/适中')

        self.button_hbox_1 = QHBoxLayout()
        self.button_hbox_1.addWidget(self.retreat_button)
        self.button_hbox_1.addWidget(self.back_pic_button)
        self.button_hbox_1.addWidget(self.next_pic_button)
        self.button_hbox_1.addWidget(self.fast_button)

        self.button_hbox_2 = QHBoxLayout()
        self.button_hbox_2.addWidget(self.pause_button)
        self.button_hbox_2.addWidget(self.stop_button)
        self.button_hbox_2.addWidget(self.max_screen_button)
        self.button_hbox_2.addWidget(self.full_screen_button)

        self.button_hbox_wid_1 = QWidget()
        self.button_hbox_wid_1.setLayout(self.button_hbox_1)

        self.button_hbox_wid_2 = QWidget()
        self.button_hbox_wid_2.setLayout(self.button_hbox_2)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.play_slider)
        self.vbox.addWidget(self.button_hbox_wid_1)
        self.vbox.addWidget(self.button_hbox_wid_2)
        self.setLayout(self.vbox)


class VideoInfo(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.security_status_label = QLabel('视频保护：')
        self.security_status_label.setMaximumHeight(20)
        self.security_status_show_label = QLabel('')
        self.security_status_show_label.setMaximumHeight(20)

        self.vid_time_len_label = QLabel('视频时长：')
        self.vid_time_len_label.setMaximumHeight(20)
        self.vid_time_len_show_label = QLabel('')
        self.vid_time_len_show_label.setMaximumHeight(20)

        self.vid_resolution_label = QLabel('分辨率：')
        self.vid_resolution_label.setMaximumHeight(20)
        self.vid_resolution_show_label = QLabel('')
        self.vid_resolution_show_label.setMaximumHeight(20)

        self.vid_fps_label = QLabel('帧率：')
        self.vid_fps_label.setMaximumHeight(20)
        self.vid_fps_show_label = QLabel('')
        self.vid_fps_show_label.setMaximumHeight(20)

        self.gbox = QGridLayout()
        self.gbox.setSpacing(0)
        self.gbox.addWidget(self.security_status_label, 1, 1)
        self.gbox.addWidget(self.security_status_show_label, 1, 2)
        self.gbox.addWidget(self.vid_time_len_label, 2, 1)
        self.gbox.addWidget(self.vid_time_len_show_label, 2, 2)
        self.gbox.addWidget(self.vid_resolution_label, 3, 1)
        self.gbox.addWidget(self.vid_resolution_show_label, 3, 2)
        self.gbox.addWidget(self.vid_fps_label, 4, 1)
        self.gbox.addWidget(self.vid_fps_show_label, 4, 2)
        self.setLayout(self.gbox)
