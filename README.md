# Pet Project Advanced Softwareengineering WS17-18
space invaders like game with angry rabbits and a police man

![rabbit](images/rabbit.png)
![rabbit](images/rabbit.png)
![rabbit](images/rabbit.png)
![rabbit](images/rabbit.png)
![rabbit](images/rabbit.png)
![player](images/player.png)
![rabbit](images/rabbit.png)
![rabbit](images/rabbit.png)
![rabbit](images/rabbit.png)
![rabbit](images/rabbit.png)
![rabbit](images/rabbit.png)

# Rabbits in TierPark 

Rabbits in TierPark is a game based on the famous game of the late 80s space invaders, a classic game one of the first video games created and very popular.

The motivation to create a version of this game as a pet project, is to understand the basic concepts of programming in python, since I have no experience programming in python, and also apply the concepts seen in the course.

The game is inspired by the book "Curso Intensivo de PYTHON" by author Eric Matthes, which I recommend a lot to learn to program in Python!

# The Game

The player control a gun that appear in the low part of the screen, the player can move the policeman to the rigth and to the left using the <> keys and shot using the barscpace. When the game begins, a familiy of rabbits come to tierpark from the top of the screen (Zombie rabbits that want to kill all the Berliners), the player shot the zombie rabbits, when the player kills all the rabbits, a new generation will come to the park that is faster, if a rabbit comes to the end of the park the player will lose and the game is over.


![image](images/Screenshot1.png)
![image](images/Screenshot2.png)



# UMLs

![image](images/uml_2.png)

In this diagram you can see some action nodes. You have a start node and an end node. 
On the right there is a branching. Object nodes are not drawn. In this way, you could insert objects in various places, which are
then available at that point. For example, a rabbit object that is killed by the police after a successful bullet shot. Or
an object representing the entire game including rabbits and the police.

![image](images/uml_3.png)

Sequence Diagram:
In this diagram each box represent one stage of the game  and describe it. Once the game start the player can have 3 states: 1: the police is killing rabbits, 2: The Rabbits kill the police and 3: The police has no more bullets and need to wait for a small period of time till some bullets are free again. The player win, wenn all the rabbits are killed and  lose when the rabbits kill him. 

![image](images/uml_1.png)

The Structure diagram emphasize the objects present in  the game. 

![image](images/uml_4.png)

The class Diagram: shows the relationship between the Classes in the game and how they are involved. The different Classes are connected in the run game file.

# Metrics

# SonarQube Scanner

SonarQube performs an anaysis of the pet project; the quality measures and issues instances where coding rules were broken. to see the results please link on the Badget:


[![sonar cube]( https://sonarcloud.io/api/project_badges/measure?project=Sonar_PetProject&metric=alert_status)](https://sonarcloud.io/dashboard?id=Sonar_PetProject)


The pet project complexity was calculated based on the number of paths through the code. This calculation gave a value of 54, is a low number indicating the code is easy to read. No duplicated blocks, files or lines. Two issues where found for an unused local variable and the other one having two branches in the same if statment. 

Overal Maintainability rating was A! (Remediation cost / Development cost : less than 0.05), no bugs rating A!. In General my code pass the SonarQube scanner no bugs and no vulnerabilities found!. 

# Code Climate

[![Maintainability](https://api.codeclimate.com/v1/badges/1a4ffcfcfc01fc55c1e8/maintainability)](https://codeclimate.com/github/tatacoa/petproject/maintainability)

This code review tool analyze all relevant files in the current working directory in my repository. 20 files where evaluated, 7 Total issues, and a general technical debt rate B (5% to 10% ratio)


# Travis CI

[![Build Status](https://travis-ci.org/tatacoa/petproject.svg?branch=master)](https://travis-ci.org/tatacoa/petproject)

# Clean Code

The clean code is based on the "Clean code cheat sheet" from this [link](https://www.planetgeek.ch/wp-content/uploads/2013/06/Clean-Code-V2.2.pdf). I use vim with [this](https://gist.github.com/tatacoa/d8d212964275bc4a505634dd74d1ce83) configuration.

[Example 1](https://github.com/tatacoa/petproject/blob/aa471e27c6e147c36cd027eb370381386c5351f3/game_stats.py#L1): General and Understandability

[Example 2](https://github.com/tatacoa/petproject/blob/aa471e27c6e147c36cd027eb370381386c5351f3/rabbits_game.py#L13): High Cohesion

[Example 3](https://github.com/tatacoa/petproject/blob/aa471e27c6e147c36cd027eb370381386c5351f3/bullet.py#L5): Class Design

[Example 4](https://github.com/tatacoa/petproject/blob/aa471e27c6e147c36cd027eb370381386c5351f3/settings.py#L1): Naming

[Example 5](https://github.com/tatacoa/petproject/blob/aa471e27c6e147c36cd027eb370381386c5351f3/game_functions.py#L9): Methods



# DSL

A  DSL example that does not contribute to my project: [DSL](https://github.com/tatacoa/petproject/blob/e86d409f61baca6231ec9d74d81ad1cd0d141ae7/dsl.py#L2)

# Functional Programing

Functional programming is great but in the fact is very dificcult for me to implement it, becasue im new in Python and have been focusing in object orentiert languages so far. For my project I choosed a functional programming style where appropriate. For some parts of this specific software a more object-oriented approach was a good fit (rabbits, police, bullets, screen). The implementacion is found [here](https://github.com/tatacoa/petproject/tree/functional-example).

[only final data structures](https://github.com/tatacoa/petproject/blob/functional-example/rabbits_game.py#L18)


(mostly) side effect free functions
- get_number_rabbits_x
- get_number_rows

[Use of higher order functions](https://github.com/tatacoa/petproject/blob/65d67c44267cf248d683625749976ad2d146002c/game_functions.py#L114)

[Function as parameter](https://github.com/tatacoa/petproject/blob/65d67c44267cf248d683625749976ad2d146002c/game_functions.py#L104)

[function as return value](https://github.com/tatacoa/petproject/blob/65d67c44267cf248d683625749976ad2d146002c/game_functions.py#L92)

[use clojures / anonymous functions](https://github.com/tatacoa/petproject/blob/65d67c44267cf248d683625749976ad2d146002c/game_functions.py#L92)



