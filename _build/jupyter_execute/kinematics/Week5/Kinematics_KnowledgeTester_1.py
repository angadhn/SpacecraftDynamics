#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Knowledge-Tester-1" data-toc-modified-id="Knowledge-Tester-1-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Knowledge Tester 1</a></span></li></ul></div>

# # Knowledge Tester 1
# 
# In L4PA6, you learned how to compute the direction cosine matrices between different reference frames to generate the angular velocity and acceleration of one frame with respect to another. In this activity, you are to perform the orientation kinematics for the wall-door-cat flap system shown below.
# 
# <img src="Figures/CatFlap_Door_Wall.png" height=450 width=450>
# 
# Specifically, you are to compute the following in the A-frame and also the B-frame:
# 1. $^A\omega^C$ and store it in a variable named `A_w_C_a_frame` and `A_w_C_b_frame`; and
# 2. $^A\alpha^C$ and store it in a variable named `A_alpha_C_a_frame` and `A_alpha_C_b_frame`.
# 
# You are to do this entire exercise by creating a variable that stores the direction cosine matrix using sympy's  `Matrix` feature.

# In[1]:


from sympy import symbols, sin, cos, Matrix
from sympy.physics.mechanics import dynamicsymbols, ReferenceFrame, init_vprinting
init_vprinting()

