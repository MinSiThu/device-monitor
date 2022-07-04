# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
# ( . >

import time
import psutil
import PySimpleGUI as sg

#    time.sleep(1)
def checkSystemStats():
    cpu_percent = str(psutil.cpu_percent())
    memory_percent = str(psutil.virtual_memory().percent)

layout = [
    [sg.Text]
]

while True:
