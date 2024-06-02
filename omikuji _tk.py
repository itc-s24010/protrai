#s24010
#実行するとランダムで6つの運勢からから一つ表示される


import random
kuji = ["大吉","中吉","末吉","小吉","凶","大凶"]
print(random.choice(kuji))


import tkinter as tk 
root = tk.Tk()

root.geometry("500x700")
root.title("おみくじ")
lbl = tk.Label(text=(random.choice(kuji)))
lbl.pack()
               
 
root.mainloop
