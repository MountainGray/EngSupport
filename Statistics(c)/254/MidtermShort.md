# Reference Sheet

### Rules and Equations

#### Addition Rule

The likeleyhood that either event $A$ **and/or** $B$ occurs.

$$P(A\ or\ B) = P(A)+P(B) -P(A\ and\ B)$$

**Note:** if $A$ and $B$ are Disjoint then $P(A\ and\ B)=0$

#### Multiplication Rule

##### For independant Processes

$$ P(A\ and\ B)=P(A) \times P(B)$$

**Note:** $A$ and $B$ must be two independant processes

##### General Rule

$$P(A\ and\ B) =P(A|B)\times P(B)$$

Note: This is for events that we believe are not independent, otherwise this is rearanged to the previous equation above

##### For Three Events

$$P(A\ and\ (B\ and\ C))=P(A|(B\ and\ C))\times P(B\ and\ C)$$

#### Complement Rule

For finding the probability of the complement of $A$, since total probability should sum to one

$$ P(A^C)=1-P(A) $$

#### Conditional Probability

The probability that $A$ occurs given $B$ has occured

$$P(A|B)={P(A\ and\ B) \over P(B)},\ \ \ P(B)\neq 0$$

#### Law of Total Probability

Suppose a sample space $\Omega$ is partitioned in 3 disjoint events $B_1,B_2,B_3$. Then for any event $A$

$$P(A)=P(A\ and\ B_1)+P(A\ and\ B_2)+P(A\ and\ B_3)$$
$$P(A)=P(A|B_1)P(B_1)+P(A|B_2)P(B_2)+P(A|B_3)P(B_3)$$

#### Sum of Conditional Probabilities

The sum of all conditional probabilitys should always equate to 1

$$P(A_1|B)+...+P(A_n|B)=1$$

#### Complement Rule for Conditional Probability

From equation above

$$P(A|B)=1-P(A^C|B)$$

#### Bayes' Theorem

The events $B_1,...,B_n$ form a partition of the sample space $\Omega$ if every sample point $\omega$ is in one and only one $B_i$. That is:

$$\Omega = \bigcup^n_{i=1}B_i$$

and $B_1,...,B_n$ are pairwise disjoint, that is to say the intersection of all pairs $B_i,B_j$ where $i\neq j$, is the empty set.

##### **To find $P(B_i|A)$**

1. Calculate
  $$P(A)=\sum^{n}_{i=1}P(A|B_i)P(B_i)$$
2. Then calculate $P(B_i|A)$ using
  $$P(B_i|A)={P(A|B_i)P(B_i)\over P(A)}$$

#### Expectation of a Random Variable

The sum of each outcome multiplied by its coorresponding probability

$$\mu =E(X)=x_1\cdot P(X=x_1)+...+X_k\cdot P(X=x_k)=\sum^k_{i=1}x_iP(X=x_i)$$

#### Variability of Random Variables

$$\sigma^2=Var(X)=\sum^k_{i=1}[x_i-E(X)]^2P(X=x_i)$$

##### Standard deviation

$$\sigma = \sqrt{\sigma^2}$$

#### Linear Combinations of Random Variables

For two independant variables

$$E(aX+bY)=a\cdot E(X)+b\cdot E(Y)$$

$$\sigma^2=Var(aX+bY)=a^2\times Var(X)+b^2\times Var(Y)$$
