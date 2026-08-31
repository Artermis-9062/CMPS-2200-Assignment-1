# CMPS 2200 Assignment 01

## Answers

**Name:** Chuong Hoang Pham

Place all written answers from `assignment-01.md` here for easier grading.

1. **Asymptotic notation**

- 1a (2 pts): Yes. Because, $2^{n+1} = 2 \cdot 2^{n}.$ There exists $c,  2 \cdot 2^{n} \leq c \cdot 2^n \iff c \geq 2.$

- 1b (2 pts): No. Because,
  $$ \lim_{x \to \infty} \frac{2^{2^n}}{2^n} = \lim_{x \to \infty} 2^{2^n-n} = \infty $$
$$ \Rightarrow 2^{2^n} \notin O(2^n)$$

- 1c (2 pts): No. Because
  $$ \lim_{x \to \infty} \frac{n^1.01}{\log ^{2} n} = \lim_{x \to \infty} \frac{1.01n^{0.01}}{\frac{2 \log n}{n}} = \lim\_{x \to \infty} \frac{1.0201n^0.01}{\frac{2}{n}} = \infty $$
$$ \Rightarrow n^{1.01} \notin O(\log^{2} n)$$

- 1d (2 pts): Yes. Because,
  $$ \lim_{x \to \infty} \frac{n^1.01}{\log ^{2} n} = \lim_{x \to \infty} \frac{1.01n^{0.01}}{\frac{2 \log n}{\ln(10) \cdot n}} = \lim\_{x \to \infty} \frac{\ln(10) \cdot 1.0201n^{0.01}}{\frac{2}{\ln(10) \cdot n}} = \infty $$
$$ \Rightarrow n^{1.01} \in \Omega(\log^{2} n)$$

- 1e (2 pts): No. Because,
  $$ \lim_{x \to \infty} \frac{\sqrt n}{\ln ^{3} n} = \lim_{x \to \infty} \frac{0.5x^{-0.5}}{\frac{3 \ln^{2} n}{n}} = \lim_{x \to \infty} \frac{0.25n^{-0.5}}{\frac{6 \ln n}{n}} = \lim_{x \to \infty} \frac{0.125n^{-0.5}}{\frac{6}{n}} = \infty $$
$$ \Rightarrow \sqrt n \notin O(\log^{2} n)$$

- 1f (2 pts): Yes. Because,
  $$ \lim_{x \to \infty} \frac{\sqrt n}{\ln ^{3} n} = \lim_{x \to \infty} \frac{0.5x^{-0.5}}{\frac{3 \ln^{2} n}{n}} = \lim_{x \to \infty} \frac{0.25n^{-0.5}}{\frac{6 \ln n}{n}} = \lim_{x \to \infty} \frac{0.125n^{-0.5}}{\frac{6}{n}} = \infty $$
$$ \Rightarrow \sqrt n \in \Omega(\log^{2} n)$$

- 1g (2 pts):

Let $f(n)$ is an element in $o(g(n)) \cap \omega(g(n))$. Therefore, by the property of $o(g(n)$ and $\omega(g(n))$, we have:
$$ f(n) < c_1 \cdot g(n), \hspace*{1cm} \forall c_1 \in \mathbb{R}, n \geq n_0 $$
Let $c_1 = 0.5$
$$ f(n) > c_2 \cdot g(n), \hspace*{1cm} \forall c_2 \in \mathbb{R}, n \geq n_1 $$
Let $c_2 = 3$

This is equivalent:
$$ 3 \cdot g(n) < f(n) < 0.5 \cdot g(n) \iff 3 \cdot g(n) < 0.5 \cdot g(n) \iff 3 < 0.5 $$
, which is a contradiction.

Therefore, $o(g(n)) \cap \omega(g(n)) = \empty$

2. **SPARC to Python**

- 2b (3 pts): It returns $n^{th}$ number in Fibonacci sequence

3. **Parallelism and recursion**

- 3b (4 pts): For every for iteration, it costs 6 operations (include checking, and assigning - time complexity $O(1)). These operations are implemented for $n$ times, which leads to the final
  - $\textbf{Work: } O(n)$
  - $\textbf{Span} \text{ (Cannot be parallelized): } O(n)$

- 3d (4 pts):
  - $\textbf{Work: } O(n)$
  - $\textbf{Span: } O(n)$

- 3e (5 pts):
  - $\textbf{Work: } O(n)$
  - $\textbf{Span: } O(\log n)$
