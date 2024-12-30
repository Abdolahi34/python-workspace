import random
from termcolor2 import HIGHLIGHTS

def input_p1():
    global  c1,c2,c3,c4,c5,c6,c7,c8,c9
    print("\nHint ...\n") #state of Play
    print(f" {c1} | {c2} | {c3} ")
    print("-"*11)
    print(f" {c4} | {c5} | {c6} ")
    print("-"*11)
    print(f" {c7} | {c8} | {c9} ")
    while True:
        x1=int(input("\nPlayer 1 :\nEnter Num of Place: (Num 1 to 9)\n"))
        if x1>=1 or x1<=9:
            if x1==1:
                if c1==1:
                    c1="X"
                    break
            elif x1==2:
                if c2==2:
                    c2="X"
                    break
            elif x1==3:
                if c3==3:
                    c3="X"
                    break
            elif x1==4:
                if c4==4:
                    c4="X"
                    break
            elif x1==5:
                if c5==5:
                    c5="X"
                    break
            elif x1==6:
                if c6==6:
                    c6="X"
                    break
            elif x1==7:
                if c7==7:
                    c7="X"
                    break
            elif x1==8:
                if c8==8:
                    c8="X"
                    break
            elif x1==9:
                if c9==9:
                    c9="X"
                    break
        else:
            print("\nInvalid data ...")

def input_p2():
    global  c1,c2,c3,c4,c5,c6,c7,c8,c9
    print("\nHint ...\n") #state of Play
    print(f" {c1} | {c2} | {c3} ")
    print("-"*11)
    print(f" {c4} | {c5} | {c6} ")
    print("-"*11)
    print(f" {c7} | {c8} | {c9} ")
    while True:
        x2=int(input("\nPlayer 2 :\nEnter Num of Place: (Num 1 to 9)\n"))
        if x2>=1 or x2<=9:
            if x2==1:
                if c1==1:
                    c1="Y"
                    break
            elif x2==2:
                if c2==2:
                    c2="Y"
                    break
            elif x2==3:
                if c3==3:
                    c3="Y"
                    break
            elif x2==4:
                if c4==4:
                    c4="Y"
                    break
            elif x2==5:
                if c5==5:
                    c5="Y"
                    break
            elif x2==6:
                if c6==6:
                    c6="Y"
                    break
            elif x2==7:
                if c7==7:
                    c7="Y"
                    break
            elif x2==8:
                if c8==8:
                    c8="Y"
                    break
            elif x2==9:
                if c9==9:
                    c9="Y"
                    break
        else:
            print("\nInvalid data ...")

def input_c():
    global  c1,c2,c3,c4,c5,c6,c7,c8,c9
    while True:
        c_list=[1,2,3,4,5,6,7,8,9]
        c=random.choice(c_list)
        c_list.remove(c)
        if c==1:
            if c1==1:
                c1="Z"
                print(f"\nThe Computer Select Cell No. {c}\n")
                break
        elif c==2:
            if c2==2:
                c2="Z"
                print(f"\nThe Computer Select Cell No. {c}\n")
                break
        elif c==3:
            if c3==3:
                c3="Z"
                print(f"\nThe Computer Select Cell No. {c}\n")
                break
        elif c==4:
            if c4==4:
                c4="Z"
                print(f"\nThe Computer Select Cell No. {c}\n")
                break
        elif c==5:
            if c5==5:
                c5="Z"
                print(f"\nThe Computer Select Cell No. {c}\n")
                break
        elif c==6:
            if c6==6:
                c6="Z"
                print(f"\nThe Computer Select Cell No. {c}\n")
                break
        elif c==7:
            if c7==7:
                c7="Z"
                print(f"\nThe Computer Select Cell No. {c}\n")
                break
        elif c==8:
            if c8==8:
                c8="Z"
                print(f"\nThe Computer Select Cell No. {c}\n")
                break
        elif c==9:
            if c9==9:
                c9="Z"
                print(f"\nThe Computer Select Cell No. {c}\n")
                break

def win_game_p1(): #p1 Borde?
    if c1=="X" and c2=="X" and c3=="X":
        return 1
    elif c4=="X" and c5=="X" and c6=="X":
        return 1
    elif c7=="X" and c8=="X" and c9=="X":
        return 1
    elif c3=="X" and c5=="X" and c7=="X":
        return 1
    elif c1=="X" and c5=="X" and c9=="X":
        return 1
    elif c1=="X" and c4=="X" and c7=="X":
        return 1
    elif c2=="X" and c5=="X" and c8=="X":
        return 1
    elif c3=="X" and c6=="X" and c9=="X":
        return 1
    else:
        return 0
def win_game_p2(): #p2 Borde?
    if c1=="Y" and c2=="Y" and c3=="Y":
        return 1
    elif c4=="Y" and c5=="Y" and c6=="Y":
        return 1
    elif c7=="Y" and c8=="Y" and c9=="Y":
        return 1
    elif c3=="Y" and c5=="Y" and c7=="Y":
        return 1
    elif c1=="Y" and c5=="Y" and c9=="Y":
        return 1
    elif c1=="Y" and c4=="Y" and c7=="Y":
        return 1
    elif c2=="Y" and c5=="Y" and c8=="Y":
        return 1
    elif c3=="Y" and c6=="Y" and c9=="Y":
        return 1
    else:
        return 0

def win_game_c(): #p2 Borde?
    if c1=="Z" and c2=="Z" and c3=="Z":
        return 1
    elif c4=="Z" and c5=="Z" and c6=="Z":
        return 1
    elif c7=="Z" and c8=="Z" and c9=="Z":
        return 1
    elif c3=="Z" and c5=="Z" and c7=="Z":
        return 1
    elif c1=="Z" and c5=="Z" and c9=="Z":
        return 1
    elif c1=="Z" and c4=="Z" and c7=="Z":
        return 1
    elif c2=="Z" and c5=="Z" and c8=="Z":
        return 1
    elif c3=="Z" and c6=="Z" and c9=="Z":
        return 1
    else:
        return 0

