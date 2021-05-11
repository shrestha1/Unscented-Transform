def recover_gaussian(sigma_points, wm, wc):
    '''
    Recover mean and sigma

    '''
    new_mu = wm @ sigma_points.T

    new_sigma = wc*(sigma_points-new_mu.reshape(1,2).T)@(sigma_points-new_mu.reshape(1,2).T).T

    return new_mu, new_sigma


