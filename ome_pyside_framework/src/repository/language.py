from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTranslator
from enum import Enum

class Locale(Enum):
    '''
    使用 enum 型別方便管理語系
    '''
    us = 0
    tw = 1

class Language:
    @staticmethod
    def change_language(locale: Locale, current_widget):
        app = QApplication.instance()
        translator = QTranslator()
        app.installTranslator(translator)

        # 讀取 qm 檔案
        translator.load(f'language/{current_widget.ui.i18n_dictionary}_{locale.name}')

        # 更新畫面
        current_widget.ui.retranslateUi(current_widget)

        # 更新物件
        translator = QTranslator()
        app.installTranslator(translator)
        translator.load(f'language/{current_widget.i18n_dictionary}_{locale.name}')
        current_widget.retranslate()