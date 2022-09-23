#!/usr/bin/env python
# coding: utf-8

# # Rigid Body Kinematics
# Kinematics or Rigid body kinematics is the study of motion while ignoring the cause of motion. In kinematics, we are interested in "position", "velocity", and “acceleration" and the relationship between them. Therefor, in a physical sense, we are interested in describing the motion of $B$ in $A$ (see {numref}`rigid_body_intro`).
# 
# ```{figure} ./images/13.png
# :name: rigid_body_intro
# 
# Motion of a body $B$ relative to frame $A$.
# ```
# 
# ## Classification of Rigid Body Motion
# 
# ```{figure} ./images/14.png
# ---
# name: 14
# ---
# ```
# Broadly, there are two classifications for rigid body motion:
# - __Translation__: the motion of $B$ in $A$ is a translation if and only if any straight line segment embedded in $B$ remains parallel to itself when observed from $A$ when $B$ moves in $A$. If this condition is not met, then we have to consider the motion as rotation.
# 
# - __Simple rotation__: the motion of $B$ in $A$ is a simple rotation if and only if there exists a unit vector $\hat{\bf n}$ that remains fixed in both $B$ and $A$, as $B$ moves in $A$. Examples in figures below:
# 
# ```{figure} ./images/15.png
# ---
# name: 15
# ---
# (i) Disk (D) is in simple rotation with respect to the ground (A).
# (ii) Shaft (B) is in simple rotation with respect to a fixed axis (A).
# ```
# 
# Coming back to our old example of a door hinged to a wall.
# 
# ```{figure} ./images/16.png
# ---
# name: 16
# ---
# ```
# 
# Here, $\hat{\bf b}_y$ is a unit vector that is fixed in both $B$ and $A$. Using our definition for simple rotation tells us that $\hat{\bf b}_y$ is $\hat{\bf n}$. So, in mathematical notation, we can say:
# <!--
# ```{figure} ./images/17.png
# ---
# name: 17
# ---
# ```-->
# 
# 
# ```{math}
# :label: eqnrb1
# \hat{\bf n} = \hat{\bf b}_y
# ```
# 
# But we must now pause to ask ourselves if there is any other unit vector that is also fixed in both $B$ and $A$? It turns out that there is, indeed, another one fixed in both $B$ and $A$: $\hat{\bf a}_y$. So, we can now also write:
# 
# <!--
# ```{figure} ./images/18.png
# ---
# name: 18
# ---
# ```-->
# 
# ```{math}
# :label: eqnrb2
# \hat{\bf n} = \hat{\bf a}_y
# ```
# Consequently, from Equations {eq}`eqnrb1` and {eq}`eqnrb2`, we get:
# <!--
# ```{figure} ./images/19.png
# ---
# name: 19
# ---
# ```
# -->
# 
# ```{math}
# :label: eqnrb3
# \hat{\bf b}_y = \hat{\bf a}_y
# ```
# 
# :::{admonition} Why is establishing Equation {eq}`eqnrb3` useful and critical?
# :class: tip, dropdown
# So far, we have written the vectors ${\bf v}$ and ${\bf e}$, in terms of the $B$ frame. As a result, they were not functions of $\theta$.
# 
# Expressing the vectors in the unit vectors attached to the A frame requires us to derive relationships between $\hat{\bf a}_i$ and  $\hat{\bf b}_i$, where $(i = x,y,z)$.
# 
# Equation {eq}`eqnrb3` allows us to derive a relationship between $\hat{\bf a}_i$ and $\hat{\bf b}_i$, which then provides a basis for developing the rigid body kinematics.
# :::
# 
# Let us explore how to derive these relationships for the vectors ${\bf e}$ and ${\bf v}$ in the doorwall example (figure is shown again below):
# 
# ```{figure} ./images/16.png
# ---
# name: 16
# ---
# ```
# 
# From the second of Equations in {eq}`eqn1`, we have:
# 
# ```{math}
# :label: eqnrb4
# {\bf e} = -e\hat{\bf b}_y.
# ```
# 
# Further, by using Equation {eq}`eqnrb3` in Equation {eq}`eqnrb4`, we can also see that:
# ```{math}
# :label: eqnrb5
# {\bf e} = -e\hat{\bf a}_y
# ```
# 
# ```{admonition} Terminology
# In the preceding example, $\theta$ is an angle describing the orientation of $B$ relative to $A$ (and vice versa). Thus, it is also called an angular position. Other common ways of referring to it are _orientation angle_ or _attitude angle_.
# ```
# 
# Now, we come to a more involved example, where we will express ${\bf v}$ in terms of the unit vectors of the $A$ frame (using the first of the equations {eq}`eqn1` as the starting point for this discussion):
# 
# ```{math}
# :label: eqnrb6
# {\bf v} = v\hat{\bf b}_x
# ```
# 
# We can now examine the relationships between the unit vectors by drawing only the unit vectors with the vector $\hat{\bf n}$ out of the plane (see figure below this passage). 
# 
# ```{figure} ./images/21.png
# ---
# name: 21
# ---
# ```
# 
# We can then derive the following relationships by examining the lower figure,  comprising only unit vectors:
# 
# <!--
# ```{figure} ./images/20.png
# ---
# name: 20
# ---
# ```-->
# 
# ```{math}
# :label: eqnrb7
# \hat{\bf b}_x& = \cos\theta\hat{\bf a}_x + \cos(90 - \theta) \hat{\bf a}_z\\
# \hat{\bf b}_z& = \cos(90 + \theta)\hat{\bf a}_x + \cos(\theta) \hat{\bf a}_z,\\
# ```
# 
# which can also be written as:
# 
# ```{math}
# :label: eqnrb8
# 
# \hat{\bf b}_x& = \cos\theta\hat{\bf a}_x    + \sin(\theta) \hat{\bf a}_z\\
# \hat{\bf b}_z& = -\sin(\theta)\hat{\bf a}_x + \cos(\theta) \hat{\bf a}_z.\\
# ```
# 
# Then, from the first of {eq}`eqnrb8`:
# 
# ```{math}
# :label: eqnrb9
# {\bf v} = v(\cos{\theta}\hat{\bf a}_x + \sin{\theta}\hat{\bf a}_z)
# ```
# 
# Along with {eq}`eqnrb3`, we have now established the complete relationship between the unit vectors that make up the $B$ frame in terms of the unit vectors of the $A$ frame. While this is very useful, we can take these relationships one step further and write the equations in matrix form as follows:
# 
# <!--
# ```{figure} ./images/22.png
# ---
# name: 22
# ---
# ```-->
# 
# ```{math}
# :label: eqnrb11
# \begin{bmatrix}
# \hat{\bf b}_x\\
# \hat{\bf b}_y\\
# \hat{\bf b}_z\\
# \end{bmatrix} =
# \begin{bmatrix}
# \cos{\theta} & 0 & \sin\theta \\
# 0 & 1 & 0 \\
# -\sin\theta & 0 & \cos\theta \\
# \end{bmatrix}
# \begin{bmatrix}
# \hat{\bf a}_x\\
# \hat{\bf a}_y\\
# \hat{\bf a}_z\\
# \end{bmatrix}
# 
# ```
# 
# Bringing our attention to the second row of the above equation tells us that:
# ```{math}
# :label: eqnrb12
# \hat{\bf b}_y=\hat{\bf a}_y.
# ```
# Visually, this can be interpreted to mean that the door B swings relative to the wall $A$ about the $\hat{\bf b}_y$-axis, which also coincides with the $\hat{\bf a}_y$-axis. In other words, this represents what is known as a simple rotation about the $y$-axis. Similar relationships can also be derived for simple rotations about $x$-axis or $z$-axis. 

# In[ ]:




