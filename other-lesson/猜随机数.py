"""
随机指定一个1到100之间的随机数，
给出一个数：大了，显示"太大了"；小了，显示"太小了"
直到猜对为止，猜对之后显示猜了几次，并问还要继续猜吗？
"""

import random
import sys

while True:
    unkown_number = random.randint(1, 100)
    guess_count = 0
    guess_flg = True

    while guess_flg:
        print("please input a number:")
        input_str = input()
        guess_count +=1
        try:
            input_number = int(input_str)
        except Exception as e:
            print(e)
            print("please input again:")
        else:
            if input_number == unkown_number:
                guess_flg = False
                print("you got it, the number is {}. guess_count:{}".format(unkown_number,guess_count))
                print("if you want to play again , please input yes.")
                again_input = input()
                if again_input == "yes":
                    pass
                else:
                    sys.exit(1)
            if input_number > unkown_number:
                print("太大了")
            else:
                print("太小了")
