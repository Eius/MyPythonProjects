import turtle
from writer import Writer
import pandas

IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.setup(height=491, width=725)
screen.title("U.S. States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

writer = Writer()
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states guessed", prompt="What's another state's name?")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in guessed_states:
        print(f"Already guessed!: {answer_state}")
        continue

    elif answer_state in all_states:
        print(f"State found!: {answer_state}")
        guessed_states.append(answer_state)
        df = data[data.state == answer_state]
        x = int(df.x)
        y = int(df.y)
        writer.write_state(x, y, answer_state)


