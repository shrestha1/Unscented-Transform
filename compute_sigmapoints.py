import numpy as np
from recover_guassian import recover_guassian
from transform import transform

sigma = 0.1*np.eye(2)
mu = np.array([1, 2])

def compute_sigmapoints(mu, sigma):
    '''
    params: mu and sigma
    mu: nd array of means
    sigma: covariance matrix

    returns: 
    sigma_points: sampled points using mean
    weights wm: weight required to recover mean
    weights wc: weight required to recover covariance

    '''
    
    #dimesion of array
    n = mu.shape[0]
    
    lambdaa = 0.5                       #lamdaa value should lie between 0-1
    beta = 2

    # Calculate sigma points
    sigma_points = np.zeros((n, 2*n+1))
    sigma_points[:, 0] = mu
    sigma_points[:, 1:n+1] = mu.reshape(n,1) \
                            + np.sqrt((n+lambdaa)*sigma)
    sigma_points[:, n+1:] = mu.reshape(n,1) \
                            - np.sqrt((n+lambdaa)*sigma)

    
    # Calculate the weights
    wm = np.zeros(2*n+1)
    wc = np.zeros(2*n+1)
    wm[0] = lambdaa/(n+lambdaa)
    
    wc[0] = wm[0] + (1-lambdaa**2 + beta)

    wm[1:] = 1/(2*(n+lambdaa))
    wc[1:] = 1/(2*(n+lambdaa))
    
    return sigma_points, wm, wc
sigma_point,a, b = compute_sigmapoints(mu, sigma)
print(transform(sigma_point))