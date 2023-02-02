THEME_COLOR = "#375362"


class Styles:
    def __init__(self):
        self.window = {
            "bg": THEME_COLOR,
            "padx": 20,
            "pady": 20
        }

        self.score = {
            "text": "Score: 0",
            "font": ("Arial", 12, "italic"),
            "fg": "white",
            "bg": THEME_COLOR
        }

        self.question_canvas_default = {
            "width": 300,
            "height": 250,
            "highlightthickness": 0,
            "bg": "white"
        }

        self.question_canvas_correct_feedback = {
            "bg": "green"
        }

        self.question_canvas_wrong_feedback = {
            "bg": "red"
        }

        self.question_text = {
            "fill": THEME_COLOR,
            "width": self.question_canvas_default["width"] - 20,
            "justify": "center",
            "font": ("Arial", 15, "italic")
        }

        self.correct_button_image = {
            "file": "images/true.png"
        }

        self.wrong_button_image = {
            "file": "images/false.png"
        }

        self.correct_button = {
            "highlightthickness": 0,
            "borderwidth": 0,
            "relief": "flat"
        }

        self.wrong_button = {
            "highlightthickness": 0,
            "borderwidth": 0,
            "relief": "flat"
        }
