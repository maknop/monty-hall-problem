# Monty Hall Problem

## Description
The Monty Hall problem involves the idea that you’re essentially in a game show and you, which will  
be referred to as the player, have three doors to choose from. Behind each of those doors lies one  
of two goats or a brand-new car. Your host, named Monty Hall, tells you to choose a door. Once you  
have chosen one of the doors, Monty then has one of the other doors that does contain one of the goats  
opened. Following this, he gives you the option to either keep your current pick or change to the other  
door not opened. It is assumed here that the player’s goal is to win the car in particular.  There are  
several assumptions made in the Monty Hall problem, such as:
1. Once you have chosen a door, Monty will always open one with a goat behind it. 
2. The door Monty opens will not be the one you chose and does not contain the car. 
3. There is an equal chance of the car being behind any of the doors. 

## Player Switches Doors Every Time
A = Picking one of three doors = 1/3  
B = Car is behind chosen door = 1/3  
C = Monty’s choice of doors to invalidate = 1/2  

![Switch](/img/does_switch.png)

```
S = { ( 1, 3, 1 ), ( 1, 3, 2 ), ( 1, 2, 1 ), ( 1, 2, 3 ),  
      ( 2, 3, 1 ), ( 2, 3, 2 ), ( 2, 1, 3 ), ( 2, 3, 2 ),  
      ( 3, 2, 1 ), ( 3, 2, 3 ), ( 3, 1, 3 ), ( 3, 1, 2 ) } = 12 total outcomes  

W = { ( 1, 3, 2 ), ( 1, 2, 3 ), ( 2, 3, 1 ),  
      ( 2, 1, 3 ), ( 3, 2, 1 ), ( 3, 1, 2 )  } = 6 outcomes  
```

Therefore, `P(W) = 1/9 + 1/9 + 1/9 + 1/9 + 1/9 + 1/9 = 6/9`  

## Player Does Not Switch Doors Every Time
A = Picking one of three doors = 1/3  
B = Car is behind chosen door = 1/3  
C = Monty’s choice of doors to invalidate = 1/2  

![Does Not Switch](/img/does_not_switch.png)

```
S = { ( 1, 3, 1 ), ( 1, 3, 2 ), ( 1, 2, 1 ), ( 1, 2, 3 ),  
      ( 2, 3, 1 ), ( 2, 3, 2 ), ( 2, 1, 3 ), ( 2, 3, 2 ),  
      ( 3, 2, 1 ), ( 3, 2, 3 ), ( 3, 1, 3 ), ( 3, 1, 2 ) } = 12 total outcomes  

W = { (1, 3, 1), (1, 2, 1), (2, 3, 2),  
      (2, 1, 2), (3, 2, 3), (3, 1, 3) } = 6 outcomes  
```

Therefore, `P(W) = 1/18 + 1/18 + 1/18 + 1/18 + 1/18 + 1/18 = 6/18 = 1/3`

## Host Randomly Picks Door
A = Picking one of three doors = 1/3
B = Car is behind chosen door = 1/3
C = Monty’s choice of doors to invalidate = 1/2

![Host Picks Door](img/host_picks_door.png)

```
S = { (1, 2, 2), (1, 2, 3), (1, 2, 1), (1, 3, 2), (1, 3, 3), (1, 3, 1),  
      (2, 1, 1), (2, 1, 3), (2, 1, 2), (2, 3, 3), (2, 3, 1), (2, 3, 2),  
      (3, 1, 1), (3, 1, 2), (3, 1, 3), (3, 2, 1), (3, 2, 3), (3, 2, 2) } = 18 total outcomes  
  
W = { (1, 2, 3), (1, 3, 2), (2, 1, 3),  
      (2, 3, 1), (3, 1, 2), (3, 2, 1) } = 6 total outcomes
```

Therefore, `P(W) = 1/18 + 1/18 + 1/18 + 1/18 + 1/18 + 1/18 = 6/18 =1/3`
