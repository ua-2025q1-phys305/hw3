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
         * `n0` (float): The initial count rate.
         * `lmbda` (float): The decay constant.
       * *Note*: Since `lambda` is a Python keyword, we use the
         variable name `lmbda` in our code.

     * Returns: The expected number of counts computed as:
       `counts` =
       $\mu_t = \int_{t-\Delta t}^t n_0 \exp(-\lambda t')dt'$.

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
  \mbox{ with }
  \mu_t = \int_{t-\Delta t}^t n_0 \exp(-\lambda t')dt'$
  where $C_t$ represents the cumulative count over $\Delta t$ at time
  $t$.


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
	 \exp\left[-\frac{1}{2}\left(\frac{\log(\lambda)-\mu}{\sigma}\right)^2\right]$,
	 where $\mu = \ln(0.01)$ and $\sigma = \ln(2)$.
       * Normalize the resulting PDF using the trapezoidal rule with
         respect to the grid so that it sums (or integrates) to 1.


### **Assignment 3**: Implement the Poisson Likelihood (2 points)

* **Objective**:
  Given a set of observed counts $\{C_t\}$ at time points $\{t\}$,
  implement a function to compute the Poisson likelihood for the
  parameters $n_0$ and $\lambda$.

* **Details**:
  In this assignment, you will write two functions in
  `src/phys305_hw3/a3.py`:

  1. **Implement `logpoisson(k, lmbda)`**
     * Purpose: Compute the logarithm of the Poisson probability mass
       function for an observed count $k$ given an expected count
       (denoted by `lmbda`).
     * Formula:
       $\ln P(k|\mu) = k \ln(\mu) - \mu - \ln(k!)$.
       Use `scipy.special.loggamma()` to calculate $\ln(k!)$ as `loggamma(k+1)`.

  2. **Implement `likelihood(obs, params)`**
     * Purpose: Compute the overall likelihood of observing a set of
       counts given your model parameters.
     * Parameters:
       * `obs`: A tuple containing:
         * `Cts`: An array of observed counts.
         * `ts`: An array of time points corresponding to the counts.
         * `dt`: The duration of the measurement interval.
       * `params`: A tuple of parameter grids (as generated by
         `np.meshgrid`), corresponding to the discretized values of
         $n_0$ and $\lambda$.

     * Hints:
       * For each measurement (i.e., each count and corresponding
         time), compute the expected count using the `count()` function
         (from Assignment 1).
       * Use your `logpoisson` function to compute the log-likelihood
         for each observation and accumulate these values.
       * Return the likelihood as the exponential of the total
         log-likelihood, i.e., $\exp(\text{total log-likelihood})$.
       * You may need to handle cases where the expected count $\mu
         \le 0$ appropriately (for instance, by returning a zero
         likelihood).


### **Assignment 4**: Construct the 2D Posterior on a Grid (2 points)

* **Objective**:
  Combine the priors from Assignment 2 and the likelihood from
  Assignment 3 to build the **unnormalized posterior** over a 2D grid
  of parameters, then normalize it so that the total probability sums
  (or integrates) to 1. In our case, the grid will represent
  discretized values of $n_0$ and $\lambda$.

* **Details**:

  In this assignment, you will implement the following in
  `src/phys305_hw3/a4.py`:

  1. **2D Trapezoidal Integration**:
     To normalize the posterior, implement a function `trapezoid2(f,
     grid)` that performs 2D integration over your grid.
     You may write helper functions such as:
     * `trapezoidx(f, grid)`: Integrates a 2D array `f` along the
       x-axis.
     * `trapezoidy(f, grid)`: Integrates a 2D array `f` along the
       y-axis.
     * *Note*: Implementing `trapezoidx()` and `trapezoidy()` is
       optional.

  2. Compute the Posterior:
     Write a function `posterior(obs, prior, params)` that calculates:
     $\text{posterior}(\lambda, n_0) \propto
     \text{likelihood}(\lambda, n_0) \times p(\lambda) \times p(n_0)$
     * Parameters:
       * `obs`: A tuple $(Cts, ts, dt)$ representing the observed
         counts, time points, and measurement interval.
       * `prior`: A 2D array containing the prior probability
         evaluated on the grid.
       * `params`: A tuple of parameter grids (e.g., generated via
         `np.meshgrid()` for $n_0$ and $\lambda$.
     * Hints:
       * Compute the unnormalized posterior by multiplying the
         likelihood (from Assignment 3) and the prior on an
         element-wise basis.
       * Normalize the posterior so that its 2D integral over the grid is approximately 1.


### **Assignment 5**: Implement Sequential Posterior Updates with `runexpr()` (2 points)

* **Objective**:

  Implement a function `runexpr()` that simulates a series of
  experiments to update the posterior distribution over model
  parameters using sequential observations.

* **Details**:
  In this assignment, you will write the `runexpr()` function in
  `src/phys305_hw3/a5.py`.
  This function should:

  * **Initialize the Experiment**:
    * Compute prior probability distributions for $n_0$ and $\lambda$
      using your implementations from Assignment 2.
    * Create a 2D grid of parameter values (using, e.g.,
      `np.meshgrid()`) and compute the combined prior on this grid.

  * **Simulate Sequential Observations**:
    * Define a set of time points and a measurement interval for the
      experiment.
    * Generate synthetic observed counts using your data generation
      function from Assignment 1.

  * **Update the Posterior**:
    * Use the observed counts and the previous posterior (starting
      with the initial prior) to update the posterior distribution by
      combining it with the likelihood (from Assignment 3).
    * Repeat the update process for a specified number of sequential
      experiments.

  * **Return the Results**:
    * The function should return a tuple `(posts, params)` where:
      * `posts` is a list of posterior distributions, starting with
        the initial prior and followed by the updated posteriors after
        each experiment.
      * `params` is a tuple of the parameter grids (e.g., arrays of
       	discretized $n_0$ and $\lambda$ values) used in the
       	computation.


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
