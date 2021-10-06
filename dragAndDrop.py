from tkinter import *
from PIL import ImageTk, Image

moveType = True
movePhase = 0
boxXList = [0, 770, 770, 0, 0, 720, 720, 50, 50, 670, 670, 100]
boxYList = [0, 0, 250, 250, 50, 50, 200, 200, 100, 100, 150, 150]
arrowTopLeftX = 10 / 3  # Distance from side of box
arrow2TopLeftX = 25 / 3
arrowTopLeftY = 50 / 3  # Distance from corner of border


def drag_start(event):
    widget = event.widget
    # widget.startX = event.x
    widget.startX = cBox.winfo_x()
    widget.startY = cBox.winfo_y()


def drag_motion(event):
    widget = event.widget
    global moveType
    # Alternate slide type
    if moveType:  # Move Horizontally
        x = cBox.winfo_x() + event.x
        cBox.place(x=x)
    else:  # Move Vertically
        y = cBox.winfo_y() + event.y
        cBox.place(y=y)


# Update cbox, arrow and gbox
def drag_stop(event):
    widget = event.widget
    global moveType
    global movePhase
    box_update = False
    x = cBox.winfo_x()
    y = cBox.winfo_y()
    box_update = update_cBox(box_update, x, y)
    if(box_update):
        update_arrow(x, y)
        update_label(x, y)
        update_gBox(x, y)


# Gets boxUpdate and box X and Y
# Updates cbox location
# Returns box update status
def update_cBox(box_update, x, y):
    box_update = box_update
    x = x
    y = y
    if movePhase == 0 and boxXList[movePhase + 1] - 20 < x < boxXList[movePhase + 1] + 20 \
            and moveType:
        cBox.place(x=boxXList[movePhase + 1])
        imgCanvasD.place(x=arrowX[movePhase + 1], y=arrowY[movePhase + 1])
        box_update = not box_update
    elif (movePhase == 4 or movePhase == 8) and boxXList[movePhase + 1] - 20 < x < boxXList[movePhase + 1] + 20 \
            and moveType:
        cBox.place(x=boxXList[movePhase + 1])
        imgCanvasD.place(x=arrowX[movePhase + 1], y=arrowY[movePhase + 1])
        box_update = not box_update
    elif (movePhase == 1 or movePhase == 5 or movePhase == 9) and boxYList[movePhase + 1] - 20 < y < boxYList[
        movePhase + 1] + 20 \
            and not moveType:
        cBox.place(y=boxYList[movePhase + 1])
        imgCanvasL.place(x=arrowX[movePhase + 1], y=arrowY[movePhase + 1])
        box_update = not box_update
    elif (movePhase == 2 or movePhase == 6 or movePhase == 10) and boxXList[movePhase + 1] - 20 < x < boxXList[
        movePhase + 1] + 20 \
            and moveType:
        cBox.place(x=boxXList[movePhase + 1])
        if movePhase + 2 != len(boxXList):
            imgCanvasU.place(x=arrowX[movePhase + 1], y=arrowY[movePhase + 1])
        box_update = not box_update
    elif (movePhase == 3 or movePhase == 7) and boxYList[movePhase + 1] - 20 < y < boxYList[movePhase + 1] + 20 \
            and not moveType:
        cBox.place(y=boxYList[movePhase + 1])
        imgCanvasR.place(x=arrowX[movePhase + 1], y=arrowY[movePhase + 1])
        box_update = not box_update
    elif moveType:
        cBox.place(x=boxXList[movePhase])
    else:
        cBox.place(y=boxYList[movePhase])
    return box_update


