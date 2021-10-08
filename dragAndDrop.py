from tkinter import *
import os, sys

moveType = True
movePhase = 0
boxXList = [0, 770, 770, 0, 0, 720, 720, 50, 50, 670, 670, 100]
boxYList = [0, 0, 250, 250, 50, 50, 200, 200, 100, 100, 150, 150]


def drag_start(event):
    """ On click cBox function

            Parameters:
            event: object clicked

            Return type:

            Description:
            Start of moving the click box
        """
    widget = event.widget
    # widget.startX = event.x
    widget.startX = cBox.winfo_x()
    widget.startY = cBox.winfo_y()


def drag_motion(event):
    """ Drag motion of box clicked

            Parameters:
            event: object clicked

            Return type:

            Description:
            Moves the box based on arrow location on a X/Y plane
            Disable box from moving past start and end points
        """
    widget = event.widget
    global moveType
    Misc.lift(greyBox)
    Misc.lift(cBox)
    # Alternate slide type
    if moveType:  # Move Horizontally
        x = cBox.winfo_x() + event.x
        # Depending on which phase, the cBox check the start and end points
        if movePhase == 0 or movePhase == 4 or movePhase == 8:
            if x <= boxXList[movePhase]:
                cBox.place(x=boxXList[movePhase])
            elif x <= boxXList[movePhase + 1]:
                cBox.place(x=x)
            else:
                cBox.place(x=boxXList[movePhase + 1])
        elif movePhase == 2 or movePhase == 6 or movePhase == 10:
            if x >= boxXList[movePhase]:
                cBox.place(x=boxXList[movePhase])
            elif x >= boxXList[movePhase + 1]:
                cBox.place(x=x)
            else:
                cBox.place(x=boxXList[movePhase + 1])
    else:  # Move Vertically

        y = cBox.winfo_y() + event.y
        if movePhase == 1 or movePhase == 5 or movePhase == 9:
            if y <= boxYList[movePhase]:
                cBox.place(y=boxYList[movePhase])
            elif y <= boxYList[movePhase + 1]:
                cBox.place(y=y)
            else:
                cBox.place(y=boxYList[movePhase + 1])
        elif movePhase == 3 or movePhase == 7 or movePhase == 11:
            if y >= boxYList[movePhase]:
                cBox.place(y=boxYList[movePhase])
            elif y >= boxYList[movePhase + 1]:
                cBox.place(y=y)
            else:
                cBox.place(y=boxYList[movePhase + 1])


def drag_stop(event):
    """ Drag stop motion of box

                Parameters:
                event: object clicked

                Return type:

                Description:
                Function to update positions based on the final location of click box
                Updates click nbox, arrows, label and grey box position
            """
    global moveType
    global movePhase
    box_update = False
    x = cBox.winfo_x()
    y = cBox.winfo_y()
    box_update = update_cbox(box_update, x, y)
    if box_update:
        update_arrow(x, y)
        update_label(x, y)
        update_gbox(x, y)
    if movePhase == 9:
        Misc.lift(imgCanvasD)


def update_cbox(box_update, x, y):
    """ Updating click box x/y

                Parameters:
                box_update: Boolean true/false based on whether box needs to be move to next phase
                x: int x-coordinates of box
                y: int y-coordinates of box

                Return type:
                box_update: Boolean returns if box updated or not

                Description:
                Updates cbox and update status based on current x and y position of box afterwhich
                returns box update status
            """
    box_update = box_update
    x = x
    y = y
    if movePhase == 0 and boxXList[movePhase + 1] - 20 < x < boxXList[movePhase + 1] + 20 \
            and moveType:
        cBox.place(x=boxXList[movePhase + 1])
        box_update = not box_update
    elif (movePhase == 4 or movePhase == 8) and boxXList[movePhase + 1] - 20 < x < boxXList[movePhase + 1] + 20 \
            and moveType:
        cBox.place(x=boxXList[movePhase + 1])
        box_update = not box_update
    elif (movePhase == 1 or movePhase == 5 or movePhase == 9) and boxYList[movePhase + 1] - 20 < y < boxYList[
        movePhase + 1] + 20 \
            and not moveType:
        cBox.place(y=boxYList[movePhase + 1])
        box_update = not box_update
    elif (movePhase == 2 or movePhase == 6 or movePhase == 10) and boxXList[movePhase + 1] - 20 < x < boxXList[
        movePhase + 1] + 20 \
            and moveType:
        cBox.place(x=boxXList[movePhase + 1])
        box_update = not box_update
    elif (movePhase == 3 or movePhase == 7) and boxYList[movePhase + 1] - 20 < y < boxYList[movePhase + 1] + 20 \
            and not moveType:
        cBox.place(y=boxYList[movePhase + 1])
        box_update = not box_update
    elif moveType:
        cBox.place(x=boxXList[movePhase])
    else:
        cBox.place(y=boxYList[movePhase])
    return box_update


def update_arrow(x, y):
    """ Update arrow x/y

                    Parameters:
                    x: int x-coordinates of box
                    y: int y-coordinates of box

                    Return type:

                    Description:
                    Updates arrow based on current x and y position of box and move phase
                """
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
    """ Update label x/y

                        Parameters:
                        x: int x-coordinates of box
                        y: int y-coordinates of box

                        Return type:

                        Description:
                        Updates label's text and alignment based on current x and y position of box and move phase
                    """
    global movePhase
    x = x
    y = y
    if movePhase + 2 != len(boxXList):
        label.place(x=labelX[movePhase + 1], y=labelY[movePhase + 1])
        if movePhase % 2 != 0:  # change text and change justify to right or left depending on phase
            label.config(text=textArray[0])
            if movePhase == 1 or movePhase == 5 or movePhase == 9:  # Left Arrow
                label.config(justify='right')
            else:  # Right Arrow
                label.config(justify='left')
        else:  # change text and center align if phase is at up or down arrow
            label.config(text=textArray[1])
            label.config(justify='center')


