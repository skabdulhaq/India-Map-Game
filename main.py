import pandas
import turtle
from tkinter import *
import math
import time as time_
from tkinter import messagebox
# import time


def final():
    states_unanswered = [states_unanswered for states_unanswered in states_given
                         if states_unanswered not in states_answered]
    write_state(name_state=f"Your Score is {len(states_answered)}/{len(states_given)}\n"
                           f"Learn Remaining {len(states_unanswered)} states\n"
                           f"We Saved them in This Folder\n"
                           f"Click On Screen To Exit", cord=(0, -20), font_size=20, type_text="normal", align="center")
    states_un = pandas.DataFrame(states_unanswered)
    states_un.to_csv(f"learn these {len(states_unanswered)} states.csv.txt")


def count_down_time(time):
    # global reps
    turtle_time.clear()
    time_in_min = math.floor(time/60)
    time_in_sec = time % 60
    if time_in_sec < 10:
        time_in_sec = f"0{time_in_sec}"

    if time >= 0:
        screen.tracer(0)
        turtle_time.clear()
        turtle_time.write(f"{time_in_min}:{time_in_sec}", False, "center", ("Courier", 30, "bold"))
        # write_state(f"{time_in_min}:{time_in_sec}", (400, 0), 30, "bold", "center")
        time_.sleep(1)
        screen.update()
        count_down_time(time-1)
        # canvas.itemconfig(count_down, text=f'{time_in_min}:{time_in_sec}')
        # timer_of_tomato = window.after(1000, count_down_time, time-1)
    if time == 0:
        final()
        # reps = reps + 1
        # alarm()
        # start_timer()




def write_state(name_state, cord, font_size, type_text, align):
    # font_size = 10
    # align = "center"
    # type_text = "normal"
    turtle_state_writer = turtle.Turtle()
    turtle_state_writer.hideturtle()
    turtle_state_writer.penup()
    turtle_state_writer.speed(1000)
    turtle_state_writer.goto(cord[0], cord[-1]-10)
    turtle_state_writer.pendown()
    turtle_state_writer.write(arg=name_state, move=False, align=align, font=("Arial", font_size, type_text))


def message_help(title):
    messagebox.showinfo(title, "Type 'exit' To Exit The Game\nType 'help' or 'rules' To Get This Message")


# read data of india and takes coordinates

# window = Tk()
# canvas = Canvas(width=200, height=100)
# window.minsize(100, 100)
states_coord = pandas.read_csv("india_states.csv")
states_of_dict = states_coord.to_dict()
states = states_of_dict["states"]
x = states_of_dict["x"]
y = states_of_dict["y"]
states_given = [value for key, value in states.items()]
states_answered = []
# timer = canvas.

# displays india image on screen

turtle1 = turtle.Turtle()
# count_down = canvas.create_text(100, 50, text="00:00", font=("Courier", 30, "bold"), fill="black")
# canvas.grid(column=0, row=0)

turtle1.speed("fastest")
turtle_time = turtle.Turtle()
img = "political-map.gif"
screen = turtle.Screen()
# screen.setup(width=600, height=690)
screen.setup(width=1.0, height=1.0)
screen.title("India State Game")
screen.addshape(img)
turtle1.shape(img)
turtle_time.hideturtle()
turtle_time.penup()
turtle_time.goto(400, 0)
#turtle_time.write("05:00", False, "center", ("Courier", 30, "bold"))
# write_state("00:00", (400, 0), 30, "bold", "center")
#write_state("Timer", (400, 50), 30, "bold", "center")

exit = False
message_help("Rules!!")

# text input
while not exit:
    if len(states_answered) == 29:
        exit = True
        write_state("You Won !!!", (0,0), 30, "bold", "center")
        write_state("Click On Screen To Exit", (0,-200), 20, "bold", "center")
 #   count_down_time(300)
    window_message = "What is the next state??"
    if len(states_answered) == 0:
        window_message = "Type a state which belongs\nto this map"
    user_input = turtle.textinput(title=f"Your score {len(states_answered)}/{len(states_given)}",
                                  prompt=window_message).title().strip()

    # check user input
    if user_input in states_given:
        # finding key
        key_of_state = states_given.index(user_input)
        # add to answered list and checking that answer is unique
        if user_input not in states_answered:
            states_answered.append(user_input)
            # print that on screen
            write_state(user_input, (x[key_of_state], y[key_of_state]), 8, "bold", "center")
    elif user_input == "Help" or user_input == "Rules":
        # message_help = messagebox.showinfo("Help Menu", "Type 'exit' To Exit The Game\n"
        #                                                 "Type 'help' or 'rules' To Get This Message")
        message_help(user_input+"!!")
    elif user_input == "Exit":
        final()
        exit = True

screen.exitonclick()