# update arrow positions
def update_arrow(x, y):
    global movePhase
    x = x
    y = y
    imgCanvasU.itemconfigure(1, state='hidden')
    imgCanvasU.itemconfigure(2, state='hidden')
    imgCanvasD.itemconfigure(1, state='hidden')
    imgCanvasD.itemconfigure(2, state='hidden')
    imgCanvasL.itemconfigure(1, state='hidden')
    imgCanvasL.itemconfigure(2, state='hidden')
    imgCanvasR.itemconfigure(1, state='hidden')
    imgCanvasR.itemconfigure(2, state='hidden')
    if movePhase == 0 and boxXList[movePhase + 1] - 20 < x < boxXList[movePhase + 1] + 20 \
            and moveType:
        imgCanvasD.itemconfigure(1, state='normal')
        imgCanvasD.itemconfigure(2, state='normal')
        imgCanvasD.place(x=arrowX[movePhase + 1], y=arrowY[movePhase + 1])
    elif (movePhase == 4 or movePhase == 8) and boxXList[movePhase + 1] - 20 < x < boxXList[movePhase + 1] + 20 \
            and moveType:
        imgCanvasD.itemconfigure(1, state='normal')
        imgCanvasD.itemconfigure(2, state='normal')
        imgCanvasD.place(x=arrowX[movePhase + 1], y=arrowY[movePhase + 1])
    elif (movePhase == 1 or movePhase == 5 or movePhase == 9) and boxYList[movePhase + 1] - 20 < y < boxYList[
        movePhase + 1] + 20 \
            and not moveType:
        imgCanvasL.itemconfigure(1, state='normal')
        imgCanvasL.itemconfigure(2, state='normal')
        imgCanvasL.place(x=arrowX[movePhase + 1], y=arrowY[movePhase + 1])
    elif (movePhase == 2 or movePhase == 6 or movePhase == 10) and boxXList[movePhase + 1] - 20 < x < boxXList[
        movePhase + 1] + 20 \
            and moveType:
        if movePhase + 2 != len(boxXList):
            imgCanvasU.itemconfigure(1, state='normal')
            imgCanvasU.itemconfigure(2, state='normal')
            imgCanvasU.place(x=arrowX[movePhase + 1], y=arrowY[movePhase + 1])
    elif (movePhase == 3 or movePhase == 7) and boxYList[movePhase + 1] - 20 < y < boxYList[movePhase + 1] + 20 \
            and not moveType:
        imgCanvasR.itemconfigure(1, state='normal')
        imgCanvasR.itemconfigure(2, state='normal')
        imgCanvasR.place(x=arrowX[movePhase + 1], y=arrowY[movePhase + 1])


# updateLabel
def update_label(x, y):
    global movePhase
    x = x
    y = y
    if movePhase + 2 != len(boxXList):
        label.place(x=labelX[movePhase + 1], y=labelY[movePhase + 1])
        if movePhase % 2 != 0:
            label.config(text=textArray[0])
            print(movePhase)
        else:
            label.config(text=textArray[1])


# Moves gbox around and call last phase if end of array
def update_gBox(x, y):
    global moveType
    global movePhase
    x = x
    y = y
    if movePhase + 2 != len(boxXList):
        if moveType:  # Horizontally
            greyBox.place(y=boxYList[movePhase + 2])
        elif not moveType:  # Vertically
            greyBox.place(x=boxXList[movePhase + 2])
        movePhase += 1
        moveType = not moveType
    elif (movePhase + 2) == len(boxXList):  # Removes all functions post final case
        last_phase()


# Sets last phase process
# Unbind cBox, remove old labels and arrows
def last_phase():
    greyBox.destroy()
    label.destroy()
    cBox.unbind("<Button-1>")
    cBox.unbind("<B1-Motion>")
    cBox.unbind("<ButtonRelease-1>")


# Screen Frame
window = Tk()
window.resizable(False, False)
window.geometry("820x300")  # Dimensions 2460x900 divide by 3
background = Canvas(window, height=300, width=820, bg="#ECF1F4")
background.place(x=-3, y=-3)

greyBox = Frame(window, width=50, height=50, bg="#ECF1F4", highlightbackground="#9F9F9F", highlightthickness=5)
greyBox.place(x=boxXList[1], y=boxYList[1])

