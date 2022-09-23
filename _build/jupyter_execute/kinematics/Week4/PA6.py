#!/usr/bin/env python
# coding: utf-8

# # JN7: Practice Activity 6
# 
# <!-- <img src="Figures/CatFlap_Door_Wall.png" height=500 width=500> -->
# ```{figure} Figures/CatFlap_Door_Wall.png
# :name: catflap-door-wall
# 
# Motion of catflap $C$ relative to the door $B$ and wall $A$.
# ```
# 
# This notebook extends the the door-wall example (see {numref}`catflap-door-wall`) by introducing a cat flap $C$. It is attached to the door $B$ and makes an angle of $\theta$ with the vertical of $B$ (i.e. $\hat{\bf b}_y$). Activity L3PA4  is to find angular acceleration of the cat flap C with respect to A, i.e., $^A\alpha^C$. Which is also shown at the very end of the file "6 Rigid body kinematics: angular velocities and angular accelerations.pdf" 

# # Create time-varying scalars using `dynamicsymbols`
# As was explained in L3PA1, the angle $\theta$ between $A$ and $B$ changes with time. Similarly, the angle $\phi$ between $B$ and $C$ also changes with time. Thus, we create both using `dynamicsymbols` as shown below:

# In[1]:


from sympy.physics.mechanics import dynamicsymbols, ReferenceFrame
from sympy import sin, cos
theta, phi = dynamicsymbols('theta phi')
thetadot, phidot = dynamicsymbols('theta phi',1) # gives the first time derivative of the angles


# We can examine the variables `thetadot` and `phidot` to ensure that they are time derivatives of `theta` and `phi`:

# In[3]:


thetadot


# In[ ]:


phidot


# # Creating Reference Frames for $A, B,$ and $C$
# This is a trivial step at this point as we have learned how to create reference frames:

# In[ ]:


A = ReferenceFrame('A') # wall frame
B = ReferenceFrame('B') # door frame
C = ReferenceFrame('C') # cat flap frame


# # Computing $^A\alpha^C$
# ## Approach 1: $^A\alpha^C \triangleq \frac{^A d}{dt}\bf ^A\omega^C$
# This subsection implements the first approach of computing $^A\alpha^C$ using $^A\omega^C$, which must expressed in the A-frame so that the derivative can be computed.
# 
# First, we must compute  $^A\omega^C$ using the chain rule:
# <!-- <img src="Figures/ChainRule.png" width ="250" height=250> -->
# ```{figure} Figures/ChainRule.png
# ```
# 
# The table below shows the  mapping used between math symbols and their equivalent variable names for computing with `sympy`. __Please note that we append `_approach1` for good bookkeeping as we are going to use other approaches__:
# 
# |Mathematical Symbol| Equivalent Variable Name|
# |-----|-------|
# |$^A\omega^B$|`A_omega_B_approach1`| 
# |$^B\omega^C$|`B_omega_C_approach1`| 
# |$^A\omega^C$|`A_omega_C_approach1`|
# |$^A\omega^C$|`B_alpha_C_approach1`| 

# From the lecture notes, we have the following: 
# 
# <!-- <img src="Figures/AwB_Approach_1.png" width ="250" height=250> -->
# ```{figure} Figures/AwB_Approach_1.png
# ```
# <!-- <img src="Figures/BwC_Approach_1.png" width ="500" height=500> -->
# ```{figure} Figures/BwC_Approach_1.png
# ```
# which can both be written in code form below:

# In[ ]:


A_omega_B_approach1 = - thetadot*A.y
B_omega_C_approach1 = - phidot * (cos(theta)*A.x + sin(theta)*A.z)


# Then, we compute the $^A\omega^C$ by the aforementioned chain rule:

# In[ ]:


A_omega_C_approach1 = A_omega_B_approach1 + B_omega_C_approach1 # Chain rule
A_omega_C_approach1


# Taking the time derivative from $A$ (i.e., $\frac{^Ad}{dt}$) of `A_omega_C_approach1` will give us $^A\alpha^C$, as shown below:

# In[ ]:


A_alpha_C_approach1 = A_omega_C_approach1.dt(A)
A_alpha_C_approach1


# ## Approach 2: Using key result 2 from lecture notes

# Our goal in this subsection is to use an alternate approach to computing $^A\alpha^C$: by using key rule 2 as shown below:
# 
# <!-- <img src="Figures/KeyRule2.png" width ="500" height=500> -->
# ```{figure} Figures/KeyRule2.png
# ```
# In the second approach, we again make use of chain rule to compute the $^A\omega^C$; however, we express all the angular velocities in the B-frame (as done in the notes):
# 
# <!-- <img src="Figures/Omega_Approach_2.png" height=250 width=250> -->
# ```{figure} Figures/Omega_Approach_2.png
# ```
# 
# This is implemented below:

# In[ ]:


A_omega_B_approach2 = - thetadot*B.y
B_omega_C_approach2 = - phidot * B.x
A_omega_C_approach2 = A_omega_B_approach2 + B_omega_C_approach2 # Chain rule again


# Then, we implement key result 2 to compute $^A\alpha^C$ as shown below:

# In[ ]:


A_alpha_C_approach2 = A_omega_C_approach2.dt(B) + A_omega_B_approach2.cross(A_omega_C_approach2)
A_alpha_C_approach2

