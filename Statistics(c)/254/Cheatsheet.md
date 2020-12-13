# Reference Sheet

## Probability

### Addition Rule

The likelihood that either event $A$ **and/or** $B$ occurs.

$$P(A\ or\ B) = P(A)+P(B) -P(A\ and\ B)$$

**Note:** if $A$ and $B$ are Disjoint then $P(A\ and\ B)=0$

### Multiplication Rule

For _Independent_ Processes

$$ P(A\ and\ B)=P(A) \times P(B)$$

General Rule for *both* dependant and independend processes

$$P(A\ and\ B) =P(A|B)\times P(B)$$

For Three Events

$$P(A\ and\ (B\ and\ C))=P(A|(B\ and\ C))\times P(B\ and\ C)$$

### Complement Rule

$$ P(A^C)=1-P(A) $$

### Conditional Probability

The probability that $A$ occurs given $B$ has occurred

$P(A|B)={P(A\ and\ B) \over P(B)}, \ \ \ P(B)\neq 0$$

### Law of Total Probability

Suppose a sample space $\Omega$ is partitioned in 3 disjoint events $B_1,B_2,B_3$. Then for any event $A$

$$P(A)=P(A\ and\ B_1)+P(A\ and\ B_2)+P(A\ and\ B_3)$$
$$P(A)=P(A|B_1)P(B_1)+P(A|B_2)P(B_2)+P(A|B_3)P(B_3)$$

### Sum of Conditional Probabilities

$$P(A_1|B)+...+P(A_n|B)=1$$

### Complement Rule for Conditional Probability

$$P(A|B)=1-P(A^C|B)$$

### Bayes' Theorem

$$P(B|A)={P(A|B) P(B)\over P(A)}$$

### **To find $P(B_i|A)$**

1. Calculate
   $$P(A)=\sum^{n}_{i=1}P(A|B_i)P(B_i)$$
2. Then calculate $P(B_i|A)$ using
   $$P(B_i|A)={P(A|B_i)P(B_i)\over P(A)}$$

## Random Variables

### Expectation of a Random Variable

The sum of each outcome multiplied by its coorresponding probability

$$\mu =E(X)=x_1\cdot P(X=x_1)+...+X_k\cdot P(X=x_k)=\sum^k_{i=1}x_iP(X=x_i)$$

### Variability of Random Variables

$$\sigma^2=Var(X)=\sum^k_{i=1}[x_i-E(X)]^2P(X=x_i)$$

#### Standard deviation

$$\sigma = \sqrt{\sigma^2}$$

### Linear Combinations of Random Variables

For two independant variables

$$E(aX+bY)=a\cdot E(X)+b\cdot E(Y)$$

$$\sigma^2=Var(aX+bY)=a^2\times Var(X)+b^2\times Var(Y)$$

## Probability Distributions

### Normal Distributions

$N(\mu , \sigma)$ : $\mu$ = mean of the distribution, $\sigma$ = standard deviation.

#### Z Scores

$$Z={x-\mu \over \sigma}={observation - mean \over SD}$$

#### Comparing Data to Normal Distribution

$$p_i={i-0.5\over n}$$

$p_i$ evaluates to a probability, you then use this value to calculate the Z Score of each data point and plot data point vs Z value, the closer to a linear distribution the data is, the more linear the data plot is.

### Bernoulli Trial

with two possible outcomes (success and failure)

$p=P($success on one trial$)$

$q=1-p=P($failure on one trial$)$

#### Bernoulli Random Variable

$P(X=1)=p$ <- Pass

$P(X=0)=q$ <- Fail

#### Geometric Distributions

If W is the waiting time for first success, which is the number of the trial on which the first success appeared

$$P(W=i)=q^{i-1}\cdot p$$

For $i=1,2,3,...$

$$E(W)=\mu ={1\over p}$$

$$\sigma = \sqrt{1-p\over p^2}$$

### Combinatorics

#### Rule 1: Multiplication

For a set of events where:

- Event 1 can be $n_1$ options
- Event 2 can be $n_2$ options
- $...$
  - Event $k$ can be $n_k$ options

The total number of combinations of each event is

$k=n_1\cdot n_2\cdot ... \cdot n_k$

#### Rule 2: Permutations

The number of permutations of a set defines the number of unique combinations of length $k$ including unique orders that the set $n$ can create

$$(n)_k=n(n-1)(n-2)...(n-k+1)$$

if k=n then

$$(n)_n=n!$$

#### Rule 3: Combinations

The number of combinations is defined as the number of unique unordered subsets of a set, this can also be viewed as number of permutations regardless of order

$$(^n_k)={(n)_k\over k}={n!\over k!(n-k)!}$$

## Foundations of Inference

The distribution of a **sample mean** is well approximated by a normal distribution if: the events are independent, and the sample size is appropriate

$\bar{x}\approx N(\mu , {\sigma \over \sqrt{n}})$

${\sigma \over \sqrt{n}}$ is the standard error or $SE$

### Confidence Intervals

$\bar{x}\pm Z^*\times SE= ({x_1},{x_2})$ Z is the 'Z score' we want to get (% likely within from table)

|Confidence Coefficient (1-$\alpha$)|$\alpha$|$\alpha \over 2$|$Z_{\alpha \over 2}$|
|:-:|:---:|:---:|:--:|:---:|
|0.90|0.1|0.05|1.645|
|0.95|0.05|0.025|1.96|
|0.98|0.2|0.01|2.33|
|0.99|0.01|0.005|2.58|

### Margin of Error

$Z^*\times SE$ is the **Margin of error**

### p-value

to find p-value you must first find the # of Standard Error away from the sample mean the null hypothesis is

$Z={\bar{x}-\mu_{0} \over SE}={\bar{x}-\mu_{0} \over {s/\sqrt{n}}}$ (s - sample variance, SE - Sample Error, n - sample size)

The p(x) is then calculated by looking at the table and finding the corresponding % chance that this variable would be observed

## linear Regression

$y = \beta_0+\beta_1 x +\in$

Model perameters=$\beta_0, \beta_1$ Explanatory variable: $x$ Response variable: $y$ Error: $\in$

$\beta_1={S_y\over S_x}R$

$\beta_0=\bar{y}-\beta_1\bar{x}$

Required: Sample mean $\bar{x}$ and $\bar{y}$, Stdv x and y

### Residuals

$e_i=y_i-\hat{y_i}$

Residual: e_i, Measured value: $y_i$, Predicted value: $\hat{y_i}$

### Correlation

$R={1\over n-1}\sum^{n}_{i=1}{x_i-\bar{x}\over s_x}{y_i-\bar{y}\over s_y}$

-1 neg lin association, 1 = pos lin association, 0= no linear association

$R^2$ is just above squared

