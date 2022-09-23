#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Problem-1:-Kinetics-of-a-Particle" data-toc-modified-id="Problem-1:-Kinetics-of-a-Particle-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Problem 1: Kinetics of a Particle</a></span><ul class="toc-item"><li><span><a href="#Previous-solution" data-toc-modified-id="Previous-solution-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Previous solution</a></span><ul class="toc-item"><li><span><a href="#The-theory" data-toc-modified-id="The-theory-1.1.1"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>The theory</a></span></li><li><span><a href="#Computing-the-solution" data-toc-modified-id="Computing-the-solution-1.1.2"><span class="toc-item-num">1.1.2&nbsp;&nbsp;</span>Computing the solution</a></span></li></ul></li></ul></li><li><span><a href="#This-solution" data-toc-modified-id="This-solution-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>This solution</a></span></li></ul></div>

# # Problem 1: Kinetics of a Particle
# 
# <img src="Figures/Problem1.png" height=300 width=300>
# 
# A small sphere has the position and velocity indicated in the figure and is acted upon by the force $\bf F$. In last week's activity, you have already determined the angular momentum of this particle about point O. Now, you are asked to compute the time derivative of the angular momentum of this particle about point O.
# 
# __Major hint__: It should not be zero; you will need to find the answer to this using the force provided to you.
# 
# As always, you may makes use of all the tools you have learned so far in SymPy to complete your work. But you can also do this whole problem by hand.

# ## Previous solution

# ### The theory
# We have the definition for angular momentum of a generic particle $P_i$ about $O$:
# 
# ${\bf H}^{P/O} \triangleq {\bf r}^{OP} \times m_{P} ^N{\bf v}^{P}$
# 
# , where:
# 
# ${\bf r}^{OP}$ is the position vector from a point $O$ to $P$;
# 
# $m_{P}$ is the mass of $P$; and
# 
# $^N{\bf v}^{P}$ is the velocity of $P$ with respect to a reference frame $N$.
# 
# So, now, we can turn to the features of `sympy` to compute the angular momentum.
# 
# ### Computing the solution

# In[1]:


from sympy import symbols, sin, cos
from sympy.physics.mechanics import ReferenceFrame, Point, dynamicsymbols
N = ReferenceFrame('N')
P = Point('P')
m_P = 2 # mass of P
r_OP = 3*N.x + 6*N.y + 4*N.z
P.set_vel(N, 5*N.y)
N_v_P = P.vel(N)
angular_momentum = r_OP.cross(m_P*N_v_P)
angular_momentum


# # This solution

# In[ ]:




