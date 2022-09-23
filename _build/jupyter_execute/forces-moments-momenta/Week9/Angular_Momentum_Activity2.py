#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Problem-2:-Angular-Momentum-of-System-of-Particles" data-toc-modified-id="Problem-2:-Angular-Momentum-of-System-of-Particles-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Problem 2: Angular Momentum of System of Particles</a></span></li><li><span><a href="#Solution" data-toc-modified-id="Solution-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Solution</a></span></li></ul></div>

# # Problem 2: Angular Momentum of System of Particles
# 
# <img src="Figures/Problem2.png" height=500 width=500>
# 
# The system of four particles has the indicated masses, positions, velocities, and external forces as shown in the figure above. For now, you can ignore the forces; we will revisit this in the next week's activities.
# 
# Your task is to compute the angular momentum of this system of particles about two points:
# 1. the point O.
# 2. the system's mass centre (so you will have to compute this). You can assume this point is called G.
# 
# You may makes use of all the tools you have learned so far in SymPy to complete your work.

# # Solution

# In[1]:


from sympy import symbols, sin, cos
from sympy.physics.mechanics import ReferenceFrame, Point, dynamicsymbols


# In[ ]:




