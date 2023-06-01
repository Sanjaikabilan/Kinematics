import numpy as np

# Define the link lengths
a1 = 1
a2 = 1

# Define the joint angles (in radians)
theta1 = 0.5
theta2 = -0.5

# Forward kinematics using homogeneous transformation matrices
T1 = np.array([[np.cos(theta1), -np.sin(theta1), 0, a1*np.cos(theta1)],
               [np.sin(theta1), np.cos(theta1), 0, a1*np.sin(theta1)],
               [0, 0, 1, 0],
               [0, 0, 0, 1]])

T2 = np.array([[np.cos(theta2), -np.sin(theta2), 0, a2*np.cos(theta2)],
               [np.sin(theta2), np.cos(theta2), 0, a2*np.sin(theta2)],
               [0, 0, 1, 0],
               [0, 0, 0, 1]])

T = T1 @ T2
x = T[0, 3]
y = T[1, 3]
print("Forward kinematics: x =", x, ", y =", y)

# Inverse kinematics using homogeneous transformation matrices
r = np.sqrt(x*x + y*y)
alpha = np.arctan2(y, x)
beta = np.arccos((a1*a1 + a2*a2 - r*r) / (2*a1*a2))
theta1 = alpha - np.arctan2(a2*np.sin(beta), a1+a2*np.cos(beta))
theta2 = np.arctan2(np.sin(beta), np.cos(beta)+(a1/a2))
print("Inverse kinematics: theta1 =", theta1, ", theta2 =", theta2)
