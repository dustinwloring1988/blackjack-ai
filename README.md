Blackjack Q-Learning Project
============================

Overview
--------

This repository contains Python scripts for implementing a simple Blackjack game and training a Q-learning model to play the game. The project consists of three main scripts:

1.  **blackjack.py**: Implements the core functionality of the Blackjack game, allowing users to play and interact with the game through a command-line interface.
    
2.  **blackjack\_qlearning.py**: Defines a Q-learning agent to learn optimal strategies for playing Blackjack. The Q-learning algorithm is applied to update the agent's Q-table based on observed rewards and state transitions.
    
3.  **train\_qlearning.py**: Utilizes the Q-learning agent to train and evaluate its performance over a specified number of training episodes. After training, the script runs a set of test games to assess the agent's ability to play Blackjack.
    

How to Run
----------

1.  Clone the repository to your local machine:
    
    bashCopy code
    
    `git clone https://github.com/your-username/blackjack-qlearning-project.git`
    
2.  Navigate to the project directory:
    
    bashCopy code
    
    `cd blackjack-qlearning-project`
    
3.  Run the main training script:
    
    bashCopy code
    
    `python train_qlearning.py`
    
    This script will train the Q-learning agent over a set number of episodes and evaluate its performance.
    
4.  Explore the game and trained model:
    
    *   **Play the Game**: If you want to manually play the Blackjack game, run the `blackjack.py` script.
        
        bashCopy code
        
        `python blackjack.py`
        
    *   **Inspect the Q-learning Model**: If you want to explore the Q-table and Q-learning model, refer to the `blackjack_qlearning.py` script.
        

Dependencies
------------

Ensure you have the following dependencies installed:

*   Python 3.x
*   NumPy

Install dependencies using:

bashCopy code

`pip install numpy`

Contributors
------------

*   Dustin Loring (@AIGym on huggingface)

License
-------

This project is licensed under the MIT License.

Feel free to customize this README to provide additional information or specific instructions for your project. If there are any external dependencies or setup steps, make sure to include them in the instructions.
