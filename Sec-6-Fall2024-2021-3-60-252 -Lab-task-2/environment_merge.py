import random
import copy

class Environment:
    def __init__(self, width, height, grid_size, num_tasks, num_barriers):
        self.width = width
        self.height = height
        self.grid_size = grid_size
        self.columns = width // grid_size
        self.rows = height // grid_size
        self.task_locations = self.generate_tasks(num_tasks)#is called to create num_tasks unique task locations.
        self.barrier_locations = self.generate_random_locations(num_barriers, exclude=set(self.task_locations.keys()))
#exclude parameter ensures that barriers are not placed at the same locations as tasks
    def generate_tasks(self, count):
        #Generating task locations with unique task numbers.
        tasks = {}# empty tasks dictionary that will store the generated task locations.
        for task_number in range(1, count + 1):
            while True:
                location = (random.randint(0, self.columns - 1), random.randint(0, self.rows - 1))#form a tuple (x(col), y(row)) representing location for the task.
                if location not in tasks:
                    tasks[location] = task_number
                    break
        return tasks

    def generate_random_locations(self, count, exclude=set()):
        #Generating unique random locations that are not in the exclude set.
        locations = set()# it is an empty set that will store the randomly generated unique locations.
        while len(locations) < count:
            location = (random.randint(0, self.columns - 1), random.randint(0, self.rows - 1))
            if location not in exclude:
                locations.add(location)
        return locations

    def is_within_bounds(self, x, y):
        #Checking if (x, y) is within the grid boundaries.
        return 0 <= x < self.columns and 0 <= y < self.rows

    def is_barrier(self, x, y):
        #Checking if (x, y) is a barrier.
        return (x, y) in self.barrier_locations

    def copy_environment(self):
        # Creating a copy of the environment to ensure independent operations like simulating with different agent without affecting the original environment.
        env_copy = Environment(self.width, self.height, self.grid_size, 0, 0)  # Create a new empty environment
        env_copy.task_locations = copy.deepcopy(self.task_locations)
        env_copy.barrier_locations = copy.deepcopy(self.barrier_locations)
        return env_copy
