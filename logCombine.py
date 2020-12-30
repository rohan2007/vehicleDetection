from tkinter import *
import threading
import sys

sys.setrecursionlimit(1000000)

root = Tk()
root.geometry("500x500")


label1 = Label(root, text="0", width=5, height=5, borderwidth=2, relief="solid")
label2 = Label(root, text="0", width=5, height=5, borderwidth=2, relief="solid")
label3 = Label(root, text="0", width=5, height=5, borderwidth=2, relief="solid")
label4 = Label(root, text="0", width=5, height=5, borderwidth=2, relief="solid")
label4 = Label(root, text="0", width=5, height=5, borderwidth=2, relief="solid")


textLabel = Label(root, text="Lane 1 : ", width=10, height=6)
textLabel2 = Label(root, text="Lane 2 : ", width=10, height=6)
textLabel3 = Label(root, text="Lane 3 : ", width=10, height=6)
textLabel4 = Label(root, text="Lane 4 : ", width=10, height=6)

textLabel.grid(row=1, column=0)
textLabel2.grid(row=2, column=0)
textLabel3.grid(row=3, column=0)
textLabel4.grid(row=4, column=0)


label1.grid(row=1, column=1)
label2.grid(row=2, column=1)
label3.grid(row=3, column=1)
label4.grid(row=4, column=1)



lane1 = 0
lane2 = 0
lane3 = 0
lane4 = 1

