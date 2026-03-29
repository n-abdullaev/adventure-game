# Your Name: Nurmukhammed
# Date: March 7
# Chapter 3 – The Wizard’s Choice

def play_chapter3(player):
    print("Chapter 3: The Wizard’s Choice")
    print("You meet an old wizard.")
    print("Do you trust the wizard or continue alone?")
    choice = input("Enter trust or alone: ").lower()

    if choice == "trust":
        print("The wizard gives you a magical key.")
        player.item = "key"
    elif choice == "alone":
        print("You continue alone without help.")
        player.item = "alone"
    else:
        print("Invalid choice. You continue alone.")
        player.item = "alone"