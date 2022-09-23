#!/usr/bin/env python
# coding: utf-8

# # Theorems for Computing Inertia Matrix $\left[I\right]$

# There are three useful theorems to compute moments of inertia. They are:
# 
# 1. __Rotation theorem__
# 2. __Parallel axis theorem__ (or translation theorem)
# 3. __Composite theorem__
# 
# Let us examine them in further detail.

# ## Rotation theorem

# ```{figure} ./images/26.png
# ---
# name: 26
# ---
# ```
# 
# - $X-Y-Z$ make up a cartesian coordinate system. 
# - $O$ is the origin.
# - $\hat{\bf n}_x,\;\hat{\bf n}_y,\;\hat{\bf n}_z$ are unit vectors directed along $X-Y-Z$ respectively. The unit vectos represent a reference frame $N$.
# 
# Also, the figure shows a rocket which has a reference frame $R$ attached to it. You are given the inertia matrix of the rocket $R$ about $O$ along the unit vectors of frame $N$.
# <!--
# ```{figure} ./images/27.png
# ---
# name: 27
# ---
# ```
# -->
# 
# ```{math}
# :label: IRaboutO
# \begin{bmatrix}
# I
# \end{bmatrix}^{R/O}
# =
# \begin{bmatrix}
# {I_{xx}}^{R/O} & {I_{xy}}^{R/O} & {I_{xz}}^{R/O} \\
# {I_{yx}}^{R/O} & {I_{yy}}^{R/O} & {I_{yz}}^{R/O} \\
# {I_{zx}}^{R/O} & {I_{zy}}^{R/O} & {I_{zz}}^{R/O} \\
# \end{bmatrix}
# ```
# Naturally, the rocket's reference frame ($R$) also has three mutually orthogonal unit vectors: $\hat{\bf r}_x$, $\hat{\bf r}_y$, and $\hat{\bf r}_z$. So, we can define another inertia matrix for $R$ about $O$ along the newly introduced rotating reference frame's unit vectors $\hat{\bf r}_x, \; \hat{\bf r}_y, \; \hat{\bf r}_z$. This matrix and its elements are:
# <!--
# ```{figure} ./images/28.png
# ---
# name: 28
# ---
# ```
# -->
# 
# ```{math}
# :label: JRaboutO
# \begin{bmatrix}
# J
# \end{bmatrix}^{R/O}
# =
# \begin{bmatrix}
# {J_{xx}}^{R/O} & {J_{xy}}^{R/O} & {J_{xz}}^{R/O} \\
# {J_{yx}}^{R/O} & {J_{yy}}^{R/O} & {J_{yz}}^{R/O} \\
# {J_{zx}}^{R/O} & {J_{zy}}^{R/O} & {J_{zz}}^{R/O} \\
# \end{bmatrix}
# ```
# 
# ::::{important}
# We begin by assuming that $R$ is a particle of mass, $m_R$. Then, let us consider a product of inertia from each matrix.
# <!--
# ```{figure} ./images/29.png
# ---
# name: 29
# ---
# ```
# -->
# ```{math}
# :label: IxyRaboutO
# {I_{xy}}^{R/O} = m_R ({\bf p}^*\times\hat{\bf n}_x)\cdot({\bf p}^*\times\hat{\bf n}_y)
# ```
# 
# and
# 
# ```{math}
# :label: JxyRaboutO
# {J_{xy}}^{R/O} = m_R ({\bf p}^*\times\hat{\bf r}_x)\cdot({\bf p}^*\times\hat{\bf r}_y)
# ```
# ${\bf p}^*$ is a position vector from $O$ to the origin of the frame $R$. We know from our discussion on direction cosine matrices that the unit vectors of $R$ can be related to the unit vectors of $N$ as:
# <!--
# ```{figure} ./images/30.png
# ---
# name: 30
# ---
# ```
# -->
# ```{math}
# :label: rCn1
# \begin{bmatrix}
# \hat{\bf r}_x\\
# \hat{\bf r}_y\\
# \hat{\bf r}_z\\
# \end{bmatrix} =
# {}^R\begin{bmatrix}
# C
# \end{bmatrix}^N
# \begin{bmatrix}
# \hat{\bf n}_x\\
# \hat{\bf n}_y\\
# \hat{\bf n}_z\\
# \end{bmatrix}
# ```
# 
# ${}^R\begin{bmatrix}C\end{bmatrix}^N$ is the direction cosine matrix of $N$ in $R$. It is a $3\times3$ matrix, which we shall assume has the following elements:
# 
# <!--
# ```{figure} ./images/31.png
# ---
# name: 31
# ---
# ```-->
# 
# ```{math}
# :label: CRaboutN1
# 
# {}^R\begin{bmatrix}C\end{bmatrix}^N
# =
# \begin{bmatrix}
# C_{11} & C_{12} & C_{13}\\
# C_{21} & C_{22} & C_{23}\\
# C_{31} & C_{32} & C_{33}\\
# \end{bmatrix}
# ```
# 
# So, we can now easily derive:
# <!--
# ```{figure} ./images/32.png
# ---
# name: 32
# ---
# ```
# -->
# ```{math}
# :label: CRaboutN2
# \begin{align}
# \hat{\bf r}_x& = C_{11}\hat{\bf n}_x + C_{12}\hat{\bf n}_y + C_{13}\hat{\bf n}_z\\
# \hat{\bf r}_y& = C_{21}\hat{\bf n}_x + C_{22}\hat{\bf n}_y + C_{23}\hat{\bf n}_z
# \end{align}
# ```
# 
# After substituting Equation {eq}`CRaboutN2` in Equation {eq}`JxyRaboutO` and some algebraic manipulation (show in handwriting below), we can rewrite the product of inertia $J^{R/O}_{xy}$ in its matrix form (shown both in handwriting and as typed Equation {eq}`JxyRaboutmatrixform`). 
# ```{math}
# :label: JxyRaboutmatrixform
# {J_{xy}}^{R/O} =
# \begin{bmatrix}
# C_{11} & C_{12} & C_{13}\\
# \end{bmatrix}
# \begin{bmatrix}
# {I_{xx}}^{R/O} & {I_{xy}}^{R/O} & {I_{xz}}^{R/O} \\
# {I_{yx}}^{R/O} & {I_{yy}}^{R/O} & {I_{yz}}^{R/O} \\
# {I_{zx}}^{R/O} & {I_{zy}}^{R/O} & {I_{zz}}^{R/O} \\
# \end{bmatrix}
# \begin{bmatrix}
# C_{21}\\
# C_{22}\\
# C_{23}\\
# \end{bmatrix}
# ```
# By performing this process for each of the inertia scalars, it can be shown that:
# ```{math}
# :label: rotationTheoremInertia
# \begin{bmatrix}
# J
# \end{bmatrix}^{R/O}
# =
# {}^R\begin{bmatrix}C\end{bmatrix}^N
# \begin{bmatrix}
# I
# \end{bmatrix}^{R/O}
# ({}^R\begin{bmatrix}C\end{bmatrix}^N)^T
# ```
# where $({}^R\begin{bmatrix}C\end{bmatrix}^N)^T$ is the transpose of the DCM of N in R. Equation {eq}`rotationTheoremInertia` is known the `Rotation Theorem for computing inertia matrix'.
# :::{admonition}Hand-calculations to derive {eq}`rotationTheoremInertia`
# :class: tip, dropdown
# 
# ```{figure} ./images/33.png
# ---
# name: 33
# ---
# ```
# 
# ```{figure} ./images/34.png
# ---
# name: 34
# ---
# ```
# ```{figure} ./images/35.png
# ---
# name: 35
# ---
# ```
# 
# ```{figure} ./images/36.png
# ---
# name: 36
# ---
# ```
# :::
# ::::

