# Your Name: Nurmukhammed
# Date: March 7
# Chapter 2 – The First Trial

def play_chapter2(path):
    print("Chapter 2: The First Trial")

    if path == "forest":
        print("A magical beast blocks your way.")
        print("Do you fight or run?")
        choice = input("Enter fight or run: ").lower()

        if choice == "fight":
            print("You defeat the beast.")
            return "victory"
        else:
            print("You escape, but lose courage.")
            return "escape"

    elif path == "mountain":
        print("A storm blocks your way.")
        print("Do you climb or wait?")
        choice = input("Enter climb or wait: ").lower()

        if choice == "climb":
            print("You survive the dangerous climb.")
            return "victory"
        else:
            print("You wait too long and lose time.")
            return "delay"

    else:
        print("You are lost.")
        return "lost"