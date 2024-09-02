import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define the physical parameters
lambda1 = 0.2  # kg-m^2
lambda2 = 0.3  # kg-m^2
lambda3 = 0.4  # kg-m^2

# Simulation parameters
tf = 10  # s
dt = 0.005  # s
tsim = np.arange(0, tf, dt)  # s
tol = 1e-6

# Initial conditions
omega10 = 0.1  # rad/s
omega20 = 15  # rad/s
omega30 = 0.1  # rad/s
psi0 = 0  # rad
theta0 = 90 * np.pi / 180  # rad
phi0 = 0  # rad

Y0 = [omega10, omega20, omega30, psi0, theta0, phi0]

def euler_eqs(t, Y):
    omega1, omega2, omega3, psi, theta, phi = Y

    # Euler's equations of motion for a rigid body
    omega1_dot = ((lambda2 - lambda3) / lambda1) * omega2 * omega3
    omega2_dot = ((lambda3 - lambda1) / lambda2) * omega1 * omega3
    omega3_dot = ((lambda1 - lambda2) / lambda3) * omega1 * omega2

    # Print sin(theta) to see the issue
    sin_theta = np.sin(theta)
    print(f"t = {t:.3f}, sin(theta) = {sin_theta:.6f}")

    # Angular velocity kinematics for Z-X-Z sequence
    psi_dot = omega1 / np.sin(theta)
    theta_dot = omega2 * np.cos(psi) - omega3 * np.sin(psi)
    phi_dot = (omega2 * np.sin(psi) + omega3 * np.cos(psi)) / np.sin(theta)

    return [omega1_dot, omega2_dot, omega3_dot, psi_dot, theta_dot, phi_dot]

# Solve the ODEs
sol = solve_ivp(euler_eqs, [0, tf], Y0, t_eval=tsim, atol=tol, rtol=tol)

# Extract results
omega1, omega2, omega3 = sol.y[0], sol.y[1], sol.y[2]
psi, theta, phi = sol.y[3], sol.y[4], sol.y[5]

# Plot the results
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(sol.t, omega1, label='omega1')
plt.plot(sol.t, omega2, label='omega2')
plt.plot(sol.t, omega3, label='omega3')
plt.xlabel('Time (s)')
plt.ylabel('Angular Velocity (rad/s)')
plt.title('Angular Velocity vs Time')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(sol.t, psi, label='psi')
plt.plot(sol.t, theta, label='theta')
plt.plot(sol.t, phi, label='phi')
plt.xlabel('Time (s)')
plt.ylabel('Euler Angles (rad)')
plt.title('Euler Angles vs Time')
plt.legend()

plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_t_handle(psi, theta, phi, dt):
    # Specify dimensions for the T-handle
    LAG = 0.5  # cm
    LBC = 4  # cm
    LAD = 2  # cm

    # Initialize arrays to store the T-handle's orientation and key points
    e1 = np.zeros((3, len(psi)))
    e2 = np.zeros((3, len(psi)))
    e3 = np.zeros((3, len(psi)))
    xA, yA, zA = np.zeros(len(psi)), np.zeros(len(psi)), np.zeros(len(psi))
    xB, yB, zB = np.zeros(len(psi)), np.zeros(len(psi)), np.zeros(len(psi))
    xC, yC, zC = np.zeros(len(psi)), np.zeros(len(psi)), np.zeros(len(psi))
    xD, yD, zD = np.zeros(len(psi)), np.zeros(len(psi)), np.zeros(len(psi))

    # Calculate the orientation of the T-handle over time
    for k in range(len(psi)):
        R1 = np.array([[np.cos(psi[k]), np.sin(psi[k]), 0],
                       [-np.sin(psi[k]), np.cos(psi[k]), 0],
                       [0, 0, 1]])
        R2 = np.array([[1, 0, 0],
                       [0, np.cos(theta[k]), np.sin(theta[k])],
                       [0, -np.sin(theta[k]), np.cos(theta[k])]])
        R3 = np.array([[np.cos(phi[k]), np.sin(phi[k]), 0],
                       [-np.sin(phi[k]), np.cos(phi[k]), 0],
                       [0, 0, 1]])
        e1[:, k] = np.dot([1, 0, 0], R3 @ R2 @ R1)
        e2[:, k] = np.dot([0, 1, 0], R3 @ R2 @ R1)
        e3[:, k] = np.dot([0, 0, 1], R3 @ R2 @ R1)
        xA[k] = -LAG * e2[0, k]
        yA[k] = -LAG * e2[1, k]
        zA[k] = -LAG * e2[2, k]
        xB[k] = xA[k] + LBC / 2 * e1[0, k]
        yB[k] = yA[k] + LBC / 2 * e1[1, k]
        zB[k] = zA[k] + LBC / 2 * e1[2, k]
        xC[k] = xA[k] - LBC / 2 * e1[0, k]
        yC[k] = yA[k] - LBC / 2 * e1[1, k]
        zC[k] = zA[k] - LBC / 2 * e1[2, k]
        xD[k] = xA[k] + LAD * e2[0, k]
        yD[k] = yA[k] + LAD * e2[1, k]
        zD[k] = zA[k] + LAD * e2[2, k]

    # Set up the figure window
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('X (cm)')
    ax.set_ylabel('Y (cm)')
    ax.set_zlabel('Z (cm)')
    ax.set_xlim([-LBC, LBC])
    ax.set_ylim([-LBC, LBC])
    ax.set_zlim([-LAD, LAD])
    ax.set_title('T-handle Animation')

    # Draw the T-handle
    AD, = ax.plot([xA[0], xD[0]], [yA[0], yD[0]], [zA[0], zD[0]], 'k-', linewidth=5)
    BC, = ax.plot([xB[0], xC[0]], [yB[0], yC[0]], [zB[0], zC[0]], 'k-', linewidth=5)

    # Animate the T-handle's motion by updating the figure with its current orientation
    def update(k):
        AD.set_data([xA[k], xD[k]], [yA[k], yD[k]])
        AD.set_3d_properties([zA[k], zD[k]])
        BC.set_data([xB[k], xC[k]], [yB[k], yC[k]])
        BC.set_3d_properties([zB[k], zC[k]])
        return AD, BC,

    ani = FuncAnimation(fig, update, frames=len(psi), interval=dt * 1000, blit=True)
    plt.show()

# Example usage
# Assuming `psi`, `theta`, `phi` are the Euler angles obtained from the previous solution
animate_t_handle(psi, theta, phi, dt)
