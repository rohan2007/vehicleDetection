from tkinter import *
import time

root = Tk()

time1 = 0
time2 = 0
time3 = 0
time4 = 0

def change(number, time1, time2, time3, time4):
    if number == 1:
        time1 += 1
    elif number == 2:
        time2 += 1
    elif number == 3:
        time3 += 1
    else:
        time4 += 1

label1 = Label(root, text=0)
label2 = Label(root, text=0)
label3 = Label(root, text=0)
label4 = Label(root, text=0)

label1.pack()
label2.pack()
label3.pack()
label4.pack()

def change1(greatest):
    if greatest[0] == 1:
        if time1 <= 120:
            label1["bg"] = "green"
            label2["bg"] = "red"
            label3["bg"] = "red"
            label4["bg"] = "red"
            change(1, time1, time2, time3, time4)
            print(time1)
    else:
        change2(greatest)
        change3(greatest)
        change4(greatest)
def change2(greatest):
    if greatest[0] == 2:
        if time2 <= 120:
            label1["bg"] = "red"
            label2["bg"] = "green"
            label3["bg"] = "red"
            label4["bg"] = "red"
            change(2, time1, time2, time3, time4)
            print(time1)
        else:
            change1(greatest)
            change3(greatest)
            change4(greatest)
def change3(greatest):
    if greatest[0] == 3:
        if time3 <= 120:
            label1["bg"] = "red"
            label2["bg"] = "red"
            label3["bg"] = "green"
            label4["bg"] = "red"
            change(3, time1, time2, time3, time4)
            print(time1)
        else:
            change1(greatest)
            change2(greatest)
            change4(greatest)
def change4(greatest):
    if greatest[0] == 4:
        if time4 <= 120:
            label1["bg"] = "red"
            label2["bg"] = "red"
            label3["bg"] = "red"
            label4["bg"] = "green"
            change(4, time1, time2, time3, time4)
            print(time1)
        else:
            change1(greatest)
            change2(greatest)
            change3(greatest)



def giveContent():
    contentList = []

    with open("log1.txt") as f_obj:
        content = f_obj.read()
        contentList.append([1, int(content)])
    with open("log2.txt") as f_obj:
        content = f_obj.read()
        contentList.append([2, int(content)])
    with open("log3.txt") as f_obj:
        content = f_obj.read()
        contentList.append([3, int(content)])
    with open("log4.txt") as f_obj:
        content = f_obj.read()
        contentList.append([4, int(content)])

    greatest = ["something", 0]



    for i in contentList:
        if i[1] > greatest[1]:
            greatest = [i[0],i[1]]
        else:
            continue

    change1(greatest)
    change2(greatest)
    change3(greatest)
    change4(greatest)


button = Button(root, text="click me!", command=giveContent())
button.pack()


root.mainloop()