# -----------------------------------------------------------------------------

print("Salam\n***Be Bazi Dooz Khosh Amadid***")

while True:
    start0=input("\nAgar Baraye Shoroe Bazi Amade ei? (Enter y)\n")
    if start0[0]=="y" or start0[0]=="Y":
        break
    else:
        print("\nInvalid data ...")

while True:
    state=int(input("\nPlayer 1 Vs Player 2? (Enter 1)\nPlayer Vs Computer? (Enter 2)\n"))
    if state==1 or state==2:
        break
    else:
        print("\nInvalid data ...")

p1_point=0
p2_point=0
c_point=0

c1,c2,c3,c4,c5,c6,c7,c8,c9=1,2,3,4,5,6,7,8,9

while True:
    f_set=int(input("Round of Game?"))
    if f_set>0:
        break
    else:
        print("invalid data ...")

if state==1: #start Game
    i_set=1
    while True: #p1 VS p2
        print(f"Set Of Game: {i_set}")
        print(f"Player 1 Point: {p1_point}\nPlayer 2 Point: {p2_point}")
        
        win_p1=0
        win_p2=0
        i_c=0
        while win_p1==0 and win_p2==0: # Main Of Game
            input_p1()
            i_c += 1
            if i_c==9:
                win_p1=win_game_p1()
                win_p2=win_game_p2()
                if win_p1==0 and win_p2==0:
                    break_game=1
                break
            if win_p1!=1:
                input_p2()
                i_c += 1
            else:
                break
            if i_c>2:
                win_p1=win_game_p1()
                win_p2=win_game_p2()
        
        if win_p1==1:
            p1_point+=1
        elif win_p2==1:
            p2_point+=1

        print("-------------------------------------")
        print(f"End the Set Of Game: {i_set}")
        print(f" {c1} | {c2} | {c3} ")
        print("-"*11)
        print(f" {c4} | {c5} | {c6} ")
        print("-"*11)
        print(f" {c7} | {c8} | {c9} ")
        if win_p1==1:
            print("\n/\/\/\ Player 1 Is Winner. /\/\/\\\n")
        elif win_p2==1:
            print("\n/\/\/\ Player 2 Is Winner. /\/\/\\\n")
        elif break_game==1:
            print("\n/\/\/\ The Game Has not Winner. /\/\/\\\n")
        print(f"Player 1 Point: {p1_point}\nPlayer 2 Point: {p2_point}\n")
        print("-------------------------------------")

        '''End Set of Game'''
        if f_set==i_set:
            result0=input("\n q  -> for Quit\n c  -> for Continue\n")
            if result0[0]=="q" or result0[0]=="Q":
                break
            else:
                c1,c2,c3,c4,c5,c6,c7,c8,c9=1,2,3,4,5,6,7,8,9
                break_game=0
                while True:
                    f_set=int(input("Chand Set Dige Mikhahi Bazi Koni?"))
                    if f_set>0:
                        i_set=1
                        break
                    else:
                        print("Invalid data ...")
        else:
            c1,c2,c3,c4,c5,c6,c7,c8,c9=1,2,3,4,5,6,7,8,9
            i_set += 1
            break_game=0

# -------------------------------------------------

else:
    i_set=1
    while True: #p1 VS Computer
        print(f"Set Of Game: {i_set}")
        print(f"Player 1 Point: {p1_point}\nComputer Point: {c_point}")
        
        win_p1=0
        win_c=0
        i_c=0
        while win_p1==0 and win_c==0: # Main Of Game
            input_p1()
            i_c += 1
            if i_c==9:
                win_p1=win_game_p1()
                win_c=win_game_c()
                if win_p1==0 and win_c==0:
                    break_game=1
                break
            win_p1=win_game_p1()
            if win_p1!=1:
                input_c()
                i_c += 1
            else:
                break
            if i_c>2:
                win_c=win_game_c()
        
        if win_p1==1:
            p1_point+=1
        elif win_c==1:
            c_point+=1

        print("-------------------------------------")
        print(f"End the Set Of Game: {i_set}")
        print(f" {c1} | {c2} | {c3} ")
        print("-"*11)
        print(f" {c4} | {c5} | {c6} ")
        print("-"*11)
        print(f" {c7} | {c8} | {c9} ")
        if win_p1==1:
            print("\n/\/\/\ Player 1 Is Winner. /\/\/\\\n")
        elif win_c==1:
            print("\n/\/\/\ Computer Is Winner. /\/\/\\\n")
        elif break_game==1:
            print("\n/\/\/\ The Game Has not Winner. /\/\/\\\n")
        print(f"Player 1 Point: {p1_point}\nComputer Point: {c_point}\n")
        print("-------------------------------------")

        '''End Set of Game'''
        if f_set==i_set:
            result0=input("\n q  -> for Quit\n c  -> for Continue\n")
            if result0[0]=="q" or result0[0]=="Q":
                break
            else:
                c1,c2,c3,c4,c5,c6,c7,c8,c9=1,2,3,4,5,6,7,8,9
                break_game=0
                while True:
                    f_set=int(input("Chand Set Dige Mikhahi Bazi Koni?"))
                    if f_set>0:
                        i_set=1
                        break
                    else:
                        print("Invalid data ...")
        else:
            c1,c2,c3,c4,c5,c6,c7,c8,c9=1,2,3,4,5,6,7,8,9
            i_set += 1
            break_game=0