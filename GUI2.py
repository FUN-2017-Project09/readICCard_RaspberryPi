# -*- coding: UTF-8 -*-
import Tkinter
from Tkinter import *
import ttk
import datetime
import sys
sys.path.append('/usr/local/src/nfcpy')
import nfc
import readICCard
import tkMessageBox
import requests

today = datetime.date.today()
TODAY = str(today.year) + "/" + str(today.month) + "/" + str(today.day)
ID = ""
datehistory = ""
stop_and_station =  ""
balance = 0
CHEAT_CARD_ID = "011203123D180320"
judge = "OK"

def defineData():
    global ID, datehistory, stop_and_station, balance
    i = 0
    try:
        hoge = readICCard.readICCard()
        forData = hoge.getUseHistory()
        ID = hoge.getIDM()
        balance = hoge.getBalance(0)
        for i  in range(20):
            if ((forData[i][1] == 15 and forData[i][3] == 15) or (forData[i][1] == "13" and forData[i][3] == "13")) and (hoge.getOperatorCode(i) == 2315 or hoge.getOperatorCode(i) == 2316):
                stop_and_station = "バス"
                datehistory = "20" + str(hoge.getYear(i)) + "/" + str(hoge.getMonts(i)) + "/" + str(hoge.getDay(i))
                break
            i+=1
    except IOError:
        if (tkMessageBox.askretrycancel("IOError", "エラー\nICカード読み取り機を認識していません\nUSBを挿し直してから再試行ボタンを押してください\nキャンセルでプログラムを終了します")):
            sys.exit(True)
        else:
            sys.exit(False)
    except AttributeError:
        tkmessageBox.showerror("AttributeError","履歴領域が存在しないカードです\n別のカードを使用してください。")
        sys.exit(True)
    except TypeError:
        tkmessageBox.showerror("TypeError","アクセスした履歴データに日付のデータがありませんでした。\n別のカードで再試行してください。")
        sys.exit(True)
    #del hoge



def reg():
    global judge
    URL = 'http://192.168.2.101/www/debugpage2/type/receive.php?node=1&ID='
    totalURL = URL + ID
    #print totalURL
    r = requests.get(totalURL)

    if r.text.count('IDm') == 0:
        URL = 'http://192.168.2.101/www/debugpage2/type/register.php?node=1&ID='
        totalURL = URL + ID
        r = requests.get(totalURL)

    else:
        check = r.text.index('時間は'.decode("utf-8"))
        if r.text[check+9] == "0":
            smonth = r.text[check+10]
        else:
            smonth = r.text[check+9 : check+11]
        if r.text[check+12] == "0":
            sday = r.text[check+13]
        else:
            sday = r.text[check+12 : check+14]
        sevdate = r.text[check+4 : check+8] + "/" + smonth + "/" + sday
        print sevdate
        print TODAY
        if sevdate != TODAY:
            judge = "OK"
        else:
            judge = "NG"

        
def GUI():
    global window
    window = Tkinter.Tk()
    window.title(u"ICカード割引")
    window.attributes("-zoomed", "1")
    #window.geometry('800x480+0+0')

    canvas = Tkinter.Canvas(window, width = 800, height = 480)
    canvas.create_rectangle(800, 480, 0, 0, fill = 'white')   
    canvas.place(x=0, y=0)

    button = Tkinter.Button(window, text = (u'読み取り開始'), width =15, height=2)
    button.bind("<Button-1>", start)
    button.place(x = 60, y = 95)
    button.config(font=("游ゴシック Light", 60))
    window.mainloop()

def windel(event):
    #window.destroy()
    #GUI()
    sys.exit(True)

def finish(event):
    sys.exit(False)
    
def start(event):
    while True:
        defineData()
        if ID != "":
            break

    reg()
    
    canvas = Tkinter.Canvas(window, width = 800, height = 480)
    canvas.create_rectangle(800, 480, 0, 0, fill = 'white')   
    canvas.place(x=0, y=0)                                    

    button1 = Tkinter.Button(window, text = '戻る', height = 2, width = 7)
    button1.config(font=("游ゴシック Light", 20))
    button1.bind("<Button-1>", windel)
    button2 = Tkinter.Button(window, text = '終了', height = 2, width = 7)
    button2.config(font=("游ゴシック Light", 20))
    button2.bind("<Button-1>", finish)

    IDmessage0  = Tkinter.Label(text = ( u'ID : ' ), background = '#FFFFFF', font=(u'游ゴシック Light', 32))
    IDmessage1  = Tkinter.Label(text = ( ID ), background = '#FFFFFF', font=(u'游ゴシック Light', 32))

    balmessage0 = Tkinter.Label(text = ( u'現在の残高 : ' ), background = '#FFFFFF', font=(u'游ゴシック Light', 32))
    balmessage1 = Tkinter.Label(text = (  balance  ), background = '#FFFFFF', font=(u'游ゴシック Light', 32))

    SASmessage0 = Tkinter.Label(text = ( u'利用した交通機関 : ' ), background = '#FFFFFF', font=(u'游ゴシック Light', 32))
    SASmessage1 = Tkinter.Label(text = ( stop_and_station ), background = '#FFFFFF', font=(u'游ゴシック Light', 32))

    OK1         = Tkinter.Label(text = u'ICカード割引 : OK', foreground = '#0000ff', background = '#aaccff', font=(u'游ゴシック Light', 28, 'underline'))
    NG1         = Tkinter.Label(text = u'ICカード割引 : NG', foreground = '#ff0000', background = '#ffaacc', font=(u'游ゴシック Light', 28, 'underline'))

    ngdatemsg   = Tkinter.Label(text = u'日付が違います : ', foreground = '#ff0000', background = '#ffaacc', font=(u'游ゴシック Light', 28))
    ngdate      = Tkinter.Label(text = datehistory , foreground = '#ff0000', background = '#ffaacc', font=(u'游ゴシック Light', 28))
    ngtransmsg  = Tkinter.Label(text = u'バスが使用されていません', foreground = '#ff0000', background = '#ffaacc', font=(u'游ゴシック Light', 28))

    twicemsg = Tkinter.Label(text = u'本日は既にご利用済みです', foreground = '#ff0000', background = '#ffaacc', font=(u'游ゴシック Light', 28))

    if judge == "OK":  
        if stop_and_station == "バス":
                if datehistory == TODAY or ID == CHEAT_CARD_ID:
                    OK1.place(x = 60, y = 300)
                else:
                    NG1.place(x = 60, y = 230)
                    ngdatemsg.place(x = 60, y = 300)
                    ngdate.place(x = 350, y = 300)
        else:
                NG1.place(x = 60, y = 230)
                ngtransmsg.place(x = 60, y = 300)
    else:
        twicemsg.place(x = 60, y = 300)

    IDmessage0.place(x = 50, y = 50)
    IDmessage1.place(x = 130 , y = 50)
    SASmessage0.place(x = 50, y = 100)
    SASmessage1.place(x = 430, y = 100)
    balmessage0.place(x = 50, y = 150)
    balmessage1.place(x = 300, y = 150)
    button1.place(x = 510, y = 300)
    button2.place(x = 655, y = 300)
    window.mainloop()

    

if __name__ == '__main__':
    GUI()
