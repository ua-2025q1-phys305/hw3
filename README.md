# PHYS305 Homework Set #3

Welcome to the repository for **Homework Set #3** in PHYS305.
This homework set is worth **10 points** and is designed to test your
understanding of topics that we've covered.
The submission cutoff time is at **Tuesday Mar 20th, 11:59pm** Arizona
time.


## Structure and Grading

This homework set consists of **five assignments**, each contributing
equally to your overall grade.
The grading breakdown is as follows:

1. **Automated Evaluation (50%)**:
   * Each assignment will be graded using `pytest`, an automated
     testing framework.
   * The correctness of your solutions accounts for 1 point per
     assignment (5 points in total).
   * You can run `pytest` in GitHub Codespaces or your local
     development environment to verify your solutions before
     submission.

2. **Documentation and Coding Practices (50%)**:
   * The remaining 1 point per assignment (5 points total) will be
     based on documentation and coding practices.
   * Clear and concise **documentation** of your code, including
     meaningful comments.
   * Adherence to good **coding practices**, such as proper variable
     naming, modular design, and code readability.

By following the interface and prototypes provided in each assignment
template, you can ensure compatibility with the autograding system and
maximize your score.


## Assignments

### **Assignment 1**: Generate Synthetic Radioactive Decay Data (2 points)

* **Objective**:
  Implement a function that generates synthetic radioactive decay
  count data given "true" values for the decay constant $\lambda$,
  detector calibration factor $\alpha$, and a fixed background $b$.

* **Details**:
  * Write a function `datagen(lambda_true, alpha_true, b, N0, dt,
    times, rng)` that returns:
    1. An array of times `ts`.
    2. An array of observed counts `Cts` drawn from the Poisson distribution.
    3. The corresponding "true means" (the Poisson parameters) for reference.
  * Assume the model:
    $C_t \sim \mathrm{Poisson}\left(\mu_t\right),
    \mu_t = \Delta t \left[\alpha \lambda N_0 e^{-\lambda t} + b\right]$.
  * Use `demo/vis.ipynb` to show that the data looks reasonable (e.g.,
    a decreasing count rate over time plus some constant offset from
    background).
  * The code should be placed in `src/phys305_hw3/a1.py`.

### **Assignment 2**: Define Priors for $\lambda$ and $\alpha$ (2 points)

* **Objective**:
  Choose and implement prior probability density functions (PDFs) for
  the two unknown parameters $\lambda$ and $\alpha$.

* **Details**:
  * Use a **Gamma** prior for $\lambda$, e.g. $\lambda \sim
    \mathrm{Gamma}(\alpha_\lambda, \beta_\lambda)$.
  * Use a **LogNormal** prior for $\alpha$, e.g. $\alpha \sim
    \mathrm{LogNormal}(\mu_\alpha, \sigma_\alpha^2)$.
  * Write functions `prior0_lambda(lambda)` and `prior0_alpha(alpha)`
    that each return PDF values. They should properly handle invalid
    parameter values (e.g., $\lambda \le 0$).
  * Use `demo/vis.ipynb` to show that these priors behave as expected
    (e.g., strictly positive for $\lambda,\alpha$).
  * The code should be placed in `src/phys305_hw3/a2.py`.

### **Assignment 3**: Implement the Poisson Likelihood (2 points)

* **Objective**:
  Given the counts $\{C_t\}$, times $\{t\}$, and fixed $b$, implement
  the Poisson likelihood for parameters $\lambda$ and $\alpha$.

* **Details**:
  * Write a function `likelihood(lmbda, alpha, counts, times, dt, N0,
    b)` that computes: $\prod_{t} \mathrm{Poisson}\left(C_t \mid
    \mu_t(\lambda,\alpha)\right)$.
    Note that `lambda` is a python keyword so we spell our variable as
    `lmbda`.
  * Handle the case where $\mu_t \le 0$ (the likelihood should be
    zero).
  * Return the **product** of probabilities, or use a log-likelihood
    internally for numerical stability.
  * Use `demo/vis.ipynb` to confirm the function behaves properly for
    a few known scenarios or parameter values.
  * The code should be placed in `src/phys305_hw3/a3.py`.

### **Assignment 4**: Construct the 2D Posterior on a Grid (2 points)

* **Objective**:
  Combine the priors (Assignment 2) and the likelihood (Assignment 3)
  to build the **unnormalized posterior** and discretize it on a 2D
  grid $(\lambda, \alpha)$.

* **Details**:
  * Implement `unnorm_posterior(lmbda, alpha, ...)` as
    $\mathrm{UnnormPosterior}(\lambda,\alpha) =
    \mathrm{Likelihood}(\lambda,\alpha) \times
    p(\lambda) \times p(\alpha)$.
  * Define a grid of values for $\lambda \in [\lambda_\min,
    \lambda_\max]$ and $\alpha \in [\alpha_\min, \alpha_\max]$.
  * Evaluate the unnormalized posterior for each grid cell, then
    normalize so that the sum over all cells $\approx 1$.
  * Store the posterior in a 2D array `post` and also return the
    arrays `lmbdas`, `alphas`.
  * The code should be placed in `src/phys305_hw3/a4.py`.

### **Assignment 5**: Posterior Summaries (2 points)

* **Objective**:
  Extract statistical summaries (e.g., posterior means, marginals,
  credible intervals) from your 2D posterior grid.

* **Details**:
  * Compute the posterior means $\mathbb{E}[\lambda]
    \quad\text{and}\quad \mathbb{E}[\alpha]$.
  * Compute 1D marginal distributions for $\lambda$ and $\alpha$ by
    summation over the other axis, e.g.
    $p(\lambda_i) = \sum_j p(\lambda_i,\alpha_j)$.
  * Determine a 95% credible interval for each parameter by locating
    appropriate percentiles in the marginal distribution.
  * Compare your results to the "true" $\lambda_\text{true}$ and
    $\alpha_\text{true}$ used in generating the synthetic data to
    check accuracy.
  * The code should be placed in `src/phys305_hw3/a5.py`.
