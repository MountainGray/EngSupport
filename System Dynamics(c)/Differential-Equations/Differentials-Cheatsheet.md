# Differentials Cheat Sheet

Overview

* Identification
* First Order Solutions
* Second Order Diff Solutions

---

## First Order ODE

Convert equations from the form

$a_1(t){d(y(t))\over dt}+a_0(t)y(t)=f(t)$ 

to

${d(y(t))\over dt}+ {a_0(t)\over a_1(t)}y(t)={f(t)\over a_1(t)}$

then define the equation as

${d(y(t))\over dt}+p(t)y(t)=q(t)$

### Homogeneous Linear First Order ODE's

${d(y(t))\over dt}+p(t)y(t)=0$

Separate variables

${d(y(t))\over dt}=-p(t)y(t)$

${d(y(t))\over y(t)}=-p(t)dt$

Integrate

$ln|y(t)|+C = -\int p(t)dt$

$|y(t)|=Be^{-\int p(t)dt}$

$y(t)=Ae^{-\int p(t)dt}$

## General Solutions to Non-homogeneous Linear First Order ODE's

### Integrating Factor

${d(y(t))\over dt}+p(t)y(t)=q(t)$

Multiply both sides by an integrating factor $\sigma (t)$

$\sigma (t){d(y(t))\over dt}+\sigma (t)p(t)y(t)=\sigma(t)q(t)$

Why am i doing this? To make the output a chain rule, so the solution to the ODE can be given by

${d(\sigma (t)y(t))\over dt}=\sigma (t)q(t)$

$\sigma (t)y(t)=\int \sigma (t)q(t)dt+C$

$y(t)={\int \sigma (t)q(t)dt+C\over \sigma(t)}$

#### Summarized

the apparent 'Two' methods

One

1. Convert the ODE into the standard form
2. Identify $p(t)$ and $q(t)$ .
3. Calculate $\sigma(t)$ .
4. Substitute $\sigma(t)$ into the general solution.
5. Calculate $\sigma(t)q(t)dt$
6. Assemble the full solution.
7. Solve for initial conditions if given.

Two

1. Convert the ODE into the standard form
2. Identify $p(t)$ and $q(t)$.
3. Calculate $\sigma(t)$.
4. Substitute $\sigma(t)$ into $d(\sigma(t)y(t))=\sigma(t)q(t)dt$ and solve the ODE.
5. Solve for initial conditions if given

### IVP's

To solve for the constants of solutions to differential equations, you must use a known initial value
    Essentially plug and solve

## Non-linear First Order ODEs

These are generally harder to solve, there are a few specific exceptions

### Separable First Order ODEs

The first order derivatives must be equal to a function of x multiplied by a function of y

${dy(x)\over dx}=X(x)Y(y)$

This style of equation can be solved by

$\int{dy(x)\over Y(y)}=\int X(x)dx$

(this may create another non solvable equation)

### First Order ODEs Containing Homogeneous Functions

Homogeneous functions are functions where all variables can be multiplied by a constant without changing the equation ie. the constants must cancel out

$f(x,y)=f(\lambda x,lambda y)$

They have a degree ex

$f(\lambda x,lambda y)=\lambda^n f(x,y)$

1. Convert the ODE into the standard form ${dy\over dx}=f(x,y)$
2. Check to see if $f(x,y)$ is a homogeneous function i.e. $f(x,y)=f(\lambda x, \lambda y)$
3. Make the substitution $u={y\over x}$
4. Solve the ODE ${dx\over x}={du\over f(u)-u}$
5. Substitute $y$ back in using $u={y\over x}$
6. Solve for any initial conditions you may have been given

### Bernoulli Equations

Bernoulli Equations have an exact solution, for equations in the form

${dy(x)\over dx}+ p(x)y(x)=q(x)y^n(x)$ (Bernoulli if $n\neq 1,0$)

First divide both sides by $y^n$

$y^{-n}(x){dy(x)\over dx}+{p{x}\over y^{n-1}(x)=q(x)}$

Then use change of variables to convert to linear ODE

$u(x)={1\over y^{n-1}(x)}=y^{1-n}(x)$

${du(x)\over dy(x)}=(1-n)y^{-n}(x)$

$y^{-n}(x)d(y(x))={d(u(x))\over (1-n)}$

${1\over 1-n}{d(u(x))\over dx}+u(x)p(x)=q(x)$

${d(u(x))\over dx}+(n-1)u(x)p(x)=(n-1)q(x)$

The equation should now be solvable by integrating factor method

Finally substitute $u(x)=y^{1-n}$ to find a solution for $y$

## Second Order ODE's



