class Game():
    def __init__ (self, 
                  turn = "X", 
                  tie = False, 
                  winner = None, 
                  board = {
                        'a1': None, 'b1': None, 'c1': None,
                        'a2': None, 'b2': None, 'c2': None,
                        'a3': None, 'b3': None, 'c3': None,
                        }
                  ):
        self.turn =  turn
        self.winner = winner
        self.tie = tie
        self.board = board

    def play_game (self):
        print( "Welcome to Tic Tac Toe")
        while (self.winner == None) and (not self.tie):
            self.render()
            self.get_move()
            self.check_winner()
            self.check_tie()
            self.switch_turns()
        self.render()



    
    def print_board(self) -> str:
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)
    

    def print_message(self) -> str:
        if self.tie:
            return print("Tie game")
        elif self.winner: 
            return print(f"{self.winner} wins the game!")
        else:
            return print(f"It's player {self.turn}'s turn!")
        
    def render(self):
        self.print_board()
        self.print_message()

    def switch_turns(self):
        self.turn = "Y" if self.turn == "X" else "X"

    def get_move(self) -> str:
        while True:
            move = input(f"Enter a valid move (example: A1): ").lower()
            if (move not in self.board) or (self.board[move] != None) :
                 print("Enter a valid move")
            else:
                self.board[move] = self.turn
                break


    def check_winner(self):
        winning_combinations = [
            ('a1', 'a2', 'a3'),  # Row 1
            ('b1', 'b2', 'b3'),  # Row 2
            ('c1', 'c2', 'c3'),  # Row 3
            ('a1', 'b1', 'c1'),  # Column 1
            ('a2', 'b2', 'c2'),  # Column 2
            ('a3', 'b3', 'c3'),  # Column 3
            ('a1', 'b2', 'c3'),  # Diagonal 1
            ('a3', 'b2', 'c1')   # Diagonal 2
        ]

        for combo in winning_combinations:
            if self.board[combo[0]] and (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]):
                self.winner = self.turn
                return  # Exit the function as we found a winner


    def check_tie(self):
        all_filled = False

        for tile in self.board:
            if tile == None:  
                all_filled = False
                break 

        if all_filled and self.winner == None:
            self.tie = True


    


    
        
game_instance = Game()
game_instance.play_game()