cBox = Frame(window, width=50, height=50, bg="#ECF1F4", highlightbackground="#1A1A1B",
             highlightthickness=5)  # Clickable Box
cBox.place(x=boxXList[0], y=boxYList[0])
cBox.bind("<Button-1>", drag_start)
cBox.bind("<B1-Motion>", drag_motion)
cBox.bind("<ButtonRelease-1>", drag_stop)

# Text Label
textArray = ["Drag & Drop\nhorizontally to\nthe next case", "Drag & Drop\nvertically to\nthe next case"]
label = Label(text=textArray[0], highlightthickness=0, bd=0, bg="#ECF1F4")
label.config(font=("Roboto", 5), justify='left')
labelX = [220 / 3 + 5, 775, 697, 5,
          220 / 3 + 5, 725, 647, 55,
          220 / 3 + 55, 670, 597]
labelY = [(40 / 3), 220/3+3, 265, 202,
          (40 / 3) + 53, (220/3)+53, 215, 152,
          (40 / 3) + 103, (220/3)+103, 165]
label.place(x=labelX[movePhase], y=labelY[movePhase])
window.update()  # IMP To allow arrows to be shown
#   R Arrow label at position 0,4,8
arrowX = [52, window.winfo_width() - 53, window.winfo_width() - 82, -4,
          52, window.winfo_width() - 103, window.winfo_width() - 132, 46,
          102, 0, window.winfo_width() - 178]  # x = 53 - 3
arrowY = [50 / 3 - 23, 50, 247, window.winfo_height() - 78,
          50 / 3 + 30, 100, 197, window.winfo_height() - 128,
          50 / 3 + 80, 0, 147]
arrowR1 = PhotoImage(file="arrow_right.png")
arrowR2 = PhotoImage(file="arrow_right.png")
arrowD1 = PhotoImage(file="arrow_down.png")
arrowD2 = PhotoImage(file="arrow_down.png")
arrowL1 = PhotoImage(file="arrow_left.png")
arrowL2 = PhotoImage(file="arrow_left.png")
arrowU1 = PhotoImage(file="arrow_up.png")
arrowU2 = PhotoImage(file="arrow_up.png")

imgCanvasR = Canvas(window, width=(arrowR1.width() * 2) + 4, height=arrowR1.height() + 20, bg="#ECF1F4",
                    highlightthickness=0)
imgCanvasR.create_image(10, arrowR1.height() + 10, image=arrowR1)
imgCanvasR.create_image(arrowR1.width() + 10, arrowR1.height() + 10, image=arrowR2)
imgCanvasR.place(x=arrowX[movePhase], y=arrowY[movePhase])

imgCanvasD = Canvas(window, height=(arrowD1.height() * 2) + 4, width=arrowD1.width() + 20, bg="#ECF1F4",
                    highlightthickness=0)
imgCanvasD.create_image(arrowD1.width() + 10, 10, image=arrowD1)
imgCanvasD.create_image(arrowD1.width() + 10, arrowD1.height() + 10, image=arrowD2)

imgCanvasL = Canvas(window, width=(arrowL1.width() * 2) + 4, height=arrowL1.height() + 20, bg="#ECF1F4",
                    highlightthickness=0)
imgCanvasL.create_image(10, arrowL1.height() + 10, image=arrowL1)
imgCanvasL.create_image(arrowL1.width() + 10, arrowL1.height() + 10, image=arrowL2)

imgCanvasU = Canvas(window, height=(arrowU1.height() * 2) + 4, width=arrowU1.width() + 20, bg="#ECF1F4",
                    highlightthickness=0)
imgCanvasU.create_image(arrowU1.width() + 10, 10, image=arrowU1)
imgCanvasU.create_image(arrowU1.width() + 10, arrowU1.height() + 10, image=arrowU2)

Misc.lift(greyBox)
Misc.lift(cBox)
window.mainloop()
