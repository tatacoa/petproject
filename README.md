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

The player control a gun that appear in the low part of the screen, the player can move the gun to the rigth and to the left using the < > keys and to shot using the barscpace. When the game beginns, a familiy of rabbits come to tierpark from the top of the screen, the player shot the rabits, when the player kill all the rabits, a new generation will come to the park that is faster, if a rabbit comes to the end of the park the player will loose and the game is over.


![image](images/Screenshot1.png)
![image](images/Screenshot2.png)
![image](images/Screenshot3.png)


# UML

![image](images/uml_1.png)

![image](images/uml_2.png)

In this diagram you can see some action nodes. Yo have a start node and an end node. 
On the right there is a branching. Object nodes are not drawn. In this way, you could insert objects in various places, which are
then available at that point. For example, a rabbit object that is killed by the police after a successful bullet shoot. Or
an object representing the entire game including rabbits and the police.

![image](images/uml_3.png)

State Diagram:

In this diagram each box represent one stage of the game  and describe it. Once the game start the player can have 3 states: 1: the police is killing rabbits, 2: The Rabbits kill the police and 3: The police has no more bullets and need to wait for a small period of time till some bullets are free again. The player win, wenn all the rabbits are killed and  loose when the rabbits kill him. 

![image](images/uml_4.png)

# Metrics

# SonarQube Scanner

SonarQube performs an anaysis of the pet project; the quality measures and issues instances where coding rules were broken. to see the results please link on the Badget:


[![sonar cube]( https://sonarcloud.io/api/project_badges/measure?project=Sonar_PetProject&metric=alert_status)](https://sonarcloud.io/dashboard?id=Sonar_PetProject)


The pet project complexity was calculated based on the number of paths through the code. This calculation gave a value of 54, is a low number indicating the code is easy to read. No duplicated blocks, files or lines. Two issues where found for an unused local variable and the other one having two branches in the same if statment. 

Overal Maintainability rating was A! (Remediation cost / Development cost : less than 0.05), no bugs rating A!. In General my code pass the SonarQube scanner no bugs and no vulnerabilities found!. 

# Code Climate

[![Maintainability](https://api.codeclimate.com/v1/badges/1a4ffcfcfc01fc55c1e8/maintainability)](https://codeclimate.com/github/tatacoa/petproject/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/1a4ffcfcfc01fc55c1e8/test_coverage)](https://codeclimate.com/github/tatacoa/petproject/test_coverage)

# CI Travis

# Clean Code

The clean code is based on the "Clean code cheat sheet" from this [link](https://www.planetgeek.ch/wp-content/uploads/2013/06/Clean-Code-V2.2.pdf). I show here some examples:

[Example 1](): Package Coupling
[Example 1](): High Cohesion
[Example 1](): Class Design
[Example 1](): Naming
[Example 1](): Methods

# DSL

# Functional Programing

# AOP

# Logical Solver

# Scala

