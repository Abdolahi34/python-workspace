from pyfiglet import print_figlet
from termcolor2 import colored
from random import randint, choice

# -----------------------------------------------------------
'''
***   Class
'''
'''
Traceback (most recent call last):
  File "d:\not_on_hard\دسته بندی نشده\پروژه\برنامه نویسی\بازی دوز (ترمینال پایتون)\نسخه 2\Dooz.py", line 624, in <module>
    DefineUser(2)
  File "d:\not_on_hard\دسته بندی نشده\پروژه\برنامه نویسی\بازی دوز (ترمینال پایتون)\نسخه 2\Dooz.py", line 582, in DefineUser
    Player1.SetColor()
AttributeError: 'User' object has no attribute 'SetColor'
'''
# resolve above error


class User:
    SelectedCell = []
    UnSelectedCell = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    def __init__(self, username="UnDefined", name="UnDefined", color="UnDefined", icon="", point=0, winner=False):
        self.username = username
        self.name = name
        self.color = color
        self.icon = icon
        self.point = point
        self.winner = winner

    @property
    def Color(self):
        return self.color

    @Color.setter
    def Color(self):
        if self.name != "Robot":
            print(f"\n{self.name}, Che Rangi ra Doost dari?")
            print(colored("1. Red", color="red"))
            print(colored("2. Green", color="green"))
            print(colored("3. Yellow", color="yellow"))
            print(colored("4. Blue", color="blue"))
            print(colored("5. Magenta", color="magenta"))
            print(colored("6. Cyan", color="cyan"))
            while True:
                _Temp3 = int(input("\nEnter Num of Color :   "))
                if 0 < _Temp3 < 7:
                    if _Temp3 == 1:
                        self.color = "red"
                    elif _Temp3 == 2:
                        self.color = "green"
                    elif _Temp3 == 3:
                        self.color = "yellow"
                    elif _Temp3 == 4:
                        self.color = "blue"
                    elif _Temp3 == 5:
                        self.color = "magenta"
                    elif _Temp3 == 6:
                        self.color = "cyan"
                    if Player1.color == Player2.color:
                        print(f"Color Of {Player1.name} = Color Of {Player2.name} ,Please Enter Different Number (Color).")
                        continue
                    else:
                        break
                else:
                    print("invalid data...")
        else:
            while True:
                _Temp8 = randint(1,6)
                if _Temp8 == 1:
                    self.color = "red"
                elif _Temp8 == 2:
                    self.color = "green"
                elif _Temp8 == 3:
                    self.color = "yellow"
                elif _Temp8 == 4:
                    self.color = "blue"
                elif _Temp8 == 5:
                    self.color = "magenta"
                elif _Temp8 == 6:
                    self.color = "cyan"
                if Player1.color != Player2.color:
                    break


    def SetName(self):
        while True:
            self.name = input(f"\nEnter Name Of {self.username} :   ")
            if Player1.name != Player2.name:
                if len(self.name) > 2:
                    break
                else:
                    print("Nam Kootah Ast.")
            else:
                print("Player 1 & Player 2 Name Yeksani Darand. Lotfan Name Digari Ra Vared Konid.")


    def SetCell(self):
        if self.name != "Robot":
            GameMap()
            while True:
                _Temp2 = int(input(f"\n{self.name}, Enter Number Of Cell (Ex. 5):   "))
                if 0 < _Temp2 < 17:
                    if _Temp2 == 1 and 1 in User.UnSelectedCell:
                        self.SelectedCell.append(1)
                        User.UnSelectedCell.remove(1)
                        break
                    elif _Temp2 == 2 and 2 in User.UnSelectedCell:
                        self.SelectedCell.append(2)
                        User.UnSelectedCell.remove(2)
                        break
                    elif _Temp2 == 3 and 3 in User.UnSelectedCell:
                        self.SelectedCell.append(3)
                        User.UnSelectedCell.remove(3)
                        break
                    elif _Temp2 == 4 and 4 in User.UnSelectedCell:
                        self.SelectedCell.append(4)
                        User.UnSelectedCell.remove(4)
                        break
                    elif _Temp2 == 5 and 5 in User.UnSelectedCell:
                        self.SelectedCell.append(5)
                        User.UnSelectedCell.remove(5)
                        break
                    elif _Temp2 == 6 and 6 in User.UnSelectedCell:
                        self.SelectedCell.append(6)
                        User.UnSelectedCell.remove(6)
                        break
                    elif _Temp2 == 7 and 7 in User.UnSelectedCell:
                        self.SelectedCell.append(7)
                        User.UnSelectedCell.remove(7)
                        break
                    elif _Temp2 == 8 and 8 in User.UnSelectedCell:
                        self.SelectedCell.append(8)
                        User.UnSelectedCell.remove(8)
                        break
                    elif _Temp2 == 9 and 9 in User.UnSelectedCell:
                        self.SelectedCell.append(9)
                        User.UnSelectedCell.remove(9)
                        break
                    elif _Temp2 == 10 and 10 in User.UnSelectedCell:
                        self.SelectedCell.append(10)
                        User.UnSelectedCell.remove(10)
                        break
                    elif _Temp2 == 11 and 11 in User.UnSelectedCell:
                        self.SelectedCell.append(11)
                        User.UnSelectedCell.remove(11)
                        break
                    elif _Temp2 == 12 and 12 in User.UnSelectedCell:
                        self.SelectedCell.append(12)
                        User.UnSelectedCell.remove(12)
                        break
                    elif _Temp2 == 13 and 13 in User.UnSelectedCell:
                        self.SelectedCell.append(13)
                        User.UnSelectedCell.remove(13)
                        break
                    elif _Temp2 == 14 and 14 in User.UnSelectedCell:
                        self.SelectedCell.append(14)
                        User.UnSelectedCell.remove(14)
                        break
                    elif _Temp2 == 15 and 15 in User.UnSelectedCell:
                        self.SelectedCell.append(15)
                        User.UnSelectedCell.remove(15)
                        break
                    elif 16 in User.UnSelectedCell:
                        self.SelectedCell.append(16)
                        User.UnSelectedCell.remove(16)
                        break
                    else:
                        print(f"Cell {_Temp2} has already been selected.")
                else:
                    print("Invalid data ...")
        else:
            _Temp2 = choice(User.UnSelectedCell)
            if _Temp2 == 1:
                self.SelectedCell.append(1)
                User.UnSelectedCell.remove(1)
            elif _Temp2 == 2:
                self.SelectedCell.append(2)
                User.UnSelectedCell.remove(2)
            elif _Temp2 == 3:
                self.SelectedCell.append(3)
                User.UnSelectedCell.remove(3)
            elif _Temp2 == 4:
                self.SelectedCell.append(4)
                User.UnSelectedCell.remove(4)
            elif _Temp2 == 5:
                self.SelectedCell.append(5)
                User.UnSelectedCell.remove(5)
            elif _Temp2 == 6:
                self.SelectedCell.append(6)
                User.UnSelectedCell.remove(6)
            elif _Temp2 == 7:
                self.SelectedCell.append(7)
                User.UnSelectedCell.remove(7)
            elif _Temp2 == 8:
                self.SelectedCell.append(8)
                User.UnSelectedCell.remove(8)
            elif _Temp2 == 9:
                self.SelectedCell.append(9)
                User.UnSelectedCell.remove(9)
            elif _Temp2 == 10:
                self.SelectedCell.append(10)
                User.UnSelectedCell.remove(10)
            elif _Temp2 == 11:
                self.SelectedCell.append(11)
                User.UnSelectedCell.remove(11)
            elif _Temp2 == 12:
                self.SelectedCell.append(12)
                User.UnSelectedCell.remove(12)
            elif _Temp2 == 13:
                self.SelectedCell.append(13)
                User.UnSelectedCell.remove(13)
            elif _Temp2 == 14:
                self.SelectedCell.append(14)
                User.UnSelectedCell.remove(14)
            elif _Temp2 == 15:
                self.SelectedCell.append(15)
                User.UnSelectedCell.remove(15)
            else:
                self.SelectedCell.append(16)
                User.UnSelectedCell.remove(16)
            print(f"Cell {_Temp2} was selected by the Robot.")


    def IsWin(self):
        """
        Rahnama :
        1  2  3  4
        5  6  7  8
        9  10 11 12
        13 14 15 16
        """

        if 1 in self.SelectedCell:
            # 1 - Ofoghi
            if 2 in self.SelectedCell:
                if 3 in self.SelectedCell:
                    if 4 in self.SelectedCell:
                        return True
            # 1 - Amoodi
            if 5 in self.SelectedCell:
                if 9 in self.SelectedCell:
                    if 13 in self.SelectedCell:
                        return True
            # 1 - Orib
            if 6 in self.SelectedCell:
                if 11 in self.SelectedCell:
                    if 16 in self.SelectedCell:
                        return True
        if 2 in self.SelectedCell:
            # 2 - Amoodi
            if 6 in self.SelectedCell:
                if 10 in self.SelectedCell:
                    if 14 in self.SelectedCell:
                        return True
        if 3 in self.SelectedCell:
            # 3 - Amoodi
            if 7 in self.SelectedCell:
                if 11 in self.SelectedCell:
                    if 15 in self.SelectedCell:
                        return True
        if 4 in self.SelectedCell:
            # 4 - Amoodi
            if 8 in self.SelectedCell:
                if 12 in self.SelectedCell:
                    if 16 in self.SelectedCell:
                        return True
            # 4 - Orib
            if 7 in self.SelectedCell:
                if 10 in self.SelectedCell:
                    if 13 in self.SelectedCell:
                        return True
        if 5 in self.SelectedCell:
            # 5 - Ofoghi
            if 6 in self.SelectedCell:
                if 7 in self.SelectedCell:
                    if 8 in self.SelectedCell:
                        return True
        if 9 in self.SelectedCell:
            # 9 - Ofoghi
            if 10 in self.SelectedCell:
                if 11 in self.SelectedCell:
                    if 12 in self.SelectedCell:
                        return True
        if 13 in self.SelectedCell:
            # 13 - Ofoghi
            if 14 in self.SelectedCell:
                if 15 in self.SelectedCell:
                    if 16 in self.SelectedCell:
                        return True


