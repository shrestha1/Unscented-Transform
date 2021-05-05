# Unscented-Transform
This repo contains the idea of unscented transform
# Background and Introduction
To linearize a non-linear dynamical system, mostly taylor approximation is done. But, Unscented transform is method to skillfully exploit the non-linear function. It is assumed that the input to the system is Guassion G(mu, sigma) and applying the non-linear function, the output loses its guassian property. Hence, the unscented transfrom presents the idea of sigma points and those points are transformed using non-linear function and later recovering the mean and sigma preserving the guassian nature.

Sigma points are calculated as:

s(1) = mu;

s(2) = mu + sqrt((n+lambda)*sigma)

s(3) = mu - sqrt((n+lambda)*sigma)

These sigma points are now transformed using the non-linear function h().

y = h(s)

New sets of transformed sigma points are obtained. These are weighted and summed to recover the mean. Similarly, the weighted sum of the product of difference of transformed sigma points and actual mean, and its transpose gives the recovered sigma points.

weights: 

wm = lambda/(n+lambda) or lambda/2(n+lambda)

wc = lambda/(n+lambda) or 1/2(n+lambda)

Recover mu and sigma which means guassian recover:

new_mu = summation(wm*y)

new_sigma = summation(ws*(y-mu)*(y-mu)')




