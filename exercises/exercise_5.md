# Exercise 5 - dictionary and functions

In this exercise, you get to familiarize yourself with strings, file handling, error handling and strings. This exercise covers 10-11

## 0. Area (\*)

Create a function that takes the base and height of a triangle as input parameters and returns the area of the triangle.

## 1. Euclidean distance (\*)

The formula for Euclidean distance in 2D between $P: (p_1, p_2)$ and $Q: (q_1, q_2)$ is:

$d(P,Q) = \sqrt{(p_1-q_1)^2 + (p_2-q_2)^2}$

a) Create a function that takes two points as input parameters and return the Euclidean between them. (\*)

b) Let the user input two points. Call the function using the users input points. (\*)

c) Use your function to calculate distances between the origin (0, 0) and each of these points: (10, 3), (-1, -9), (10, -10), (4, -2), (9, -10). (\*)

---

## 2. Mathematical functions (\*)

Make the following functions with **def** or **lambda** and plot their graphs in the same figure window, with $x\in [-10,10]$ :

a) $f(x) = x^2 -3$ (\*)

b) $g(x) = 4x-7$ (\*)

What could the relation between $f(x)$ and $g(x)$ be?

---

## 3. Name cleaner (\*)

Create a function that takes a name as an input and:

- removes all leading and trailing blank spaces
- make capitalize the first character of each name, and make the rest lowercase

Use your function on this list of strings:

```
["  MaRcUs ", " iDA aNderSon", "OLOF Olofsson            "  ]
```

---

## 4. Change (\*\*)

Create a function that takes a value as input parameter and print out the banknotes and coins in Swedish currency representing this value. For example 5289 would give the following printout:

- 5st 1000-lapp
- 1st 200-lapp
- 1st 50-lapp
- 1st 20-lapp
- 1st 10-krona
- 1st 5-krona
- 2st 2-krona

Now let the user input a value, and use the function to calculate the change.

## 5. Curriculum (\*)

Create a dictionary containing all the courses that you will study in this program, with the course names as **keys** and the amount of points as **value**. Then calculate the number of points that you will study in total. (\*)

## 6. Dice simulation (\*)

Simulate 1000000 dice rolls and save the number of ones, twos, ..., sixes in a dictionary. Then print them out in the terminal. (\*)

## 7. Pokemon list (\*)

Read in the file pokemon_list.txt in Python. Create a variable with name pokedex with the key:value **"pokemon":"type, index"**. For example when searching for the keys "Gengar" and "Pikachu": (\*)

```python

print(pokedex["Gengar"])
print(pokedex["Pikachu"])

Spöke/Gift, 94
Elektrisk, 25
```

## 8. Morse code (\*\*)

Read in the file morse.txt, save it in a dictionary and create a function that lets the user input a message to get it translated to morse code. For example (\*\*)

```python

print(morse("SOS"))
print(morse("POKEMON"))
```

```
...---...
.------.-.------.
```

## 9. Theory

a) What is a function in Python, and why is it used?

b) Explain the difference between parameters and arguments.

c) What is the difference between \*args and \*\*kwargs in a function definition?

d) What is the difference between a regular function and a lambda function in Python?

e) Explain the purpose of the get() method. How is it different from accessing a key directly?

f) What is the difference between .keys(), .values(), and .items() methods?

g) Can dictionary keys be mutable types like lists or other dictionaries? Why or why not?

## Glossary

Fill in this table either by copying this into your own markdown file or copy it into a spreadsheet if you feel that is easier to work with.

| terminology          | explanation |
| -------------------- | ----------- |
| def                  |             |
| function call        |             |
| argument             |             |
| return statement     |             |
| parameter            |             |
| default parameter    |             |
| keyword arguments    |             |
| variable arguments   |             |
| positional arguments |             |
| lambda functions     |             |
| dict()               |             |
| get()                |             |
| items()              |             |
| in operator          |             |
| del                  |             |
| update()             |             |
