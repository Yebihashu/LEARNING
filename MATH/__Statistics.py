""" Expectation and its estimators, unbaised vs biased estimator
----------------------------------------------------------------
1. Expectation - ideal measuring of expectation:
Given a random variable X. Its expectation can be measured and calculated by sampling many times (N -> ∞):
μ = E(X) = 1/N * ∑ x , where N -> ∞

2. Expectation estimator - actuall measuring of expectation:
In reality, we can not sample many times (N -> ∞), so we use a sample of size N to estimate the expectation. 
This is not the true expectation, but an estimate value.
μ_est = E(X) = 1/N * ∑ x 

3. Uunbiased / Biased estimator
The expectation estimaotr in (2) doesn't give the true expectation value of X, but an estimate one. This means that each time we run this estimator, 
it will give a different results. If the expectation of these results (ideal one, for ∞ results) is the real value we try to estimate - in this example it is μ, 
then this estimator is called unbiased.

In general, an estimator is called unbaised if the mean of its results is the true valuve we try to estimate.
It is biased if the mean of its results has some offset from the true value.

Sometimes we perefer to use an unbiased estimator, because of some advatnage it may give, depending on the situation.  

4. Expectation - calculation the ideal value instead of measuring/estimating.
if we knows the probability of each outcome, we do not need to measure, but calculate the exact expectation as:
Given a random variable X. Its expectation:
μ = E(X) = ∑ x * P(x) , where P(x) is the probability of x, 
Note:  ∑ P(x) = 1

Example: X - the number obtained for one roll of a dice. 
        P(x) = 1/6 for x = 1, 2, 3, 4, 5, 6
        μ = E(X) = ∑ x * P(x) = 1/6 * (1 + 2 + 3 + 4 + 5 + 6) = 3.5
""" 

""" Expectation of sum of two random variables
----------------------------------------------------------------
Given two random variables X and Y. Their expectations P(x) and P(y) are known.
Given a new random variable Z = X + Y. What is the expectation of Z?
Examle 1: X - number of oranges given from a tree at a year. 
          Y - number of apples given from a tree at a year. 
          Z - number of fruits given from the tree at a year.
Examle 2: X - number of obtained for first dice rolling. 
          Y - number of obtained for second dice rolling. 
          Z - the sum of the numbers obtained for two dice rollings.
          There are 36 possible outcomes pairs for rolling two dices, each has 1/36 chance to happen.
          The outcome of the values of Z are :
          2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
          where their chance to happen are the sum of the chances of the paris bring them. 

Instead of calculating the expectation of Z by summing up the chances of the pairs bringing them,
we can calculate the expectation of Z by summing up the expectations of X and Y. Proof:
μx = E(X) = ∑ x * P(x) 
μy = E(Y) = ∑ y * P(y) 
μz = E(Z) = ∑∑ (x + y) * P(x , y) = ∑∑ (x + y) * P(x) * P(y) = ∑∑ x*P(x)*P(y) + y*P(x)*P(y) = 
          = ∑∑ x*P(x)*P(y) + ∑∑y*P(x)*P(y) = ∑ x*P(x)*(∑P(y)) + ∑ y*P(y)*(∑P(x)) = 
          = ∑ x*P(x)*(1) + ∑ y*P(y)*(1) = ∑ x*P(x) + ∑ y*P(y) = μx + μy

"""

""" Depended random variable
----------------------------------------------------------------
TODO

"""

""" Expectation of sum of two dependent random variables
----------------------------------------------------------------
TODO

"""

""" Expectation of a product of two independent random variables
----------------------------------------------------------------
TODO

"""

""" Expectation of a product of two dependent random variables
----------------------------------------------------------------
TODO


Z = X + Y
 
E(X) = ∑ x * P(x) 
E(Y) = ∑ y * P(y) 

E(Z) = ∑ z * P(z) = ∑∑ (x+y) * P(x,y)



"""
