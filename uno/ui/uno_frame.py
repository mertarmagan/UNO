from time import sleep

from PIL import Image, ImageTk
from tkinter import Tk, BOTH, StringVar, DISABLED, NORMAL
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
        self.player1_group, self.player2_group, self.player3_group, self.player4_group, self.center_group = None, None, None, None, None
        self.players = []
        self.cnt_p1, self.cnt_p2, self.cnt_p3, self.cnt_p4 = None, None, None, None
        self.blue_btn, self.pick_card_btn, self.red_btn, self.yellow_btn, self.green_btn = None, None, None, None, None
        self.buttons = []
        self.init_ui()

    def init_ui(self):
        self.master.title("UNO")
        self.grid()

        Style().configure("Highlight.TFrame", background='#32CD32')
        Style().configure("Default.TFrame", background='white')
        Style().configure("Center.TFrame", background='red')

        self.create_frames()
        self.create_labels()
        self.create_buttons()

    def draw_hand(self, cards):
        for i in range(0, len(cards)):
            c_n = cards[i].getImageName()
            load_image(self.player1_group, c_n, "uno/ui/images/{}.png".format(c_n), i * 30 + 20, 0)

    def create_buttons(self):
        self.pick_card_btn = Button(self.player1_group, text="DRAW")
        self.red_btn = Button(self.player1_group, text="RED")
        self.yellow_btn = Button(self.player1_group, text="YELLOW")
        self.green_btn = Button(self.player1_group, text="GREEN")
        self.blue_btn = Button(self.player1_group, text="BLUE")

        self.pick_card_btn.pack(side="left")
        self.red_btn.pack(side="right")
        self.yellow_btn.pack(side="right")
        self.green_btn.pack(side="right")
        self.blue_btn.pack(side="right")

        self.buttons = [self.blue_btn, self.red_btn, self.yellow_btn, self.green_btn]

    def create_frames(self):
        self.player1_group = LabelFrame(self.master, text="Player 1", labelanchor="n", style="Default.TFrame",
                                        borderwidth="50")
        self.player2_group = LabelFrame(self.master, text="Player 2", labelanchor="n", style="Default.TFrame")
        self.player3_group = LabelFrame(self.master, text="Player 3", labelanchor="n", style="Default.TFrame")
        self.player4_group = LabelFrame(self.master, text="Player 4", labelanchor="n", style="Default.TFrame")
        self.center_group = LabelFrame(self.master, text="CENTER", labelanchor="n", style="Center.TFrame")

        self.player1_group.grid(row=2, column=0, columnspan=3, sticky="nsew", ipadx=300, ipady=150)
        self.player2_group.grid(row=1, column=2, sticky="nsew")
        self.player3_group.grid(row=0, column=0, columnspan=3, sticky="nsew", ipadx=300)
        self.player4_group.grid(row=1, column=0, sticky="nsew")
        self.center_group.grid(row=1, column=1, sticky="nsew", ipadx=50, ipady=80)

        self.players = [self.player1_group, self.player2_group, self.player3_group, self.player4_group]

    def create_labels(self):
        self.cnt_p1 = Label(self.player1_group, text="# of cards:").pack(side="top")
        self.cnt_p2 = Label(self.player2_group, text="# of cards:").pack()
        self.cnt_p3 = Label(self.player3_group, text="# of cards:").pack()
        self.cnt_p4 = Label(self.player4_group, text="# of cards:").pack()

    def highlight_player(self, cur_player_i):
        for i in range(len(self.players)):
            if i == cur_player_i:
                self.players[i].configure(style="Highlight.TFrame")
            else:
                self.players[i].configure(style="Default.TFrame")

    def update_cur_card(self, card):
        cur_card = card.getImageName()
        load_image(self.center_group, cur_card, "uno/ui/images/{}.png".format(cur_card), 30, 30)

    def toggle_color_buttons(self):
        for i in range(len(self.buttons)):
            state = str(self.buttons[i]["state"])
            if state == "disabled":
                self.buttons[i].config(state=NORMAL)
            if state == "normal":
                self.buttons[i].config(state=DISABLED)


def run(game):
    root = Tk()

    w = 1024  # width for the Tk root
    h = 768  # height for the Tk root

    # get screen width and height
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    # set the dimensions of the screen
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # game.players[0].print_hand()
    app = UnoFrame()

    app.draw_hand(game.players[0].cards)

    game.players[0].draw_card(game.deck.draw_card(game.draw_pile))
    app.draw_hand(game.players[0].cards)

    # app.toggle_color_buttons()

    app.highlight_player(1)
    app.update_cur_card(game.get_current_card())

    root.mainloop()
