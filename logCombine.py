from tkinter import *
import threading
import sys

sys.setrecursionlimit(1000000)

root = Tk()

label1 = Label(root, text="0")
label2 = Label(root, text="0")
label3 = Label(root, text="0")
label4 = Label(root, text="0")

label1.pack()
label2.pack()
label3.pack()
label4.pack()


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
                label1["bg"] = "red"
                label2["bg"] = "green"
                label3["bg"] = "red"
                label4["bg"] = "red"
                lane2 += 1

                print("lane 2: ")
                print(lane2)

        global lane3

        if content3 > content2 and content3 > content4:
            label1["bg"] = "red"
            label2["bg"] = "red"
            label3["bg"] = "green"
            label4["bg"] = "red"

            lane3 += 1

            print("lane 3: ")
            print(lane3)

        global lane4

        if content4 > content2 and content4 > content3:
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
            label1["bg"] = "green"
            label2["bg"] = "red"
            label3["bg"] = "red"
            label4["bg"] = "red"
            lane1 += 1

            print("lane 1: ")
            print(lane1)

        global lane3

        if content3 > content1 and content3 > content4:
            label1["bg"] = "red"
            label2["bg"] = "red"
            label3["bg"] = "green"
            label4["bg"] = "red"

            lane3 += 1

            print("lane 3: ")
            print(lane3)

        global lane4

        if content4 > content1 and content4 > content3:
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
            label1["bg"] = "green"
            label2["bg"] = "red"
            label3["bg"] = "red"
            label4["bg"] = "red"
            lane1 += 1

            print("lane 1: ")
            print(lane1)

        global lane2

        if content2 > content1 and content2 > content4:
            label1["bg"] = "red"
            label2["bg"] = "green"
            label3["bg"] = "red"
            label4["bg"] = "red"
            lane2 += 1

            print("lane 2: ")
            print(lane2)

        global lane4

        if content4 > content1 and content4 > content2:
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
                label1["bg"] = "green"
                label2["bg"] = "red"
                label3["bg"] = "red"
                label4["bg"] = "red"
                lane1 += 1

                print("lane 1: ")
                print(lane1)

        global lane2

        if content2 > content1 and content2 > content3:
                label1["bg"] = "red"
                label2["bg"] = "green"
                label3["bg"] = "red"
                label4["bg"] = "red"
                lane2 += 1

                print("lane 2: ")
                print(lane2)

        global lane3

        if content3 > content1 and content3 > content2 :

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
                    changing1()
                    lane1 += 1
            else:
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
                    changing2()
                    lane2 += 1
            else:
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
                    changing3()
                    lane3 += 1
            else:
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
                    changing4()
                    lane4 += 1
            else:
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






button = Button(root, text="Click me!", command=something)
button.pack()


root.mainloop()
