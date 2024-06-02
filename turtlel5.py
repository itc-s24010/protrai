from turtle import *
import random
shape = ("turtle")
col = ["orange","limegreen","gold","plum","tomato"]
for i in range(200):
    color(random.choice(col))
    forward(100)
    left(100)

done()
