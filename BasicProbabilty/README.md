# 📘 **Probability and Statistics: Complete Reference Guide**

This document is a comprehensive guide to essential concepts in **Probability and Statistics**, designed for beginners, students, and enthusiasts. It includes clear definitions, categorized sections, mathematical notations, and formulas where applicable.

---

## 📑 **Table of Contents**

1. [Introduction](#introduction)
2. [Probability Basics](#probability-basics)

   * Experiment
   * Sample Space $S$
   * Event
   * Probability $P$
3. [Types of Events](#types-of-events)

   * Independent Events
   * Dependent Events
   * Mutually Exclusive Events
   * Complementary Events
4. [Random Variables](#random-variables)
5. [Probability Distributions](#probability-distributions)

   * Discrete vs Continuous
   * Common Distributions
6. [Descriptive Statistics](#descriptive-statistics)

   * Central Tendency
   * Dispersion
7. [Inferential Statistics](#inferential-statistics)

   * Estimation
   * Hypothesis Testing
   * Confidence Intervals
8. [Formulas Reference](#formulas-reference)
9. [Glossary](#glossary)

---

## 🧠 **Introduction**

**Probability** deals with the chance of occurrence of events. **Statistics** involves collecting, organizing, analyzing, and interpreting data to make informed decisions.

### 🔍 Key Differences:

* **Probability:** Starts with known data to predict outcomes.
* **Statistics:** Starts with data and infers unknowns.

---

## 🎲 **Probability Basics**

### 🔬 Experiment

A repeatable process with uncertain outcomes.

### 📂 Sample Space $S$

The set of all possible outcomes:
$S = \{s_1, s_2, ..., s_n\}$

### 📌 Event

A subset of the sample space:
$A \subseteq S$

### 🎯 Probability $P$

The measure of likelihood of an event:
$P(A) = \frac{\text{Number of favorable outcomes}}{\text{Total outcomes}}$

Properties:

* $0 \leq P(A) \leq 1$
* $P(S) = 1$
* $P(A') = 1 - P(A)$

---

## 🔗 **Types of Events**

### ✅ Independent Events

Events that do not affect each other:
$P(A \cap B) = P(A) \cdot P(B)$

### 🔄 Dependent Events

One event affects the other:
$P(A \cap B) = P(A) \cdot P(B|A)$

### 🚫 Mutually Exclusive Events

Events that cannot occur together:
$P(A \cap B) = 0$

### 🔁 Complementary Events

Events that cover all possibilities:
$P(A') = 1 - P(A)$

---

## 🎲 **Random Variables**

A **random variable** assigns numerical values to outcomes:

* **Discrete:** Countable outcomes (e.g., dice rolls)
* **Continuous:** Uncountably infinite outcomes (e.g., weight, height)

Notation:

* $X \sim \text{Binomial}(n, p)$
* $X \sim \mathcal{N}(\mu, \sigma^2)$

---

## 📈 **Probability Distributions**

### Discrete Distributions:

* **Bernoulli**: $P(X=1)=p, P(X=0)=1-p$
* **Binomial**: $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$
* **Poisson**: $P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}$

### Continuous Distributions:

* **Uniform**: $f(x) = \frac{1}{b-a}$
* **Normal (Gaussian)**: $f(x) = \frac{1}{\sqrt{2\pi \sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$
* **Exponential**: $f(x) = \lambda e^{-\lambda x}$

---

## 📊 **Descriptive Statistics**

### Measures of Central Tendency:

* **Mean** $\mu = \frac{\sum x_i}{n}$
* **Median**: Middle value
* **Mode**: Most frequent value

### Measures of Dispersion:

* **Range** = Max - Min
* **Variance** $\sigma^2 = \frac{\sum (x_i - \mu)^2}{n}$
* **Standard Deviation** $\sigma = \sqrt{\sigma^2}$
* **IQR**: Q3 - Q1 (Interquartile Range)

---

## 📉 **Inferential Statistics**

### Estimation:

* **Point Estimation**: Single value as estimate
* **Interval Estimation**: Range of values using confidence intervals

### Hypothesis Testing:

* **Null Hypothesis (H₀)**: No effect/difference
* **Alternative Hypothesis (H₁)**: There is an effect/difference
* Test statistics: z-test, t-test, chi-square, etc.

### Confidence Intervals:

$CI = \bar{x} \pm Z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}$

---

## 📐 **Formulas Reference**

| Concept             | Formula                                                                    |
| ------------------- | -------------------------------------------------------------------------- |
| Probability         | $P(E) = \frac{f}{N}$                                                       |
| Mean                | $\mu = \frac{\sum x_i}{n}$                                                 |
| Variance            | $\sigma^2 = \frac{\sum (x_i - \mu)^2}{n}$                                  |
| Standard Deviation  | $\sigma = \sqrt{\sigma^2}$                                                 |
| Binomial            | $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$                                  |
| Normal PDF          | $f(x) = \frac{1}{\sqrt{2\pi \sigma^2}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}$ |
| Confidence Interval | $CI = \bar{x} \pm Z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}$              |

---

## 📚 **Glossary**

| Term                    | Definition                                   |
| ----------------------- | -------------------------------------------- |
| **Experiment**          | A procedure to obtain outcomes               |
| **Event**               | One or more outcomes of interest             |
| **Sample Space**        | All possible outcomes                        |
| **Random Variable**     | Numeric outcome of a random event            |
| **Mean**                | Average of values                            |
| **Variance**            | Spread of values around the mean             |
| **Hypothesis**          | Assumption about a population                |
| **Confidence Interval** | Range likely to contain population parameter |

---

