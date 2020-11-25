# Intro to Mathematical Modeling, Numerical Methods, and Problem Solving

In the world of engineering there are problems that appear that are difficult to comprehend on first glance. When trying to design solutions or make predictions about these systems it is advantageous to make mathematical models of these scenarios and use different mathematical methods to solve these problems. That is the gist of what this course covers.

---

## Mathematical Modeling

Setting up a proper mathematical model for a scenario is the key to solving for critical values. This may look like calculating the impact force of a falling object due to things like air resistance, or solving for the state of an electrical circuit after a given amount of time.

## Numerical Methods

Numerical methods come into play when the scenario that has been modeled is too complex/difficult to solve algebraically. Numerical methods can be implemented in this case to find numerical solutions to the questions with a certain amount of accuracy.

Numerical methods can be used to model the progression of a system throughout time, it may be to difficult to calculate the progression from the initial equation, and instead one may model a system by its initial state and progressing by multiplying its derivative by a time step

As an example

$$ {dT(t)\over dt}=-k(T-T_a) $$
$${y2-y1\over ∆t}=-k(T1-Ta)$$
$$y_2=y_1-k(T_1-T_a)\Delta T $$

The accuracy over time of this progression is called **Numerical Stability**
