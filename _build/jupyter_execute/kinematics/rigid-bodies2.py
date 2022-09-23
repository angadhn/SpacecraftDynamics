#!/usr/bin/env python
# coding: utf-8

# ## Angular Velocity and Angular Acceleration

# ### Angular velocity
# 
# Angular velocity is defined as the time rate of change of orientation.
# 
# Angular velocity is denoted using the greek letter omega. For example, in the figure below, ${}^{A}{\boldsymbol \omega}^{B}$ is the angular velocity of B in A
# 
# ```{figure} ./images/42.png
# ---
# name: 42
# ---
# ```
# 
# #### Case 1: Simple Rotation
# 
# The motion of $B$ in $A$ is a simple rotation if and only if there exists a unit vector $\hat{\bf n}$ that remains fixed in both $B$ and $A$ as $B$ moves in $A$. Mathematically, simple rotation leads to
# 
# ```{figure} ./images/43.png
# ---
# name: 43
# ---
# ```
# 
# ##### Examples
# 
# ```{figure} ./images/44.png
# ---
# name: 44
# ---
# ```
# 
# #### Case 2: General 3-D Rotation
# 
# Below, body $B$ is moving freely relative to frame $A$.
# 
# ```{figure} ./images/45.png
# ---
# name: 45
# ---
# ```
# 
# $\hat{\bf b}_x$, $\hat{\bf b}_y$ and $\hat{\bf b}_z$ are rigidly fixed to $B$.
# 
# The angular velocity of body $B$ in frame $A$ is mathematically defined as:
# 
# ```{figure} ./images/46.png
# ---
# name: 46
# ---
# ```
# 
# which can then be written in a more compressed form as:
# 
# ```{figure} ./images/47.png
# ---
# name: 47
# ---
# ```
# 
# where $\omega_x,\;,\omega_y,\;\omega_z$ are scalar components of the angular velocity vector in the $x$, $y$, and $z$ directions respectively.
# 
# 
# #### Addition rule for angular velocity (aka Chain rule for angular velocity)
# Given three bodies $A, B$ and $C$ that move relative to each other and also a fixed reference frame $N$, the following rule is provided to compute the $^N{\boldsymbol \omega}^C$:
# 
# ```{figure} ./images/48.png
# ---
# name: 48
# ---
# ```
# In typeface, this can be written as:
# :::{math}
# ^N{\boldsymbol \omega}^C = {^N{\boldsymbol \omega}^A}+ ^A{\boldsymbol \omega}^B + ^B{\boldsymbol \omega}^C
# :::
# 
# 
# ### Angular acceleration:
# 
# Angular acceleration is the time rate of change of angular velocity vector.
# 
# In the figure above, $B$ is moving freely in $A$. The angular acceleration of $B$ in $A$ is denoted as ${}^{A}{\boldsymbol \alpha}^{B}$. It is defined as:
# 
# $$
# {}^{A}{\boldsymbol \alpha}^{B} = \frac{{}^{A}d}{dt}{}^{A}{\boldsymbol \omega}^{B}
# $$
# 
# Indeed, one must be careful to express the angular velocity in the appropriate reference frame prior to computing its time derivative. Unfortunately, it is not always convenient (or desirable and might even be impossible) to switch between reference frames before computing the derivative. So, some special results are presented to tackle such scenarios, which are presented after the next example.
# 
# #### Example
# 
# The door-wall example is modified to have an additional object: a cat flap $C$ which makes an angle $\phi$ with $\hat{\bf b}_y$.
# 
# ```{figure} ./images/49.png
# ---
# name: 49
# ---
# ```
# 
# You are asked to compute the angular acceleration of the cat flap $C$ with respect to $A$.
# 
# :::{admonition} Solution
# :class: tip, dropdown
# ```{figure} ./images/50.png
# ---
# name: 50
# ---
# ```
# 
# ```{figure} ./images/51.png
# ---
# name: 51
# ---
# ```
# :::
# 
# #### Special results involving time derivatives
# 
# ##### KEY RESULT 1
# 
# As before, $A$ is a fixed reference frame with unit vectors rigidly attached to it, i.e., $\hat{\bf a}_i(i=x,y,z)$. Likewise, $B$ is a rigid body with unit vectors rigidly attached to it, i.e., $\hat{\bf b}_i(i=x,y,z)$.
# 
# ```{figure} ./images/52.png
# ---
# name: 52
# ---
# ```
# 
# $\bf v$ is an arbitrary vector that is fixed in $B$ and given in its component form by:
# 
# ```{figure} ./images/53.png
# ---
# name: 53
# ---
# ```
# 
# $v_1, v_2, v_3$ are the scalar components of $\bf v$ in frame $B$ and as it is fixed in $B$ it follows:
# 
# ```{figure} ./images/54.png
# ---
# name: 54
# ---
# ```
# 
# ```{figure} ./images/55.png
# ---
# name: 55
# ---
# ```
# 
# ###### Example
# 
# We will prove key result 1 (boxed in red above) is true for a trivial case: _simple rotation_.
# 
# ```{figure} ./images/56.png
# ---
# name: 56
# ---
# ```
# 
# As before, $A$ is a fixed reference frame with unit vectors rigidly attached to it, i.e., $\hat{\bf a}_i(i=x,y,z)$.
# 
# Likewise, $B$ is a rigid body with unit vectors rigidly attached to it, i.e., $\hat{\bf b}_i(i=x,y,z)$.
# 
# $B$ is hinged to $A$ such that it is in simple rotation, such that:
# 
# ```{figure} ./images/57.png
# ---
# name: 57
# ---
# ```
# 
# $\bf v$ is an arbitrary vector that is fixed in $B$ and given in its component form by: ${\bf v} = v_1\hat{\bf b}_x$
# 
# Prove that:
# 
# ```{figure} ./images/58.png
# ---
# name: 58
# ---
# ```
# 
# :::{admonition} Solution
# :class: tip, dropdown
# ```{figure} ./images/59.png
# ---
# name: 59
# ---
# ```
# :::
# 
# ##### KEY RESULT 2
# 
# As before, $A$ is a fixed reference frame with unit vectors rigidly attached to it, i.e., $\hat{\bf a}_i(i=x,y,z)$. Likewise, $B$ is a rigid body with unit vectors rigidly attached to it, i.e., $\hat{\bf b}_i(i=x,y,z)$.
# 
# ```{figure} ./images/52.png
# ---
# name: 52
# ---
# ```
# 
# ${\bf v}$ is an arbitrary vector that is moves relative to both $A$ and $B$. It is in its component form by:
# 
# ```{figure} ./images/60.png
# ---
# name: 60
# ---
# ```
# 
# :::{admonition} Proof
# :class: tip, dropdown
# ```{figure} ./images/61.png
# ---
# name: 61
# ---
# ```
# 
# This is a very powerful formula. However, it relies on our ability to derive an expression for the angular velocity vector in an appropriate frame. We will now use it in our cat flap example.
# :::
# 
# ###### Example
# 
# ```{figure} ./images/62.png
# ---
# name: 62
# ---
# ```
# 
# You are asked to find angular acceleration of the cat flap $C$ with respect to $A$ using **key result 2**.
# 
# :::{admonition} Solution
# :class: tip, dropdown
# ```{figure} ./images/63.png
# ---
# name: 63
# ---
# ```
# 
# we may then invoke KEY RESULT 2 to rewrite the right hand-side as
# 
# ```{figure} ./images/64.png
# ---
# name: 64
# ---
# ```
# 
# This angular velocity of $C$ in $A$ can be computed using the chain rule given by Equation $6.1$ as:
# 
# ```{figure} ./images/65.png
# ---
# name: 65
# ---
# ```
# :::
# 
# <!--```{figure} ./images/66.png
# ---
# name: 66
# ---
# ```-->
