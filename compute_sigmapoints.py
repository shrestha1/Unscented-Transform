import numpy as np
sigma = 0.1*np.eye(2)
mu = np.array([1, 2])

def compute_sigmapoints(mu, sigma):
    n = mu.shape[0]
    lambdaa = 0.5 #lamdaa value should lie between 0-1
    print("inside")
    sigma_points = np.zeros((n, 2*n+1))
    sigma_points[:, 0] = mu
    sigma_points[:, 1:n+1] = mu.reshape(n,1) + np.sqrt((n+lambdaa)*sigma)
    sigma_points[:, n+1:] = mu.reshape(n,1) - np.sqrt((n+lambdaa)*sigma)

    print(sigma_points)
    # pass

print(compute_sigmapoints(mu, sigma)