from tkinter import *
import requests


def get_quote():
    result = requests.get(url="https://api.kanye.rest")
    result.raise_for_status()
    quote = result.json()["quote"]
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="resources/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="", width=250, font=("Arial", 20, "bold"),
                                fill="white", tags="quote")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="resources/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote, relief="flat")
kanye_button.grid(row=1, column=0)

get_quote()

window.mainloop()