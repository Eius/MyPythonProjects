import json
from tkinter import messagebox


def get_style(style: str):
    styles_file = "styles.json"
    try:
        with open(styles_file, "r") as file:
            all_styles = json.load(file)
            result = all_styles[style]

    except (FileNotFoundError, KeyError) as e:
        if isinstance(e, FileNotFoundError):
            messagebox.showerror(title="FileNotFoundError",
                                   message=f"{styles_file} file was not found! "
                                           f"\nTerminating program...")
        elif isinstance(e, KeyError):
            messagebox.showerror(title="KeyError",
                                   message=f"Style '{style}' was not found! "
                                           f"\nTerminating program...")
        exit()
    return result
