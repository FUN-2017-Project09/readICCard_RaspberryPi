#!/usr/bin/env python
# -*- coding: utf-8 -*-

import readICCard
import sys

#message output
FAIL = '\033[91m'
GREEN = '\033[92m'
ENDC = '\033[0m'
def method(method):
    p = GREEN + '----- ' + method + ' -----' + ENDC
    print(p)
def error(message):
    p = FAIL + message + ENDC
    print(p)
    sys.exit()

# test
try:
    hoge = readICCard.readICCard()
    method("getIDM")
    print(hoge.getIDM())
    method("getUseHistory")
    print(hoge.getUseHistory())
    method("getEntryHistory")
    print(hoge.getEntryHistory())
    method("Year-Month-Day")
    print(hoge.getYear(0))
    print(hoge.getMonts(0))
    print(hoge.getDay(0))
    method("getProcess")
    print(hoge.getProcess(0))
    method("getBalance")
    print(hoge.getBalance(0))
    method("getOperatorCode")
    print(hoge.getOperatorCode(0))
except IOError:  
    error("sudoで実行していない / 読み取り機を認識していない(IOError)")
except AttributeError:
    #ゲームセンターのカードで確認
    #属性参照や代入の失敗
    error("importミス / 同じファイル名がある / 履歴が存在しないカード(AttributeError)")
except TypeError:
    error("アクセスした履歴に日付はありません(TypeError)")
except MemoryError:
    error("操作中にメモリが不足(MemoryError)")
except NameError:
    error("ローカルまたはグローバルの名前が見つかりませんでした(NameError)")
except OSError:
    error("システム関数がエラーを返却しました(OSError)")
except RuntimeError:
    error("予期せぬエラーが発生しました(RuntimeError)")
