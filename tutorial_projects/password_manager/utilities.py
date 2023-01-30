import json
from tkinter import messagebox


def get_style(key: str):
    styles_file = "data/styles.json"
    try:
        with open(styles_file, "r") as file:
            all_styles = json.load(file)
            result = all_styles[key]

    except (FileNotFoundError, KeyError) as e:
        if isinstance(e, FileNotFoundError):
            messagebox.showerror(title="FileNotFoundError",
                                 message=f"{styles_file} file was not found! "
                                         f"\nTerminating program...")
        elif isinstance(e, KeyError):
            messagebox.showerror(title="KeyError",
                                 message=f"Style '{key}' was not found! "
                                         f"\nTerminating program...")
        exit()
    return result


def get_config():
    config_file = "data/config.json"
    try:
        with open(config_file, "r") as file:
            config = json.load(file)
            return config

    except FileNotFoundError as e:
        with open(config_file, "w"):
            pass


def save_config(new_data):
    config_file = "data/config.json"

    try:
        with open(config_file, "r") as file:
            # Reading old data
            data = json.load(file)

    except FileNotFoundError:
        with open(config_file, "w") as file:
            # If file does not exist, create it and write new data into it
            json.dump(new_data, file, indent=4)

    else:
        # Updating old data with new data
        data.update(new_data)

        with open(config_file, "w") as file:
            # Saving updated data
            json.dump(data, file, indent=4)
