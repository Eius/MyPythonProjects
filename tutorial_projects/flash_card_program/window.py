import tkinter as tk
from data_manager import DataManager

BG_COLOR = "#B1DDC6"
CARD_FLASH_INTERVAL = 2500


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        # Word Picker
        self.data_manager = DataManager()
        self.current_data = self.data_manager.pick_random_word()
        self.column_1_header = self.data_manager.col_1
        self.column_2_header = self.data_manager.col_2

        # Timer
        self.timer_handle = None
        self.current_card = None

        # Window
        self.title("Flash Cards")
        self.config(padx=50, pady=50, background=BG_COLOR)
        self.minsize(width=900, height=576)

        # Front Canvas
        self.front_image = tk.PhotoImage(file="images/card_front.png")
        self.back_image = tk.PhotoImage(file="images/card_back.png")
        self.canvas = tk.Canvas(self, height=526, width=800, background=BG_COLOR, highlightthickness=0)

        # Wrong button
        self.wrong_image = tk.PhotoImage(file="images/wrong.png")
        self.wrong_button = tk.Button(self, image=self.wrong_image, highlightthickness=0, relief="flat",
                                      border=0, command=self.on_wrong_click)
        # Right button
        self.right_image = tk.PhotoImage(file="images/right.png")
        self.right_button = tk.Button(self, image=self.right_image, highlightthickness=0, relief="flat",
                                      border=0, command=self.on_right_click)

        self.arrange_widgets()
        self.show_front_card(self.current_data["Dutch"])
        self.start_timer()

        self.mainloop()

    def arrange_widgets(self):
        self.wrong_button.grid(column=0, row=1)
        self.right_button.grid(column=1, row=1)

    def show_front_card(self, dutch_word):
        self.canvas.grid(column=0, row=0, columnspan=2, sticky="ew", padx=(22, 0))
        self.canvas.delete("text_item", "image_item")
        self.canvas.create_image(400, 526 / 2, image=self.front_image, tags="image_item")
        self.canvas.create_text(400, 150, text=f"{self.column_1_header}", font=("Arial", 40, "italic"),
                                tags="text_item")
        self.canvas.create_text(400, 263, text=f"{dutch_word}", font=("Arial", 60, "bold"),
                                tags="text_item")
        self.current_card = "front"

    def show_back_card(self, english_word):
        self.canvas.grid(column=0, row=0, columnspan=2, sticky="ew", padx=(22, 0))
        self.canvas.delete("text_item", "image_item")
        self.canvas.create_image(400, 526 / 2, image=self.back_image, tags="image_item")
        self.canvas.create_text(400, 150, text=f"{self.column_2_header}", font=("Arial", 40, "italic"),
                                tags="text_item", fill="white")
        self.canvas.create_text(400, 263, text=f"{english_word}", font=("Arial", 60, "bold"),
                                tags="text_item", fill="white")
        self.current_card = "back"

    def on_wrong_click(self):
        self.data_manager.save_unknown_words()
        self.current_data = self.data_manager.pick_random_word()
        self.show_front_card(self.current_data["Dutch"])
        self.start_timer()

    def on_right_click(self):
        self.data_manager.remove_known_word(self.current_data)
        self.current_data = self.data_manager.pick_random_word()
        self.show_front_card(self.current_data["Dutch"])
        self.start_timer()

    def start_timer(self):
        if self.timer_handle is None:
            self.timer_handle = self.after(CARD_FLASH_INTERVAL, self.flip_card)
        else:
            self.after_cancel(self.timer_handle)
            self.timer_handle = self.after(CARD_FLASH_INTERVAL, self.flip_card)

    def flip_card(self):
        if self.current_card == "front":
            self.show_back_card(self.current_data["English"])
        else:
            self.show_front_card(self.current_data["Dutch"])
        self.timer_handle = self.after(CARD_FLASH_INTERVAL, self.flip_card)


