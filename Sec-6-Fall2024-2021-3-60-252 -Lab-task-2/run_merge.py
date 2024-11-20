import pygame
import sys
from agent_merge import Agent
from environment_merge import Environment

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
GRID_SIZE = 40
STATUS_WIDTH = 500
BACKGROUND_COLOR = (255, 255, 255)
BARRIER_COLOR = (0, 0, 0)       # Barrier color is black
TASK_COLOR = (255, 0, 0)        # Task color is red
TEXT_COLOR = (0, 0, 0)
BUTTON_COLOR = (0, 200, 0)
BUTTON_HOVER_COLOR = (0, 255, 0)
BUTTON_TEXT_COLOR = (255, 255, 255)
MOVEMENT_DELAY = 50  # Milliseconds between movements which prevent the agent from moving too fast.

def reset_agent(agent, original_environment):
    # Reset the agent's state and assign a new copy of the environment.
    agent.environment = original_environment.copy_environment()
    agent.position = [0, 0]
    agent.rect.topleft = (0, 0)
    agent.path = []
    agent.task_completed = 0
    agent.completed_tasks = []
    agent.total_path_cost = 0
    agent.moving = False

def main():
    pygame.init()

    # Set up display with an additional status panel
    screen = pygame.display.set_mode((WINDOW_WIDTH + STATUS_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Pygame AI Grid Simulation Comparison: UCS vs A*")

    # Clock to control frame rate
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 24)

    # Initialize the original environment
    original_environment = Environment(WINDOW_WIDTH, WINDOW_HEIGHT, GRID_SIZE, num_tasks=5, num_barriers=15)

    # Initialize agents with copies of the environment and creates a copy of the original environment so that each agent works in its own independent environment.
    agent_ucs = Agent(original_environment.copy_environment(), GRID_SIZE, algorithm="UCS")
    agent_astar = Agent(original_environment.copy_environment(), GRID_SIZE, algorithm="A*")
    agents = [agent_ucs, agent_astar]
#all_sprites is a Pygame Group object used to manage and update all sprites (graphical objects) in the simulation.
#Using a Group makes it easier to perform operations like drawing or updating all sprites at once.
    all_sprites = pygame.sprite.Group()
    all_sprites.add(agent_ucs, agent_astar)

    # Start button positioned on the right side (status panel)
    button_width, button_height = 100, 50
    button_x = WINDOW_WIDTH + (STATUS_WIDTH - button_width) // 2
    button_y = WINDOW_HEIGHT // 2 - button_height // 2
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    simulation_started = False
    current_agent_index = 0  # Track which agent is being simulated

    # Variables for movement delay
    last_move_time = pygame.time.get_ticks()

    # Main loop
    running = True
    while running:
        clock.tick(60)  # Limit to 60 FPS

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if not simulation_started and event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    simulation_started = True
                    agents[current_agent_index].find_nearest_task()

        # Clear the screen
        screen.fill(BACKGROUND_COLOR)

        # Draw grid and barriers
        for x in range(original_environment.columns):
            for y in range(original_environment.rows):
                rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(screen, (200, 200, 200), rect, 1)  # Draw grid lines(1 as i want the line to be outlined not filled)

        # Draw barriers
        for (bx, by) in original_environment.barrier_locations:
            barrier_rect = pygame.Rect(bx * GRID_SIZE, by * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, BARRIER_COLOR, barrier_rect)

        # Draw tasks with numbers
        for (tx, ty), task_number in original_environment.task_locations.items():
            task_rect = pygame.Rect(tx * GRID_SIZE, ty * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, TASK_COLOR, task_rect)
            task_num_surface = font.render(str(task_number), True, (255, 255, 255))# render takes input as text format
            task_num_rect = task_num_surface.get_rect(center=task_rect.center)
            screen.blit(task_num_surface, task_num_rect)

        # Draw agents
        all_sprites.draw(screen)#This draws all agents in the all_sprites group on the screen.

        # Display status panel
        status_x = WINDOW_WIDTH + 10
        font_large = pygame.font.Font(None, 30)

        for index, agent in enumerate(agents):
            algorithm_text = f"Algorithm: {agent.algorithm}"
            algorithm_surface = font_large.render(algorithm_text, True, TEXT_COLOR)
            screen.blit(algorithm_surface, (status_x, 10 + index * 150))

            # Display tasks completed, position, and total cost
            task_status_text = f"Tasks Completed: {agent.task_completed}"
            position_text = f"Position: {agent.position}"
            completed_tasks_text = "Completed Tasks: " + ", ".join(
                [f"{task}(Cost: {cost})" for task, cost in agent.completed_tasks]
            )
            total_cost_text = f"Total Path Cost: {agent.total_path_cost}"

            status_surface = font.render(task_status_text, True, TEXT_COLOR)
            position_surface = font.render(position_text, True, TEXT_COLOR)
            completed_tasks_surface = font.render(completed_tasks_text, True, TEXT_COLOR)
            total_cost_surface = font.render(total_cost_text, True, TEXT_COLOR)

            screen.blit(status_surface, (status_x, 40 + index * 150))
            screen.blit(position_surface, (status_x, 70 + index * 150))
            screen.blit(completed_tasks_surface, (status_x, 100 + index * 150))
            screen.blit(total_cost_surface, (status_x, 130 + index * 150))

        # Draw the start button if simulation hasn't started
        if not simulation_started:
            mouse_pos = pygame.mouse.get_pos()
            if button_rect.collidepoint(mouse_pos):
                button_color = BUTTON_HOVER_COLOR
            else:
                button_color = BUTTON_COLOR
            pygame.draw.rect(screen, button_color, button_rect)
            button_text = font.render("Start", True, BUTTON_TEXT_COLOR)
            text_rect = button_text.get_rect(center=button_rect.center)
            screen.blit(button_text, text_rect)
        else:
            # Automatic movement with delay
            current_time = pygame.time.get_ticks()
            if current_time - last_move_time > MOVEMENT_DELAY:
                agent = agents[current_agent_index]
                if not agent.moving and agent.environment.task_locations:# if The agent is not currently moving and there is still task to complete,it finds the nearest task and starts moving towards it.
                    agent.find_nearest_task()
                elif agent.moving:
                    agent.move()
                else:
                    # Switch to the next agent after completion
                    current_agent_index += 1
                    if current_agent_index < len(agents):
                        reset_agent(agents[current_agent_index], original_environment)
                        agents[current_agent_index].find_nearest_task()
                    else:
                        simulation_started = False  # End simulation when both agents are done
                last_move_time = current_time

        # Draw the status panel separator
        pygame.draw.line(screen, (0, 0, 0), (WINDOW_WIDTH, 0), (WINDOW_WIDTH, WINDOW_HEIGHT))

        # Update the display
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":#the script is run directly not from the module
    main()
