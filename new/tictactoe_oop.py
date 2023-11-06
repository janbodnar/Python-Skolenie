
import random

class TicTacToe:
    
    def __init__( self ):
        self.gameBoard = [
            [" "," "," "],
            [" "," "," "],
            [" "," "," "]
        ]

    def __str__( self ):
        res = "\n"
        for i in range( 0, 3 ):
            res = res + "     |     |\n"
            res = res + f"  {self.gameBoard[i][0]}  |  {self.gameBoard[i][1]}  |  {self.gameBoard[i][2]}\n"
            res = res + "     |     |\n"
            if i != 2:
                res = res + "-----------------\n"
        return res

    def occupiedCell( self, cellNumber ):
        if self.gameBoard [int(cellNumber / 3)] [int(cellNumber % 3)] != " ":
            return True
        else:
            return False
    
    def setValueInCell( self, i, j, letter ):
        self.gameBoard [i][j] = letter

    def checkWinner( self ):
        for n in range( 0, 3 ):
            if (self.gameBoard[n][0] == self.gameBoard[n][1] and self.gameBoard[n][0] == self.gameBoard[n][2]) == True:
                return self.gameBoard[n][0]
            if (self.gameBoard[0][n] == self.gameBoard[1][n] and self.gameBoard[0][n] == self.gameBoard[2][n]) == True:
                return self.gameBoard[0][n]
        if (self.gameBoard[1][1] == self.gameBoard[0][0] and self.gameBoard[1][1] == self.gameBoard[2][2]) == True:
            return self.gameBoard[1][1]
        if (self.gameBoard[1][1] == self.gameBoard[0][2] and self.gameBoard[1][1] == self.gameBoard[2][0]) == True:
            return self.gameBoard[1][1]
        return ' '

nextGame = 'y'
while nextGame == 'y':

    game = TicTacToe()
    print( game )
    
    filledCells = 0
    while True:
        valueOK = False
        while valueOK != True:
            print( "Enter your move (1..9):" )
            usersMove = input()
            if usersMove < '1' or  usersMove > '9':
                print( "Invalid input!" )
                continue
            else:
                usersMove = int( usersMove )
            if game.occupiedCell( usersMove - 1 ) == True:
                print("Occupied cell! Try again!")
            else:
                valueOK = True
        game.setValueInCell( int((usersMove - 1) / 3), int((usersMove - 1) % 3), 'X' )
        filledCells += 1
        if game.checkWinner() == 'X':
            print( game )
            print( "You won!!" )
            break
        if filledCells == 9:
            print( game )
            print( "No winner :-(" )
            break
        valueOK = False
        while valueOK != True:
            computersMove = random.randint(0, 8)
            if game.occupiedCell( computersMove ) == False:              
                valueOK = True
        game.setValueInCell( int(computersMove / 3), int(computersMove % 3), 'O' )
        filledCells += 1
        print( game )
        if game.checkWinner() == 'O':
            print( "Computer won!!" )
            break
    print("Play next game? (y/n)")
    nextGame = input()
