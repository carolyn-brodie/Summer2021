from tkinter import *
from PIL import Image

basewidth = 300

img = Image.open('/Users/zachg/PycharmProjects/Summer2021a/summer_work/Graphs/BME.png')

wpercent = (basewidth / float(img.size[0]))

hsize = int((float(img.size[1]) * float(wpercent)))

img = img.resize((basewidth, hsize), Image.ANTIALIAS)

img.save('/Users/zachg/PycharmProjects/Summer2021a/summer_work/Graphs/BME.png')




root = Tk()
canvas = Canvas(root, width=500, height=500)
canvas.pack()
# img = PhotoImage(file='/Users/zachg/PycharmProjects/Summer2021a/BME.png')
img = PhotoImage(file='/Users/zachg/PycharmProjects/Summer2021a/summer_work/Graphs/BME.png')
canvas.create_image(250, 250, image=img)
root.mainloop()