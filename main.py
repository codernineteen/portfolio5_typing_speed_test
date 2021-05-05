from tkinter import *
from tkinter import ttk
import time
import math
import tkinter.messagebox
import numpy as np

paragraph_set = {
    'Easy':"this is a simple paragraph that is meant to be nice and easy to type which is why there will be mommas no periods or any capital letters so i guess this means that it cannot really be considered a paragraph but just a series of run on sentences this should help you get faster at typing as im trying not to use too many difficult words in it although i think that i might start making it hard by including some more difficult letters I'm typing pretty quickly so forgive me for any mistakes i think that i will not just tell you a story about the time i went to the zoo and found a monkey and a fox playing together they were so cute and i think that they were not supposed to be in the same cage but they somehow were and i loved watching them horse"
}

timer = None
test_minute = None
#-----------------------------함수
def minute_select():
    global test_minute
    test_minute = minutes.get()
    if test_minute == "1minute test":
        test_minute = 1.08
    else:
        test_minute = 5.08
    work_sec = test_minute*60
    start_timer(work_sec)


def start_timer(count):
    global timer_text, text_input
    count_min = math.floor(count/60)
    count_sec = round(count % 60)
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    timer_text = ttk.Label(mainframe, text=f"{count_min}:{count_sec}").grid(column=2, row=0, sticky=E)

    if count > 0:
        global timer
        timer = root.after(1000, start_timer, count-1)
    else:
        user_input = list(text_input.get("1.0", END))
        without_space = [item for item in user_input if item != ' ' and item != '\n']
        gross_speed = round(len(without_space) / 5 / test_minute)

        tkinter.messagebox.showinfo("Test done", f"You've been finished Typing test.\n your Gross speed is {gross_speed}")



#-----------------------------코드


root = Tk()
root.title('Typing Test')
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

minutes = ttk.Combobox(mainframe)
minutes['values'] = ('1minute test', '5minute test')
minutes.current(0)
minutes.grid(column=0, row=0)

ttk.Button(mainframe, text="Start", command=minute_select).grid(column=1, row=0, sticky=(W,E))
timer_text = ttk.Label(mainframe, text="0:00").grid(column=2, row=0, sticky=E)




paragraph = Text(root, wrap='word')
paragraph.insert(CURRENT, paragraph_set['Easy'])
paragraph.grid(column=0, row=1)

text_input = Text(root, height=20)
text_input.grid(column=0, row=2)




root.mainloop()