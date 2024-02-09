# TicTacToe AI

### Project Description
I tasked myself to create an <b> unbeatable </b> `TicTacToe AI` entirely within `Python` without the use of any AI libraries. I successfully did so within just over <b> 400 lines of code </b>. 

I created this game with 2 different gamemodes: one to play against the `AI` and one for casual `PVP`. You are also able to choose whether you want to play the game as `X` or `O`.

### Libraries
- <b>`PyGame`</b>: To setup the GUI
- <b>`Time`</b>: As to allow the user time to make a move
- <b>`Numpy`</b>: For the 'backend'
- <b>`Sys`</b>: To exit the system
- <b>`Random`</b>: For the AI's first move
- <b>`Copy`</b>: Implemented in the `MiniMax Function`
- <b>`Const`</b>: Just a self-made python file for any constants

### Code Structure

The code is written within 3 main classes:

1. `class Board`:
    
    This class is primarily for the computer to understand the moves made and the boards current position. A 3x3 matrix is created which marks that positon by whichever player made the move. This is then interpreted by the next function which then converts it into a visible GUI.

2. `class Game`: 

    This class focuse on the GUI aspect of the game. Using Pygame, I was able to draw out the whole board along with the `X`s, the `O`s, the lines for when someone wins, and even a text box indicating the outcome of the game. 

3. `class AI`: 

    This class is where the magic for the AI takes place. Although it is the smallest out of the three, it is the most crucial. Its main goal is to implement the `Minimax` Function. 

    `Minimax`: This is a very popular algorithm which implements recursion and the concept of weights in order to allow the computer to pick the best possible move. Here is a nice explanation if you are willing to learn more: https://brilliant.org/wiki/minimax/

### Reflection

This project sparked an interest within me for AI/Machine Learning and its endless possibilites. It also allowed me to gain a vast amount of experience within `Object Oriented Programming (OOP)` which is always a useful skill to have. Playing around with Pygame also me to gain an interest towards game development: (C# and Unity?). Overall, it was a great experience and I enjoyed it which is really all that truly matters.

### Future Plans?

I will definetly put more hours into `Machine Learning` (specifically reinforcement learning) and spend more time researching `Neural Networks` and how they function. Learning this skill will open a new world of possibilites for me. Outside of Python, I want to start learning `SQL` and implement that into Machine Learning for databases and other things. `C++` is also a compelling sight for me right now as it has so many endless possibilites.




