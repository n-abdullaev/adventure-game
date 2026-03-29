# Your Name: Nurmukhammed
# Date: March 7
# Chapter 4 – The Crystal Chamber

def play_chapter4(item):
    print("Chapter 4: The Crystal Chamber")

    if item == "key":
        print("You unlock the chamber safely.")
        return "safe"
    elif item == "alone":
        print("You force the door open and trigger a trap.")
        return "trap"
    else:
        print("You cannot enter properly.")
        return "fail"