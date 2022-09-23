#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Knowledge-Tester-2" data-toc-modified-id="Knowledge-Tester-2-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Knowledge Tester 2</a></span></li></ul></div>

# # Knowledge Tester 2
# <img src="Figures/Particle_sliding_on_Double_Pendulum.png" height=300 width=300>
# 
# This notebook uses the example of a particle $P$ sliding on a double pendulum (see figure above); this system was first presented to you in the file "7 Particle Kinematics". Your objective is to compute:
# 1. $^N{\bf a}^P$, acceleration of $P$ in $N$. __You should save the final answer in a variable named `N_a_P_vector`__ ; and
# 2. $^A{\bf a}^P$, acceleration of $P$ in $A$.  __You should save the final answer in a variable named `A_a_P_vector`__.
# 
# __You are to complete this task using the appropriate velocity/acceleration transfer theorems and express all your answers in the unit vectors attached to the $A$ frame.__
# 
# Other suggestions for variable names that will help you in your computation of the accelerations are:
# 1.  `l_scalar` that represents $l$, the length of the links $A$ and $B$; 
# 2. `theta_1_scalar` to represent  $\theta_1$;
# 3. `theta_2_scalar` to represent $\theta_2$; and
# 4. `x_scalar` to represent $x$; and
# 5. `N` to represent the reference frame $N$; and
# 6. `A` to represent the reference frame $A$; and
# 7. `B` to represent the reference frame $B$; and
# 8. `O` to represent the point $O$; and
# 9. `Q` to represent the point $Q$; and
# 10. `P` to represent the point $P$.
# 
# Note that you have to choose which of the variables are time-varying. Please enter all of your work in the code cell below and 

# In[1]:


from sympy import symbols, sin, cos
from sympy.physics.mechanics import dynamicsymbols, ReferenceFrame, init_vprinting
init_vprinting()

