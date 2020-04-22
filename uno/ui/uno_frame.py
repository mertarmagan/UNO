from time import sleep

from PIL import Image, ImageTk
from tkinter import Tk, BOTH, StringVar
from tkinter.ttk import Frame, Label, Style, LabelFrame, Button


def card_clicked(id):
    print("{} is pressed.".format(id))


def load_image(parent, card_id, path, x_coor, y_coor):
    img = Image.open(path)
    p_img = ImageTk.PhotoImage(img)

    label = Label(parent, image=p_img)
    label.image = p_img

    button = Button(parent, image=p_img, command=lambda: card_clicked(card_id))
    button.place(x=x_coor, y=y_coor)


class UnoFrame(Frame):

    def __init__(self):
        super().__init__()
        self.player1_group = LabelFrame(self.master, text="Player 1", labelanchor="n", borderwidth="50")
        self.cnt_p1 = Label(self.player1_group, text="# of cards:").pack(side="top")



        self.init_ui()

    def init_ui(self):
        self.master.title("UNO")
        self.grid()

        Style().configure("TFrame", background="#777")

        player2_group = LabelFrame(self.master, text="Player 2", labelanchor="n")
        player3_group = LabelFrame(self.master, text="Player 3", labelanchor="n")
        player4_group = LabelFrame(self.master, text="Player 4", labelanchor="n")
        center_group = LabelFrame(self.master, text="CENTER")

        self.player1_group.grid(row=2, column=0, columnspan=3, sticky="ew", padx=5, ipadx=300, ipady=150)
        player2_group.grid(row=1, column=2, sticky="ns")
        player3_group.grid(row=0, column=0, columnspan=3, sticky="ew", padx=5, ipadx=300)
        player4_group.grid(row=1, column=0, sticky="ns")
        center_group.grid(row=1, column=1, sticky="nsew")

        self.cnt_p2 = Label(player2_group, text="# of cards:").pack()
        self.cnt_p3 = Label(player3_group, text="# of cards:").pack()
        self.cnt_p4 = Label(player4_group, text="# of cards:").pack()

        pick_card_btn = Button(self.player1_group, text="DRAW")
        pick_card_btn.place(x=0, y=200)

    def draw_init(self, cards):
        for i in range(0, len(cards)):
            c_n = cards[i].getImageName()
            load_image(self.player1_group, c_n, "uno/ui/images/{}.png".format(c_n), i * 30 + 20, 0)

    """def change_num_label(self, label, num):
        label.config(text="# of cards: {}".format(num))"""


def run(game):
    root = Tk()

    w = 800  # width for the Tk root
    h = 800  # height for the Tk root

    # get screen width and height
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    # set the dimensions of the screen
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    app = UnoFrame()
    app.draw_init(game.players[0].cards)
    root.mainloop()
