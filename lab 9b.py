# Lab 9b
# Name: Allison  Luo

# lab_9b.py
# URL to public GitHub repo: https://github.com/allisonluo23/lab9

# Create your own github repo
# Add a .py file
# Create a simple version of an agent based simulation, 
# based on the code in the last lecture, and the github repo linked at the end
# 1. Create an Agent class
# 2. Create a World class
# 3. Initialize the world
# 4. Create a loop
# Ask each agent in sequence to find an empty patch
# Move the agent to the empty patch
# 5. End

import random

class Agent:
    def __init__(self, id, world):
        self.id = id
        self.world = world
        self.position = None

    def find_empty_patch(self):
        empty_patches = [(i, j) for i in range(self.world.size) for j in range(self.world.size) if self.world.grid[i][j] is None]
        if empty_patches:
            return random.choice(empty_patches)
        return None

    def move_to_patch(self, patch):
        if self.position is not None:
            self.world.grid[self.position[0]][self.position[1]] = None
        self.position = patch
        self.world.grid[patch[0]][patch[1]] = self.id

class World:
    def __init__(self, size, num_agents):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        self.agents = [Agent(id=i, world=self) for i in range(num_agents)]

    def initialize_world(self):
        for agent in self.agents:
            empty_patch = agent.find_empty_patch()
            if empty_patch:
                agent.move_to_patch(empty_patch)

    def step(self):
        for agent in self.agents:
            empty_patch = agent.find_empty_patch()
            if empty_patch:
                agent.move_to_patch(empty_patch)

    def display(self):
        for row in self.grid:
            print(' '.join([str(cell) if cell is not None else '.' for cell in row]))

def run_simulation(size, num_agents, num_steps):
    world = World(size=size, num_agents=num_agents)
    world.initialize_world()
    print("Initial World State:")
    world.display()
    for step in range(num_steps):
        print(f"\nStep {step + 1}:")
        world.step()
        world.display()

if __name__ == "__main__":
    size = 5  # Size of the grid (5x5)
    num_agents = 3  # Number of agents
    num_steps = 10  # Number of steps to simulate
    run_simulation(size, num_agents, num_steps)
