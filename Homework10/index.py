"""
Student portion of Zombie Apocalypse mini-project
"""
import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list=None,
                 zombie_list=None, human_list=None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list is not None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list is not None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list is not None:
            self._human_list = list(human_list)
        else:
            self._human_list = []

    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._zombie_list = []
        self._human_list = []

    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))

    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)

    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        # replace with an actual generator
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))

    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)

    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        # replace with an actual generator
        for human in self._human_list:
            yield human

    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        height = self.get_grid_height()
        width = self.get_grid_width()
        visited = poc_grid.Grid(height, width)
        distance_field = [[height * width for _col in range(width)] for _row in range(height)]

        boundary = poc_queue.Queue()

        if entity_type == ZOMBIE:
            for zombie in self.zombies():
                boundary.enqueue(zombie)
                visited.set_full(*zombie)
                distance_field[zombie[0]][zombie[1]] = 0
        elif entity_type == HUMAN:
            for human in self.humans():
                boundary.enqueue(human)
                visited.set_full(*human)
                distance_field[human[0]][human[1]] = 0

        while boundary.__len__() > 0:
            current_cell = boundary.dequeue()
            neighbor_cell = self.four_neighbors(current_cell[0], current_cell[1])

            for neighbor in neighbor_cell:
                if visited.is_empty(neighbor[0], neighbor[1]) and self.is_empty(neighbor[0], neighbor[1]):
                    visited.set_full(neighbor[0], neighbor[1])
                    boundary.enqueue(neighbor)
                    distance_field[neighbor[0]][neighbor[1]] = distance_field[current_cell[0]][current_cell[1]] + 1

        return distance_field

    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        for human in self.humans():
            rate = zombie_distance_field[human[0]][human[1]]
            best_step = [human]
            neighbors = self.eight_neighbors(*human)

            for cell in neighbors:
                if zombie_distance_field[cell[0]][cell[1]] > rate and self.is_empty(*cell):
                    rate = zombie_distance_field[cell[0]][cell[1]]
                    best_step = [cell]
                elif zombie_distance_field[cell[0]][cell[1]] == rate and self.is_empty(*cell):
                    best_step.append(cell)

            self._human_list[self._human_list.index(human)] = random.choice(best_step)

    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        for zombie in self.zombies():
            rate = human_distance_field[zombie[0]][zombie[1]]
            best_step = [zombie]
            neighbors = self.four_neighbors(*zombie)

            for cell in neighbors:
                if human_distance_field[cell[0]][cell[1]] < rate and self.is_empty(*cell):
                    rate = human_distance_field[cell[0]][cell[1]]
                    best_step = [cell]
                elif human_distance_field[cell[0]][cell[1]] == rate and self.is_empty(*cell):
                    best_step.append(cell)

            self._zombie_list[self._zombie_list.index(zombie)] = random.choice(best_step)

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

poc_zombie_gui.run_gui(Apocalypse(30, 40))

