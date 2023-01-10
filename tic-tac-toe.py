import random

position = ["1,1", "1,2", "1,3", "2,1", "2,2", "2,3", "3,1", "3,2", "3,3"]
a = "."
count = 0
GAME_ON = True
row_1 = [a, a, a]
row_2 = [a, a, a]
row_3 = [a, a, a]
print("     "+ " 1   " + " 2   "+ " 3")
print("1 = " + str(row_1))
print("2 = " + str(row_2))
print("3 = " + str(row_3))

print("How to play!")
print("Enter the value of rows and columns so that you can occupy that position with 'X'.")
print("The entered value of row and columns can only be 1 or 2 or 3.")
print("You should enter the value of row and columns as => 1,3 or 2,1 .")
print("Make sure you type the comma between numbers")
print("Where the first value is for row and second value is for column.")
print("Ex => If you type 3,3 then you occupy the position which is at third row and third column.\n")

def score_check_user():
    if (row_1[0] + row_1[1]+row_1[2]) == "XXX":
        print("You win")
        return GAME_ON == False
    elif (row_1[0] + row_2[0]+row_3[0]) == "XXX":
        print("You win")
        return GAME_ON == False
    elif (row_3[0] + row_3[1]+row_3[2]) == "XXX":
        print("You win")
        return GAME_ON == False
    elif (row_1[2] + row_2[2]+row_3[2]) == "XXX":
        print("You win")
        return GAME_ON == False
    elif (row_1[0] + row_2[1] + row_3[2]) == "XXX":
        print("You win")
        return GAME_ON == False
    elif (row_1[2] + row_2[1] + row_3[0]) == "XXX":
        print("You win")
        return GAME_ON == False
    elif (row_1[1] + row_2[1] + row_3[1]) == "OOO":
        print("You win")
        return GAME_ON == False
    elif (row_2[0] + row_2[1] + row_2[2]) == "OOO":
        print("You win")
        return GAME_ON == False
    else:
        if len(position) == 1:
            return GAME_ON == False

def score_check_comp():
    if (row_1[0] + row_1[1]+row_1[2]) == "OOO":
        print("Computer wins!")
        return GAME_ON == False
    elif (row_1[0] + row_2[0]+row_3[0]) == "OOO":
        print("Computer wins!")
        return GAME_ON == False
    elif (row_3[0] + row_3[1]+row_3[2]) == "OOO":
        print("Computer wins!")
        return GAME_ON == False
    elif (row_1[2] + row_2[2]+row_3[2]) == "OOO":
        print("Computer wins!")
        return GAME_ON == False
    elif (row_1[1] + row_2[1] + row_3[1]) == "OOO":
        print("Computer wins!")
        return GAME_ON == False
    elif (row_2[0] + row_2[1] + row_2[2]) == "OOO":
        print("Computer wins!")
        return GAME_ON == False
    elif (row_1[0] + row_2[1] + row_3[2]) == "OOO":
        print("Computer wins!")
        return GAME_ON == False
    elif (row_1[2] + row_2[1] + row_3[0]) == "OOO":
        print("Computer wins!")
        return GAME_ON == False
    else:
        if len(position) == 1:
            return GAME_ON == False


while GAME_ON:
    pos = input("Enter the number of row and column: ")
    q1 = pos.split(",")
    r1 = int(q1[0])
    c1 = int(q1[1]) - 1
    count += 1
    position.remove(pos)

    if (r1 <4 or c1 <4):
        if r1 == 1:
            row_1[c1] = "X"
        elif r1 == 2:
            row_2[c1] = "X"
        elif r1 == 3:
            row_3[c1] = "X"
        else:
            pass
        print(row_1)
        print(row_2)
        print(row_3)
        if count > 4:
            ON = score_check_user()
            if ON == False:
                break
    else:
        print("Invalid input.")

    com_pos = random.choice(position)
    q2 = com_pos.split(",")
    r2 = int(q2[0])
    c2 = int(q2[1]) - 1
    count += 1
    print("Computer occupies position :" + str(r2) + "," + str(c2))
    position.remove(com_pos)
    print("comp count" + str(count))

    if r2 == 1:
        row_1[c2] = "O"
    elif r2 == 2:
        row_2[c2] = "O"
    elif r2 == 3:
        row_3[c2] = "O"
    else:
        pass
    print(row_1)
    print(row_2)
    print(row_3)
    if count >5:
        ON = score_check_comp()
        if ON == False:
            break
