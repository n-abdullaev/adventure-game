# Your Name: Nurmukhammed
# Date: March 7
# Chapter 2 – The First Trial

def play_chapter2(player):
    print("Chapter 2: The First Trial")

    if player.path == "forest":
        print("A magical beast blocks your way.")
        print("Do you fight or run?")
        choice = input("Enter fight or run: ").lower()

        if choice == "fight":
            print("You defeat the beast.")
            player.chapter2_result = "victory"
        else:
            print("You escape, but lose courage and some health.")
            player.chapter2_result = "escape"
            player.lose_health(30)

    elif player.path == "mountain":
        print("A storm blocks your way.")
        print("Do you climb or wait?")
        choice = input("Enter climb or wait: ").lower()

        if choice == "climb":
            print("You survive the dangerous climb.")
            player.chapter2_result = "victory"
        else:
            print("You wait too long and lose time and some health.")
            player.chapter2_result = "delay"
            player.lose_health(30)

    else:
        print("You are lost and become weaker.")
        player.chapter2_result = "lost"
        player.lose_health(50)