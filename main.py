import pandas
import turtle

def correct(t, x, y, answer):
    t.goto(x, y)
    t.pendown()
    t.write(answer)
    t.penup()

screen = turtle.Screen()
screen.title("U.S. States Game")

img = "blankstates.gif"
screen.addshape(img)
screen.bgpic(img)

t = turtle.Turtle()
t.pencolor("black")
t.hideturtle()
t.penup()

states = pandas.read_csv("50_states.csv")

counter = 0
guessed_states = []

while counter < 50:    
    answer = screen.textinput(title=f"{counter}/50 States Correct", prompt="Name a state")
    
    if answer is None or answer.lower() == "exit":
        break
    
    answer = answer.title()
    if answer in states["state"].values and answer not in guessed_states:
        guessed_states.append(answer)
        state_data = states[states.state == answer]
        x = int(state_data.x)
        y = int(state_data.y)        
        counter += 1
        correct(t, x, y, answer)

screen.exitonclick()
