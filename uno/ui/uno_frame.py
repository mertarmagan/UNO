# -*- coding: utf-8 -*-
import threading
from tkinter import DISABLED, NORMAL, StringVar, Tk
from tkinter.ttk import Button, Frame, Label, LabelFrame, Style

from PIL import Image, ImageTk

from uno.player import HumanPlayer


class UnoFrame(Frame):
    def __init__(self):
        super().__init__()
        self.current_aval = []
        self.text0 = StringVar()
        self.text1 = StringVar()
        self.text2 = StringVar()
        self.text3 = StringVar()
        self.texts = [self.text0, self.text1, self.text2, self.text3]
        (
            self.player1_group,
            self.player2_group,
            self.player3_group,
            self.player4_group,
            self.center_group,
        ) = (None, None, None, None, None)
        self.players = []
        self.cnt_p1, self.cnt_p2, self.cnt_p3, self.cnt_p4 = None, None, None, None
        self.labels = []
        (
            self.blue_btn,
            self.pick_card_btn,
            self.red_btn,
            self.yellow_btn,
            self.green_btn,
        ) = (None, None, None, None, None)
        self.buttons = []
        self.card_buttons = []
        self.color_event = threading.Event()
        self.event = threading.Event()
        self.card_input = -1
        self.color_input = -1

        self.init_ui()

    def init_ui(self):
        self.master.title("UNO")
        self.grid()

        Style().configure("Highlight.TFrame", background="#32CD32")
        Style().configure("Default.TFrame", background="white")
        Style().configure("Center.TFrame", background="red")

        self.create_frames()
        self.create_labels()
        self.create_buttons()

    def show_hand(self, cards, aval_cards, cur_player):
        self.event.clear()
        self.color_event.clear()
        self.current_aval = aval_cards
        for i in range(len(self.card_buttons)):
            self.card_buttons[i].destroy()
        self.card_buttons.clear()
        for i in range(len(cards)):
            c_n = cards[i].get_image_name()
            self.load_image(
                self.player1_group,
                c_n,
                "uno/ui/images/{}.png".format(c_n),
                i * 30 + 20,
                0,
                False,
            )
            if cards[i] not in aval_cards or not isinstance(cur_player, HumanPlayer):
                self.card_buttons[i].config(state=DISABLED)
            else:
                self.card_buttons[i].config(state=NORMAL)

    def create_buttons(self):
        self.red_btn = Button(
            self.player1_group,
            text="RED",
            command=lambda: self.color_clicked("red"),
            state=DISABLED,
        )
        self.green_btn = Button(
            self.player1_group,
            text="GREEN",
            command=lambda: self.color_clicked("green"),
            state=DISABLED,
        )
        self.blue_btn = Button(
            self.player1_group,
            text="BLUE",
            command=lambda: self.color_clicked("blue"),
            state=DISABLED,
        )
        self.yellow_btn = Button(
            self.player1_group,
            text="YELLOW",
            command=lambda: self.color_clicked("yellow"),
            state=DISABLED,
        )

        self.red_btn.pack(side="left")
        self.green_btn.pack(side="left")
        self.blue_btn.pack(side="left")
        self.yellow_btn.pack(side="left")

        self.buttons = [self.red_btn, self.green_btn, self.blue_btn, self.yellow_btn]

    def create_frames(self):
        self.player1_group = LabelFrame(
            self.master,
            text="Player 0",
            labelanchor="n",
            style="Default.TFrame",
            borderwidth="50",
        )
        self.player2_group = LabelFrame(
            self.master, text="Player 1", labelanchor="n", style="Default.TFrame"
        )
        self.player3_group = LabelFrame(
            self.master, text="Player 2", labelanchor="n", style="Default.TFrame"
        )
        self.player4_group = LabelFrame(
            self.master, text="Player 3", labelanchor="n", style="Default.TFrame"
        )
        self.center_group = LabelFrame(
            self.master, text="CENTER", labelanchor="n", style="Center.TFrame"
        )

        self.player1_group.grid(
            row=2, column=0, columnspan=3, sticky="nsew", ipadx=300, ipady=150
        )
        self.player2_group.grid(row=1, column=2, sticky="nsew")
        self.player3_group.grid(row=0, column=0, columnspan=3, sticky="nsew", ipadx=300)
        self.player4_group.grid(row=1, column=0, sticky="nsew")
        self.center_group.grid(row=1, column=1, sticky="nsew", ipadx=50, ipady=80)

        self.players = [
            self.player1_group,
            self.player2_group,
            self.player3_group,
            self.player4_group,
        ]

    def create_labels(self):
        self.cnt_p1 = Label(self.player1_group, textvariable=self.text0).pack(
            side="top"
        )
        self.cnt_p2 = Label(self.player2_group, textvariable=self.text1).pack()
        self.cnt_p3 = Label(self.player3_group, textvariable=self.text2).pack()
        self.cnt_p4 = Label(self.player4_group, textvariable=self.text3).pack()

        self.labels = [self.cnt_p1, self.cnt_p2, self.cnt_p3, self.cnt_p4]

    def highlight_player(self, cur_player_i):
        for i in range(len(self.players)):
            if i == cur_player_i:
                self.players[i].configure(style="Highlight.TFrame")
            else:
                self.players[i].configure(style="Default.TFrame")

    def update_cur_card(self, card):
        cur_card = card.get_image_name()
        self.load_image(
            self.center_group,
            cur_card,
            "uno/ui/images/{}.png".format(cur_card),
            30,
            30,
            True,
        )

    def toggle_color_buttons(self, bool):
        for i in range(len(self.buttons)):
            if bool:
                self.buttons[i].config(state=NORMAL)
            else:
                self.buttons[i].config(state=DISABLED)

    def update_num_of_cards(self, player_i, num):
        self.texts[player_i].set("# of cards: {}".format(num))

    def load_image(self, parent, card_name, path, x_coor, y_coor, is_center_card):
        img = Image.open(path)
        p_img = ImageTk.PhotoImage(img)

        label = Label(parent, image=p_img)
        label.image = p_img

        button = Button(
            parent, image=p_img, command=lambda: self.card_clicked(card_name)
        )
        button.place(x=x_coor, y=y_coor)

        if not is_center_card:
            self.card_buttons.append(button)
        else:
            button.config(state=DISABLED)

    def card_clicked(self, card_name):
        print("{} is pressed.".format(card_name))

        for index, c in enumerate(self.current_aval):
            if c.get_image_name() == card_name:
                if card_name in {"wild", "wild_draw4"}:
                    self.toggle_color_buttons(True)
                else:
                    self.toggle_color_buttons(False)
                self.card_input = index
                break
        self.event.set()

    def color_clicked(self, color):
        print("{} is selected.".format(color))
        if color == "red":
            self.color_input = 0
        elif color == "green":
            self.color_input = 1
        elif color == "blue":
            self.color_input = 2
        elif color == "yellow":
            self.color_input = 3
        self.color_event.set()


class UI:
    def __init__(self, game_thread):
        self.frame = None
        self.game_thread = game_thread
        self.run()

    def run(self):
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
        root.geometry("%dx%d+%d+%d" % (w, h, x, y))

        self.frame = UnoFrame()

        # app.draw_hand(game.players[0].cards)

        # game.players[0].draw_card(game.deck.draw_card(game.draw_pile))
        # app.draw_hand(game.players[0].cards)

        # app.toggle_color_buttons()

        # app.highlight_player(1)
        # app.update_cur_card(game.get_current_card())
        def task():
            g = threading.Thread(target=self.game_thread, args=[self.frame, root])
            g.start()

        root.after(0, task)
        root.mainloop()
