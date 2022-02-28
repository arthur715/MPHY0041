import numpy as np
from scipy.special import expit

def sigmoid(value):
    return expit(value)

def fit_LogReg_GRAD(y, features, eps=0.00000000001, alpha=0.001):
    #sample size
    N = features.shape[0]
    #feature dim
    p = features.shape[1] + 1
    #initalize beta with 0s
    betas = np.zeros(p)

    #add column of 1 to X
    X = np.c_[np.ones(N),features]
    #compute predictions for class 1
    prob1 = sigmoid( X @ betas)
    #compute predictions for class 2
    prob0 = 1.0 - prob1

    old_cost = 100000000
    #compute the cost (J) of the current solution
    #COMPLETE THIS LINE
    cost =
    while np.abs(old_cost - cost) > eps:
        #beta update (one steo of the gradient descent)
        #COMPLETE THIS LINE
        betas =
        prob1 = sigmoid( X @ betas)
        prob0 = 1.0 - prob1
        old_cost = cost
        #recompute cost
        #COMPLETE THIS LINE (same as in line 24)
        cost =
    return(betas)
