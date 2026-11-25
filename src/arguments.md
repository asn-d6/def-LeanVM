# Non-interactive arguments

From Chiesa and Yogev, Sections 4.1 and 7.1.

A *non-interactive argument* (NARG) is a tuple

```math
\mathsf{NARG} = (\mathcal{P},\mathcal{V})
```

where $\mathcal{P}$ is an oracle algorithm known as the *argument prover* and $\mathcal{V}$ is an
oracle algorithm known as the *argument verifier*.

The argument prover $\mathcal{P}$ receives as input an instance $x$ and witness $w$, and outputs
an argument string $\pi$. The argument verifier $\mathcal{V}$ receives as input the instance $x$
and argument string $\pi$, and outputs a bit denoting whether to accept (the bit is $1$) or
reject (the bit is $0$).

## Oracle setting

We provide security definitions for non-interactive arguments in a general oracle setting, which
is specified by a collection $\mathcal{D}$ of oracle distributions. In the $\mathcal{D}$-oracle
setting all parties receive oracle access to a list of functions $\mathbf{f}$ sampled from the
distribution $\mathcal{D}(\lambda,n)$, where $\lambda \in \mathbb{N}$ is the security parameter
and $n \in \mathbb{N}$ is the instance size bound. Both parameters are known to the argument
prover and argument verifier as well as to any malicious party, but we suppress them as inputs to
parties to simplify notation.

**Definition 7.1.1 (oracle distribution).** An **oracle distribution $\mathcal{D}$** receives as
input a security parameter $\lambda \in \mathbb{N}$ and an instance size bound
$n \in \mathbb{N}$ and samples a list of functions $\mathbf{f}$. A non-interactive argument
$\mathsf{NARG} = (\mathcal{P},\mathcal{V})$ for a relation $\mathcal{R}$ has **oracle
distribution $\mathcal{D}$** if the argument prover $\mathcal{P}$ and argument verifier
$\mathcal{V}$ have query access to oracles sampled from $\mathcal{D}(\lambda,n)$, when using
security parameter $\lambda$ and instances $x$ with $\lvert x \rvert_{\mathcal{R}} \leq n$.

**Random permutation (not in the book).** For a finite set $S$, the random permutation oracle
distribution samples a permutation $p$ of $S$ uniformly at random. The list of functions is
$\mathbf{f} = (p, p^{-1})$.

## Completeness

**Definition (completeness error; not in the book).** A non-interactive argument
$\mathsf{NARG} = (\mathcal{P},\mathcal{V})$ for a relation $\mathcal{R}$ with oracle distribution
$\mathcal{D}$ has **completeness error** $c_{\mathrm{ARG}}$ if for every security parameter
$\lambda \in \mathbb{N}$, instance size bound $n \in \mathbb{N}$, and instance-witness pair
$(x, w) \in \mathcal{R}$ with $\lvert x \rvert_{\mathcal{R}} \leq n$,

```math
\Pr\left[
\mathcal{V}^{\mathbf{f}}(x,\pi)=1
\;\middle\vert\;
\!\begin{array}{l}
\mathbf{f} \gets \mathcal{D}(\lambda,n)
\\ \pi \gets \mathcal{P}^{\mathbf{f}}(x,w)
\end{array}\!
\right]
\geq
1 - c_{\mathrm{ARG}}(\lambda,n)
\enspace.
```

This is Definition 7.1.2 of the book with an error. The (perfect) completeness of the book is
completeness error $0$.
