# Your Name: Nurmukhammed
# Date: March 7
# Main file that runs the game

import chapter1
import chapter2
import chapter3
import chapter4
import chapter5

path = chapter1.play_chapter1()
chapter2_result = chapter2.play_chapter2(path)
item = chapter3.play_chapter3()
chapter4_result = chapter4.play_chapter4(item)
chapter5.play_chapter5(chapter4_result)