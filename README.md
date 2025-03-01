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
    $$C_t \sim \mathrm{Poisson}\left(\mu_t\right), \quad
    \mu_t = \Delta t \left[\alpha \lambda N_0 e^{-\lambda t} + b\right].$$
  * Provide a small test or a plot to show that the data looks
    reasonable (e.g., a decreasing count rate over time plus some
    constant offset from background).
  * The code should be put in `a1.py`.
