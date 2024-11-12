class Board:
     
    def __init__(self):
        
        self.board = [" "," "," "],[" "," "," "],[" "," "," "]

    def show_board(self):

        for line in self.board:
            print(line)

    def check_box(self, row, column, player):

        if player == 1:
            self.board[row-1][column-1] = "X"
        if player == 2:
            self.board[row-1][column-1] = "O"

    def check_winner(self):
        spaces = 0

        for x in range(len(self.board)):
            check = 0
            across = 0
            if self.board[x] == ["X","X","X"] or self.board[x] == ["O","O","O"]:
                print("Winner!")
                board.show_board()
                return False
            for y in range(len(self.board)):
                if self.board[y][y] == "O":
                    across += 1
                    print(across)
                    if across == 3:
                        print("Winner!")
                        board.show_board()
                        return False
                elif self.board[y][y] == "X":
                    across -= 1
                    print(across)
                    if across == -3:
                        print("Winner!")
                        board.show_board()
                        return False
                if self.board[y][x] == "O":
                    check += 1
                    spaces += 1
                    if check == 3:
                        print("Winner!")
                        board.show_board()
                        return False
                    elif spaces == 9:
                        print("Tie!")
                        board.show_board()
                        return False
                elif self.board[y][x] == "X":
                    check -= 1
                    spaces += 1
                    if check == -3:
                        print("Winner!")
                        board.show_board()
                        return False
                    elif spaces == 9:
                        print("Tie!")
                        board.show_board()
                        return False
                if self.board[0][2] == "X" and self.board[1][1] == "X" and self.board[2][0] == "X":
                    print("Winner")
                    return False
                elif self.board[0][2] == "O" and self.board[1][1] == "O" and self.board[2][0] == "O":
                    print("Winner")
                    return False
        return True
            

            
            

class Player:

    def get_move(self, player):
        possible_ans = [1,2,3]
        not_valid = True

        while not_valid:
            player_row = input("Which row would you like to play? (1/2/3)")

            try:
                if int(player_row) in possible_ans:
                    player_col = input("While column would you like to play? (1/2/3)")
                    if int(player_col) in possible_ans:
                        if board.board[int(player_row)-1][int(player_col)-1] == " ":
                            board.check_box(int(player_row),int(player_col),player)
                            break
                        else:
                            print("Already Taken!")
                    else:
                        print("Please put a valid input")
                else:
                    print("Please put a valid input")
            except ValueError:
                print("Please put a valid input")


board = Board()
player = Player()
playing = True
turn = 1

while playing:
    board.show_board()
    if turn == 1:
        player.get_move(1)
        playing = board.check_winner()
        turn += 1
    elif turn == 2:
        player.get_move(2)
        playing = board.check_winner()
        turn -= 1
    

    

    

