# Asteroid Game

Asteroid arcade game written in Python. Control a spaceship and survive incoming asteroids as long as you can!

## Gameplay
- Pilot a spaceship through open space
- Shoot asteroids before they collide with your ship
- Try to survive, one hit ends the game
- Each destroyed asteroid is logged as an event

## Technologies Used
- Python
- Pygame (graphics, input handling, collision detection)

## Project Structure 

```
asteroids/
├── main.py           # Main game loop
├── player.py         # Player spaceship logic
├── asteroid.py       # Asteroid behavior
├── shot.py           # Player projectiles
├── utils.py          # Helper functions (e.g., logging)
├── assets/           # Images / sounds (if applicable)
└── README.md         # Project documentation

```

## How to Run on Local

1. Make sure Python3 is installed on local

2.  Install pygame 
   ```
   pip install pygame
   ```
3. Activate virtual environment
 ```
   source .venv/bin/activate

 ```

4. Run the game 

   ```
   python3 main.py
 
   ```

## Game Logic Highlights
  ### Collision Detection 
- Game checks for collision between:
   * Player <-> Asteroid
   * Shots <-> Asteroid 
- When shot hits asteroid: 
  * the event “asteroid_shot” is logged
  * but the shot and asteroid are removed from the game 

## Features 
- Real-time collision detection
- Event logging
- Object-oriented design
- Clean game loop structure 

## Author
Created by A. Ibrahim