import numpy as np
from compute_sigmapoints import compute_sigmapoints
from transform import transform
from recover_gaussian import recover_gaussian

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

fig = plt.figure() 
ax = fig.add_subplot(111)
sigma = 0.1*np.eye(2)
mu = np.array([1, 2])

n = len(mu)


sigma_points, w_m, w_c = compute_sigmapoints(mu, sigma)
print("sigma points before transform: \n", sigma_points)
print("sigma points: ", sigma_points[0,:])


# finding the minor axis len from the mu
min_indice = np.argmin(sigma_points, axis=1)[1]
dx, dy = mu - sigma_points[:,min_indice]
minoraxis = np.sqrt(dx**2+dy**2)
print("minoraxis: ", minoraxis)

#finding the major axis len from the mu,
max_indice = np.argmax(sigma_points, axis=1)[0]
dx, dy = mu - sigma_points[:,max_indice]
majoraxis = np.sqrt(dx**2+dy**2)
print("majoraxis: ", majoraxis)

# angle should be obtained from the major axis
angle = np.arctan(dy/dx)*180/3.1415

ellipse = Ellipse((mu[0],mu[1]), majoraxis*2+0.5, minoraxis*2+0.5, angle=angle, alpha=0.4)
plt.plot(sigma_points[0,:], sigma_points[1,:], 'x', mew=2.5, ms=5, color='g')
ax.add_artist(ellipse)

sigma_points_trans = transform(sigma_points)
print("sigma points after transform: \n",sigma_points)

mu_trans, sigma_trans = recover_gaussian(sigma_points_trans, w_m, w_c)
print("sigma point trans: \n", sigma_points_trans)
print("mu_trans: \n", mu_trans)
print("sigma_trans: \n", sigma_trans)

x_min = min(mu[0], mu_trans[0])
x_max = max(mu[0], mu_trans[0]+2)

y_min = min(mu[1], mu_trans[1])
y_max = max(mu[1], mu_trans[1]+2)

# finding the minor axis len from the mu
min_indice = np.argmin(sigma_points_trans, axis=1)[1]
dx, dy = mu_trans - sigma_points_trans[:,min_indice]
minoraxis = np.sqrt(dx**2+dy**2)
print("minoraxis: ", minoraxis*2)

#finding the major axis len from the mu,
max_indice = np.argmax(sigma_points_trans, axis=1)[0]
dx, dy = mu_trans - sigma_points_trans[:,max_indice]
majoraxis = np.sqrt(dx**2+dy**2)
print("majoraxis: ", majoraxis*2)

# angle should be obtained from the major axis
angle = np.arctan(dy/dx)*180/3.1415

ellipse = Ellipse((mu_trans[0],mu_trans[1]), majoraxis*2+1, minoraxis*2, angle=angle, alpha=0.5)

plt.plot(sigma_points_trans[0,:], sigma_points_trans[1,:], 'x', mew=2.5, ms=5, color='r')

ax.add_artist(ellipse)

plt.title("Unscented Transform")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
ax.set_xlim(x_min-3,x_max+3)
ax.set_ylim(y_min-3,y_max+1)
ax.legend(["Original Sigma Points", "Recovered Sigma Points"])
plt.show()