
import random


class TicTacToe:

    def __init__(self):

        self.initGame()


    def initGame(self):

        self.gameBoard = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

        self.filledCells = 0


    def showBoard(self):

        res = "\n"


        for i in range(0, 3):

            c1 = self.getCell(i, 0)
            c2 = self.getCell(i, 1)
            c3 = self.getCell(i, 2)

            res = res + "     |     |\n"
            res = res + f"  {c1}  |  {c2}  $  {c3}\n"
            res = res + "     |     |\n"
            if i != 2:
                res = res + "-----------------\n"

            # res = f'''     |     |
            #          {c1} |  {c2}  |  {c3}
            #               |     |
            # '''
            # if i != 2:
            #     res = res + "-----------------\n"

        print(res)


    def isOccupied(self, cellNumber):

        r = cellNumber // 3
        c = cellNumber % 3

        if self.getCell(r, c) != ' ':
            return True
        else:
            return False


    def setCellValue(self, r, c, letter):

        self.gameBoard[r][c] = letter


    def getCell(self, r, c):

        return self.gameBoard[r][c]


    def checkWinner(self):

        for n in range(0, 3):

            if (self.getCell(n, 0) == self.getCell(n, 1) \
                and self.getCell(n, 0) == self.getCell(n, 2)) == True:

                return self.getCell(n, 0)

            if (self.getCell(0, n) == self.getCell(1, n) \
                and self.getCell(0, n) == self.getCell(2, n)) == True:

                return self.getCell(0, n)

        if (self.getCell(1, 1) == self.getCell(0, 0) \
            and self.getCell(1, 1) == self.getCell(2, 2)) == True:

            return self.getCell(1, 1)

        if (self.getCell(1, 1) == self.getCell(0, 2) \
           and self.getCell(1, 1) == self.getCell(2, 0)) == True:

           return self.getCell(1, 1)

        return ' '


    def start(self):

        while True:

            valueOK = False

            while valueOK != True:

                print("Enter your move (1..9):")
                userMove = int(input())

                if userMove < 1 or userMove > 9:

                    print("Invalid input!")
                    continue

                if self.isOccupied(userMove - 1) == True:

                    print("Occupied cell! Try again!")
                else:

                    valueOK = True

            r = (userMove - 1) // 3
            c = (userMove - 1) % 3

            self.setCellValue(r, c, 'X')
            self.filledCells += 1

            if self.checkWinner() == 'X':

                self.showBoard()
                print("You won!!")
                break

            if self.filledCells == 9:

                self.showBoard()
                print("No winner :-(")
                break


            valueOK = False

            while valueOK != True:

                computerMove = random.randint(0, 8)

                if self.isOccupied(computerMove) == False:
                    valueOK = True

            rc = computerMove // 3
            cc = computerMove % 3

            self.setCellValue(rc, cc, 'O')

            self.filledCells += 1
            self.showBoard()

            if self.checkWinner() == 'O':

                print("Computer won!!")
                break


nextGame = 'y'

while nextGame == 'y':

    game = TicTacToe()
    game.showBoard()
    game.start()


    print("Play next game? (y/n)")
    nextGame = input()

