import numpy as np
import sys
import toka     
import webcam
from grabcut import App

#写真を出力したい場所（パス名）
filename_Output = "/Users/uboT/Documents/Python/OpenCV/4trim/Code/Output/Output.png"

#とった写真を保存する
webcam.webcam(filename_Output)

#マスク画像の生成
grabcut=App()
grabcut.run(filename_Output)

#撮った写真を透過してOutputに出力する
toka.toka(filename_Output)
