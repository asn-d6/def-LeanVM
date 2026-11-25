# Knowledge soundness

From Chiesa and Yogev, Sections 5.1 and 7.1.

Knowledge soundness requires that there exists an efficient procedure, called the *extractor*,
that finds a witness from the argument prover (thereby demonstrating the malicious prover's
knowledge).

The definition below captures a flavor of knowledge soundness that is known as *straightline*,
because the extractor only needs information associated to a single execution of the argument
prover. In more detail, the extractor finds the witness given only the argument prover's output
and query-answer trace with the oracle (as well as the resulting query-answer trace of the
argument verifier).

**Definition 7.1.5 (straightline knowledge soundness).** A non-interactive argument
$\mathsf{NARG} = (\mathcal{P},\mathcal{V})$ for a relation $\mathcal{R}$ with oracle distribution
$\mathcal{D}$ has **straightline knowledge soundness error $\kappa_{\mathrm{ARG}}$ with extraction
time $\mathbf{et}_{\mathrm{ARG}}$** if there exists a probabilistic algorithm $\mathcal{E}$ (the
*extractor*) such that for every security parameter $\lambda \in \mathbb{N}$, instance size bound
$n \in \mathbb{N}$, query bound $t \in \mathbb{N}$, and $t$-query deterministic argument prover
$\tilde{\mathcal{P}}$,

```math
\Pr\left[
\begin{array}{l}
|x|_{\mathcal{R}} \leq n
\\ \land\; (x,w) \notin \mathcal{R}
\\ \land\; b=1
\end{array}
\;\middle\vert\;
\!\begin{array}{l}
\mathbf{f} \gets \mathcal{D}(\lambda,n)
\\ (x,\pi) \xleftarrow{\mathsf{tr}} \tilde{\mathcal{P}}^{\mathbf{f}}
\\ b \xleftarrow{\mathsf{tr}_{\mathcal{V}}} \mathcal{V}^{\mathbf{f}}(x,\pi)
\\ w \gets \mathcal{E}(x,\pi,\mathsf{tr},\mathsf{tr}_{\mathcal{V}})
\end{array}\!
\right]
\leq
\kappa_{\mathrm{ARG}}(\lambda,n,t)
\enspace.
```

Moreover, $\mathcal{E}$ runs in time $\mathbf{et}_{\mathrm{ARG}}(\lambda,n,t)$.

**Remark 7.1.9 (query bound).** The query bound $t$ for algorithms in the above definitions is an
upper bound on the *total* number of queries to any of the functions in the list $\mathbf{f}$
sampled from $\mathcal{D}(\lambda,n)$.

**Remark 5.1.4 (probabilistic provers).** The knowledge soundness definitions are stated for
*deterministic* provers for simplicity. These imply definitions for probabilistic provers. The
definition of *straightline* knowledge soundness for probabilistic argument provers
$\tilde{\mathcal{P}}$ is the same as in Definition 7.1.5 except that the execution
$(x,\pi) \xleftarrow{\mathsf{tr}} \tilde{\mathcal{P}}^{\mathbf{f}}$ in the experiment also takes
into account the randomness of $\tilde{\mathcal{P}}$. The knowledge error and extractor time
bounds for probabilistic provers are directly implied by the corresponding bounds for
deterministic provers.
