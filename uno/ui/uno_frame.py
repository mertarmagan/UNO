from PIL import Image, ImageTk
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Style, LabelFrame, Button
import tkinter as tk


class UnoFrame(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.master.title("UNO")
        self.grid()

        Style().configure("TFrame", background="#777")

        player1_group = LabelFrame(
            self.master, text="Player 1", labelanchor="n", borderwidth="50")
        player2_group = LabelFrame(
            self.master, text="Player 2", labelanchor="n")
        player3_group = LabelFrame(
            self.master, text="Player 3", labelanchor="n")
        player4_group = LabelFrame(
            self.master, text="Player 4", labelanchor="n")
        center_group = LabelFrame(self.master, text="CENTER")

        player1_group.grid(row=2, column=0, columnspan=3,
                           sticky="ew", padx=5, ipadx=300, ipady=150)
        player2_group.grid(row=1, column=2, sticky="ns")
        player3_group.grid(row=0, column=0, columnspan=3,
                           sticky="ew", padx=5, ipadx=300)
        player4_group.grid(row=1, column=0, sticky="ns")
        center_group.grid(row=1, column=1, sticky="nsew")

        label1 = Label(player1_group, text="# of cards:")
        label2 = Label(player2_group, text="# of cards:").pack()
        label3 = Label(player3_group, text="# of cards:").pack()
        label4 = Label(player4_group, text="# of cards:").pack()

        self.loadImage(player1_group, "blue_0", "uno/images/blue_0.png", 10, 0)
        self.loadImage(player1_group, "blue_1", "uno/images/blue_1.png", 35, 0)

    def loadImage(self, parent, card_id, path, x_coor, y_coor):
        img = Image.open(path)
        p_img = ImageTk.PhotoImage(img)
        label = Label(parent, image=p_img)
        label.image = p_img
        #label.place(x=x_coor, y=y_coor)

        button = Button(parent, image=p_img,
                        command=lambda: self.cardClicked(card_id))
        button.place(x=x_coor, y=y_coor)

    def cardClicked(self, id):
        print("{} is pressed.".format(id))


def main():

    root = Tk()

    w = 800  # width for the Tk root
    h = 800  # height for the Tk root

    # get screen width and height
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # set the dimensions of the screen
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    app = UnoFrame()
    root.mainloop()


if __name__ == '__main__':
    main()
