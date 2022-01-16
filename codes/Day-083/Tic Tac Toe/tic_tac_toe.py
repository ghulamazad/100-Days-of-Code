class TicTacToe:
    board = {
        '7': ' ', '8': ' ', '9': ' ',
        '4': ' ', '5': ' ', '6': ' ',
        '1': ' ', '2': ' ', '3': ' '
    }

    board_keys = [key for key in board]

    def printBoard(self):
        """
            Print Board
        """
        print(self.board['7'] + '|' + self.board['8'] + '|' + self.board['9'])
        print('-+-+-')
        print(self.board['4'] + '|' + self.board['5'] + '|' + self.board['6'])
        print('-+-+-')
        print(self.board['1'] + '|' + self.board['2'] + '|' + self.board['3'])

    def check_winner(self, count, turn):
        """
            Now we will check if player X or O has won.
        """
        if count >= 5:
            if self.board['7'] == self.board['8'] == self.board['9'] != ' ':  # across the top
                self.printBoard()
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                return True
            elif self.board['4'] == self.board['5'] == self.board['6'] != ' ':  # across the middle
                self.printBoard()
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                return True
            elif self.board['1'] == self.board['2'] == self.board['3'] != ' ':  # across the bottom
                self.printBoard()
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                return True
            # down the left side
            elif self.board['1'] == self.board['4'] == self.board['7'] != ' ':
                self.printBoard()
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                return True
            elif self.board['2'] == self.board['5'] == self.board['8'] != ' ':  # down the middle
                self.printBoard()
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                return True
            # down the right side
            elif self.board['3'] == self.board['6'] == self.board['9'] != ' ':
                self.printBoard()
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                return True
            elif self.board['7'] == self.board['5'] == self.board['3'] != ' ':  # diagonal
                self.printBoard()
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                return True
            elif self.board['1'] == self.board['5'] == self.board['9'] != ' ':  # diagonal
                self.printBoard()
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                return True

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        return False

    def change_player(self, turn):
        """
          Now we have to change the player after every move.
        """

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

        return turn

    def restart(self):
        """
            Restart the game or not.
        """
        restart = input("Do want to play Again?(y/n)")
        if restart in ['y', 'Y']:
            for key in self.board_keys:
                self.board[key] = " "

            return False
        else:
            return True

    def start_game(self):
        """
            Start Game
        """

        isExit = False
        while not isExit:
            count = 0
            turn = 'X'
            for _ in range(10):
                self.printBoard()
                print("It's your turn," + turn + ".Move to which place?")

                move = input()

                if self.board[move] == ' ':
                    self.board[move] = turn
                    count += 1
                else:
                    print("That place is already filled.\nMove to which place?")
                    continue

                if self.check_winner(count, turn):
                    break
                else:
                    turn = self.change_player(turn)

            isExit = self.restart()
