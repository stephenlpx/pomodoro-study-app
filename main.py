from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


#  TIMER MECHANISM  #

def start_timer():
    work_time = 30
    count_down(work_time)
    window.config(bg=PINK)
    canvas.config(bg=PINK)
    timer_label.config(bg=PINK, text="Timer")


def rest():
    short_rest = SHORT_BREAK_MIN * 60
    count_down(short_rest)
    timer_label.config(text="Break")
    window.config(bg=YELLOW)
    canvas.config(bg=YELLOW)
    timer_label.config(bg=YELLOW)
# COUNTDOWN MECHANISM  #

def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
         count_sec = f"0{count_sec}"




    canvas.itemconfig(timer_text, text=f"{count_min}: {count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# UI SETUP  #

window = Tk()
window.title("Pomodoro study tool")
window.config(padx=100, pady=50, bg=YELLOW)



#create canvas and saves the image directory
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")

#create the image and text on the canvas
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(103,130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))


#labels
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=("Calibri", 24,"bold"))
timer_label.grid(column=2,row=0)
check_mark_label = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16, "normal"))
check_mark_label.grid(column=2, row=3)

#buttons
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=1, row=3)
reset_button = Button(text="Break", command=rest)
reset_button.grid(column=3, row=3)

#canvas grid (the image)
canvas.grid(column=2, row=2)




window.mainloop()