#!/usr/bin/env python
# coding: utf-8

# # JN6: Practice Activity 5
# In this interactive activity, you will learn about two methods that you can use on a `ReferenceFrame` to define its angular velocity (and, therefore, also its angular acceleration).
# 
# 
# ## Case 1: Given just orientation angle between two frames
# 
# The figure below is that of the rolling disk, which was covered in the lecture (see your notes file titled "6 rigid body kinematics: angular velocities and accelerations.pdf")
# <!-- <img src="Figures/Rolling_Disk.png" height=450 width=450> -->
# ```{figure} Figures/Rolling_Disk.png
# :name: door-wall-modified
# 
# Motion of a rolling disk $D$ relative to ground $A$.
# ```
# You can see that the  information given here is:
# 1. the angle $\theta$ between frames $A$ and $D$; and
# 2. direction of rotation of the disk.
# 
# You can use this information to define the orientation of $D$ and $A$, as follows.
# 
# First we use `dynamicsymbols` to create the variable `theta` to represent the angle shown in the picture:

# In[1]:


from sympy.physics.mechanics import dynamicsymbols, ReferenceFrame
theta = dynamicsymbols('theta')


# Then, we represent $A$ and $D$ by creating two `ReferenceFrame` using the variables `A` and `D`, as shown below:

# In[2]:


A = ReferenceFrame('A')
D = ReferenceFrame('D')


# Then, we can provide information regarding the rotation of `D` relative to `A` by using `D.orient`, as below; this is a method that we apply to the variable `D` with the negative of the angle (can you remember why?):

# In[3]:


D.orient(A, 'Axis', (-theta, A.z))


# The `orient` method takes the following sequence of information in the parantheses:
# 1. Frame of rotation, in this case, `A`
# 2. the type of rotation, in this case it is the `Axis` (however, we will learn to provide it DCMs in the next notebook); and
# 3. a pair of values in round brackets, containing the angle and the specific axis of rotation.
# __ You will get an error (or incorrect result) if you do not provide the information in the order listed above__.
# 
# 
# You can now see that `sympy` has the power to automatically compute $^A\omega^D$. In other words, this is the angular velocity of `D` in `A`; you can see that this has been done by using the `.ang_vel_in` method:

# In[5]:


D.ang_vel_in(A)


# In fact, `sympy` also has the power to automatically compute the angular acceleration of `D` in `A`, as shown below:

# In[6]:


D.ang_acc_in(A)


# `sympy` can also generate $^D {\bf C} ^A$ the direction cosine matrix of $A$ relative to $D$.

# In[7]:


D.dcm(A)


# As you can imagine, this is incredibly powerful because `sympy` can automatically compute the rotational kinematics as long as you provide `sympy` the correct information in the `orient` method: direction of rotation angle (`-theta`), type of rotation (`Axis`), and axis of rotation (`A.z`).

# ## Case 2: If you are only given angular speed and direction of rotation then you should use the `.set_ang_vel`
# In some cases, you are not given an orientation angle. Instead, you are given the angular speed and the direction of rotation. An example of this is the rotating shaft (shown below and also covered in the lecture):
# <!-- <img src="Figures/Rotating_Shaft.png" height=450 width=450>. -->
# ```{figure} Figures/Rotating_Shaft.png
# :name: door-wall-modified
# 
# Motion of a shaft $B$ rotating relative to fixed axis $A$.
# ```
# The shaft is rotating at the constant speed $4$ radian per second. So, from the figure, we can easily infer that the $^A\omega^B = 4 \hat{\bf n} = 4 \hat{\bf a}_z$. Here, we made the assumption that $\hat{\bf n} = 4 \hat{\bf a}_z$. Let's see how we can let provide this information to `sympy`.
# 
# First, we create the $A$ and $B$ frames using `ReferenceFrame`; the frames are assigned the variable names `A` and `B`:

# In[8]:


A = ReferenceFrame('A')
B = ReferenceFrame('B')


# Then, we can can define $^A\omega^B$ using a new method on `B`; this method is called  `set_ang_vel`. This is done as shown:

# In[9]:


B.set_ang_vel(A, 4*A.z)


# The sequence of information in the `set_ang_vel` is:
# 1. The frame relative to which we define the orientation. In this example, it is `A`.
# 2. The vector expression of the angular velocity. In this example, it is `4*A.z`.
# 
# We can examine that the angular velocity is indeed assigned to `B` by using the `ang_vel_in` command (which was described in the above subsection on rolling disk). We can do this in the following way:

# In[10]:


B.ang_vel_in(A)


# $^A\alpha^B$, the angular acceleration of B in A, has also been automatically computed:

# In[11]:


B.ang_acc_in(A)


# This should be zero because the rotation speed is constant i.e., $4$ rad/s.
# 
# Though the information on angular velocity and acceleration is automatically computed, extracting the direction cosine matrix is not possible as the angle is not specified in the problem statement. Thus, if you try to run `B.dcm(A)`, an error message will appear.

# In[12]:


B.dcm(A)


# So, ultimately, the problem and assoicated figure dictates whether one uses `.orient` or `.set_ang_vel` on a `ReferenceFrame` variable in defining the orientation kinematics.
