#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Overview-of-Practice-Activity" data-toc-modified-id="Overview-of-Practice-Activity-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Overview of Practice Activity</a></span></li><li><span><a href="#Solution" data-toc-modified-id="Solution-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Solution</a></span></li></ul></div>

# # Overview of Practice Activity
# 
# 
# 
# ```{figure} ./images/Problem2.png
# ---
# height: 300
# width: 300
# name: 1
# ---
# Door wall
# ```
# 
# 
# The figure {ref}`1` shows a composite system made up of three slender rods; the total mass of this system is $M$. For this system, you are to derive the inertia matrix of the system about the point O; that is, determine all the 9 elements of $[{\bf I}]^{S/O}$. Recall that:
# 
# $[{\bf I}]^{S/O} = \begin{bmatrix}
# I^{S/O}_{xx} & I^{S/O}_{xy} & I^{S/O}_{xz} \\
# I^{S/O}_{yx} & I^{S/O}_{yy} & I^{S/O}_{yz} \\
# I^{S/O}_{zx} & I^{S/O}_{zy} & I^{S/O}_{zz}
# \end{bmatrix} $
# 
# where the diagonal elements are moment of inertia scalars and off-diagonal elements are product of inertia scalars.
# 
# So, your task reduces to calculating each of these terms and  assembling it in a matrix using sympy's `Matrix` feature.
# 
# 
# __<span style="background-color:cyan">IMPORTANT:</span>__ You are to store your inertia matrix solution in the variable name `I_matrix_of_S_about_O`.
# 
# __Hints:__
# 1. $M$ will be useful to determine the mass of individual sections of the composite system.
# 
# 2. To support your calculations, you are provided  the some information regarding the inertia scalars of a slender rod about its mass center ($G$ in the figure):
# 
# 
# 
# ```{figure} ./images/Problem22.png
# ---
# height: 300
# width: 300
# name: 1
# ---
# Door wall
# ```
# 
# 
# The figure above essentially tells you that the moment of inertia scalar about G in a direction perpendicular to rigid rod's length is $\frac{1}{12}$(mass of the rod)$\cdot$(length of the rod)$^2$.
# 
# Additionally, you are also told that, for this slender rigid rod in the figure: 
# - the moment of inertia about G of along its length is zero.
# - the products of inertia about G in all directions are all zero.

# # Solution

# In[1]:


from sympy import symbols, Matrix

