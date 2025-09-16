# RPG Game

A 2D top-down RPG game built with Python and Pygame featuring animated sprites, combat mechanics, and tile-based movement.

## Features

- **Animated Character Movement** - Smooth directional animations for player and enemies
- **Combat System** - Collect weapons and shoot projectiles to defeat enemies
- **Health System** - Visual health bars for both player and enemies
- **Collision Detection** - Realistic collision with blocks, water, and enemies
- **Enemy AI** - Enemies move randomly and shoot at the player
- **Particle Effects** - Visual feedback for player movement
- **Tile-based World** - Structured game world with different terrain types

## Controls

- **Arrow Keys** - Move your character (up, down, left, right)
- **Z Key** - Shoot projectiles (requires weapon pickup)
- **ESC/Close Window** - Exit game

## Game Elements

- **P** - Player starting position
- **E** - Enemy spawn points
- **W** - Weapon pickups
- **B** - Solid blocks (impassable)
- **R** - Water areas (impassable)
- **.** - Ground (walkable)

## Installation

1. Make sure you have Python installed on your system
2. Install Pygame:
   ```
   pip install pygame
   ```
3. Run the game:
   ```
   python main.py
   ```

## Requirements

- Python 3.x
- Pygame 2.x

## Game Mechanics

### Player
- Move around the map using arrow keys
- Collect weapons to enable shooting
- Avoid enemies and environmental hazards
- Health decreases when hit by enemy projectiles
- Game ends when health reaches zero

### Enemies
- Move randomly around the map
- Shoot projectiles at regular intervals
- Have individual health bars
- Can be defeated by player projectiles
- Cause collision damage to player on contact

### Combat
- Pick up weapons (W tiles) to enable shooting
- Press Z to fire projectiles in your facing direction
- Projectiles travel until hitting blocks or targets
- Both player and enemies can be damaged by projectiles

## File Structure

```
GameFiles/
├── main.py           # Main game loop and initialization
├── configuration.py  # Game settings and constants
├── sprites.py        # Player, enemy, and sprite classes
├── weapons.py        # Weapon and projectile classes
└── assets/           # Game images and resources
    └── images/
        ├── terrain.png
        ├── cats.png
        ├── evil.png
        ├── sword.png
        └── powerBall.png
```

## Customization

You can modify game settings in `configuration.py`:
- Window dimensions
- Movement speed
- Health values
- Layer ordering
- Colors
- Tile map layout

## Troubleshooting

**Game won't start:**
- Ensure Pygame is installed: `pip install pygame`
- Check that all asset files are present in the assets/images/ directory

**Performance issues:**
- Adjust FPS setting in configuration.py
- Reduce sprite animation speed

## Credits

Built with Python and Pygame framework.