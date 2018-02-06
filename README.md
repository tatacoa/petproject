# Pet Project Dashboard Advanced Softwareengineering WS17-18
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

![image](images/Screenshot1.png)
![image](images/Screenshot2.png)
![image](images/Screenshot3.png)


# UML

![image](images/ULM1.png)

![image](images/ULM2.png)
In this diagram you can see some action nodes. Yo have a start node and an end node. 
On the right there is a branching. Object nodes are not drawn. In this way, you could insert objects in various places, which are
then available at that point. For example, a rabbit object that is killed by the police after a successful bullet shoot. Or
an object representing the entire game including rabbits and the police.

![image](images/UML3.png)
State Diagram:

In this diagram each box represent one stage of the game  and describe it. Once the game start the player can have 3 states: 1: the police is killing rabbits, 2: The Rabbits kill the police and 3: The police has no more bullets and need to wait for a small period of time till some bullets are free again. The player win, wenn all the rabbits are killed and  loose when the rabbits kill him. 

![image](images/ULM4.png)



# SonarQube Scanner

SonarQube performs an anaysis of the pet project; the quality measures and issues instances where coding rules were broken. to see the results please link on the Badget:


[![sonar cube]( https://sonarcloud.io/api/project_badges/measure?project=Sonar_PetProject&metric=alert_status)](https://sonarcloud.io/dashboard?id=Sonar_PetProject)


The pet project complexity was calculated based on the number of paths through the code. This calculation gave a value of 54, is a low number indicating the code is easy to read. No duplicated blocks, files or lines. Two issues where found for an unused local variable and the other one having two branches in the same if statment. 

Overal Maintainability rating was A! (Remediation cost / Development cost : less than 0.05), no bugs rating A!. In General my code pass the SonarQube scanner no bugs and no vulnerabilities found!. 

[I'm an inline-style link](https://github.com/tatacoa/petproject/blob/ee7915f0faf42276e62e945d54f5a2e4ab89005a/bullet.py#L5)

