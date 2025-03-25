import gymnasium as gym
import numpy as np
import pygame

# Initialize Pygame for keyboard control
pygame.init()
WINDOW_SIZE = (400, 300)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Car Racing Control")

# Create the CarRacing-v3 environment
env = gym.make('CarRacing-v3', render_mode='human')


# Keyboard control mapping
def get_manual_action():
    keys = pygame.key.get_pressed()
    steering = 0.0
    acceleration = 0.0
    brake = 0.0

    if keys[pygame.K_LEFT]:
        steering = -1.0
    if keys[pygame.K_RIGHT]:
        steering = 1.0
    if keys[pygame.K_UP]:
        acceleration = 1.0
    if keys[pygame.K_DOWN]:
        brake = 1.0
    
    return np.array([steering, acceleration, brake])

obs, info = env.reset()
done = False

time_step = 0  # Track the number of time steps

while not done:
    time_step += 1
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # Get action from keyboard input
    action = get_manual_action()
    
    # Take the action in the environment
    obs, reward, done, truncated, info = env.step(action)
    
    # Render every 3 frames for performance efficiency
    if time_step % 3 == 0:
        env.render()
    
    if truncated:
        break

# Close the environment
env.close()
pygame.quit()