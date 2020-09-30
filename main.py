import os
import shutil
from time import sleep
import threading
import tkinter as tk
from tkinter import filedialog
import hashlib

print('简易文件比对TOOL=====V0.2')

work_dir = '暂未设定'
lineNub = 10

filename = 0
nowline = int(0)
filelist = []

root = tk.Tk()
root.title('简易文件比对V0.1===真的假的鸭？')
root.geometry('550x100')

lineNub_show = tk.StringVar()
lineNub_show.set(lineNub)
work_dir_show = tk.StringVar()
work_dir_show.set(work_dir)


def CpToNewMkdir(md5, file2):
    shutil.copy(file2, os.path.join(work_dir, md5))
    filelist.append(file2)


def getFileMd5(filename):
    thisfile = open(filename, 'rb')
    filemd5 = hashlib.md5()
    filemd5.update(thisfile.read())
    hash = filemd5.hexdigest()
    thisfile.close()
    return str(hash).upper()


def Compared_MD5(md5, filepath):
    for name in os.listdir(work_dir):
        i = os.path.join(work_dir, name)
        if os.path.isfile(i):
            if i != filepath:
                if getFileMd5(i) == md5:
                    if md5 not in os.listdir(work_dir):
                        os.mkdir(os.path.join(work_dir, md5))
                    CpToNewMkdir(md5, i)
                else:
                    pass
            else:
                pass
        else:
            pass


def getDir():
    global work_dir
    work_dir = filedialog.askdirectory()
    work_dir_show.set(work_dir)


def find_run(md5, filepath):
    global nowline
    while nowline > int(lineNub):
        sleep(0.05)
    nowline = nowline + 1
    now_line = threading.Thread(target=Compared_MD5, args=(md5, filepath))
    now_line.run()


def main():
    global filename
    for name in os.listdir(work_dir):
        file_absolute_path = os.path.join(work_dir, name)
        if os.path.isfile(file_absolute_path):
            print(name)
            filemd5 = getFileMd5(file_absolute_path)
            find_run(filemd5, file_absolute_path)
        else:
            pass
    er = tk.Tk()
    er.geometry('700x500')
    text = tk.Label(er, text='在指定文件夹下对比结束')
    text.grid(row=0, column=0)
    er.mainloop()

def del_aft_cp():
    for filepath in filelist:
        os.remove(filepath)


def mainrun():
    main_run = threading.Thread(target=main)
    main_run.start()


def set_lineNub():
    global lineNub
    lineNub = set_lineNub_entry.get()
    lineNub_show.set(lineNub)


set_dir_bt = tk.Button(root, text='设置工作目录', command=getDir)
start_bt = tk.Button(root, text='开始对比', command=mainrun)
del_bt = tk.Button(root, text='重复文件移动至MD5命名的文件夹之后，从工作文件夹中删除', command=del_aft_cp)
work_dir_print = tk.Label(root, textvariable=work_dir_show)
set_lineNub_entry = tk.Entry(root)
set_lineNub_bt = tk.Button(root, text='设置最大比对线程数,默认10', command=set_lineNub)
lineNub_print = tk.Label(root, textvariable=lineNub_show)

set_dir_bt.grid(row=0, column=0)
work_dir_print.grid(row=0, column=1)
set_lineNub_bt.grid(row=1, column=0)
set_lineNub_entry.grid(row=1, column=1)
lineNub_print.grid(row=1, column=2)
start_bt.grid(row=2, column=0)
del_bt.grid(row=2, column=1)

root.mainloop()

# ==============================================================================================================
