import numpy as np

def transform(sigma_points):
    '''
    transform the sigma points
    linear or non-linear 
    '''
        # linear transform of points

    sigma_points[0,:] = sigma_points[0,:]+1
    sigma_points[1,:] = sigma_points[1,:]+2

    # for non linear transform of points
    x = sigma_points[0,:]
    y = sigma_points[1,:]

    r = np.sqrt(x*x+y*y)
    theta = np.arctan2(y,x)
    sigma_points = np.array([r, theta])
    # print("points: \n",points )
    return sigma_points
  