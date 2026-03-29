# Your Name: Nurmukhammed
# Date: March 7
# Chapter 4 – The Crystal Chamber

def play_chapter4(player):
    print("Chapter 4: The Crystal Chamber")

    if player.item == "key" and player.health > 50:
        print("You unlock the chamber safely.")
        return "safe"
    elif player.item == "alone" and player.health > 50:
        print("You force the door open and trigger a trap.")
        return "trap"
    else:
        print("You are too weak to enter the chamber properly.")
        return "fail"