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

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QRadioButton, QSlider, QHBoxLayout, QVBoxLayout, QGridLayout, \
    QLineEdit, QFileDialog, QDesktopWidget
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


class SettingsWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.copyright_words_label = QLabel('版权文字信息')
        self.copyright_words_textline = QLineEdit(self)
        self.copyright_pic_label = QLabel('版权图片信息')
        self.copyright_pic_path = QLineEdit(self)
        self.copyright_pic_path_button = QPushButton('选择图片')
        # self.copyright_pic_path_button.clicked.connect(self.get_path)

        self.copyright_info_label = QLabel('版权保护设置')
        self.copyright_info_words = QRadioButton('版权文字')
        self.copyright_info_pic = QRadioButton('版权图片')
        self.copyright_info_words_pic = QRadioButton('版权文字+图片')
        self.copyright_info_hbox = QHBoxLayout()
        self.copyright_info_hbox.addWidget(self.copyright_info_words)
        self.copyright_info_hbox.addWidget(self.copyright_info_pic)
        self.copyright_info_hbox.addWidget(self.copyright_info_words_pic)
        self.copyright_info_hbox_wid = QWidget()
        self.copyright_info_hbox_wid.setLayout(self.copyright_info_hbox)

        self.check_hbox = QHBoxLayout()
        self.check_hbox_wid = QWidget()
        self.cancel_button = QPushButton('取消')
        self.cancel_button.clicked.connect(self.cancelEvent)
        self.ok_button = QPushButton('确定')
        self.ok_button.clicked.connect(self.closeEvent)
        self.check_hbox.addWidget(self.cancel_button)
        self.check_hbox.addWidget(self.ok_button)
        self.check_hbox_wid.setLayout(self.check_hbox)

        self.gbox = QGridLayout()
        self.gbox.addWidget(self.copyright_words_label, 1, 1, 1, 1)
        self.gbox.addWidget(self.copyright_words_textline, 2, 1, 1, 4)
        self.gbox.addWidget(self.copyright_pic_label, 3, 1)
        self.gbox.addWidget(self.copyright_pic_path, 4, 1, 1, 3)
        self.gbox.addWidget(self.copyright_pic_path_button, 4, 4, 1, 1)
        self.gbox.addWidget(self.copyright_info_label, 5, 1, 1, 1)
        self.gbox.addWidget(self.copyright_info_hbox_wid, 6, 1, 1, 4)
        self.gbox.addWidget(self.check_hbox_wid, 7, 1, 1, 4)

        self.setWindowTitle('设置')
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.setWindowModality(Qt.ApplicationModal)
        self.setLayout(self.gbox)
        self.show()
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def get_path(self):
        file_name, tmp = QFileDialog.getOpenFileName(self, '打开图片', 'picture', '*.png *.jpg *.bmp')
        if file_name == '':
            return
        self.copyright_pic_path.setText(file_name)

    def cancelEvent(self):
        self.close()

    def closeEvent(self, event):
        self.close()
