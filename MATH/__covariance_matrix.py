"""
1. The data: 
we have data of N events, each contains D features. 

           event1  event2   ..  eventN
feature1    x11      x12         x1N
feature2    x21      x22         x2N 
 :  
featureD    xD1      xD2         xDN


This is actually N points in dimenstion D 


2. For example, lets take N points of 2 features 
The data matrix is 2xN

A  = [ x1  x2   ..  xN ] 
     [ y1  y2       yN ]
       

> The mean is        
E(A) = [E(x)] = [sum(x)/N]
       [E(y)]   [sum(y)/N]
       

> The variance information is not only per feature, because it doesn't give enough information about the dat abehaviour. 
  There can be two different data which have the same variance per feature, but the covariance between features may be different, 
  In order to have as much as possible information, we want the variance between every deature and other,
  V(x,x) , V(y,y) and V(x,y)
  
  where
  V(x,x) = E((x-E(x))^2)         = (x-E(x)) * (x-E(x)).T / (N-1)    Note: (N-1) is for Bessel's correction
  V(y,y) = E((y-E(y))^2)         = (y-E(y)) * (y-E(y)).T / (N-1)    Note: (N-1) is for Bessel's correction
  V(x,y) = E((x-E(x))*(y-E(y)))  = (x-E(x)) * (y-E(y)).T / (N-1)    Note: (N-1) is for Bessel's correction
  
  
  We can get these values in matrix form using the follow formula:  
  X is mean centered A : 
  X = A-E(A)
  C is the covariance matrix, contains all variance and covariance information of the data:
  C = E(X * X.T) =  (X * X.T) / (N-1) = [ V(x,x) V(x,y) ]
                                        [ V(y,x) V(y,y) ]   
     
3. lets be v a vector , and we want to project each point over it 
   u - projected point over v. 
   
   u = X.T * v = v.T * X  
   (u is column vector of N values)
        
4. what us the direction v where the variamce of the projected points is maximum
   Var(u) = u.T * u / (N-1) = 
          = (X.T * v).T * (X.T * v) / (N-1) =
          = v.T * X * X.T * v / (N-1) =
          = v.T * C * v 

   We want the direction with maximum variance:
   max (v.T * C * v)  , while |v| = 1
    v

   This is constrained optimization problem , we can use Lagrange multipliers to solve it.
   L(v, λ) = v.T * C * v + λ * (1 - v.T * v)

"""