# -----------------------------------------------------------
'''
***   def
'''


def GameMap():
    """
    S -> Space
    C -> Character

    Rahnama ye Naghshe :

    SCCS|SCCS|SCCS|SCCS
    SCCS|SCCS|SCCS|SCCS
    SCCS|SCCS|SCCS|SCCS
    SCCS|SCCS|SCCS|SCCS

    Ex.
     1  | 2  | 3  | 4
     10 | 11 | 12 | 13
    """

    global Player2Roll

    print("\n*** Map Of Game :")
    print(colored(f"{Player1.name} -> x", color=Player1.color))
    if Player2Roll == 1: print(colored(f"{Player2.name} -> O\n", color=Player2.color))
    else: print(colored("Computer -> O\n", color=Player2.color))

    # Start Line 1
    # Start Cell 1
    if 1 in Player1.SelectedCell: print(" " + colored(Player1.icon, color=Player1.color) + " ", end=" | ")
    elif 1 in Player2.SelectedCell: print(" " + colored(Player2.icon, color=Player2.color) + " ", end=" | ")
    else: print(" 1 ", end=" | ")  # End Cell 1
    # Start Cell 2
    if 2 in Player1.SelectedCell: print(colored(Player1.icon, color=Player1.color) + " ", end=" | ")
    elif 2 in Player2.SelectedCell: print(colored(Player2.icon, color=Player2.color) + " ", end=" | ")
    else: print("2 ", end=" | ")  # End Cell 2
    # Start Cell 3
    if 3 in Player1.SelectedCell: print(colored(Player1.icon, color=Player1.color) + " ", end=" | ")
    elif 3 in Player2.SelectedCell: print(colored(Player2.icon, color=Player2.color) + " ", end=" | ")
    else: print("3 ", end=" | ")  # End Cell 3
    # Start Cell 4
    if 4 in Player1.SelectedCell: print(colored(Player1.icon, color=Player1.color) + "  ")
    elif 4 in Player2.SelectedCell: print(colored(Player2.icon, color=Player2.color) + "  ")
    else: print("4  ")  # End Cell 4
    # End Line 1

    print("-" * 19)

    # Start Line 2
    # Start Cell 5
    if 5 in Player1.SelectedCell: print(" " + colored(Player1.icon, color=Player1.color) + " ", end=" | ")
    elif 5 in Player2.SelectedCell: print(" " + colored(Player2.icon, color=Player2.color) + " ", end=" | ")
    else: print(" 5 ", end=" | ")  # End Cell 5
    # Start Cell 6
    if 6 in Player1.SelectedCell: print(colored(Player1.icon, color=Player1.color) + " ", end=" | ")
    elif 6 in Player2.SelectedCell: print(colored(Player2.icon, color=Player2.color) + " ", end=" | ")
    else: print("6 ", end=" | ")  # End Cell 6
    # Start Cell 7
    if 7 in Player1.SelectedCell: print(colored(Player1.icon, color=Player1.color) + " ", end=" | ")
    elif 7 in Player2.SelectedCell: print(colored(Player2.icon, color=Player2.color) + " ", end=" | ")
    else: print("7 ", end=" | ")  # End Cell 7
    # Start Cell 8
    if 8 in Player1.SelectedCell: print(colored(Player1.icon, color=Player1.color) + "  ")
    elif 8 in Player2.SelectedCell: print(colored(Player2.icon, color=Player2.color) + "  ")
    else: print("8  ")  # End Cell 8
    # End Line 2

    print("-" * 19)

    # Start Line 3
    # Start Cell 9
    if 9 in Player1.SelectedCell: print(" " + colored(Player1.icon, color=Player1.color) + " ", end=" | ")
    elif 9 in Player2.SelectedCell: print(" " + colored(Player2.icon, color=Player2.color) + " ", end=" | ")
    else: print(" 9 ", end=" | ")  # End Cell 9
    # Start Cell 10
    if 10 in Player1.SelectedCell: print(colored(Player1.icon, color=Player1.color) + " ", end=" | ")
    elif 10 in Player2.SelectedCell: print(colored(Player2.icon, color=Player2.color) + " ", end=" | ")
    else: print("10", end=" | ")  # End Cell 10
    # Start Cell 11
    if 11 in Player1.SelectedCell: print(colored(Player1.icon, color=Player1.color) + " ", end=" | ")
    elif 11 in Player2.SelectedCell: print(colored(Player2.icon, color=Player2.color) + " ", end=" | ")
    else: print("11", end=" | ")  # End Cell 11
    # Start Cell 12
    if 12 in Player1.SelectedCell: print(colored(Player1.icon, color=Player1.color) + "  ")
    elif 12 in Player2.SelectedCell: print(colored(Player2.icon, color=Player2.color) + "  ")
    else: print("12 ")  # End Cell 12
    # End Line 3

    print("-" * 19)

    # Start Line 4
    # Start Cell 13
    if 13 in Player1.SelectedCell: print(" " + colored(Player1.icon, color=Player1.color) + " ", end=" | ")
    elif 13 in Player2.SelectedCell: print(" " + colored(Player2.icon, color=Player2.color) + " ", end=" | ")
    else: print(" 13", end=" | ")  # End Cell 13
    # Start Cell 14
    if 14 in Player1.SelectedCell: print(colored(Player1.icon, color=Player1.color) + " ", end=" | ")
    elif 14 in Player2.SelectedCell: print(colored(Player2.icon, color=Player2.color) + " ", end=" | ")
    else: print("14", end=" | ")  # End Cell 14
    # Start Cell 15
    if 15 in Player1.SelectedCell: print(colored(Player1.icon, color=Player1.color) + " ", end=" | ")
    elif 15 in Player2.SelectedCell: print(colored(Player2.icon, color=Player2.color) + " ", end=" | ")
    else: print("15", end=" | ")  # End Cell 15
    # Start Cell 16
    if 16 in Player1.SelectedCell: print(colored(Player1.icon, color=Player1.color) + "  ")
    elif 16 in Player2.SelectedCell: print(colored(Player2.icon, color=Player2.color) + "  ")
    else: print("16 ")  # End Cell 16
    # End Line 4


