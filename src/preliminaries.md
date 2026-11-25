# Preliminaries

From Chiesa and Yogev, Sections 1.1, 1.3 and 2.1.

## Relations

A relation $\mathcal{R}$ is a set consisting of instance-witness pairs $(x, w)$. We write
$\lvert x \rvert_{\mathcal{R}}$ to denote the size of an instance; this could be the number of
bits to describe $x$ (namely, $`\mathrm{len}(x)`$) or some other measure suitable for instances
of the relation $\mathcal{R}$ (hence the relation subscript in the notation).

## Sampling

We denote by $a \gets D$ the process of sampling $a$ according to the distribution $D$.
Similarly, given a finite set $S$, we denote by $a \gets S$ the process of sampling $a$ according
to the uniform distribution over $S$.

## Probabilistic experiments

We introduce notation for defining random variables and events over these.

We write

```math
\left\{ x \;\middle\vert\; x \gets A \right\}
```

to denote the random variable that consists of the string $x$ sampled according to the
probabilistic algorithm $A$.

We write

```math
\Pr\left[ f(x)=1 \;\middle\vert\; x \gets A \right]
```

to denote the probability of the event that $f(x)=1$ when $x$ is sampled according to the
probabilistic algorithm $A$, for a given boolean function $f$.

We write

```math
\Pr\left[ D(x)=1 \;\middle\vert\; x \gets A \right]
```

to denote the probability of the event that $D(x)=1$ when $x$ is sampled according to the
probabilistic algorithm $A$, for a given probabilistic algorithm $D$. In this case the
probability is over the randomness of both $A$ and $D$.

Sometimes we implicitly define the algorithm $A$ or the boolean function *within the expression
itself*, by using pseudocode and logical expressions. For example, we can write

```math
\left\{
(y,z)
\;\middle\vert\;
\!\begin{array}{l}
y \gets B
\\ z \gets C(y)
\end{array}\!
\right\}
```

to denote the random variable $x := (y,z)$ that is obtained by the algorithm $A$ that samples $y$
according to $B$, samples $z$ according to $C$ on input $y$, and outputs the pair $(y,z)$. We can
also write

```math
\Pr\left[
y=z
\;\middle\vert\;
\!\begin{array}{l}
y \gets B
\\ z \gets C(y)
\end{array}\!
\right]
```

to denote the probability that the random variable $x = (y,z)$ sampled as above is such that
$f(x)=1$ where $f$ is the boolean function that given a pair $x=(y,z)$ outputs $1$ if and only if
$y=z$.

## Oracle algorithms

We consider algorithms that are granted *query access* to an oracle $f$. In more detail, an
oracle algorithm is an algorithm that, in addition to an input, receives query access to an
oracle, which it can query any number of times via a special operation. The operation consists of
specifying an input for the oracle (a *query*) and in the following computational step receiving
the corresponding oracle output (an *answer*). An oracle algorithm may be deterministic or
probabilistic (it has the ability to use randomness separately from any random answers from the
oracle itself).

For an algorithm $A$, oracle $f$, and input $a$, we use the notation

```math
b \gets A^{f}(a)
```

to denote the fact that $A$, given query access to $f$ and given input $a$, outputs $b$; note
that $b$ may be a random variable if $A$ is probabilistic (i.e., if $A$ has its own private
randomness).

For $t \in \mathbb{N}$, an oracle algorithm $A$ is $t$-query if $A$ makes at most $t$ queries
(regardless of the answers that it receives from the oracle).

## Query-answer traces

Sometimes we analyze the *query-answer trace* between an algorithm $A$ and an oracle $f$. We use
the notation

```math
b \xleftarrow{\mathsf{tr}} A^{f}(a)
```

to denote the fact that $\mathsf{tr}$ is the ordered list of query-answer pairs made/received by
the algorithm $A$ on input $a$; note that $\mathsf{tr}$ is a random variable if the algorithm $A$
is probabilistic. We denote by $\lvert \mathsf{tr} \rvert$ the number of query-answer pairs in the
trace $\mathsf{tr}$.
