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

To simplify debugging and to help you visualize your progress, a
Jupyter notebook is provided at `demo/vis.ipynb`.
This notebook demonstrates how the functions developed for each
assignment interact and shows sample visualizations. Use the notebook
alongside `pytest` to validate your code and to better understand the
behavior of your implementations.


### **Assignment 1**: Generate Synthetic Radioactive Decay Data (2 points)

* **Objective**:
  Implement functions that generate synthetic radioactive decay count
  data given "true" values of $n_0$ (initial count rate) and the
  decay constant $\lambda$.

* **Details**:
  You are required to implement two key functions in
  `src/phys305_hw3/a1.py`:

  1. `count(ts, dt, groundtruth)`
     * Purpose: Compute the expected number of counts over a
       measurement interval $[t-\Delta t, t]$ using the radioactive
       decay law.

     * Parameters:
       * `ts` (float or ndarray): The end time(s) of the measurement interval.
       * `dt` (float): The duration $\Delta t$ of the measurement interval.
       * `groundtruth` (tuple): A tuple $(n_0, \lambda)$ where:
         * `n_0` (float): The initial count rate.
         * `\lambda` (float): The decay constant.
     * Returns: The expected number of counts computed as:
       $\text{counts} = n_0 \left(e^{-\lambda (t - \Delta t)} - e^{-\lambda t}\right)$

  2. `sample(ts, dt, groundtruth)`
     * Purpose: Generate synthetic observed counts by drawing samples
       from a Poisson distribution with the mean provided by the
       `count()` function.
     * Parameters: `ts`, `dt`, `groundtruth`: Same as in the `count()`
       function.
     * Returns: A sampled count (or an array of counts, if `ts` is an
       array) obtained from a Poisson distribution.
     * Hints:
       * Call your `count()` function to compute the expected counts.
       * Use `np.random.poisson()` to generate a random sample with
         that expected value.

* **Model Specification**:
  The radioactive decay data is modeled as follows:
  $C_t \sim \text{Poisson}\left(\mu_t\right),
  \quad \text{with}
  \quad \mu_t = n_0 \left(e^{-\lambda (t - \Delta t)} - e^{-\lambda t}\right)$
  where $C_t$ represents the observed count at time $t$.

* **Visualization**:
  Use the provided Jupyter notebook at `demo/vis.ipynb` to verify that
  the synthetic data looks reasonable---for example, observe the
  expected decreasing trend of counts over time.

* **Submission**:
  Ensure your implementation is placed in `src/phys305_hw3/a1.py` and
  that your code is well-documented with clear function docstrings and
  inline comments.


### **Assignment 2**: Define Priors for $n_0$ and $\lambda$ (2 points)

* **Objective**:
  Choose and implement prior probability density functions (PDFs) for
  the two unknown parameters of the radioactive decay model: the
  initial count rate $n_0$ and the decay constant $\lambda$.

* **Details**:
  In this assignment, you will implement two functions in
  `src/phys305_hw3/a2.py`:

  1. `prior0_n0(l=0, u=300, n=301)`
     * Purpose: Create a uniform prior for $n_0$ over a specified
       interval $[l, u]$.
     * Hints:
       * Use `numpy.linspace()` to generate a discretized grid of
         $n_0$ values.
       * Create a uniform prior by assigning equal probability to each
         grid point.
       * Normalize the prior using the trapezoidal integration rule so
         that the total probability integrates to 1.

  2. `prior0_lmbda(l=1e-4, u=1, n=401, mu=np.log(0.01), sigma=np.log(2))`
     * Purpose: Create a log-normal prior for the decay constant $\lambda$.
     * Hints:
       * Use `numpy.logspace()` to generate a log-spaced grid of
         $\lambda$ values.
       * Compute the unnormalized log-normal prior values using the
         formula:
         $p(\lambda) \propto
	 \exp\left[-\frac{1}{2}\left(\frac{\log(\lambda)-\mu}{\sigma}\right)^2\right]$
       * Normalize the resulting PDF using the trapezoidal rule with
         respect to the grid so that it sums (or integrates) to 1.

* **Visualization**:
  Use the provided Jupyter notebook at `demo/vis.ipynb` to verify that
  your priors behave as expected.

* **Submission**:
  Place your implementations in `src/phys305_hw3/a2.py`. Ensure that
  your code is well-documented with clear docstrings and inline
  comments.


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


## Additional Notes

* **Collaboration**:
  You are encouraged to discuss ideas with your peers, but your
  submission must reflect your own work.
* **Help and Resources**:
  If you encounter any difficulties, please refer to the course
  materials, consult your instructor, or seek help during office
  hours.
* **Deadlines**:
  Be mindful of the submission deadline, as late submissions will not
  be accepted.

Good luck, and have fun working on the assignments!
