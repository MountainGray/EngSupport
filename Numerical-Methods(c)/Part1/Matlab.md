# Matlab

MATLAB or *Matrix laboratory* in.s a powerful engineering tool, with many various functions, these notes will leverage matlab to exicute numerical methods. I will not fully explain how to use matlab and its GUI, but I will document some syntax so that the code documented is understandable, and aspects of how matlab computes.

## General syntax

### ; vs ,

Both of these punctuations seperate individual statements, but the semicolon supresses the output, whereas the comma will output the  result of a statement at execution.

## Operators

### Math Operations

|Symbol | Function|
|:-: |:-: |
|+|Addition|
|-|Subtraction|
|.*|multiplication|
|./|right division|
|  ||
|||
|||
|||

### Matrix Operations

|Symbol | Function|
|:-: |:-: |
|*|Matrix Multiplication |
|^-1|Matrix inversion|
|`|Matrix Inversion|
|||
|||
|||
|||
|||

## Data Types

### Vectors

- line vectors

```matlab
a = [1, 2, 3]
```

- Row Vectors

```matlab
b=[1; 2; 3]
```

## Functions

zeros()

ones()

linspace(x1,x2,n): Create a vector with **n** evenly spaced values between x1 & x2

logspace(x1,x2,n): Create a vector with *logarithmically* spaced values between $10^{x1}$ to $10^{x2}$

### Creating a function

```matlab
function output = functionName(input)
    operation=input^2
    output=operation.*2
end
```

this creates a function that can be called

## Outputs + formating

Output to a textfile:

```matlab
save filename.txt variable -ascii -double
```

Output formatting

short:

Long

shortE
