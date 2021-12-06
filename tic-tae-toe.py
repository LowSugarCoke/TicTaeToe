# 1. Create a board using a 2-dimensional array and initialize each element as empty.
#    You can represent empty using any symbol you like. Here, we are going to use a hyphen. '-'.
# 2. Write a function to check whether the board is filled or not.
#    Iterate over the board and return false if the board contains an empty sign or else return true.
# 3. Write a function to check whether a player has won or not.
#    We have to check all the possibilities that we discussed in the previous section.
#    Check for all the rows, columns, and two diagonals.
# 4. Write a function to show the board as we will show the board multiple times to the users while they are playing.
# 5. Write a function to start the game.
#    5.a Select the first turn of the player randomly.
#    5.b Write an infinite loop that breaks when the game is over (either win or draw).
#        Show the board to the user to select the spot for the next move.
#        Ask the user to enter the row and column number.
#        Update the spot with the respective player sign.
#        Check whether the current player won the game or not.
#        If the current player won the game, then print a winning message and break the infinite loop.
#        Next, check whether the board is filled or not.
#        If the board is filled, then print the draw message and break the infinite loop.
#    5.c Finally, show the user the final view of the board.

class TicTaeToe:
    def __init__(self):
        self.board=[];
        return;
    
    def CreateBoard(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row);
                
    def DrawBoard(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()
    
    def IsGameEnd(self,row,col, player):        
        if self.board[row][0] == self.board[row][1] == self.board[row][2] == player:
            return True
        elif self.board[0][col] == self.board[1][col] == self.board[2][col] == player:
            return True
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        elif self.board[2][0] == self.board[1][1] == self.board[0][2] == player:
            return True;
        else:
            return False;
    
    def UserInput(self):
        try:
            row,col = list(map(int,(input("Enter row and column numbers to fix spot: ").split())))
            return row,col
        except ValueError:
            print("Type error, try again")
            return self.UserInput()
        
    def FixOnSpot(self,row,col,player):
        
        while(row>2 or row<0 or col >2 or col<0):
            row,col = list(map(int,(input("Out of range, Please enter again: ").split()))) 
        
        while(self.board[row][col]!="-"):
            row,col = list(map(int,(input("Repeat, Please enter again: ").split())))
            
        
        self.board[row][col] = player
            
        
    def StartGame(self):
        
        self.CreateBoard();
        self.DrawBoard();
        time =0
        while True:
            print("Player 1(O) turn")
            row, col = self.UserInput()
            self.FixOnSpot(row,col,"O")
            self.DrawBoard();
            
            if(self.IsGameEnd(row,col, "O")):
                print("Player %s win" % "O")
                break
            
            time+=2 
            
            if time >=9:
                print("Tie game")
                break     
        
            print("Player 2(X) turn")
            row_2, col_2 = self.UserInput()             
            self.FixOnSpot(row_2,col_2,"X")
            self.DrawBoard();
            
            if(self.IsGameEnd(row,col, "X")):
                print("Player %s win" % "X")
                break
            
            
           
       
       
if __name__ == '__main__':
    play_game =TicTaeToe()
    play_game.StartGame();




