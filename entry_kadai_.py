#24010
#受け取った名前に挨拶をする

import tkinter as tk #tkinterをtkと略して使用する

def dispLabel():
    #entryメゾットを使用して入力を受け付け変数aに格納
    a = entry.get()
    print(f"aは{type(a)}") #ログの出方
    lbl.config(text=f"{a}さんこんんちは")


root = tk.Tk()
root.title("エントリーウィジェット")
root.geometry("400x200") #画面の大きさを決める

lbl = tk.Label(text="ラべル", font=("Helvetica", 20))
entry = tk.Entry(font=("Helvetica", 20))
btn = tk.Button(text="ボタン", font=("Helvetica", 20), command=dispLabel)

lbl.pack()
entry.pack()
btn.pack()

tk.mainloop()
