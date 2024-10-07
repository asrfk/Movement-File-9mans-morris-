import pygame
from settings import *
from playboard import PlayBoard


class PlayerMovement:
    def __init__(self, play_board, game_type, grid):
        #Initialize the player movement with the play board, game type, and grid layout.
        self.play_board = play_board
        self.game_type = game_type
        self.grid = grid  # This is the grid defining valid piece placements
        self.board_state = [[None for _ in row] for row in self.grid]
        self.cell_height = self.play_board.play_surface.get_height() // len(self.grid)
        self.cell_width = self.play_board.play_surface.get_width() // len(self.grid[0])
        self.current_player = 1  # 1 for Player 1, 2 for Player 2

    def handle_mouse_event(self, event):
        #Handles placing a piece when a mouse event occurs.
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Convert mouse position to board coordinates
            mouse_x, mouse_y = event.pos
            board_x, board_y = self.screen_to_board_coords(mouse_x, mouse_y)

            # Check if the position is valid according to the grid
            if self.is_valid_position(board_y, board_x):
                if self.board_state[board_y][board_x] is None:
                    # Determine the player color based on the current player
                    if self.current_player == 1:
                        player_color = Colors[DEFAULT_PLAYER_1_COLOR].value  # Player 1's color
                    else:
                        player_color = Colors[DEFAULT_PLAYER_2_COLOR].value  # Player 2's color

                    # Pass the player color when drawing the dot
                    self.play_board.draw_player_dot(board_y, board_x, player_color)
                    self.board_state[board_y][board_x] = self.current_player  # Update board state
                    print(f"Player {self.current_player} placed a piece at ({board_x}, {board_y})")

                    # Switch turn
                    self.current_player = 2 if self.current_player == 1 else 1
                else:
                    print("Position already occupied.")
            else:
                print("Invalid position. Cannot place a piece here.")

    def is_valid_position(self, row, col):
        #Check if the board position is valid based on the layout grid."""
        try:
            return self.grid[row][col] == 1  # Only positions with 1 are valid for placement
        except IndexError:
            return False

    def screen_to_board_coords(self, x, y):
        #Convert screen coordinates to board coordinates.
        x -= 300  # Adjust for play surface position
        y -= 100
        board_x = x // self.cell_width
        board_y = y // self.cell_height
        return int(board_x), int(board_y)
