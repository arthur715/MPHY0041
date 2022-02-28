import numpy as np
from scipy.special import expit

def sigmoid(value):
    return expit(value)

def fit_LogReg_IWLS(y, features, eps=0.0000001):
    #sample size
    N = features.shape[0]
    #feature dim
    p = features.shape[1] + 1
    #initalize beta with 0s
    betas = np.zeros(p)

    #add column of 1 to features to get our X matrix
    X = np.c_[np.ones(N),features]
    #compute predictions for class 1: linear combination between input (X) and
    # coefficients (betas) passed through the sigmoid function
    prob1 = sigmoid( X @ betas)
    #compute predictions for class 0 (1.0 - prob1)
    prob0 = 1.0 - prob1
    #COMPLETE THIS CODE: W MATRIX
    W =
    old_loglike = 100000
    #compute LogLikelihood:
    #COMPLETE THIS CODE: logLiklihood of the current solution
    loglike =
    while np.abs(loglike - old_loglike) > eps:
        #update betas:
        #1) compute the z-vector
        #COMPLETE THIS CODE
        z =
        #2) upate the beta values (weighted least squares)
        #COMPLETE THIS CODE
        betas_new =
        betas = betas_new
        prob1 = sigmoid( X @ betas)
        prob0 = 1.0 - prob1
        #COMPLETE THIS CODE (same as in line 23):
        W =
        old_loglike = loglike
        #COMPLETE THIS CODE (same as in line 27):
        loglike =
    return(betas)
