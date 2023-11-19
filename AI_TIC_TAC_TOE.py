
def printBoard(State):
    print("   C0  C1  C2 ")
    print("R0 ", State[0][0], "|", State[0][1], "|", State[0][2])
    print("   ---|---|---")
    print("R1 ", State[1][0], "|", State[1][1], "|", State[1][2])
    print("   ---|---|---")
    print("R2 ", State[2][0], "|", State[2][1], "|", State[2][2])
    
def choice():
    global ai
    global human
    choice=input('ENTER WHAT YOU WANT X or O').upper()
    if choice=='X':
        human='X'
        ai='O'
    elif choice=='O':
        human='O'
        ai='X'
    else:
        print('INVALID PLEASE SELECT X OR O')
        choice()
        
def Playerturn(State):
    noX = 0
    noY = 0
    for i in range(3):
        for j in range(3):
            if State[i][j] == ' ':
                continue
            elif State[i][j] == 'X':
                noX += 1
            elif State[i][j] == 'O':
                noY += 1
    if noX == noY:
        return 'X'
    else:
        return 'O'
    
    
def Inputval(State,pos):
    [i,j]= pos
    State[i][j]=Playerturn(State)
    
def AvMoves(State):
    moves = set()
    for i in range(3):
        for j in range(3):
            if State[i][j] == ' ':
                moves.add((i, j))
    return moves

def isMovesleft(State):
    for i in range(3):
        for j in range(3):
            if State[i][j] == ' ':
                return True
    return False
def Score(State):
    ##checking Rows for win
    for row in range(3):
        if State[row][0]==State[row][1] and State[row][1]==State[row][2]:
            if State[row][0]==ai:
                return 10
            elif State[row][0]==human:
                return -10
    ##checking col for win
    for col in range(3):
        if State[0][col]==State[1][col] and State[1][col]==State[2][col]:
            if State[0][col]==ai:
                return 10
            elif State[0][col]==human:
                return -10
    ## checking diagonals
    if (State[0][0]==State[1][1] and State[1][1]==State[2][2]) or (State[0][2]==State[1][1] and State[1][1]==State[2][0]):
        if State[1][1]==ai:
            return 10
        elif State[1][1]==human:
            return -10
        
    return 0
def Game_Over(State):
    if isMovesleft(State) and Score(State)==0:
        return False
    else:
        return True

def ai_move(State):
    print("AI's move :")
    best=bestMove(State)
    Inputval(State,best)
    printBoard(State)

def human_move(State):
    row, col = map(int, input("Enter your move (row col): ").split())
    if (row, col) in AvMoves(State):
        Inputval(State,(row,col))
        printBoard(State)
    else:
        print("Invalid move. The cell is already occupied. Try again.")    

def minimax(board,depth,ismax):
    score = Score(board)
    if (score == 10) :  
        return score - depth
    if (score == -10) : 
        return score + depth
    if (isMovesleft(board) == False) : 
        return 0
    if (ismax) :      
        best = -1000   
        for i in range(3) :          
            for j in range(3) : 
                if (board[i][j]==' ') :
                    board[i][j] = ai
                    best = max( best, minimax(board,depth + 1,not ismax) )
                    board[i][j] = ' '
        return best 
    else : 
        best = 1000 
        for i in range(3) :          
            for j in range(3) : 
                if (board[i][j] == ' ') : 
                    board[i][j] = human
                    best = min(best, minimax(board, depth + 1, not ismax))
                    board[i][j] = ' '
        return best

def bestMove(State):
    bestscore=-1000
    bestmove=(-1,-1)
    for i in range(3) :      
        for j in range(3) : 
          if (State[i][j] == ' ') :
            State[i][j] = ai
            currentscore= minimax(State,0,False)
            State[i][j] = ' '
            if currentscore>bestscore:
                bestmove=(i,j)
                bestscore=currentscore
    print('the best move is',bestmove)
    return bestmove

def Start_Game(State):
    if human=='X':
        human_move(State)
        if Game_Over(State)==False :
            ai_move(State)
    else:
        ai_move(State)
        if Game_Over(State)==False :    
            human_move(State)

        

def main():
    board =[[' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' ']]
    board1=[['X','O',' '],
            [' ','X','O'],
            [' ',' ',' ']]
    board2=[['X','O','X'],
            ['O','X','O'],
            ['O','X','O']]
    print('Welcome to TIC-TAC-TOE')
    printBoard(board)
    choice()
    print(' ai =',ai)
    print(' you =',human)
    while Game_Over(board)==False :
        Start_Game(board)
    if Score(board)==0:
        print('Its a TIE')
    elif Score(board)>0:
        print('Ai Won')
    elif Score(board)<0:
        print('You Won')
          
main()