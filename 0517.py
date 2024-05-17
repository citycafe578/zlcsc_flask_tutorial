import pyautogui as pg
from tkinter import*
# pg.moveTo(500, 500)
# pg.click(clicks=2, interval=0.5, button='right')
# pg.press('c')

# pg.keyDown('ctrl')
# pg.press('a')
# pg.keyUp('ctrl')

# pg.dragTo(100, 100)

# print(pg.position())
# print(pg.size())


window = Tk()
window.title("安安")
window.minsize(width = 500, height = 500)
window.resizable(width = False, height = False)
label = Label(text="安安", font = ("times new roman", 18))
label2 = Label(text="我好餓", font = ("times new roman", 18), padx = 10, pady = 15, bg = "green", fg = "purple")
label.pack()
label2.pack()
window.mainloop()