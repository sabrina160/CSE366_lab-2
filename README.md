# Pygame AI Grid Simulation: UCS vs A*
This project visualizes task scheduling and pathfinding in a grid environment using two algorithms: Uniform Cost Search (UCS) and A*. It includes real-time simulations of agent movement, task completion, and workload evaluation.
# Objective
The goal is to simulate an environment where multiple tasks are distributed across a grid with barriers, and agents optimize their path using UCS or A* algorithms. The objectives are:

- Compare Algorithms: Evaluate the efficiency of UCS and A* in completing tasks.
- Task Visualization: Provide a graphical representation of the grid, agents, tasks, and barriers.
- Real-Time Updates: Display dynamic status information, including completed tasks and path costs.
# Features
# Algorithms
- Uniform Cost Search (UCS): Finds the shortest path by cumulative cost without heuristics.
- A*: Combines path cost with heuristic (Manhattan Distance) for better optimization.
# Simulation
- Dynamic Environment: Tasks, barriers, and agents are displayed in a grid-based environment.
- Real-Time Updates: Shows task completion status, agent paths, and cost metrics.
- Interactive Start: Users can start the simulation by clicking the "Start" button.
# Visualization
- Grid Representation: Displays barriers, tasks, and agents in a structured grid.
- Agent Movement: Animates agents as they complete tasks.
- Status Panel: Shows algorithm names, completed tasks, positions, and total path costs.
# Setup Instructions
# Prerequisites
- Python 3.13.0
# Libraries:
- pygame
- heapq
# Installation
1. Clone the repository:
   ```bash
     git clone https://github.com/sabrina160/CSE366_lab-2.git
     cd CSE366_lab-2
2. Install the required libraries:
   ```bash
      pip install pygame
# How to Run
1. Navigate to the project folder:
   ```bash
     cd CSE366_lab-2
2. Run the main simulation:
   ```bash
   python run.py
3. A Pygame window will open, displaying the grid environment. Click the Start button to begin the simulation.

# Controls
- Start Simulation: Click the "Start" button to initiate the simulation.
- Exit Simulation: Click the close button on the Pygame window to exit.
# Project Details
# Task and Barrier Generation
- Tasks are randomly distributed on the grid and assigned unique task numbers.
- Barriers are placed randomly, ensuring no overlap with task locations.
# Algorithms
Uniform Cost Search (UCS)
- Explores all possible paths to find the shortest path based on uniform movement cost.
A* Search
- Combines path cost with the Manhattan Distance heuristic to prioritize efficient paths.
# Agent
- Task Completion: Agents complete tasks sequentially based on the chosen algorithm.
- Path Cost Calculation: Each step contributes a uniform cost of 1.
- Independent Environments: Each agent operates in a separate copy of the environment.
# Code Structure
- agent.py: Defines the Agent class for movement, task completion, and algorithm logic.
- environment.py: Contains the Environment class for task and barrier generation.
- run.py: The main script that integrates the environment, agents, and visualization.
# Visualization Details
# Grid
- Tasks: Represented as red squares with task numbers.
- Barriers: Shown as black squares.
- Agents: Represented as blue squares, moving across the grid.
# Status Panel
Displays:
- Algorithm name (UCS or A*)
- Number of tasks completed
- Agent position
- Total path cost
- Cost of each completed task
# Customization
# Environment Parameters
- Grid Size: Change the GRID_SIZE constant in run.py.
- Number of Tasks: Modify num_tasks in the Environment initialization.
- Number of Barriers: Adjust num_barriers in the Environment initialization.
# Movement Speed
- Modify MOVEMENT_DELAY in run.py to control the delay (in milliseconds) between agent movements.

