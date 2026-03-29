# Your Name: Nurmukhammed
# Date: March 7
# Chapter 5 – The Final Ending

def play_chapter5(result, player):
    print("Chapter 5: The Final Ending")
    print("Final Status:", player.get_status())

    if result == "safe":
        print("You restore the Last Crystal and save Eldoria.")
    elif result == "trap":
        print("You reach the crystal, but darkness defeats you.")
    else:
        print("You fail to restore the crystal. Eldoria falls.")