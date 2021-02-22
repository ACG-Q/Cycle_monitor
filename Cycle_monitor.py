#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Feb 19, 2021 11:51:06 AM CST  platform: Windows NT

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont
import tkinter.filedialog as tkFile

import threading,time,sys,configparser,os

from win10toast import ToastNotifier

TIME_SWITCH = True
PWD = os.getcwd()
INI_PATH = PWD+'\\配置.ini'
ICON_PATH = '.\\drink_128.ico'
TIME_MIN = '1'
TIME_TIME = '30'
TIME_TITLE = '饮水提醒'
TIME_MSG = '每天2000ML'
SELECT = 'select'

config = configparser.ConfigParser()

def read_config():
    global TIME_TIME,TIME_TITLE,TIME_MSG,ICON_PATH
    if os.path.exists(INI_PATH):
        config.read(INI_PATH)
        TIME_TIME = config[SELECT]['time']
        TIME_TITLE = config[SELECT]['title']
        TIME_MSG = config[SELECT]['msg']
        ICON_PATH = config[SELECT]['icon']

def save_config():
    if SELECT not in config.sections():config.add_section(SELECT)
    config.set(SELECT,'time',TIME_TIME)
    config.set(SELECT,'title',TIME_TITLE)
    config.set(SELECT,'msg',TIME_MSG)
    config.set(SELECT,'icon',ICON_PATH)
    with open(INI_PATH,'w') as f:
        config.write(f)

