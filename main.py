# Your Name: Nurmukhammed
# Date: March 7
# Main file that runs the game

from player import Player
import chapter1
import chapter2
import chapter3
import chapter4
import chapter5

def main():
    print("Welcome to The Last Crystal of Eldoria")
    name = input("Enter your hero name: ")

    player = Player(name)

    chapter1.play_chapter1(player)
    chapter2.play_chapter2(player)
    chapter3.play_chapter3(player)
    chapter4_result = chapter4.play_chapter4(player)
    chapter5.play_chapter5(chapter4_result, player)

if __name__ == "__main__":
    main()