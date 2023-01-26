from config import *
from tkinter import *
import win32gui
import winsound

work_dict = {
    "duration": WORK_MIN,
    "title_text": "Work",
    "title_color": GREEN,
    "add_checkmark": True
}

short_break_dict = {
    "duration": SHORT_BREAK_MIN,
    "title_text": "Short break",
    "title_color": PINK,
    "add_checkmark": False

}

long_break_dict = {
    "duration": LONG_BREAK_MIN,
    "title_text": "Long break",
    "title_color": RED,
    "add_checkmark": False
}

timer_is_on = False
timer_handle = None
checkmarks = 0
curr_set = 0
set_dict = {
        0: work_dict,
        1: short_break_dict,
        2: work_dict,
        3: short_break_dict,
        4: work_dict,
        5: short_break_dict,
        6: work_dict,
        7: long_break_dict
    }


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(str(timer_handle))
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="0:00")
    global checkmarks
    global curr_set
    global timer_is_on
    checkmarks = 0
    curr_set = 0
    timer_is_on = False
    checkmarks_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer(is_button_click=True):
    global timer_is_on
    global curr_set
    global set_dict

    if not timer_is_on and is_button_click:
        timer_is_on = True
        count_down_time = set_dict[curr_set]["duration"] * 60
        count_down(count_down_time)
        change_timer_label()
        curr_set += 1

    elif timer_is_on and not is_button_click:
        focus_window()
        count_down_time = set_dict[curr_set]["duration"] * 60
        count_down(count_down_time)
        change_timer_label()
        add_checkmark()
        curr_set += 1
        if curr_set > len(set_dict) - 1:
            curr_set = 0


def focus_window():
    hwnd = win32gui.FindWindow(None, WINDOW_TITLE)
    win32gui.SetForegroundWindow(hwnd)
    win32gui.ShowWindow(hwnd, 9)
    win32gui.FlashWindow(hwnd, True)

    # Play default system sound
    winsound.PlaySound("SystemAsterisk", winsound.SND_ASYNC)


def change_timer_label():
    global curr_set
    global set_dict
    title_text = set_dict[curr_set]["title_text"]
    title_color = set_dict[curr_set]["title_color"]
    timer_label.config(text=title_text, fg=title_color)


def add_checkmark():
    global curr_set
    global set_dict
    global checkmarks
    previous_set = set_dict.get(curr_set - 1)

    if previous_set and previous_set["add_checkmark"]:
        checkmarks += 1
        marks = ""
        for _ in range(0, checkmarks):
            marks += "✔"
        checkmarks_label.config(text=marks)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    formatted_minutes = str(int(count) // 60).zfill(1)
    formatted_seconds = str(int(count) % 60).zfill(2)
    timer_string = f"{formatted_minutes}:{formatted_seconds}"
    canvas.itemconfig(timer_text, text=timer_string)
    if count > 0:
        global timer_handle
        timer_handle = window.after(1000, count_down, count - 1)
    else:
        start_timer(is_button_click=False)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title(WINDOW_TITLE)
window.config(padx=150, pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="0:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

timer_label = Label(text="Pomodoro", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=2, row=1)

start_button = Button(text="Start", relief="groove", width=7, highlightthickness=0, font=(FONT_NAME, 12, "bold"),
                      command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", relief="groove", width=7, highlightthickness=0, font=(FONT_NAME, 12, "bold"),
                      command=reset_timer)
reset_button.grid(column=3, row=3)

checkmarks_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 14, "normal"))
checkmarks_label.grid(column=2, row=4)

mainloop()