class Toplevel1:
    def __init__(self, top=None):
        read_config()
        top.geometry("250x210")
        top.minsize(250, 210)
        top.maxsize(250, 210)
        top.resizable(1,  1)
        top.title("循环提示器")

        self.Label1 = tk.Label(top)
        self.Label1.place(x=0, y=10, height=30, width=110)
        self.Label1['disabledforeground']="#a3a3a3"
        self.Label1['foreground']="#000000"
        self.Label1['text']='''时间循环(分钟):'''

        self.Spinbox1 = ttk.Spinbox(top, from_=1.0, to=100.0)
        self.Spinbox1.place(x=120, y=10, height=30, width=110)
        font = tkFont.Font(family='微软雅黑', size='20')
        self.Spinbox1['font']=font
        self.Spinbox1['from']=TIME_MIN
        self.Spinbox1.set(TIME_TIME)

        font = tkFont.Font(family='微软雅黑', size='10')

        self.Label2 = tk.Label(top)
        self.Label2.place(x=0, y=35, height=30, width=80)
        self.Label2['disabledforeground']="#a3a3a3"
        self.Label2['font']=font
        self.Label2['foreground']="#000000"
        self.Label2['text']='''提示信息:'''

        self.Text2 = tk.Text(top)
        self.Text2.place(x=9, y=60, height=25, width=228)
        self.Text2['background']="white"
        self.Text2['font']=font
        self.Text2['foreground']="black"
        self.Text2['highlightbackground']="#d9d9d9"
        self.Text2['highlightcolor']="black"
        self.Text2['selectbackground']="blue"
        self.Text2['selectforeground']="white"
        self.Text2['wrap']="word"
        self.Text2.insert('0.0',TIME_TITLE)

        self.Text1 = tk.Text(top)
        self.Text1.place(x=9, y=85, height=50, width=228)
        self.Text1['background']="white"
        self.Text1['font']=font
        self.Text1['foreground']="black"
        self.Text1['highlightbackground']="#d9d9d9"
        self.Text1['highlightcolor']="black"
        self.Text1['selectbackground']="blue"
        self.Text1['selectforeground']="white"
        self.Text1['wrap']="word"
        self.Text1.insert('0.0',TIME_MSG)

        self.Button1 = tk.Button(top)
        self.Button1.place(x=10, y=150, height=30, width=70)
        self.Button1['activebackground']="#ececec"
        self.Button1['activeforeground']="#000000"
        self.Button1['disabledforeground']="#a3a3a3"
        self.Button1['foreground']="#000000"
        self.Button1['highlightbackground']="#d9d9d9"
        self.Button1['pady']="0"
        self.Button1['text']='''循环开始'''

        self.Button2 = tk.Button(top)
        self.Button2.place(x=170, y=150, height=30, width=70)
        self.Button2['activebackground']="#ececec"
        self.Button2['activeforeground']="#000000"
        self.Button2['disabledforeground']="#a3a3a3"
        self.Button2['foreground']="#000000"
        self.Button2['pady']="0"
        self.Button2['text']='''循环结束'''

        self.Button3 = tk.Button(top)
        self.Button3.place(x=90, y=150, height=30, width=70)
        self.Button3['activebackground']="#ececec"
        self.Button3['activeforeground']="#000000"
        self.Button3['disabledforeground']="#a3a3a3"
        self.Button3['foreground']="#000000"
        self.Button3['pady']="0"
        self.Button3['text']='''选择图标'''

        self.Label2 = tk.Label(top)
        self.Label2.place(x=5, y=180, height=25, width=240)
        self.Label2['font']=font
        self.Label2['justify']='left'
        self.Label2['text']="❗调试信息:等待....❗"

        self.Label3 = tk.Label(top)
        self.Label3.place(x=5, y=130, height=20, width=240)
        self.Label3['font']=font
        self.Label3['justify']='left'
        self.Label3['text']="图标："+ICON_PATH

        self.button()

        top.mainloop()

    def button(self):
        self.Button1['command'] = self.start
        self.Button2['command'] = self.stop
        self.Button3['command'] = self.getIcoPath

    def start(self):
        global TIME_SWITCH,TIME_MSG,TIME_TIME,TIME_TITLE
        time = self.Spinbox1.get()
        msg = self.Text1.get('0.0','end').replace(' ','').replace('\n','')
        title = self.Text2.get('0.0','end').replace(' ','').replace('\n','')
        if msg.isspace() or len(msg) == 0:msg = '感谢使用!!'
        if int(time) < 0:
            self.Spinbox1.set(TIME_MIN)
            self.Label2['text']=f"❗调试信息:最少{TIME_MIN}分钟❗"
            return
        self.Label2['text']=f"❗调试信息:开始循环,每{time}分钟提示一次❗"
        
        self.Button1['state']=tk.DISABLED
        self.Text1['state']=tk.DISABLED
        self.Text2['state']=tk.DISABLED
        
        TIME_SWITCH = True
        TIME_MSG = msg
        TIME_TIME = time
        TIME_TITLE = title
        
        self.timethread = threading.Thread(target=loop_call,args=(time,title,msg),daemon=True)
        self.timethread.start()
        save_config()

    def stop(self):
        global TIME_SWITCH
        if self.Button1['state'] == tk.DISABLED:
            self.Label2['text']="❗调试信息:结束循环❗"
            TIME_SWITCH = False
            self.Button1['state']=tk.NORMAL
            self.Text1['state']=tk.NORMAL
            self.Text2['state']=tk.NORMAL
            return
        self.Label2['text']="❗调试信息:还未开始循环❗"

    def getIcoPath(self):
        global ICON_PATH
        # os.path.relpath(path, start)
        path = tkFile.askopenfilename()
        if PWD[:1] == path[:1]:path = os.path.relpath(path, PWD)
        ICON_PATH = path
        self.Label3['text']="图标："+path
        

def loop_call(t:str,title:str,msg:str):
    s = int(t) * 60
    toaster(f'{title}提醒','开始倒计时....')
    start_time = time.time()
    while TIME_SWITCH:
        Date = time.strftime('%Y{y}%m{m}%d{d} %H{h}%M{f}%S{s}').format(y='年', m='月', d='日', h='时', f='分', s='秒')
        end_time = time.time()
        if TIME_SWITCH and end_time - start_time >= s:
            toaster(title,f'{Date}：{msg}')
            start_time = time.time()
            # print(f'[{Date}] 线程{threading.get_ident()}发送Message信息:{msg}')
    # Date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print(f'[{Date}] 线程{threading.get_ident()}结束')    
    toaster(f'{title}提醒',f'{title}结束')
    return

def toaster(title,msg):
    toaster = ToastNotifier()
    toaster.show_toast(title,
                   msg,
                   icon_path=ICON_PATH,
                   duration=5)

if __name__ == "__main__":
    root = tk.Tk()
    Toplevel1(root)




