from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QAction
from PySide6.QtCore import Slot, Signal, QCoreApplication, QUrl
from PySide6.QtMultimedia import QSoundEffect
from src.repository.language import Language, Locale
from src.video_window import MainWindow as VideoWindow
from ui_py.main_window import Ui_MainWindow as Window


class MainWindow(QMainWindow):
    i18n_dictionary = 'src_main_window'
    video_window = None

    shutdown_message = 'Shutdown ?'
    restart_message = 'Restart ?'

    def __init__(self):
        super().__init__()
        self.setGeometry(600, 100, 700, 700)
        self.ui = Window()
        self.ui.setupUi(self)
        self.ui.i18n_dictionary = 'ui_main_window'

        self.ui.menu_language.triggered.connect(self.change_language)
        Language.change_language(Locale.tw, self)

        self.sound_effect = QSoundEffect()
        self.ui.button_sound_play.released.connect(self.click_sound_play)
        self.ui.button_video_play.released.connect(self.click_video_play)

        self.ui.button_restart.released.connect(self.click_restart)
        self.ui.button_shut_down.released.connect(self.click_shutdown)

    @Slot()
    def click_shutdown(self):
        import os
        reply = QMessageBox.critical(
            self, 'Shutdown', self.shutdown_message, QMessageBox.Yes | QMessageBox.Abort, QMessageBox.Abort)
        if reply == QMessageBox.Yes:
            os.system('shutdown /s /t 1')

    @Slot()
    def click_restart(self):
        import os
        reply = QMessageBox.critical(
            self, 'Restart', self.restart_message, QMessageBox.Yes | QMessageBox.Abort, QMessageBox.Abort)
        if reply == QMessageBox.Yes:
            os.system('shutdown /r /t 1')

    @Slot()
    def click_video_play(self):
        available_geometry = self.screen().availableGeometry()
        self.video_window = VideoWindow()
        self.video_window.resize(
            available_geometry.width() / 3, available_geometry.height() / 2)
        self.video_window.show()

    @Slot()
    def click_sound_play(self):
        volume = self.ui.slider_sound_effect.value() / 100  # volume 0.0 ~ 1.0
        self.sound_effect.setSource(
            QUrl.fromLocalFile('resource/sound/alert.wav'))
        self.sound_effect.setVolume(volume)
        self.sound_effect.play()

    @Slot(QAction)
    def change_language(self, action: QAction):
        # todo: 語言跟當前相同時不更新
        selected_locale = action.objectName()[7:]
        Language.change_language(Locale[selected_locale], self)

    def retranslate(self):
        ''' 切換語系的資料需要在這集中重新翻譯 '''
        self.name = QCoreApplication.translate('MainWindow', 'LANGUAGE')

    def get_image_path(self, ui_relative_path: str):
        '''
        QtDesigner 只能從.ui 檔案開啟的位置取得圖片路徑
        通過 form setting 可以指定 founction 在程式執行時替換路徑
        '''
        # print(ui_relative_path[1:], flush=True)
        # ./resource/image/logo.png
        return ui_relative_path[1:]
