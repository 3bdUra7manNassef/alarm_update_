
#*module on my project
from tkinter.ttk import *
from tkinter import *
from time import strftime
import time
from playsound import playsound


window_1 = Tk()
window_1.resizable(False, False)
window_1.geometry('1000x1000')
window_1.config(background='gray3')
window_1.title('alarm by 3bdo')

lb_sec_val = 0 
lb_minute_val = 0
lb_hour_val = 0

#!!!this is a command for a btn~s!!!#

def btn_Sec_plus_cmd():
    global lb_sec_val
    lb_sec_val += 1
    lb_sec.config(text='second_' + str(lb_sec_val))


def btn_Sec_mine_cmd():
    global lb_sec_val
    lb_sec_val -= 1
    lb_sec.config(text='second_' + str(lb_sec_val))


def btn_hour_mine_cmd():
    global lb_hour_val
    lb_hour_val -= 1
    lb_hour.config(text='hour_' + str(lb_hour_val))


def btn_hour_plus_cmd():
    global lb_hour_val
    lb_hour_val += 1
    lb_hour.config(text='hour_' + str(lb_hour_val))


def btn_minute_plus_cmd():
    global lb_minute_val
    lb_minute_val += 1
    lb_minute.config(text='minute_' + str(lb_minute_val))


def btn_minute_mine_cmd():
    global lb_minute_val
    lb_minute_val -= 1
    lb_minute.config(text='minute_' + str(lb_minute_val))

def btn_start():
    time.sleep(lb_sec_val + (lb_minute_val*60)+ (lb_hour_val*60*60))
    playsound('نغمه للمنبه مفزعه بصوت عادل شكل قوم ياولا.mp3')
    playsound('ميمز انا نايم نايم.mp3')
    while True:
        playsound('نغمه للمنبه مفزعه بصوت عادل شكل قوم ياولا.mp3')

def btn_window_2_show():
    window_2 = Tk()
    window_2.title('Clock by 3bdo')

    def timec():
        string = strftime('%I:%M:%S %p') # Corrected time format
        lable.config(text = string)
        lable.after(1000,timec) # Changed time to timec (typo)

    lable = Label(window_2, font=("ds-digital",80),background = "black",foreground="green") # Corrected Label capitalization and spelling of "green"
    lable.pack(anchor = 'center')
    timec()




# Labels
lb_sec = Label(window_1, text='second_0')
lb_hour = Label(window_1, text='hours_0')
lb_minute = Label(window_1, text='minute_0')

# Buttons
btn_Sec_plus = Button(window_1, text='second_+', command=btn_Sec_plus_cmd)
btn_Sec_mine = Button(window_1, text='second_-', command=btn_Sec_mine_cmd)
btn_minute_plus = Button(window_1, text='minute+', command=btn_minute_plus_cmd)
btn_minute_mine = Button(window_1, text='minute-', command=btn_minute_mine_cmd)
btn_hour_mine = Button(window_1, text='hours-', command=btn_hour_mine_cmd)
btn_hour_plus = Button(window_1, text='hours+', command=btn_hour_plus_cmd)
btn_clock = Button(window_1,text='window clock',command=btn_window_2_show)
btn_start = Button(window_1,text='start',bg='#66CDAA',command=btn_start)

# Button and Label packing
btn_hour_mine.pack()
btn_hour_plus.pack()
btn_minute_mine.pack()
btn_minute_plus.pack()
btn_Sec_mine.pack()
btn_Sec_plus.pack()

lb_sec.pack()
lb_hour.pack()
lb_minute.pack()

btn_start.pack()
btn_clock.pack()

window_1.mainloop()
