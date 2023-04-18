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
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    time.config(text="Timer")
    checkmark.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        time.config(text="Long break", fg=RED)
        countdown(LONG_BREAK_MIN*60)
    elif reps % 2 != 0:
        time.config(text="Work", fg=GREEN)
        countdown(WORK_MIN*60)
    elif reps % 2 == 0:
        time.config(text="Short break", fg=PINK)
        countdown(SHORT_BREAK_MIN*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer
    count_min = math.floor((count/60))
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            string = ""
            for i in range(math.floor(reps/2)):
                string += "✔"
            checkmark.config(text=string)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="25:00", fill="white", font=(FONT_NAME, 50, "bold"))
canvas.grid(column=1, row=1)

time = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 30, "bold"), fg=GREEN)
time.grid(column=1, row=0)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

checkmark = Label(bg=YELLOW, fg=GREEN)
checkmark.grid(column=1, row=3)

window.mainloop()