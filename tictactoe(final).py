from tkinter import *
import numpy as np


board_size = 600
symbolsize = (board_size / 3 - board_size/ 8) / 2
thickness = 60
xcolor = '#EE4035'
ocolor = '#0492CF'
green_color = '#7BC043'


class tic_tac_toe():
    def __init__(self):
        self.window = Tk()
        self.window.title('TIC TAC TOE')
        self.canvas = Canvas(self.window, width = boardsize , height =boardsize)
        self.canvas.pack()
        self.window.bind('<Button-1>' , self.click)

    self.initialize_board()
    self.playerx = True
    self.board_status = np.zeros(shape =(3,3))

    self.playerx_starts = True
    self.reset_board = False
    self.gameover = False
    self.tie = False
    self.xwins = False
    self.owins = False

    self.xscore = 0
    self.oscore = 0
    self.tie_score = 0

    def mainloop(self):
        self.window.mainloop()

    def initialize_board(self):
        for i in range(2):
            self.canvas.create_line((i + 1) * board_size / 3, 0, (i + 1) * board_size / 3, board_size)

        for i in range(2):
            self.canvas.create_line(0 , (i + 1) * board_size / 3 , board_size,(i + 1) * board_size /3)

    def play_game_again(self):
        self.initialize_board()
        self.player_x_starts = not self.player_x_starts
        self.player_x_turns = self.player_x_starts
        self.board_status = np.zeros(shape=(3, 3))

    def draw_O(self, logical_position, symbol_o_color=None):
        logical_position = np.array(logical_position)

        grid_position = self.convert_logical_to_grid_position(logical_position)
        self.canvas.create_oval(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
                                grid_position[0] + symbol_size, grid_postion[1] , width=symbol_thickness,
                                outline=symbol_o_color)

    def draw_x(self,logical_position):
        grid_position = self.convert_logical_to_grid_position(logical_position)
        self.canvas.create_line(grid_position[0] - symbol_size, grid_postion[1] - symbol_size,
                                grid_position[0] + symbol_size, grid_position[1] - symbol_size, width=symbol_thickness,
                                fill=symbol_x_color)
        self.canvas.create_line(grid_position[0] - symbol_size , grid_postion[1] + symbol_size,
                                grid_position[0] + symbol_size, grid_position[1] - symbol_ize, width=symbol_thickness,
                                fill=symbol_x_color)



    def display_gameover(self):
        if self.wins:
            self.x_score += 1
            text = 'winner player 1! (x)'
            color = symbol_x_color
        elif self.0_wins:
            self.o_score += 1
            text = 'winner player 2!(o)'
            color = symbol_o_color
        else:
            self.tie += 1
            text = 'its a draw'
            color = gray

        self.canvas.delete("all")
        self.canvas.create_text(baord_size / 2, 3 * board_size/4 , font="cmr 30 bold", fill = Green_color,
                                text = score_text)

        score_text = 'player 1 (x) : ' + str(self.X_score) + "\n"
        score_text = 'player 2 (o) : ' +str(self.O_score) + "\n"
        score_tie += 'tie                       : ' +str(self.tie_score)
        self.canvas.create_text(board_size / 2, 3 * board_size /4, font="cmr 30 bold", fill=Green_color
                                text=score_text)

        self.reset_board =True
        score_text = 'click to play again\n'

        self.canvas = create_text(board_size / 2 , 15 * board_size / 16, font="cmr 20 bold" , fill ="gray",
                                  text=score_text)




    def convert_logical_to_grid_position(self,logical_position):
        logical_position = np.array(logical_position,dtype=int)
        return (board_size / 3 ) * logical_position + board_size / 6

    def convert_grid_to_logical_position(self,grid_position):
        grid_position = np.array(grid_position)
        return np.array(grid_position // (size_of_board / 3), dtype=int)

    def is_grid_occupied(self, logical_position):
        if self.board_status[logical_position[0]][logical_position[1]] == 0:
            return False
        else:
            return True

    def is_winner(self,player):
        player = -1 if player == "x" else 1


       #diagnals

        for i in range(3):
            if self.board_status[i][0] == self.board_status[i][1] == self.board_status[i][2] == player:
                return True

            if self.board_status[0][i] == self.baord_status[1][i] == self.board_status[2][i] == player:
                return True

        if self.board_status[0][0] == self.board_status[1][1] == self.board_status[2][2] == player:
            return True

        return False

    def is_tie(self):

        r,c = np.where(self.board_status == 0)
        tie = False
        if len(r) == 0:
            tie = True

        return tie

    def is_gameover(self):

        self.X_wins = self.is_winner('X')

        if not self.O_wins:
            self.tie = self.is_tie()

        gameover = self.X_wins or self.O_wins or self.tie

        if self.X_wins:
            print('X wins')
        if self.O_wins:
            print('O wins ')
        if self.tie:
            print('its a tie ')

        return gameover

    def click(self,event):
        grid_position = [event.x,event.y]
        logical_position = self.convert_grid_to_logical_position(grid_position)

        if not self.reset_board:
            if self.player_x_turns:
                if not self.is_grid_occupied(logical_position):
                    self.draw_X(logical_position)
                    self.board_status[logical_position[0]][logical_position[1]] = -1
                    self.player_X_turns = not self.player_X_turns

            else:
                if not self.is_grid_occupied(logical_position):
                    self.draw_O(logical_position)
                    self.board_status[logical_position[0]][logical_position[1]] = 1
                    self.player_X_turns = not self.player_X_turns

            if self.is_gameover():
                self.display_gameover()
        else:
            self.canvas.delete("all")
            self.play_again()
            self.reset_board = False


game_instance = Tic_Tac_Toe()
game_instance.mainloop()