# ## Parallel axes theorem

# In the previous section we presumed that the rocket was a point mass. What happens if this assumption is relaxed and rockets are better approximated as a system of particles?
# 
# - ${\bf p}^*$ is a position vector from $O$ to $R^*$ (the origin of the frame $R$ and also the mass center of the rocket).
# 
# - ${\bf p}_i$ is a position vector from $O$ to ${P}_i$, the $i^{\text{th}}$ particle on the rocket body.
# 
# - ${\bf r}_i$ is a position vector from $R^*$ to $P_i$. So,
# 
# ```{math}
# :label: posvec_rocket_inertia
# {\bf p}_i = {\bf p}^* + {\bf r}_i 
# ```
# 
# ```{figure} ./images/37.png
# ---
# name: 37
# ---
# ```
# 
# Now, we know that the product of inertia for this system of particles along the $\hat{n}_x,\;\hat{n}_y,\;\hat{n}_z$ directions given by:
# <!--
# ```{figure} ./images/38.png
# ---
# name: 38
# ---
# ```
# 
# The terms highlighted in green go to zero because $\sum_im_ir_i = 0$ by the definition of mass centers.
# 
# ```{figure} ./images/39.png
# ---
# name: 39
# ---
# ```
# -->
# 
# ```{math}
# :label: rocket_Ixy1
# {I_{xy}}^{R/O} = \sum_{i} m_i ({\bf p}_i\times\hat{\bf n}_x)\cdot({\bf p}_i\times\hat{\bf n}_y).
# ```
# 
# Upon substituting Equation {eq}`posvec_rocket_inertia` into Equation {eq}`rocket_Ixy1` and performing algebraic manipulations, we get:
# 
# ```{math}
# :label: rocket_Ixy2
# {I_{xy}}^{R/O} = \sum_{i} m_i ({\bf p}^* \times\hat{\bf n}_x)\cdot({\bf p}^*\times\hat{\bf n}_y) + \sum_{i} m_i ({\bf r}_i\times\hat{\bf n}_x)\cdot({\bf r}_i\times\hat{\bf n}_y).
# ```
# 
# The first term on the RHS of Equation {eq}`rocket_Ixy2` is, in fact, the inertia of $R^*$ about $O$. Similarly, the second term on the RHS of Equation {eq}`rocket_Ixy2` is the moment of inertia of $R$ about $R$^*$. Thus, we can rewrite Equation {eq}`rocket_Ixy2` as:
# 
# ```{math}
# :label: rocket_Ixy3
# {I_{xy}}^{R/O} = {I_{xy}}^{R/R^*} + {I_{xy}}^{R^*/O}.
# ```
# 
# where, $I^{R/R^*}_{xy}$ is the product of inertia of $R$ about the mass center $R^*$. $I^{R^*/O}_{xy}$is the product of inertia of $R^*$ about $O$.
# 
# This result extrapolates to the moment of inertia scalars. For example,
# <!--
# ```{figure} ./images/40.png
# ---
# name: 40
# ---
# ```-->
# ```{math}
# :label: rocket_Ixy4
# {I_{xx}}^{R/O} = {I_{xx}}^{R/R^*} + {I_{xx}}^{R^*/O}
# ```
# and, more generally, to the inertia matrix:
# ```{math}
# :label: rocket_Ixy5
# [I]^{R/O} = [I]^{R/R^*} + [I]^{R^*/O}.
# ```
# <!--
# ```{figure} ./images/41.png
# ---
# name: 41
# ---
# ```
# -->
# 
# :::{important}
# This rule to compute the inertia matrix about some point $O$  is only valid when only we use the mass center as an intermediate transfer point.
# :::

# ## Composite theorem

# ```{figure} ./images/42.png
# ---
# name: 42
# ---
# ```
# If $S$ is a system comprising many smaller systems from the set ${S_1, S_2, ..., S_n}$, the composite theorem to compute an inertia scalar states that:
# ```{math}
# {I_{ab}}^{S/O} = \sum_{i=1}^{n} {I_{ab}}^{S_i/O}
# ```
