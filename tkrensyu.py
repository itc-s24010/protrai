import tkinter as tk#まずこの行を書く必要がある

root = tk.Tk()#初めのおまじない

root.geometry("500x750")#ウィンドウのサイズを決める
root.title("ハローアプリ")#ウィンドウのタイトルを決める
lbl = tk.Label(text="こんにちは世界")#いつもの
lbl.pack() #lblを配置させる必要がある




root.mainloop