def StartGame():
    global CellsFull, ExitVar, Player2Roll, SetOfGameInt
    while True:
        i0 = 0
        while i0 < SetOfGameInt:
            ResetVariable()
            print("-"*14)
            print(f"\nSet Of Game: {i0 + 1}/{SetOfGameInt}")

            # Main Of Game
            while True:
                # Player 1
                if not User.UnSelectedCell:
                    CellsFull = True
                    break
                Player1.SetCell()
                if Player1.IsWin():
                    GameMap()
                    Player1.winner = True
                    break
                # Player 2
                if not User.UnSelectedCell:
                    CellsFull = True
                    break
                Player2.SetCell()
                if Player2.IsWin():
                    GameMap()
                    Player2.winner = True
                    break

            i0 += 1

            if CellsFull:
                PrintNoWinner()
            elif Player1.winner:
                PrintWinner()
            elif Player2.winner:
                PrintWinner()

        SetOfGameInt = 0

        ExitVar = KhasteShodi()
        if ExitVar == 3:
            break
        elif not ExitVar:
            SetOfGameFunc()
            continue

        else:
            if Player2Roll == 2:
                while True:
                    print(f" {Player1.name} Bemanad? (Enter 1)")
                    print(" Afrade Digari Mikhahand Bazi Konand? (Enter 2)   ")
                    _Temp6 = int(input())
                    if _Temp6 == 1:
                        DefineUser(3)
                        Player2.point = 0
                        break
                    elif _Temp6 == 2:
                        DefineUser(1)
                        Player1.point = 0
                        Player2.point = 0
                        break
                    else:
                        print("invalid data...")
                Player2Roll = 1
                SetOfGameFunc()
                continue
            else:
                while True:
                    print(f"\n {Player1.name} Mikhahad Ba Robot Bazi Konad? (Enter 1)")
                    print(f" {Player2.name} Mikhahad Ba Robot Bazi Konad? (Enter 2)")
                    print(" User Digari Mikhahad Ba Robot Bazi Konad? (Enter 3)   ")
                    _Temp7 = int(input())
                    if _Temp7 == 1:
                        Player2.point = 0
                        DefineUser(4)
                        break
                    elif _Temp7 == 2:
                        Player1.name = Player2.name
                        Player1.point = Player2.point
                        Player2.point = 0
                        Player1.color = Player2.color
                        DefineUser(4)
                        break
                    elif _Temp7 == 3:
                        Player1.point = 0
                        Player2.point = 0
                        DefineUser(2)
                        DefineUser(4)
                        break
                    else:
                        print("invalid data...")
                Player2Roll = 2
                SetOfGameFunc()
                continue


