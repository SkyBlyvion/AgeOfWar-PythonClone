
# 🎮 Age of War Clone Game

Welcome to the **Age of War Clone** project! This game is a 2D side-scroller inspired by the classic flash game *Age of War*, where two sides (player and enemy) send units to destroy each other's buildings. The player's goal is to spawn units, engage in combat, and destroy the enemy building located on the opposite side of the screen.

---

## 📝 Project Structure

```
age_of_war/
│
├── assets/              # Directory for all game assets like images, sounds, etc.
│   └── sprites/         # Sprites for units, buildings, backgrounds, etc.
│
├── src/                 # Source code directory
│   ├── entities/        # Game entities (buildings, units, etc.)
│   │   └── building.py  # The Building class
│   │   └── unit.py      # The Unit class
│   │
│   ├── main.py          # Main game loop and initial setup
│   ├── game.py          # Core game logic (unit spawning, updating)
│   └── utils.py         # Helper functions (e.g., health bars, collision)
│
└── README.md            # Project overview
```

---

## 🚀 Getting Started

### Prerequisites

Before you can run the game, you need to have the following installed:

- **Python 3.x**
- **Pygame library**

You can install Pygame by running:

```bash
pip install pygame
```

### Running the Game

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/age-of-war-clone.git
    ```
   
2. Navigate to the project folder:
    ```bash
    cd age_of_war
    ```

3. Run the game:
    ```bash
    python src/main.py
    ```

---

## 🛠️ Features

- **Player and Enemy Buildings**: Each side has a building with 4000 health points. The goal is to reduce the enemy building's health to 0.
- **Units**: Both the player and the enemy can spawn units. The units automatically move towards the opposing building and deal damage when they reach it.
- **Health Bars**: Buildings have dynamic health bars that display current health. As units deal damage, the health bars are updated.
- **Real-Time Combat**: Units from both sides engage in real-time combat on the battlefield.
- **Modular Codebase**: The project is structured to be scalable, allowing easy additions of new units, buildings, and game mechanics.

---

## 📁 File Breakdown

### `src/main.py`
The main entry point of the game. It initializes Pygame, sets up the game window, and starts the game loop.

### `src/game.py`
Manages the core game logic including unit spawning, movement, and updating game states (e.g., health, combat).

### `src/entities/building.py`
Defines the `Building` class, which represents the player's and enemy's buildings. It handles health, damage, and rendering.

### `src/entities/unit.py`
Defines the `Unit` class, which represents the units that move across the battlefield. Each unit deals damage when it reaches the enemy building.

### `src/utils.py`
This file will contain utility functions for collision detection, health bar drawing, and other reusable game logic.

---

## 🎯 Roadmap

- **Player Controls**: Add a control panel for the player to select and spawn different types of units.
- **Combat System**: Implement unit-on-unit combat where units can engage and damage each other.
- **Advanced AI**: Improve enemy AI to balance difficulty and challenge the player with different strategies.
- **Unit Upgrades**: Introduce upgrades and age progression for both the player and the enemy, inspired by the *Age of War* mechanics.

---

## 🤝 Contributing

We welcome contributions to the project! If you find any issues or want to add features, feel free to submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

---

## ⚖️ License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## 📧 Contact

For questions or feedback, please reach out to us at:

- **Email**: richtofen60@gmail.com
- **GitHub**: [SkyBlyvion](https://github.com/SkyBlyvion)
