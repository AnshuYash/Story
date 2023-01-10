from tkinter import *
import random
size = 40
x1=120
y1=250
bog="#A6D1E6"
fog="Black"
position = ["1","2","3","4","5","6","7","8","9"]
count = count_1= 0
count = count_1
u1=u2=u3=u4=u5=u6=u7=u8=u9=b1=b2=b3=b4=b5=b6=b7=b8=b9=0

def score_check():
    # row 1, 2, 3 checked
    global size,x1,y1,bog,fog, u1, u2, u3, u4, u5, u6, u7, u8, u9, b1, b2, b3, b4, b5, b6, b7, b8, b9

    if (u1 + u2 + u3 == 6) or  (u4 + u5 + u6 == 6) or (u7 + u8 + u9 == 6):
        Label(window, text="User wins!", font=('Bookman Old Style', size, 'normal'),bg=bog, fg=fog).place(x=x1, y=y1)
    # col 1,2,3 checked
    elif (u1 + u4 + u7) == 6 or (u2 + u5 + u8) == 6 or (u3 + u6 + u9) == 6:
        Label(window, text="User wins!", font=('Bookman Old Style', size, 'normal'),bg=bog, fg=fog).place(x=x1, y=y1)
    # diagonal checked
    elif (u1 + u5 + u9) == 6 or (u3 + u5 + u7) == 6:
        Label(window, text="User wins!", font=('Bookman Old Style', size, 'normal') ,bg=bog, fg=fog).place(x=x1, y=y1)
    # comp row checked
    elif (b1 + b2 + b3) == 3 or (b4 + b5 + b6) == 3 or (b7 + b8 + b9) == 3:
        Label(window, text="Computer wins!", font=('Bookman Old Style', size, 'normal'), bg=bog, fg=fog).place(x=x1, y=y1)
    # comp col 1,2,3 checked
    elif (b1 + b4 + b7) == 3 or (b2 + b5 + b8) == 3 or (b3 + b6 + b9) == 3:
        Label(window, text="Computer wins!", font=('Bookman Old Style', size, 'normal'), bg=bog, fg=fog).place(x=x1, y=y1)
    # comp diagonal checked
    elif (b1 + b5 + b9) == 3 or (b3 + b5 + b7) == 3:
        Label(window, text="Computer wins!", font=('Bookman Old Style', size, 'normal'),bg=bog, fg=fog).place(x=x1, y=y1)
    else:
        if len(position) == 1:
            Label(window, text="It's a Draw!", font=('Bookman Old Style', size, 'normal'), bg=bog, fg=fog).place(x=x1, y=y1)
        return " "
def game_start():
    global u1, u2, u3, u4, u5, u6, u7, u8, u9, b1, b2, b3, b4, b5, b6, b7, b8, b9,bog,count_1,count
# user game code
    a1 = pass_var.get()
    user.delete(0, END)
    count += 1
    if a1 == "1":
        u1 = int(2)
        Label(text="X", bg="#3AB4F2", font=('Bookman Old Style', 50, 'normal')).place(x=100, y=170)
    elif a1 == "2":
        u2 = int(2)
        Label(text="X", bg="#3AB4F2", font=('Bookman Old Style', 50, 'normal')).place(x=225, y=170)
    elif a1 == "3":
        u3 = int(2)
        Label(text="X", bg="#3AB4F2", font=('Bookman Old Style', 50, 'normal')).place(x=350, y=170)
    elif a1 == "4":
        u4 = int(2)
        Label(text="X", bg="#3AB4F2", font=('Bookman Old Style', 50, 'normal')).place(x=100, y=290)
    elif a1 == "5":
        u5 = int(2)
        Label(text="X", bg="#3AB4F2", font=('Bookman Old Style', 50, 'normal')).place(x=225, y=290)
    elif a1 == "6":
        u6 = int(2)
        Label(text="X", bg="#3AB4F2", font=('Bookman Old Style', 50, 'normal')).place(x=350, y=290)
    elif a1 == "7":
        u7 = int(2)
        Label(text="X", bg="#3AB4F2", font=('Bookman Old Style', 50, 'normal')).place(x=100, y=410)
    elif a1 == "8":
        u8 = int(2)
        Label(text="X", bg="#3AB4F2", font=('Bookman Old Style', 50, 'normal')).place(x=225, y=410)
    elif a1 == "9":
        u9 = int(2)
        Label(text="X", bg="#3AB4F2", font=('Bookman Old Style', 50, 'normal')).place(x=350, y=410)
    else :pass

    position.remove(a1)
    if count >=3:
        score_check()
    else:pass
# compute game code

    com_pos = random.choice(position)
    position.remove(com_pos)
    if com_pos == "1":
        b1 = 1
        Label(text="O", bg="#3AB4F2",font=('Bookman Old Style', 50, 'normal')).place(x=100, y=170)
    elif com_pos == "2":
        b2 = 1
        Label(text="O", bg="#3AB4F2", font=('Bookman Old Style', 50, 'normal')).place(x=225, y=170)
    elif com_pos == "3":
        b3 = 1
        Label(text="O", bg="#3AB4F2", font=('Bookman Old Style', 50, 'normal')).place(x=350, y=170)
    elif com_pos == "4":
        b4 = 1
        Label(text="O", bg="#3AB4F2", font=('Bookman Old Style', 50, 'normal')).place(x=100, y=290)
    elif com_pos == "5":
        b5 = 1
        Label(text="O", bg="#3AB4F2", font=('Bookman Old Style', 50, 'normal')).place(x=225, y=290)
    elif com_pos == "6":
        b6 = 1
        Label(text="O", bg="#3AB4F2", font=('Bookman Old Style', 50, 'normal')).place(x=350, y=290)
    elif com_pos == "7":
        b7 = 1
        Label(text="O", bg="#3AB4F2", font=('Bookman Old Style', 50, 'normal')).place(x=100, y=410)
    elif com_pos == "8":
        b8 = 1
        Label(text="O", bg="#3AB4F2", font=('Bookman Old Style', 50, 'normal')).place(x=225, y=410)
    elif com_pos == "9":
        b9 = 1
        Label(text="O", bg="#3AB4F2", font=('Bookman Old Style', 50, 'normal')).place(x=350, y=410)
    else :pass
    count_1 = count
    if count >= 3:
        score_check()
    else:pass
window = Tk()
window.title("Tic-Tac-Toe")
window.resizable(False, False)
window.config(padx=50, pady=100, bg="#3AB4F2")
canvas = Canvas(width=500, height=500, bg="#3AB4F2", highlightthickness=0)
ttt_image = PhotoImage(file="TTT.png")
pass_var = StringVar()
pass_var.set("")
canvas.create_image(250, 330, image=ttt_image)
Label(window, text="Enter the number in the from 1 to 9\n to capture your position on board",
      font=('Bookman Old Style', 15, 'normal'), background="#A6D1E6").place(x=100, y=0)
user = Entry(window,font=('Bookman Old Style', 20, 'normal'),textvariable=pass_var, bg="#A6D1E6", width=3)
user.place(x=100, y=80)
user.focus()
entry_button = Button(text="Submit", command=game_start, width=10, font=('Bookman Old Style', 14, 'normal'), bg="#A6D1E6", fg="black")
entry_button.place(x=200, y=80)
canvas.pack()
window.mainloop()
