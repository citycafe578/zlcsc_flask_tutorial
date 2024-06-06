import pyautogui as pg
import time
#https://zlshcsc.github.io/
#查看螢幕的大小
print(pg.size())
time.sleep(3)
print(pg.position())
print(pg.onScreen(1000000, 51514515))

#移動滑鼠位置
pg.moveTo(500, 500)
while(True):
    pg.moveTo(500, 500)

#有關滑鼠點擊
pg.click()
pg.click(clicks=2, interval=0.5, button='right')
pg.dragTo(500, 500, duration=2, button='left')
pg.scroll(5)

#有關鍵盤點擊
pg.press('c')

pg.keyDown('ctrl')
pg.press('a')
pg.keyUp('ctrl')

#但如果有特殊功能要注意
pg.hotkey('ctrl', 'c')
pg.hotkey('ctrl', 'v')
pg.hotkey('ctrl', 'shift', 'esc')

#你還可以截圖
#但是要先pip
#pip install pyscreeze pillow
pg.screenshot('1.png')
pg.screenshot('1.png', region=(0,0, 300, 400))