# Your Name: Nurmukhammed
# Date: March 7
# Chapter 1 – The Call to Adventure

def play_chapter1():
    print("Chapter 1: The Call to Adventure")
    print("You are chosen to save the Last Crystal of Eldoria.")
    print("Do you go to the Enchanted Forest or the Mountain Pass?")
    choice = input("Enter forest or mountain: ").lower()

    if choice == "forest":
        print("You enter the Enchanted Forest.")
        return "forest"
    elif choice == "mountain":
        print("You take the Mountain Pass.")
        return "mountain"
    else:
        print("Invalid choice. You lose time.")
        return "invalid"