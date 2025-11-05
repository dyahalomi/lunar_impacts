import numpy as np
import matplotlib.pyplot as plt


import matplotlib 
matplotlib.rc('xtick', labelsize=23) 
matplotlib.rc('ytick', labelsize=23) 

t_w = 0.48
rho_b = 2.851
sigma = 52
S = 11.43
F_2 = 1
rho_p = 8.9
theta = 0
V = np.arange(10,72.1)


d_c = (3.918 * F_2 *  t_w**(2/3)* S**(1/3) *(sigma/70)**(1/3))/(rho_p**(1/3) * rho_b**(1/9) * (V *np.cos(theta))**(2/3))


plt.figure(figsize = [18,9])
plt.plot(V, d_c, 'k', lw = 3)
plt.ylabel("critical diamter [cm]", fontsize = 23)
plt.xlabel("velocity [km/s]", fontsize = 23)
plt.title("Ballistic Limit Curve for Whipple Shield", fontsize = 27)

plt.savefig('ballistic_curve.pdf')
plt.show()


