from tkinter import *
import math


def start_timer():
    text_input.focus()
    calc = Button(text="Calculate", command=calc_text, width=10, font=('Bookman Old Style', 14, 'bold'), bg="#A6D1E6",
                  fg="black")
    calc.place(x=250, y=450)
    count_down(int(1 * 60))


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(text_item, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


def calc_text():
    a1 = text_input.get()
    words = a1.split(" ")
    if words[0] == "":
        no_word = "❌ " + "0" + " word/min"
        Label(text=no_word, font=('Bookman Old Style', 14, 'bold'), bg="#3AB4F2", fg="red").place(x=330, y=250)
    else:
        no_word = "✔ " + str(len(words)) + " words/min"
        Label(text=no_word, font=('Bookman Old Style', 14, 'bold'), bg="#3AB4F2", fg="green").place(x=330, y=250)


window = Tk()
window.title("Words Per Min")
pass_var = StringVar()
window.config(padx=20, pady=20, bg="#3AB4F2")
canvas = Canvas(width=500, height=500, bg="#3AB4F2", highlightthickness=0)
text1 = Label(text="....TIMER....", fg="black", bg="#3AB4F2", font=("Bookman Old Style", 35))
text1.place(x=130, y=20)
watch_image = PhotoImage(file="watch.png")
canvas.create_image(150, 250, image=watch_image)
text_item = canvas.create_text(150, 240, text="00:00", font=("Bookman Old Style", 35, "bold"), fill="#2C3333")
start_button = Button(text="START", fg="black", bg="#A6D1E6", font=("Bookman Old Style", 15, "bold"),
                      command=start_timer)
start_button.place(x=100, y=450)
text_input = Entry(font=('Bookman Old Style', 10, 'normal'), width=50, textvariable=pass_var, bg="#A6D1E6")
text_input.place(x=50, y=400)
canvas.pack()
window.mainloop()
