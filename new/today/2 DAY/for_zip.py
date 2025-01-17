#!/usr/bin/python

words1 = ["cup", "bottle", "table", "rock", "apple"]
words2 = ["trousers", "nail", "head", "water", "pen"]

for w1, w2 in zip(words1, words2):
    print(w1, w2)