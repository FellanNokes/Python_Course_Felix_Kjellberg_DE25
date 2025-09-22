# Exercise 3 - sequences

In this exercise, you get to familiarize yourself with sequences in Python.

## 0. Dice rolls (\*)

Simulate 10 dice rolls and **append** the rolls to a list. Do this once again but now use **list comprehension** instead to create the list.

a) sort the list in **ascending** order (\*)

b) sort the list in **descending** order (\*)

c) find the **maximum** and **minimum** value in the list (\*)

d) calculate the **mean** (average) of the list (\*)

e) find the **median** of the list (\*)

f) extract only the unique values from the list. The output should be a list (\*)

## 1. Food menu (\*)

Create a:

a) **list** with the following elements: "vegetarian lasagna", "spaghetti", "fish", "soup", "pancakes". (\*)

b) **list** with the weekdays (\*)

c) create a food menu with each day corresponding to each food item and print it out like this (\*)

```bash
Day        Food
-----------------
Monday     vegetarian lasagna
Tuesday    spaghetti
Wednesday  fish
Thursday   soup
Friday     pancakes
```

## 2. Squares (\*)

a) Use **list comprehension** to create a list of squares from -10 to 10 (\*)

b) Plot this list using **matplotlib**. (\*)

## 3. Chessboard (\*\*)

a) Create this list using **list comprehension**: (\*)

```python
['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1']
```

b) Create a 2D list to hold the coordinates in a chessboard like this (\*\*)

```
[[A1, B1, C1, D1, E1, F1, G1, H1],
 [A2, B2, C2, D2, E2, F2, G2, H2],
 [A3, B3, C3, D3, E3, F3, G3, H3],
 [A4, B4, C4, D4, E4, F4, G4, H4],
 [A5, B5, C5, D5, E5, F5, G5, H5],
 [A6, B6, C6, D6, E6, F6, G6, H6],
 [A7, B7, C7, D7, E7, F7, G7, H7],
 [A8, B8, C8, D8, E8, F8, G8 ,H8]]
```

c) Instead of lists use tuples to hold the coordinates in a chessboard like this (\*\*)

```
(("A",1),("B",1),("C",1),("D",1),("E",1),("F",1),("G",1),("H",1)),
(("A",2),("B",2),("C",2),("D",2),("E",2),("F",2),("G",2),("H",2)),
(("A",3),("B",3),("C",3),("D",3),("E",3),("F",3),("G",3),("H",3)),
(("A",4),("B",4),("C",4),("D",4),("E",4),("F",4),("G",4),("H",4)),
(("A",5),("B",5),("C",5),("D",5),("E",5),("F",5),("G",5),("H",5)),
(("A",6),("B",6),("C",6),("D",6),("E",6),("F",6),("G",6),("H",6)),
(("A",7),("B",7),("C",7),("D",7),("E",7),("F",7),("G",7),("H",7)),
(("A",8),("B",8),("C",8),("D",8),("E",8),("F",8),("G",8),("H",8))
```

## 4. Dice rolls convergence (\*\*)

Simulate:

a) 100 dice rolls and count the number of outcome six. (\*)

b) 10, 100, 1000, 10000, 100000, 1000000 dice rolls. Count the number of outcome six in each simulation and store it in a list. Compute the probability of outcome six in each simulation. (\*\*)

c) Use matplotlib to plot this list. (\*)

## 5. Monte Carlo simulation (\*\*\*)

a) Simulate 5000 uniformly distributed points between -1 and 1, $X\sim U(-1,1)$. Now calculate the Euclidean distances between each point and the origin (0,0), $d_i = \sqrt{x_i^2 + y_i^2}$. For $d_i < 1$ plot the point with one color, and for $d_i > 1$ plot the point in another color, $i = \{1,\ldots, 5000\}$. (\*\*)

b) Calculate the fraction between number of inner points and number of outer points. What do you this will converge to when number of points reaches infinity? (\*\*)

## 6. A cute rabbit among two ferocious snakes (\*\*\*)

There are three identical doors, behind two of them, there are ferocious snakes and behind one of them is a cute little rabbit. Your aim is to pick a door and get the cute rabbit. You start picking one door randomly and suddenly another door opens and snake slithers away _pssss_. Now you have a choice to either stay with your door or change to the remaining door.

<img src="https://github.com/kokchun/assets/blob/main/python/snakes_rabbits.png?raw=true" width = 200>

a) What is your choice and why? (\*\*)

b) Randomly assign which door has the rabbit, and randomly pick an initial door. Now simulate 10, 100, 1000, 10000, 100000, 1000000 times for staying and for switching doors. Calculate the proportion of finding the rabbits for each set of simulations. Plot the results (\*\*)

## 7. Theory

a) What is a sequence in Python? Give examples of sequence types.

b) What is the difference between a list and a tuple?

c) How does indexing work in Python sequences? What happens if you use a negative index?

d) How does Python handle out-of-range indices in slicing vs indexing?

e) Which of the following sequence types are mutable: list, tuple, str, range?

f) What is sequence unpacking? Provide an example.

g) What are some common use cases for enumerate() and zip() when working with sequences?

h) What is the difference between sorted() and .sort() in lists?

## Glossary

Fill in this table either by copying this into your own markdown file or copy it into a spreadsheet if you feel that is easier to work with.

| terminology     | explanation |
| --------------- | ----------- |
| sequence        |             |
| list            |             |
| tuple           |             |
| set             |             |
| range           |             |
| indexing        |             |
| slicing         |             |
| comprehension   |             |
| zip             |             |
| enumermate      |             |
| unpacking       |             |
| membership test |             |
|                 |             |
