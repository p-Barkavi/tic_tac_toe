import random,copy

def drawBoard(board):
    print(board['t-l'] + '|' +board['t-m'] + '|' +board['t-r'] )
    print('------')
    print(board['m-l'] + '|' +board['m-m'] + '|' +board['m-r'] )
    print('------')
    print(board['l-l'] + '|' +board['l-m'] + '|' +board['l-r'] )

def inputPlayerLetter():
    letter=' '
    while not(letter=='X' or letter=='O'):
        print('Do you want to be X or O')
        letter=input().upper()

    if letter=='X':
        return['X','O']
    else:
        return['O','X']

def whoGoesFirst():
    if random.randint(0,1)==0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    print('Do you want to play again?(yes or no):')
    return input().lower().startswith('y')

def makeMove(board,letter,move):
    board[move]=letter

def isWinner(bo,le):
    return((bo['t-l']==le and bo['t-m']==le and bo['t-r']==le) or
           (bo['m-l']==le and bo['m-m']==le and bo['m-r']==le) or
           (bo['l-l']==le and bo['l-m']==le and bo['l-r']==le) or
           (bo['t-l']==le and bo['m-m']==le and bo['l-r']==le) or
           (bo['t-r']==le and bo['m-m']==le and bo['l-l']==le) or
           (bo['t-l']==le and bo['m-l']==le and bo['l-l']==le) or
           (bo['t-r']==le and bo['m-r']==le and bo['l-r']==le) or
           (bo['t-m']==le and bo['m-m']==le and bo['l-m']==le))

def isSpaceFree(board,move):
    return board[move]==' '

def getPlayerMove(board):
    move=' '
    while move not in 't-l t-m t-r m-l m-m m-r l-l l-m l-r'.split() or not isSpaceFree(board,move):
        print('What is your next move? (t-,m-,l-& L,M,R)')
        move=input()
    return move

def ChooseRandomMoveFromList(board,movesList):
    possibleMoves=[]
    for i in movesList:
        if isSpaceFree(board,i):
            possibleMoves.append(i)

    if len(possibleMoves) !=0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
        
    for i in 't-l t-m t-r m-l m-m m-r l-l l-m l-r'.split():
        dupe = copy.copy(board)
        if isSpaceFree(dupe, i):
            makeMove(dupe, computerLetter, i)
            if isWinner(dupe, computerLetter):
                return i

    for i in 't-l t-m t-r m-l m-m m-r l-l l-m l-r'.split():
        dupe = copy.copy(board)
        if isSpaceFree(dupe, i):
            makeMove(dupe, playerLetter, i)
            if isWinner(dupe, playerLetter):
                return i

    move = ChooseRandomMoveFromList(board, ['t-l', 't-r', 'l-l', 'l-r'])
    if move !=None:
        return move
    
    if isSpaceFree(board, 'm-m'):
        return 'm-m'
    
    return ChooseRandomMoveFromList(board, ['t-m', 'l-m', 'm-l', 'm-r'])
    
def isBoardFull(board):
    for i in 't-l t-m t-r m-l m-m m-r l-l l-m l-r'.split():
        if isSpaceFree(board,i):
            return False
    return True

print('Welcome to tic tac toe')

while True:
    theboard={'t-l':' ','t-m':' ','t-r':' ',
              'm-l':' ','m-m':' ','m-r':' ',
              'l-l':' ','l-m':' ','l-r':' '}
    playerLetter,computerLetter=inputPlayerLetter()
    turn=whoGoesFirst()
    print('The '+turn+' will go first')
    gameIsPlaying=True

    while gameIsPlaying:
        if turn=='player':
            drawBoard(theboard)
            move=getPlayerMove(theboard)
            makeMove(theboard,playerLetter,move)

            if isWinner(theboard,playerLetter):
                drawBoard(theboard)
                print('You won the game !!')
                gameIsPlaying=False
            else:
                if isBoardFull(theboard):
                    drawBoard(theboard)
                    print('The game is a tie')
                    break
                else:
                    turn='computer'
        else:
            move=getComputerMove(theboard,computerLetter)
            makeMove(theboard,computerLetter,move)
            if isWinner(theboard,computerLetter):
                drawBoard(theboard)
                print('The computer has beaten you')
                gameIsPlaying=False
            else:
                if isBoardFull(theboard):
                    drawBoard(theboard)
                    print('The game ended in tie')
                    break
                else:
                    turn='player'
    if not playAgain():
        break
