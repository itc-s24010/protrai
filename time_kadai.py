#24010
#実行ができたら時間を表示させる「時計アプリ」作成。
#時計アプリはモジュール名「time_kadai.py」で作成。
#時計アプリを使いやすくバージョンアップしていきます。

import datetime
import tkinter as tk #GUIアプリでは作ることができるモジュール

#時間を処理する部分を関数で実装
def update_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%Y年%m月%d日 %H時%M分%S秒")

    lbl.config(text=current_time)
    root.after(1000, update_time)
    
#ウィンドウを作成
root = tk.Tk()#初め

root.title("時計アプリ")

lbl = tk.Label()
lbl.config(text="", font = ("Helvetica", 20))
lbl.pack()

#関数呼び出し
update_time()

root.mainloop() #終わり
