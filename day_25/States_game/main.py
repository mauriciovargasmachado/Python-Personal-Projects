import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states)<50:

    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 States Correct", prompt="Name another state name!").title()

    if answer_state == "Exit":
        break

    elif answer_state in all_states:
        guessed_states.append(answer_state)
        my_turtle = turtle.Turtle()
        my_turtle.hideturtle()
        my_turtle.penup()
        state_data =data[data.state == answer_state]
        my_turtle.goto(int(state_data.x), int(state_data.y))
        my_turtle.write(answer_state)

turtle.mainloop()

