FONT_BOLD = ("Arial", 10, "bold")
FONT_NORMAL = ("Arial", 9, "normal")


class CoordinateFrameStyle:
    def __init__(self):
        super().__init__()
        self.column_label = {
            "font": FONT_BOLD
        }

        self.current_location_label = {
            "text": "Current location:",
            "anchor": "e",
            "font": FONT_BOLD
        }

        self.current_location_entry = {
            "justify": "center",
            "bg": "#c2ffc2",
            "font": FONT_BOLD
        }

        self.row_label = {
            "anchor": "e",
            "font": FONT_BOLD
        }

        self.row_value = {
            "bd": 2,
            "relief": "ridge",
            "font": FONT_NORMAL
        }
