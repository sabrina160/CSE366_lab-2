import pygame
import heapq

class Agent(pygame.sprite.Sprite):#In Pygame, wheb agent inherits the pygame.sprite.Sprite, the pygame.sprite.Sprite class provides a convenient way to group and manage game objects. 
    def __init__(self, environment, grid_size, algorithm="UCS"):
        super().__init__() #is used to call the initializer (constructor) of the parent class.this statement ensures that the initialization 
        #logic of the parent pygame.sprite.Sprite class is executed before adding any additional initialization logic specific to the Agent class.
        self.image = pygame.Surface((grid_size, grid_size))#self.image and self.rect are key properties. self.image defines what the sprite looks 
        #like (its surface), and self.rect defines its position and size.
        self.image.fill((0, 0, 255))  # Agent color is blue
        self.rect = self.image.get_rect()
        self.grid_size = grid_size
        self.environment = environment
        self.position = [0, 0]  # Starting at the top-left corner of the grid
        self.rect.topleft = (0, 0)
        self.task_completed = 0
        self.completed_tasks = []#it Stores completed tasks along with their costs.
        self.path = []  # List of positions to follow
        self.moving = False  # Flag to indicate if the agent is moving
        self.total_path_cost = 0  # Track the total path cost
        self.algorithm = algorithm  # Algorithm to use: "UCS" or "A*"

    def move(self):
        if self.path:
            next_position = self.path.pop(0)#If there are remaining positions in self.path, the next position (the first element) is retrieved and removed from the list using the pop(0) operation.
            self.position = list(next_position)#update the agents position.
            self.rect.topleft = (self.position[0] * self.grid_size, self.position[1] * self.grid_size)
            self.total_path_cost += 1  # Each time the agent moves to a new position, the total path cost is incremented
            self.check_task_completion()#After moving, the agent checks if it has reached a task location by calling it.
        else:
            self.moving = False  # Stop moving when path is exhausted that means the agent has finished its current path 

    def check_task_completion(self):
        #Checking if the agent has reached a task location.
        position_tuple = tuple(self.position)#stores the agent's current position as a list and converts the list to a tuple
        if position_tuple in self.environment.task_locations:# if the Agent's Position Matches a Task Location
            task_number = self.environment.task_locations.pop(position_tuple)#it retrieves and removes the task associated with position_tuple
            cost = self.total_path_cost
            self.task_completed += 1
            self.completed_tasks.append((task_number, cost))# creates a tuple containing the task number and the cost to reach it.

    def find_nearest_task(self):
        #Finding the nearest task using the selected algorithm.
        nearest_task = None
        shortest_path = None
        for task_position in self.environment.task_locations.keys():#keys() represent the task position.self.environment.task_locations ei dictonary er moddhe task_position ta ase
            if self.algorithm == "UCS":
                path = self.ucs_find_path_to(task_position)
            elif self.algorithm == "A*":
                path = self.a_star_find_path_to(task_position)
            else:
                raise ValueError("Unknown algorithm specified.")
            
            if path:#If a valid path to task_position is found
                if not shortest_path or len(path) < len(shortest_path):#If shortest_path is None
                    shortest_path = path
                    nearest_task = task_position
        if shortest_path:#If a valid shortest_path was found
            self.path = shortest_path[1:]  # Exclude the current position
            self.moving = True

    def ucs_find_path_to(self, target):
        #Finding the shortest path to the target position using UCS (no heuristic).
        start = tuple(self.position)
        goal = target
        queue = []
        heapq.heappush(queue, (0, [start]))  # (cost, path)
        visited = set()

        while queue:
            cost, path = heapq.heappop(queue)
            current = path[-1]#Sets current as the last position in the path.
            if current == goal:
                return path
            if current in visited:# if the position/node is visited then continue
                continue
            visited.add(current)
#This part is used to explore the neighboring positions of the current node in the pathfinding process using the Uniform Cost Search (UCS) algorithm.
            neighbors = self.get_neighbors(*current)# retrieves the neighboring positions of current.

            for neighbor in neighbors:
                if neighbor not in visited:
                    new_path = list(path)#Creates a new path by copying the existing path and appending the neighbor.
                    new_path.append(neighbor)#and appending the neighbor.to this new path
                    heapq.heappush(queue, (cost + 1, new_path))  # Uniform cost of 1
        return None  #if No path found

    def a_star_find_path_to(self, target):
        #Finding the shortest path to the target position using A* (cost + heuristic).
        start = tuple(self.position)
        goal = target
        queue = []
        heapq.heappush(queue, (self.manhattan_distance(start, goal), 0, [start]))  # (estimated_cost, cost_so_far, path)
        visited = set()

        while queue:
            estimated_cost, cost_so_far, path = heapq.heappop(queue)
            current = path[-1]
            if current == goal:
                return path
            if current in visited:
                continue
            visited.add(current)

            neighbors = self.get_neighbors(*current)
            for neighbor in neighbors:
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    new_cost = cost_so_far + 1  # Uniform cost of 1 that represents the uniform cost of moving from the current node to its
                    #neighboring node and every move the agent makes is assumed to have a cost of 1
                    heuristic = self.manhattan_distance(neighbor, goal)
                    estimated_cost = new_cost + heuristic
                    heapq.heappush(queue, (estimated_cost, new_cost, new_path))
        return None  # if No path found

    def manhattan_distance(self, point1, point2):
        #Calculating the Manhattan distance between two points.
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    def get_neighbors(self, x, y):
        #Getting walkable neighboring positions.
        neighbors = [] # initially empty but will store a list of neighbors position.
        directions = [("up", (0, -1)), ("down", (0, 1)), ("left", (-1, 0)), ("right", (1, 0))]#Each tuple has two elements: a direction name up and a coordinate change (dx, dy).
        for _, (dx, dy) in directions:# _, is used to ignore the first element of the directions
            nx, ny = x + dx, y + dy
            if self.environment.is_within_bounds(nx, ny) and not self.environment.is_barrier(nx, ny):# checking if the new position is valid 
                #(within the boundaries and the new postion is not a barrier)
                neighbors.append((nx, ny))
        return neighbors
