#  By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Kuba
#               Ben Goertz
#               Owen Bell
# Section:      ENGR-102:533,557
# Assignment:   Lab Topic 12 Team
# Date:         11/17/23

# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

import matplotlib.pyplot as plt
import numpy as np

x_values = np.linspace(-2.0,2.0,20)

def y_values(f):
    return x_values ** 2 / (4 * f)

plt.plot(x_values,y_values(2),'r',linewidth=3)
plt.plot(x_values,y_values(6),'b',linewidth=3)
plt.xlabel('x')
plt.ylabel('1/4f * x^2')
plt.title('Parabola Plots with Varying Focal Length')
plt.legend(['f=2','f=6'])
plt.show()

x_values = np.linspace(-4.0,4.0,25)

def y_values(x):
    return 2*x**3 + 3*x**2 - 11*x - 6

plt.plot(x_values,y_values(x_values),'g^')
plt.xlabel('x')
plt.ylabel('2x^3 + 3x^2 − 11x − 6')
plt.title('Plot of Cubic Polynomial')
plt.show()

x_values = np.linspace(-2*np.pi,2*np.pi,100)

plt.subplot(211)
plt.plot(x_values, np.sin(x_values),'orange',linewidth=3)
plt.ylabel('sin(x)')
plt.legend(['sin(x)'])
plt.grid()

plt.subplot(212)
plt.plot(x_values, np.cos(x_values),'m',linewidth=3)
plt.ylabel('cos(x)')
plt.legend(['cos(x)'],loc='lower right')
plt.grid()

plt.xlabel('x')
plt.suptitle('Plot of cos(x) and sin(x)')
plt.show()
