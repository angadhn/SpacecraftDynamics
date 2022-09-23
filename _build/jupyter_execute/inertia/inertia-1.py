#!/usr/bin/env python
# coding: utf-8

# # Mass/Inertia Scalars

# - __Mass__: measure of amount of materia in a body. Units of measurement: $kg$, $lb$.
# - __Mass center__: consider a set of particles as shown below which together make up the system of particles $S$:
# 
# The $i^{\text{th}}$ particle has a mass $m_i$
# 
# ```{figure} ./images/1.png
# ---
# name: 1
# ---
# ```
# 
# $S^*$ is a fictitious particle such that:
# <!--
# ```{figure} ./images/2.png
# ---
# name: 2
# width: 400px
# ---
# ```
# -->
# 
# ```{math}
# :label: masscenter_1
# \sum_{i} m_i {\bf p}_i = 0
# ```
# 
# This fictitious particle is called __mass center__. So, how does one locate the mass centre from a point $O$?
# 
# ```{figure} ./images/3.png
# ---
# name: 3
# ---
# ```
# 
# * ${\bf r}^*$; position  vector from $O$ to $S^*$
# * ${\bf q}_n$; position  vector from $O$ to $P_n$ 
# 
# So, the position vector to locate the $n^{th}$ particle is:
# 
# $$
# {\bf p}_n = {\bf r}^* - {\bf q}_n
# $$
# 
# Thus, expanding {eq}`masscenter_1`
# 
# ```{figure} ./images/4.png
# ---
# name: 4
# ---
# ```
# 
# For a continuum:
# 
# ```{figure} ./images/5.png
# ---
# name: 5
# ---
# ```
# 
# ```{figure} ./images/6.png
# ---
# name: 6
# ---
# ```
# 
# where, $dm$ is elemental mass that can be obtained from density $\rho$ and elementar volume $dV$.

# ## Composite theorem for mass centre

# ```{figure} ./images/7.png
# ---
# name: 7
# ---
# ```
# 
# ```{figure} ./images/8.png
# ---
# name: 8
# ---
# ```
# 
# where, 
# 
# * $r^*_i$ is the position vector locating the mass centre of $S_i$, the $i^{\text{th}}$ system of particles.
# 
# * $m_{s_{i}}$ is the mass of $i^{\text{th}}$ system.
# 
# * $r^*$ is the mass centre of the composite system $S$.

# ### Example #1

# ```{figure} ./images/9.png
# ---
# name: 9
# ---
# ```
# 
# **Given**:
# * $F$ and $R$ are the bodies of mass density $\rho\; kgm^{-2}$ and $\sigma\;kgm^{-1}$ respectively.
# * $P$ is a particle of mass $m$.
# 
# **Find**:
# * Mass centre of the combined system.

# ### Example #2

# $F$ is split into two: $F_1$ and $F_2$.
# 
# $m_{F_{1}}$ = $\rho H_a$, is mass of $F_1$.
# 
# $m_{F_{2}}$ = $\rho B_a$, is mass of $F_2$.
# 
# Also, 
# 
# $m_{R}$ = $\sigma L$, is mass of $R$.
# 
# Then,
# 
# ```{figure} ./images/10.png
# ---
# name: 10
# ---
# ```
# 
# Similarly,
# 
# ```{figure} ./images/11.png
# ---
# name: 11
# ---
# ```
# 
# and
# 
# ```{figure} ./images/12.png
# ---
# name: 12
# ---
# ```

# ## Inertia scalar

# For a particle $P$ of mass $m$, we can define a parameter called the inertia scalar. This is defined relative to an arbitrary point $O$. There are two such inertia scalars:
# 
# ```{figure} ./images/13.png
# ---
# name: 13
# ---
# ```

# ### 1. Product of inertia

# #### Notation
# 
# $I^{P/O}_{ab}$ is the product of inertia of $P$ along two lines through point $O$ that are parallel to unit vectors $\hat{n}_a$ and $\hat{n}_b$.
# 
# ```{figure} ./images/14.png
# ---
# name: 14
# ---
# ```
# 
# __8.5__ can be extended for both systems of particles and continua.
# 
# 
# #### Product of inertia of system particles
# 
# ```{figure} ./images/15.png
# ---
# name: 15
# ---
# ```
# 
# #### Product of inertia of continua
# 
# ```{figure} ./images/16.png
# ---
# name: 16
# ---
# ```
# 
# ```{figure} ./images/17.png
# ---
# name: 17
# ---
# ```
# 
# ```{warning}
# In all cases, $I_{ab} = I_{ba}$ because the formula relies on the dot product of vectors.
# ```

# ### 2. Moment of inertia

# ```{figure} ./images/18.png
# ---
# name: 18
# ---
# ```
# 
# #### Notation
# 
# $I^{P/O}_{aa}$ is the moment of inertia of P about a line through point $O$ which is parallel to the unit vector $\hat{n}_a$.
# 
# ```{figure} ./images/19.png
# ---
# name: 19
# ---
# ```
# 
# __8.8__ can be extended to both systems of particles and continua.
# 
# #### Moment of inertia of system of particles
# 
# ```{figure} ./images/20.png
# ---
# name: 20
# ---
# ```
# #### Moment of inertia of system of particles
# 
# ```{figure} ./images/21.png
# ---
# name: 21
# ---
# ```
# 
# ```{figure} ./images/22.png
# ---
# name: 22
# ---
# ```
# 
# #### Example
# 
# ```{figure} ./images/23.png
# ---
# name: 23
# ---
# ```
# 
# * $P$ is a particle of mass $m$.
# * $\hat{n}_x,\;\hat{n}_y,\;\hat{n}_z$ are unit vectors that are mutually orthogonal.
# * $\vec{r} = x\hat{n}_x + y\hat{n}_y + z\hat{n}_z$
# 
# **Find**:
# 
# $$
# I^{P/O}_{xx} \qquad I^{P/O}_{yy} \qquad I^{P/O}_{zz}
# $$
# 
# :::{admonition} Solution
# :class: tip, dropdown
# ```{figure} ./images/24.png
# ---
# name: 24
# ---
# ```
# :::

# ## From inertia scalars to inertia matrix

# - From the previous example, we now have some insight that we will be interested in computing the moments of inertia and products of inertia about a set of unit vectors that make up a reference frame.
# 
# - For this discussion, we assume that the unit vectors are: $\hat{n}_x,\;\hat{n}_y,\;\hat{n}_z$.
# 
# - The inertia scalars can be used to define a square matrix called the inertia matrix.
# 
# **Notation**:
# 
# * $\left[I\right]^{S/O}$ is the inertia matrix of $S$, a system of particles about the point $O$.
# * The diagonal elements of this matrix are the moments of inertia.
# * The off-diagonal elements are the products of inertia.
# * So, the inertia matrix is represented as:
# 
# ```{figure} ./images/25.png
# ---
# name: 25
# ---
# ```
# 
# ```{warning}
# In all cases, $I_{ab} = I_{ba}$ because the formula relies on the dot product of vectors.
# 
# - Rigid body/ continua: The inertia scalars of a rigid body can also be arranged into an inertia matrix.
# ```
