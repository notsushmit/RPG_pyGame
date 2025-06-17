

# 🕹️ 2D Adventure Game using Python

Welcome to a unique project that combines a classic 2D tile-based adventure game built with **Python & Pygame** and an **IoT motor control simulation** using threading and timers. This project demonstrates game development, sprite animation, and basic IoT control concepts all in one place.

---

## 🎮 Game Overview

The game is a simple 2D top-down adventure:

* The player navigates through a tile-based map.
* Blocks, water tiles, enemies, and collectible weapons enrich the gameplay.
* The player can move in four directions, equip a sword, and shoot bullets.
* Enemies move randomly and shoot back.
* Health bars for both player and enemies are displayed and updated dynamically.

---

## ⚙️ IoT Motor Control

Besides the game, the project includes an **IoT motor control simulation**:

* It demonstrates motor on/off states.
* Uses threading for a timer-based motor operation.
* Simulates overload (OVLD) conditions and frequency settings.

---

## 🎮Controls

| Action      | Key           |
| ----------- | ------------- |
| Move Up     | `↑` Arrow Key |
| Move Down   | `↓` Arrow Key |
| Move Left   | `←` Arrow Key |
| Move Right  | `→` Arrow Key |
| Shoot Sword | `Z` Key       |
| Quit Game   | Close Window  |

---

## 📁 Project Structure

| File                   | Description                                                                                                                                    |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **`main.py`**          | Entry point for the game. Initializes the window, loads spritesheets, and runs the game loop.                                                  |
| **`configuration.py`** | Stores global configuration settings (screen size, tile map, layers, colors, health, etc.).                                                    |
| **`sprites.py`**       | Contains classes for all in-game sprites: Player, Enemy, Block, Ground, Water, Health Bars, and Particles.                                     |
| **`weapons.py`**       | Contains Weapon, Bullet, and Enemy Bullet classes with animations and collision detection.                                                     |
| **`IOT.py`**           | Simulates an IoT motor with timer-based control, overload detection, and frequency settings. Runs a basic motor state machine using threading. |

---

## 🗺️ Features

✅ Tile-based map defined in `configuration.py`
✅ Animated sprites for the player, enemies, weapons, and environment
✅ Player-enemy interaction with health bars and shooting mechanics
✅ Simple camera system to navigate the map
✅ IoT motor control simulation using Python threads and state machines

---

## 🚀 Getting Started

### 1️⃣ Prerequisites

* Python 3.x
* Pygame
* Matplotlib & NumPy (for the IoT part)

Install dependencies:

```bash
pip install pygame matplotlib numpy
```

---

### 2️⃣ Run the Game

```bash
python main.py
```

### 3️⃣ Run the IoT Motor Simulation

```bash
python IOT.py
```

---

## 🎨 Assets

Ensure you have the following image assets in an `assets/images/` directory:

* `terrain.png` — terrain tiles
* `cats.png` — player sprite sheet
* `evil.png` — enemy sprite sheet
* `sword.png` — weapon sprite sheet
* `powerBall.png` — bullet sprite sheet

---
