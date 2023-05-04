# OME PySide6 Framework
## Install
```shell
# 1. 安裝虛擬環境
py -m venv .venv

# 2. 執行虛擬環境
# linux/mac
source .venv/Scripts/activate
# windows
.venv\Scripts\activate

# 3.
py install.py

# 4.
py update.py

# 5.
py main.py
```


## 打包
1. 建立 .spec 檔案
2. pyinstaller_template.py 內容複製到 .spec
3. 執行pyinstaller
```shell
pyinstaller .spec
```

## .ui/.ts/.qm 更新
```shell
# 更新全部
py update.py

# 或者使用個別 qt 指令 pyside-uic / pyside-lupdate / pyside-lrelease
```