def PrintNoWinner():
    print("*** No Winner. ***")
    print_figlet("End", font="digital")


def PrintWinner():
    if Player1.winner:
        Player1.point += 1
        print(f" *** {Player1.name} Is Winner. ***")
        print(f"Point Of {Player1.name}: {Player1.point}\nPoint Of {Player2.name}: {Player2.point}")
    elif Player2.winner:
        Player2.point += 1
        print(f" *** {Player2.name} Is Winner. ***")
        print(f"Point Of {Player2.name}: {Player2.point}\nPoint Of {Player1.name}: {Player1.point}")


def ResetVariable():
    global CellsFull, ExitVar
    CellsFull = False
    ExitVar = False
    Player1.winner = False
    Player2.winner = False
    User.UnSelectedCell = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    Player1.SelectedCell = []
    Player2.SelectedCell = []


def SetOfGameFunc():
    global SetOfGameInt
    while True:
        SetOfGameInt = int(input("\nChand Set Mikhahi Bazi Koni?   "))
        if 0 < SetOfGameInt:
            break
        else:
            print("invalid data...")


def SetPlayer2():
    global Player2Roll
    while True:
        Player2Roll = int(input("\nBa Ki Mikhahi Bazi koni?\n 1. User Vs User\n 2. User Vs Robot   "))
        if Player2Roll == 1 or Player2Roll == 2:
            if Player2Roll == 2:
                Player2.name = "Robot"
            break
        else:
            print("invalid data...")


