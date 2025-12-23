GAME = [["_"] * 3 for _ in range(3)]

def place(x: int, y: int, turn: str):
    global GAME
    if(x >= 0 and x < 3 and y >= 0 and y < 3 and GAME[x][y] == "_"):
        GAME[x][y] = turn
        print(f"{turn} placed at position ({x}, {y})")
    else:
        print("Enter valid position")
   

def next(turn: str) -> str:
    return "O" if turn == "X" else "X"

def check_win(turn: str) -> bool:
    global GAME
    flag = False

    # check rows
    for i in range(3):
        row = GAME[i]
        # print("row: ", row)
        if(row == [turn] * 3):
            flag = True
            break
   
    # check cols
    for i in range(3):
        col = [GAME[i][0] for i in range(3)]
        # print("col: ", col)
        if(col == [turn] * 3):
            flag = True
            break
   
    # check diag1
    if(flag != True and [GAME[0][0], GAME[1][1], GAME[2][2]] == [turn] * 3):
        flag = True
       
       
    # check diag2
    if(flag != True and [GAME[0][2], GAME[1][1], GAME[2][0]] == [turn] * 3):
        flag = True

    return flag

def check_fill() -> bool:
    global GAME
    for i in range(3):
        for j in range(3):
            if(GAME[i][j] == "_"):
                return False
    return True

def main():
    TURN = "X"
    global GAME
    print(GAME)
    while not check_win(TURN) and not check_fill():
        print(f"Player {TURN}'s turn: ")
        x, y = map(int, input("Enter position: ").split())
       
        if(x == -1 and y == -1):
            print("Game Ended")
            break
       
        place(x, y, TURN)
        print(GAME)
       
        if(check_win(TURN)):
            print(f"Winner is player {TURN}")
            break

        TURN = next(TURN)

main()
