# Pygame AI Grid Simulation: UCS vs A*
This project visualizes task scheduling and pathfinding in a grid environment using two algorithms: Uniform Cost Search (UCS) and A*. It includes real-time simulations of agent movement, task completion, and workload evaluation.
# Objective
The goal is to simulate an environment where multiple tasks are distributed across a grid with barriers, and agents optimize their path using UCS or A* algorithms. The objectives are:

-Compare Algorithms: Evaluate the efficiency of UCS and A* in completing tasks.
-Task Visualization: Provide a graphical representation of the grid, agents, tasks, and barriers.
-Real-Time Updates: Display dynamic status information, including completed tasks and path costs.
# Features
# Algorithms
Uniform Cost Search (UCS): Finds the shortest path by cumulative cost without heuristics.
A*: Combines path cost with heuristic (Manhattan Distance) for better optimization.
# Simulation
Dynamic Environment: Tasks, barriers, and agents are displayed in a grid-based environment.
Real-Time Updates: Shows task completion status, agent paths, and cost metrics.
Interactive Start: Users can start the simulation by clicking the "Start" button.
# Visualization
Grid Representation: Displays barriers, tasks, and agents in a structured grid.
Agent Movement: Animates agents as they complete tasks.
Status Panel: Shows algorithm names, completed tasks, positions, and total path costs.
# Setup Instructions
# Prerequisites
Python 3.x
# Libraries:
pygame
heapq
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
Start Simulation: Click the "Start" button to initiate the simulation.
Exit Simulation: Click the close button on the Pygame window to exit.
