import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the physical parameters
lambda1 = 0.2  # kg-m^2
lambda2 = 0.3  # kg-m^2
lambda3 = 0.2  # kg-m^2

# Simulation parameters
tf = 10  # s
dt = 0.005  # s
tsim = np.arange(0, tf, dt)  # s
tol = 1e-6

# Initial conditions for angular velocities
omega10 = 0.1  # rad/s
omega20 = 15  # rad/s
omega30 = 0.1  # rad/s

# Initial conditions for quaternion (representing no initial rotation)
q0 = [1, 0, 0, 0]  # (w, x, y, z)

# Combine initial conditions
Y0 = [omega10, omega20, omega30] + q0

def quat_mult(q, r):
    """
    Multiply two quaternions q and r.
    """
    w1, x1, y1, z1 = q
    w2, x2, y2, z2 = r
    return [
        w1*w2 - x1*x2 - y1*y2 - z1*z2,
        w1*x2 + x1*w2 + y1*z2 - z1*y2,
        w1*y2 - x1*z2 + y1*w2 + z1*x2,
        w1*z2 + x1*y2 - y1*x2 + z1*w2
    ]

def quat_conjugate(q):
    """
    Return the conjugate of quaternion q.
    """
    w, x, y, z = q
    return [w, -x, -y, -z]

def euler_eqs_quat(t, Y):
    omega1, omega2, omega3, qw, qx, qy, qz = Y

    # Euler's equations of motion for a rigid body
    omega1_dot = ((lambda2 - lambda3) / lambda1) * omega2 * omega3
    omega2_dot = ((lambda3 - lambda1) / lambda2) * omega1 * omega3
    omega3_dot = ((lambda1 - lambda2) / lambda3) * omega1 * omega2

    # Quaternion derivative
    omega_quat = [0, omega1, omega2, omega3]
    quat = [qw, qx, qy, qz]
    quat_dot = 0.5 * np.array(quat_mult(quat, omega_quat))

    return [omega1_dot, omega2_dot, omega3_dot, quat_dot[0], quat_dot[1], quat_dot[2], quat_dot[3]]

# Solve the ODEs
sol = solve_ivp(euler_eqs_quat, [0, tf], Y0, t_eval=tsim, atol=tol, rtol=tol)

# Check if the integration was successful
if sol.status == 0:
    print("Integration successful.")
else:
    print(f"Integration failed with status {sol.status}: {sol.message}")

# Print the final time to check if it reached 10 seconds
print(f"Final time: {sol.t[-1]}")

# Extract results
omega1, omega2, omega3 = sol.y[0], sol.y[1], sol.y[2]
qw, qx, qy, qz = sol.y[3], sol.y[4], sol.y[5], sol.y[6]

# Function to convert quaternion to Euler angles (Z-X-Z sequence)
def quat_to_euler_zxz(q):
    """
    Convert a quaternion to Euler angles (Z-X-Z sequence).
    """
    w, x, y, z = q
    # Compute the Euler angles
    psi = np.arctan2(2*(w*z + x*y), 1 - 2*(y**2 + z**2))
    theta = np.arccos(2*(w*y - z*x))
    phi = np.arctan2(2*(w*z + y*x), 1 - 2*(x**2 + y**2))
    return psi, theta, phi

# Extract Euler angles from quaternions
psi, theta, phi = np.zeros(len(qw)), np.zeros(len(qw)), np.zeros(len(qw))
for i in range(len(qw)):
    psi[i], theta[i], phi[i] = quat_to_euler_zxz([qw[i], qx[i], qy[i], qz[i]])

# Plot the results
plt.figure(figsize=(12, 6))

# Plot angular velocities
plt.subplot(3, 1, 1)
plt.plot(sol.t, omega1, label='omega1')
plt.plot(sol.t, omega2, label='omega2')
plt.plot(sol.t, omega3, label='omega3')
plt.xlabel('Time (s)')
plt.ylabel('Angular Velocity (rad/s)')
plt.title('Angular Velocity vs Time')
plt.legend()

# Plot Euler angles
plt.subplot(3, 1, 2)
plt.plot(sol.t, psi, label='psi')
plt.plot(sol.t, theta, label='theta')
plt.plot(sol.t, phi, label='phi')
plt.xlabel('Time (s)')
plt.ylabel('Euler Angles (rad)')
plt.title('Euler Angles vs Time')
plt.legend()

# Plot quaternions
plt.subplot(3, 1, 3)
plt.plot(sol.t, qw, label='qw')
plt.plot(sol.t, qx, label='qx')
plt.plot(sol.t, qy, label='qy')
plt.plot(sol.t, qz, label='qz')
plt.xlabel('Time (s)')
plt.ylabel('Quaternion Components')
plt.title('Quaternion Components vs Time')
plt.legend()

plt.tight_layout()
plt.show()

# Function to convert quaternion to rotation matrix
def quat_to_rot_matrix(q):
    """
    Convert a quaternion q to a rotation matrix.
    """
    w, x, y, z = q
    return np.array([
        [1 - 2*(y**2 + z**2), 2*(x*y - z*w), 2*(x*z + y*w)],
        [2*(x*y + z*w), 1 - 2*(x**2 + z**2), 2*(y*z - x*w)],
        [2*(x*z - y*w), 2*(y*z + x*w), 1 - 2*(x**2 + y**2)]
    ])

def animate_t_handle_quat(qw, qx, qy, qz, dt):
    # Specify dimensions for the T-handle
    LAG = 0.5  # cm
    LBC = 4  # cm
    LAD = 2  # cm

    # Initialize arrays to store the T-handle's orientation and key points
    e1 = np.zeros((3, len(qw)))
    e2 = np.zeros((3, len(qw)))
    e3 = np.zeros((3, len(qw)))
    xA, yA, zA = np.zeros(len(qw)), np.zeros(len(qw)), np.zeros(len(qw))
    xB, yB, zB = np.zeros(len(qw)), np.zeros(len(qw)), np.zeros(len(qw))
    xC, yC, zC = np.zeros(len(qw)), np.zeros(len(qw)), np.zeros(len(qw))
    xD, yD, zD = np.zeros(len(qw)), np.zeros(len(qw)), np.zeros(len(qw))

    # Calculate the orientation of the T-handle over time
    for k in range(len(qw)):
        q = [qw[k], qx[k], qy[k], qz[k]]
        R = quat_to_rot_matrix(q)
        e1[:, k] = R @ np.array([1, 0, 0])
        e2[:, k] = R @ np.array([0, 1, 0])
        e3[:, k] = R @ np.array([0, 0, 1])
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

    ani = FuncAnimation(fig, update, frames=len(qw), interval=dt * 1000, blit=True)
    plt.show()

# Example usage
# Assuming `qw`, `qx`, `qy`, `qz` are the quaternion components obtained from the previous solution
animate_t_handle_quat(qw, qx, qy, qz, dt)

