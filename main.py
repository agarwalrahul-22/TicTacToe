global board
board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
player = "X"

def printBoard(board):
    for line in board:
        print(line)

def makeMove():
    global player
    x = int(input("Player " + player + " Enter the X coordinate? "))
    y = int(input("Player " + player + " Enter the y coordinate?  "))
    
    while board[y][x] != " ":
        print("you must choose an empty spot!")
        x = int(input("Player " + player + ", what is the X coordinate? "))
        y = int(input("Player " + player + " Enter the y coordinate?  "))
        
         
    if player == "X":
        board[y][x] = "X"
        player = "O"
    else:
        board[y][x] = "O"
        player = "X"
        
def isWin():
    if player == "O":
      p="X"
    else:
      p = "O"


    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[x][y] != p:
                win = False
                break
        if win:
            print("Player " + p + " Won the game") 
            return True

    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[y][x] != p:
                win = False
                break
        if win:
            print("Player " + p + " Won the game") 
            return True
            
    win = True
    for y in range(len(board)):
        if board[y][y] != p:
            win = False
            break
    if win:
        print("Player " + p + " Won the game") 
        return True   

    win = True
    for y in range(len(board)):
        if board[y][len(board)-y-1] != p:
            win = False
            break
    if win:
        print("Player " + p + " Won the game") 
        return True

    return False
    
    
def tictac():
    printBoard(board)
    makeMove()
    
def main():
    gamewon = False
    while gamewon == False:
        tictac()
        gamewon = isWin()
    print("GAMEOVER")
    printBoard(board)
    
        
        
        
main()
