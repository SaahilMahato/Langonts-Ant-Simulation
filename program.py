import numpy as np
import pygame


class LangtonsAnt:
    def __init__(self, width, height, cell_size, grid=None):
        pygame.init()

        # define the board's properties
        self.board_size = (self.width, self.height) = (width, height)
        self.black_cell_color = (0, 0, 0)
        self.white_cell_color = (255, 255, 255)
        self.cell_size = cell_size
        self.rows = self.height // self.cell_size
        self.columns = self.width // self.cell_size
        self.grid_size = (self.columns, self.rows)
        self.grid = grid
        self.initialize_grid()
        self.screen = pygame.display.set_mode(self.board_size)
        self.steps = 0
        pygame.display.set_caption(f"Generation: {self.steps}")

        # define the ant's properties
        self.ant_position = self.create_ant()   # choose an arbitrary position as ant
        self.UP = 0
        self.RIGHT = 1
        self.DOWN = 2
        self.LEFT = 3
        self.DIR = self.UP

        #
        pygame.display.flip()

    # initialize grid into random values of 0 and 1 if the user provided no input
    def initialize_grid(self):
        if not self.grid:
            self.grid = np.zeros(self.grid_size)

    # function to choose a random cell as ant
    def create_ant(self):
        ant_position = np.random.randint(0, [self.columns-1, self.rows-1])
        self.grid[ant_position[0]][ant_position[1]] = 1
        print("Ant's initial position:", ant_position)
        return ant_position

    # define define ant's moves
    def turn_right(self):
        self.DIR += 1
        if self.DIR > self.LEFT:
            self.DIR = self.UP

    def turn_left(self):
        self.DIR -= 1
        if self.DIR < self.UP:
            self.DIR = self.LEFT

    def move_forward(self):
        if self.DIR == self.UP:
            self.ant_position[1] -= 1
        elif self.DIR == self.RIGHT:
            self.ant_position[0] += 1
        elif self.DIR == self.DOWN:
            self.ant_position[1] += 1
        elif self.DIR == self.LEFT:
            self.ant_position[0] -= 1
        if self.ant_position[0] > self.columns-1:
            self.ant_position[0] = 0
        elif self.ant_position[0] < 0:
            self.ant_position[0] = self.columns-1
        if self.ant_position[1] > self.rows-1:
            self.ant_position[1] = 0
        elif self.ant_position[1] < 0:
            self.ant_position[1] = self.rows-1

    def move_ant(self):
        cell_state = self.grid[self.ant_position[0]][self.ant_position[1]]
        if cell_state == 0:
            self.turn_right()
            self.grid[self.ant_position[0]][self.ant_position[1]] = 1
            self.move_forward()
        elif cell_state == 1:
            self.turn_left()
            self.grid[self.ant_position[0]][self.ant_position[1]] = 0
            self.move_forward()
        print("Ant's position:", self.ant_position)
        self.steps += 1
        pygame.display.set_caption(f"Steps: {self.steps}")

    def draw_grid(self):
        for i in range(self.columns):
            for j in range(self.rows):
                if self.grid[i][j] == 1:
                    pygame.draw.rect(self.screen, self.white_cell_color,
                                     (i * self.cell_size, j * self.cell_size,
                                      self.cell_size - 1, self.cell_size - 1))
                elif self.grid[i][j] == 0:
                    pygame.draw.rect(self.screen, self.black_cell_color,
                                     (i * self.cell_size, j * self.cell_size,
                                      self.cell_size - 1, self.cell_size - 1))
        pygame.display.flip()

    def run(self):
        paused = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_p:
                        paused = not paused
            if not paused:
                self.draw_grid()
                self.move_ant()


if __name__ == '__main__':
    LangtonsAnt(500, 500, 5).run()