def something():

    with open("log1.txt") as f_obj:
        content = f_obj.read()
        content1 = int(content)
    with open("log2.txt") as f_obj:
        content = f_obj.read()
        content2 = int(content)
    with open("log3.txt") as f_obj:
        content = f_obj.read()
        content3 = int(content)
    with open("log4.txt") as f_obj:
        content = f_obj.read()
        content4 = int(content)

    def changing1():
        global lane2

        if content2 > content3 and content2 > content4:
            label1["text"] = content1
            label2["text"] = content2
            label3["text"] = content3
            label4["text"] = content4

            label1["bg"] = "red"
            label2["bg"] = "green"
            label3["bg"] = "red"
            label4["bg"] = "red"
            lane2 += 1

            print("lane 2: ")
            print(lane2)

        global lane3

        if content3 > content2 and content3 > content4:
            label1["text"] = content1
            label2["text"] = content2
            label3["text"] = content3
            label4["text"] = content4

            label1["bg"] = "red"
            label2["bg"] = "red"
            label3["bg"] = "green"
            label4["bg"] = "red"

            lane3 += 1

            print("lane 3: ")
            print(lane3)

        global lane4

        if content4 > content2 and content4 > content3:
            label1["text"] = content1
            label2["text"] = content2
            label3["text"] = content3
            label4["text"] = content4

            label1["bg"] = "red"
            label2["bg"] = "red"
            label3["bg"] = "red"
            label4["bg"] = "green"

            lane4 += 1

            print("lane 4: ")
            print(lane4)

    def changing2():
        global lane1

        if content1 > content3 and content1 > content4:
            label1["text"] = content1
            label2["text"] = content2
            label3["text"] = content3
            label4["text"] = content4

            label1["bg"] = "green"
            label2["bg"] = "red"
            label3["bg"] = "red"
            label4["bg"] = "red"
            lane1 += 1

            print("lane 1: ")
            print(lane1)

        global lane3

        if content3 > content1 and content3 > content4:
            label1["text"] = content1
            label2["text"] = content2
            label3["text"] = content3
            label4["text"] = content4

            label1["bg"] = "red"
            label2["bg"] = "red"
            label3["bg"] = "green"
            label4["bg"] = "red"

            lane3 += 1

            print("lane 3: ")
            print(lane3)

        global lane4

        if content4 > content1 and content4 > content3:
            label1["text"] = content1
            label2["text"] = content2
            label3["text"] = content3
            label4["text"] = content4

            label1["bg"] = "red"
            label2["bg"] = "red"
            label3["bg"] = "red"
            label4["bg"] = "green"

            lane4 += 1

            print("lane 4: ")
            print(lane4)

    def changing3():
        global lane1

        if content1 > content2 and content1 > content4:
            label1["text"] = content1
            label2["text"] = content2
            label3["text"] = content3
            label4["text"] = content4

            label1["bg"] = "green"
            label2["bg"] = "red"
            label3["bg"] = "red"
            label4["bg"] = "red"
            lane1 += 1

            print("lane 1: ")
            print(lane1)

        global lane2

        if content2 > content1 and content2 > content4:
            label1["text"] = content1
            label2["text"] = content2
            label3["text"] = content3
            label4["text"] = content4

            label1["bg"] = "red"
            label2["bg"] = "green"
            label3["bg"] = "red"
            label4["bg"] = "red"
            lane2 += 1

            print("lane 2: ")
            print(lane2)

        global lane4

        if content4 > content1 and content4 > content2:
            label1["text"] = content1
            label2["text"] = content2
            label3["text"] = content3
            label4["text"] = content4

            label1["bg"] = "red"
            label2["bg"] = "red"
            label3["bg"] = "red"
            label4["bg"] = "green"

            lane4 += 1

            print("lane 4: ")
            print(lane4)

    def changing4():
        global lane1

        if content1 > content2 and content1 > content3:
            label1["text"] = content1
            label2["text"] = content2
            label3["text"] = content3
            label4["text"] = content4

            label1["bg"] = "green"
            label2["bg"] = "red"
            label3["bg"] = "red"
            label4["bg"] = "red"
            lane1 += 1

            print("lane 1: ")
            print(lane1)

        global lane2

        if content2 > content1 and content2 > content3:
            label1["text"] = content1
            label2["text"] = content2
            label3["text"] = content3
            label4["text"] = content4

            label1["bg"] = "red"
            label2["bg"] = "green"
            label3["bg"] = "red"
            label4["bg"] = "red"
            lane2 += 1

            print("lane 2: ")
            print(lane2)

        global lane3

        if content3 > content1 and content3 > content2:
            label1["text"] = content1
            label2["text"] = content2
            label3["text"] = content3
            label4["text"] = content4

            label1["bg"] = "red"
            label2["bg"] = "red"
            label3["bg"] = "green"
            label4["bg"] = "red"

            lane3 += 1

            print("lane 3: ")
            print(lane3)

    def change1():
        global lane1

        if content1 > content2 and content1 > content3 and content1 > content4:
            if lane1 >= 120:
                if lane1 >= 240:
                    lane1 = 0
                    something()
                else:
                    label1["bg"] = "red"
                    label1["text"] = content1
                    changing1()
                    lane1 += 1
            else:
                label1["text"] = content1
                label2["text"] = content2
                label3["text"] = content3
                label4["text"] = content4

                label1["bg"] = "green"
                label2["bg"] = "red"
                label3["bg"] = "red"
                label4["bg"] = "red"
                lane1 += 1

                print("lane 1: ")
                print(lane1)

    def change2():
        global lane2

        if content2 > content1 and content2 > content3 and content2 > content4:
            if lane2 >= 120:
                if lane2 >= 240:
                    lane2 = 0
                    something()
                else:
                    label2["bg"] = "red"
                    label2["text"] = content2
                    changing2()
                    lane2 += 1
            else:
                label1["text"] = content1
                label2["text"] = content2
                label3["text"] = content3
                label4["text"] = content4

                label1["bg"] = "red"
                label2["bg"] = "green"
                label3["bg"] = "red"
                label4["bg"] = "red"
                lane2 += 1

                print("lane 2: ")
                print(lane2)

    def change3():
        global lane3

        if content3 > content1 and content3 > content2 and content3 > content4:
            if lane3 >= 120:
                if lane3 >= 240:
                    lane3 = 0
                    something()
                else:
                    label3["bg"] = "red"
                    label3["text"] = content3
                    changing3()
                    lane3 += 1
            else:
                label1["text"] = content1
                label2["text"] = content2
                label3["text"] = content3
                label4["text"] = content4

                label1["bg"] = "red"
                label2["bg"] = "red"
                label3["bg"] = "green"
                label4["bg"] = "red"

                lane3 += 1

                print("lane 3: ")
                print(lane3)

    def change4():
        global lane4

        if content4 > content1 and content4 > content2 and content4 > content3:
            if lane4 >= 120:
                if lane4 >= 240:
                    lane4 = 0
                    something()
                else:
                    label4["bg"] = "red"
                    label4["text"] = content4
                    changing4()
                    lane4 += 1
            else:
                label1["text"] = content1
                label2["text"] = content2
                label3["text"] = content3
                label4["text"] = content4

                label1["bg"] = "red"
                label2["bg"] = "red"
                label3["bg"] = "red"
                label4["bg"] = "green"

                lane4 += 1

                print("lane 4: ")
                print(lane4)

    change1()
    change2()
    change3()
    change4()

button = Button(root, text="Click me!", command=something, padx=50)
button.grid(row=5, column=0)
button.configure(height=5, width=10)

root.mainloop()