def update_gbox(x, y):
    """ Update grey box x/y

                        Parameters:
                        x: int x-coordinates of box
                        y: int y-coordinates of box

                        Return type:

                        Description:
                        Updates grey box based on current x and y position of box and move phase
                    """
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


def last_phase():
    """ Last phase of movement

                        Parameters:

                        Return type:

                        Description:
                        Updates label, grey box and click box status
                    """
    greyBox.destroy()
    label.place(x=126 - (label.winfo_width() / 2), y=175 - (label.winfo_height() / 4))
    label.config(text="Final Case", font=("Roboto",6,"bold"), justify="center")
    label.lift()
    cBox.unbind("<Button-1>")
    cBox.unbind("<B1-Motion>")
    cBox.unbind("<ButtonRelease-1>")


# Screen Frame
window = Tk()
window.resizable(False, False)
window.geometry("820x300")  # Dimensions 2460x900 divide by 3
background = Canvas(window, height=300, width=820, bg="#ECF1F4")
background.place(x=-3, y=-3)

# Grey Box
greyBox = Frame(window, width=50, height=50, bg="#ECF1F4", highlightbackground="#9F9F9F", highlightthickness=3)
greyBox.place(x=boxXList[1], y=boxYList[1])

# Click Box
cBox = Frame(window, width=50, height=50, bg="#ECF1F4", highlightbackground="#1A1A1B",
             highlightthickness=3)  # Click-able Box
cBox.place(x=boxXList[0], y=boxYList[0])
cBox.bind("<Button-1>", drag_start)
cBox.bind("<B1-Motion>", drag_motion)
cBox.bind("<ButtonRelease-1>", drag_stop)

# Text Label
textArray = ["Drag & Drop\nhorizontally to\nthe next case", "Drag & Drop\nvertically to\nthe next case"]
label = Label(text=textArray[0], highlightthickness=0, bd=0, bg="#ECF1F4")
label.config(font=("Roboto", 5), justify='left')
labelX = [220 / 3 + 5, 775, 699, 5,
          220 / 3 + 5, 725, 649, 55,
          220 / 3 + 55, 675, 599]
labelY = [(40 / 3), 220 / 3 + 3, 265, 202,
          (40 / 3) + 53, (220 / 3) + 53, 215, 152,
          (40 / 3) + 103, (220 / 3) + 86, 165]
label.place(x=labelX[movePhase], y=labelY[movePhase])
window.update()  # IMP To allow arrows to be shown


#   R Arrow label at position 0,4,8
arrowX = [55, window.winfo_width() - 35, window.winfo_width() - 78, 15,
          55, window.winfo_width() - 85, window.winfo_width() - 128, 65,
          105, window.winfo_width() - 135, window.winfo_width() - 178]  # x = 53 - 3
arrowY = [50 / 3 - 3, 55, 267, window.winfo_height() - 75,
          50 / 3 + 49, 105, 217, window.winfo_height() - 125,
          50 / 3 + 99, 115, 167]


ar1 = os.path.join(os.path.dirname(sys.executable),'arrow_right.png')
ad1 = os.path.join(os.path.dirname(sys.executable),'arrow_down.png')
al1 = os.path.join(os.path.dirname(sys.executable),'arrow_left.png')
au1 = os.path.join(os.path.dirname(sys.executable),'arrow_up.png')
"""
Uncomment this path and comment the top variables to run on py 
ar1= "arrow_right.png"
ad1= "arrow_down.png"
al1= "arrow_left.png"
au1= "arrow_up.png"
"""
arrowR1 = PhotoImage(file=ar1)
arrowR2 = PhotoImage(file=ar1)
arrowD1 = PhotoImage(file=ad1)
arrowD2 = PhotoImage(file=ad1)
arrowL1 = PhotoImage(file=al1)
arrowL2 = PhotoImage(file=al1)
arrowU1 = PhotoImage(file=au1)
arrowU2 = PhotoImage(file=au1)

imgCanvasR = Canvas(window, width=(arrowR1.width() * 2), height=arrowR1.height(), bg="#ECF1F4",
                    highlightthickness=0)
imgCanvasR.create_image(0, 0, image=arrowR1, anchor="nw")
imgCanvasR.create_image(arrowR1.width(), 0, image=arrowR2, anchor="nw")
imgCanvasR.place(x=arrowX[movePhase], y=arrowY[movePhase])

imgCanvasD = Canvas(window, height=(arrowD1.height() * 2), width=arrowD1.width(), bg="#ECF1F4",
                    highlightthickness=0)
imgCanvasD.create_image(arrowD1.width() / 2, 5, image=arrowD1)
imgCanvasD.create_image(arrowD1.width() / 2, arrowD1.height() + 5, image=arrowD2)

imgCanvasL = Canvas(window, width=(arrowL1.width() * 2), height=arrowL1.height(), bg="#ECF1F4",
                    highlightthickness=0)
imgCanvasL.create_image(0, 0, image=arrowL2, anchor="nw")
imgCanvasL.create_image(arrowL1.width(), 0, image=arrowL2, anchor="nw")

imgCanvasU = Canvas(window, height=(arrowU1.height() * 2), width=arrowU1.width(), bg="#ECF1F4",
                    highlightthickness=0)
imgCanvasU.create_image(arrowD2.width() / 2, 5, image=arrowU1)
imgCanvasU.create_image(arrowD2.width() / 2, arrowD2.height() + 5, image=arrowU2)

Misc.lift(greyBox)
Misc.lift(cBox)
window.mainloop()