def KhasteShodi():
    global Player2Roll
    while True:
        _Temp4 = str(input("Khaste Shodi?\n Yes -> y\n No (RePlay This Game) -> n   "))
        if _Temp4[0] == "y" or _Temp4[0] == "Y":
            while True:
                if Player2Roll == 1:
                    _Temp5 = int(input("Exit Game?\n 1. Exit Play With User (Play With Robot)\n 2. Exit Game   "))
                    if _Temp5 == 1:
                        return True
                    elif _Temp5 == 2:
                        return 3
                    else:
                        print("invalid data...")
                else:
                    _Temp5 = int(input("Exit Game?\n 1. Exit Play With Robot (Play With User)\n 2. Exit Game   "))
                    if _Temp5 == 1:
                        return True
                    elif _Temp5 == 2:
                        return 3
                    else:
                        print("invalid data...")
        elif _Temp4[0] == "n" or _Temp4[0] == "N":
            return False
        else:
            print("invalid data...")


def DefineUser(Code = 1):
    global Player2Roll
    if Code == 1: # Player 1 & 2
        Player1.SetName()
        Player1.SetColor()
        Player2.SetName()
        Player2.SetColor()
    elif Code == 2: # Only player 1
        Player1.SetName()
        Player1.SetColor()
    elif Code == 3: # Only Player 2
        Player2.SetName()
        Player2.SetColor()
    elif Code == 4: # Only Robot
        Player2.name = "Robot"
        Player2.SetColor()


# -----------------------------------------------------------
"""
***   Variable
"""

Player2Roll = 1
CellsFull = False
ExitVar = False
SetOfGameInt = 0

Player1 = User("Player 1")
Player2 = User("Player 2")
Player1.icon = "X"
Player2.icon = "O"

# -----------------------------------------------------------

print("")
print_figlet("Dooz", font="digital")
print("   In the name of God")
print("\nSalam\nBe Bazi Dooz Khosh Amadid.")
while True:
    _Temp1 = str(input("\nAmade ei? (yes -> y)   "))
    if _Temp1[0] == "y" or _Temp1[0] == "Y":
        break
    else:
        print("invalid data...")
SetPlayer2()
if Player2Roll == 1:
    DefineUser(1)
    SetOfGameFunc()
    StartGame()
else:
    DefineUser(2)
    DefineUser(4)
    SetOfGameFunc()
    StartGame()
