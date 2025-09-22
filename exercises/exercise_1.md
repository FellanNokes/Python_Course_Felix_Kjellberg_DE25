# Exercise 1 - Count with python

In this exercise, you get to familiarize yourself with fundamental Python. This exercise covers lectures 04 in the course.

## 0. Pythagorean theorem (*)

a) A right angled triangle has the catheti: a = 3 and b = 4 length units. Compute the hypothenuse of the triangle. (\*)

b) A right angled triangle has hypothenuse c = 7.0 and a cathetus a = 5.0 length units. Compute the other cathetus and round to one decimal. (\*)

## 1. Classification accuracy (\*)

A machine learning algorithm has been trained to predict whether or not it would rain the next day. Out of 365 predictions, it got 300 correct, compute the accuracy of this model.

## 2. Classification accuracy (\*)

A machine learning model has been trained to detect fire. Here is the result of its predictions:

<table>
<tbody>
  <tr>
    <td>True Positive (TP)
      <ul>
        <li>Reality: fire</li>
        <li>Predicted: fire</li>
        <li>Number of TP: 2</li>
      </ul>
    </td>
    <td>False Positive (FP)
      <ul>
        <li>Reality: no fire</li>
        <li>Predicted: fire</li>
        <li>Number of FP: 2</li>
      </ul>
    </td>
  </tr>

  <tr>
    <td>False Negative (FN)
      <ul>
        <li>Reality: fire</li>
        <li>Predicted: no fire</li>
        <li>Number of FN: 11</li>
      </ul>
    </td>
    <td>True Negative (TN)
      <ul>
        <li>Reality: no fire</li>
        <li>Predicted: no fire</li>
        <li>Number of TN: 985</li>
      </ul>
    </td>
  </tr>
</tbody>
</table>

Calculated the accuracy using the following formula:

$\text{accuracy} = \frac{TP+TN}{TP+TN+FP+FN}$

Is this a good model? Why? Why not?

## 3. File metadata - format print (*)

There is a file with the following metadata:

- name: orders_data.csv
- file size: 3.14mb
- modified 2024

Create variables for each of them and print out the following to the screen

```
=== File metadata ===
Filename: sales_data.csv
Size (MB): 24.7
Last Modified Year: 2023
```

## 4. Unit converter - inch to cm (*)

Screen sizes are defined using inches for example my computer has 15'' and it corresponds to the diagonal of the screen. Let the user type in a value in inches and output the result in centimeters.

## 5. Count characters in a text (*)

Create a program to let a user input a text, count the number of characters and print it out to the screen. Space can also be counted as a character here.

Hint: `len()` function

## 6. Data types (*)

Create variables of type bool, int, float, str and list. Then use `type` function and check each variables type.

```
radius = 5 has type <class 'int'>
PI = 3.1415 has type <class 'float'>
cool_subject = 'math' has type <class 'str'>
is_cool = True has type <class 'bool'>
numbers = [1, 2, 41, 2] has type <class 'list'>
```

## 7. Theory

a) What is the difference between input() and print() in Python?

input() is where user can input something to the program
print() is where the program outputs something to the use

b) What data type does the input() function return by default? How can you use it to get numeric input?

by default input() returns a string, by specifying which type of data you want before like this int(input("insert number"))

c) Explain how formatted string literals (f-strings) improve readability in output statements. Give an example.

You can add data to the print message for example (print(f"you have entered this {number} number"))

d) Can a variable change its data type during runtime in Python? Show an example.

yes, if we have pi = 3.14 its a float but if i type pi = str(pi) its now a string

e) What does it mean that Python is "dynamically typed"? How is that different from statically typed languages?

it means that variables are determined and check during runtime rather then durning compilation. You dont have to declare which type it is either. I can just type pi = 3.14 and it knows it's a float.

## Glossary

Fill in this table either by copying this into your own markdown file or copy it into a spreadsheet if you feel that is easier to work with.

| terminology       | explanation |
| ----------------- | ----------- |
| data type         |classification of data thats specifies the kind of value a variable can hold|
| variable          |A container that holds a value|
| assignment        |Assigning a value to a variable|
| dynamically typed |Determining data type at runtime rather then during compilation|
| input             |data a user inputs to the program|
| output            |data that the programs output|
| type casting      |used to change data types of variables|
| boolean           |Data type that is either true or false|
| string            |A data type that contains a bunch of characters|
| f-string          |Allows you to format obejcts into strings|
| indentation       |Allows the programmer to run the code in diffrent blocks, also increases readabillity|
| convention        |rules and guidelines for naming variables, functions and classes to increase readabillity|
|                   |             |
