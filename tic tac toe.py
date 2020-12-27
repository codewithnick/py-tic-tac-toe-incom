from tkinter import *
bclick = True
tk = Tk()
tk.title("Tic Tac toe")
tk.geometry("300x400")
n = 9
btns = []
def tt1():
    ttt(btns[0])
def tt2():
    ttt(btns[1])
def tt3():
    ttt(btns[2])
def tt4():
    ttt(btns[3])
def tt5():
    ttt(btns[4])
def tt6():
    ttt(btns[5])
def tt7():
    ttt(btns[6])
def tt8():
    ttt(btns[7])
def tt9():
    ttt(btns[8])
def ttt(button):
    global bclick
    print(button)
    if button["text"] == "" and bclick == True:
        print("if")
        button.config(text="X")
        bclick = False
    elif button["text"] == "" and bclick == False:
        print("else")
        button["text"] = "0"
        bclick = True
for i in range(9):
    btns.append(Button(font=('Times 20 bold'), bg='white', fg='black', height=2, width=4))
    row = 1
    column = 0
    index = 1
    print(btns)
    buttons = StringVar()
for i in btns:
    i.grid(row=row, column=column)
    print(i, i["command"])
    column += 1
    if index % 3 == 0:
        row += 1
        column = 0
    index += 1
btns[0].config(command=tt1)
btns[1].config(command=tt2)
btns[2].config(command=tt3)
btns[3].config(command=tt4)
btns[4].config(command=tt5)
btns[5].config(command=tt6)
btns[6].config(command=tt7)
btns[7].config(command=tt8)
btns[8].config(command=tt9)
tk.mainloop()
