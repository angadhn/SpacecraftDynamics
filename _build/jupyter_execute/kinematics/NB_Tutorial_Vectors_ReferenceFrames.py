#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Interactive-Textbook" data-toc-modified-id="Interactive-Textbook-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Interactive Textbook</a></span></li><li><span><a href="#How-to-interact-with-this-tutorial" data-toc-modified-id="How-to-interact-with-this-tutorial-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>How to interact with this tutorial</a></span></li><li><span><a href="#Pre-knowledge-for-this-tutorial" data-toc-modified-id="Pre-knowledge-for-this-tutorial-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Pre-knowledge for this tutorial</a></span></li><li><span><a href="#Reference-Frames-and-Vectors" data-toc-modified-id="Reference-Frames-and-Vectors-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Reference Frames and Vectors</a></span><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Initial-program-setup:-get-the-necessary-tools!" data-toc-modified-id="Initial-program-setup:-get-the-necessary-tools!-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Initial program setup: get the necessary tools!</a></span></li><li><span><a href="#Create-the-vector-'v'" data-toc-modified-id="Create-the-vector-'v'-4.3"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>Create the vector 'v'</a></span></li><li><span><a href="#Some-operations-on-vector-'v'" data-toc-modified-id="Some-operations-on-vector-'v'-4.4"><span class="toc-item-num">4.4&nbsp;&nbsp;</span>Some operations on vector 'v'</a></span></li></ul></li><li><span><a href="#Vector-algebra" data-toc-modified-id="Vector-algebra-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Vector algebra</a></span><ul class="toc-item"><li><span><a href="#Addition" data-toc-modified-id="Addition-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Addition</a></span><ul class="toc-item"><li><span><a href="#Activity" data-toc-modified-id="Activity-5.1.1"><span class="toc-item-num">5.1.1&nbsp;&nbsp;</span>Activity</a></span></li></ul></li><li><span><a href="#Multiplication" data-toc-modified-id="Multiplication-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Multiplication</a></span><ul class="toc-item"><li><span><a href="#Scalar-product" data-toc-modified-id="Scalar-product-5.2.1"><span class="toc-item-num">5.2.1&nbsp;&nbsp;</span>Scalar product</a></span></li><li><span><a href="#Dot-product" data-toc-modified-id="Dot-product-5.2.2"><span class="toc-item-num">5.2.2&nbsp;&nbsp;</span>Dot product</a></span></li><li><span><a href="#Cross-product" data-toc-modified-id="Cross-product-5.2.3"><span class="toc-item-num">5.2.3&nbsp;&nbsp;</span>Cross product</a></span><ul class="toc-item"><li><span><a href="#Activity:" data-toc-modified-id="Activity:-5.2.3.1"><span class="toc-item-num">5.2.3.1&nbsp;&nbsp;</span>Activity:</a></span></li></ul></li></ul></li></ul></li><li><span><a href="#Additional-useful-features" data-toc-modified-id="Additional-useful-features-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Additional useful features</a></span><ul class="toc-item"><li><span><a href="#Activity" data-toc-modified-id="Activity-6.1"><span class="toc-item-num">6.1&nbsp;&nbsp;</span>Activity</a></span></li></ul></li></ul></div>

# # Interactive Textbook
# I've written this <span style="color: red;">interactive notebook</span> to help get you started using SymPy for use in DEN4108 Engineering Mechanics: Dynamics. This particular notebook is a tutorial and set of exercises for you to do that will gradually help you start to get the basics of vector algebra using SymPy.
# 
# Each unit of the module has more such notebooks as well as other resources. Work through them at your own pace each week. I hope you enjoy learning to program.
# 
# -Angadh Nanjangud

# # How to interact with this tutorial
# 
# Execute a code cell (such as the one right below this line) by clicking on it
# and simultaneously pressing 'Shift+Enter'. You will then see a new line appear,
# which says `My name is  Bond. James Bond`. You may change the text stored in
# `name` to your name. Recall that `name` is a [variable](NB_Tutorial_variable.ipynb#Definition)
# which stores a [string](NB_Tutorial_string.ipynb#Conceptual-Definition).

# In[1]:


name = 'Bond. James Bond.'
print('My name is ', name)


# All the code cells below can be run in this manner. In spots which have
# activities, you should type in your responses. This will help you assess your
# understanding.
# 
# # Pre-knowledge for this tutorial
# The concepts in computing that you should become familiar with before embarking on this tutorial are covered in three short notebooks on:
# 1. [Variables](NB_Tutorial_variable.ipynb)
# 2. [Strings](NB_Tutorial_string.ipynb)
# 
# # Reference Frames and Vectors
# 
# ## Introduction
# 
# In our first lecture, we have reviewed vectors and reference frames.
# One of the important topics discussed was the component form of representing
# a vector, which allows us to write a vector using its scalar components and
# some unit vectors.
# 
# For example: ${\bf v}= v_1 \hat{\bf{a}}_x + v_2 \hat{\bf{a}}_y + v_3
# \hat{\bf{a}}_z$
# is the representation of a vector ${\bf v}$ using the scalars $v_i$ $(i=1,2,3)$
# and a set of unit vectors $\hat{\bf{a}}_j$ $(j=x,y,z)$. The set of unit vectors
# are called a reference frame, which we shall call $A$, for the sake of this
# notebook- here, we also assume that these vectors have the special property of being orthogonal.
# 
# Engineering dynamicists utilize their understanding of vectors to generate
# models that describe the motion of engineering systems. Some exciting and
# important
# examples of systems analysed using dynamics models are rockets, spacecraft,
# aircraft, drones, etc. As these systems are quite complex, dynamicists have
# developed tools that facilitate their modeling. Another important aspect of a
# dynamicist's work is in the analyses of motion behaviours using these models.
# This also helps in exploring aspects of the design space to improve the
# performance of machines (e.g., robots) or aid in understanding anomalies and
# failures in engineering systems.
# 
# The objective of this notebook is to introduce you to some fundamental tools
# that
# facilitate such complex mathematical modeling of systems using computers. To do
# so,
# we will use a computer's ability to perform algebra (woking with symbols)- this
# is enabled by a symbolic library known as SymPy, which is written in Python.
# Here, we will learn not only to express a vector in its symbolic form but also
# to
# perform routine vector algebra operations (addition and multiplication) in
# SymPy.
# This will allow us to eventually develop a model that describes the motion of
# a spacecraft orbiting the Earth.
# 
# ## Initial program setup: get the necessary tools!
# As with most programming languages, the first few lines are dedicated to
# importing tools that allow us to achieve this notebook's objective.
# For this, we will use SymPy's `symbols` and `ReferenceFrame`.

# In[2]:


from sympy import symbols
from sympy.physics.mechanics import ReferenceFrame


# ## Create the vector 'v'
# 
# We will first create the scalar components of the vector $\bf v$, i.e.,
# $v_i$ $(i=1,2,3)$. It is good practice to declare symbols as real to
# encourage SymPy to provide simpler results- this is why we have included
# `real=True`.

# In[ ]:


v1, v2, v3 = symbols('v1, v2, v3', real=True)


# Then, we create a reference frame- this provides the orthogonal unit vectors for
# constructing general vectors such as $\bf v$.

# In[ ]:


A = ReferenceFrame('A')


# The three orthonormal vectors (orthogonal unit vectors) associated with this
# frame $A$ can be accessed by appending either `.x`, `.y`, or `.z` to it. Let us
# examine each of these.

# In[ ]:


A.x


# In[ ]:


A.y


# In[ ]:


A.z


# Now, we can construct the vector $\bf v$ by multiplying its scalars by the
# frame's
# associated unit vectors. This vector will be stored, as shown below, in the
# variable
# `v`.

# In[ ]:


v = v1*A.x + v2*A.y + v3*A.z


# The vectors stored in variable `v` can be displayed:

# In[ ]:


v


# Now, a little bit of Python and computer programming terminology.
# `v` and `A` appear to the left hand side of `=` in the code snippets above,
# which
# attaches these two letters to a Vector or a ReferenceFrame. In other words,
# `v` and `A` are containers that store something. In computing, such containers
# are
# typically referred to as variables.
# 
# If we are unsure of or wish to learn what kind (or type) of object a variable
# holds,
# Python allows us to request this (and other) details by using a question mark,
# as
# below:

# In[ ]:


get_ipython().run_line_magic('pinfo', 'v')


# The first line of the newly opened window tells us that `v` is a `Vector`. This
# is
# cool because we have just used `symbols` and `ReferenceFrame` to write a vector
# in
# its component form using abstract symbols and not numbers!
# 
# You may now close thenewly opened window in the bottom half of your browser.
# 
# ## Some operations on vector 'v'
# As we are aware, vectors have some important properties. One of these is its
# magnitude and SymPy allows us to access this information easily.
# The scalar magnitude of `v` can be found by:

# In[ ]:


v.magnitude()


# A unit vector in the same direction as $\mathbf{v}$ can also be found with:

# In[ ]:


v.normalize()


# which is equivalent to:

# In[ ]:


v / v.magnitude()


# # Vector algebra
# 
# ## Addition
# To add a new vector, ${\bf w}= w_1 \hat{\bf{a}}_x + w_2 \hat{\bf{a}}_y
# + w_3 \hat{\bf{a}}_z$, to the vector ${\bf v}$ that we created above, we have to do the following steps:

# In[ ]:


w1, w2, w3 = symbols("w1, w2, w3", real=True)
w = w1*A.x + w2*A.y + w3 * A.z
w


# Then, the two vectors can be added:

# In[ ]:


v + w


# ### Activity
# 1. Can you write one line of code to add $\bf v$ to itself?

# In[ ]:


# Enter your code below
v+v


# 2. Can you create a new vector $\bf u$ expressed in a new reference frame $B$?

# In[ ]:


# Enter your code below
B = ReferenceFrame('B')
u1, u2, u3 = symbols("u1, u2, u3", real=True)
u = u1*B.x + u2*B.y + u3 * B.z


# 3. What is the result of adding $\bf u$ to $\bf v$? Does this make sense?

# In[ ]:


# Enter your code below
u + v


# ## Multiplication
# 
# It is quite straightforward to multiply a vector by a scalar. For example:
# 
# ### Scalar product

# In[ ]:


10 * v


# ### Dot product
# Compute the dot product between two vectors:

# In[ ]:


v.dot(v)


# ### Cross product
# Similarly, one can also take the cross products between two vectors:

# In[ ]:


v.cross(v)


# #### Activity:
# Can you write code to compute the dot and cross products product between
# $\bf v$ and $\bf w$?

# In[ ]:


# Enter your code below
v.cross(w)


# # Additional useful features
# 1. The matrix form of both vectors and dyadics can be found if the frame of
# interest is provided.

# In[ ]:


v.to_matrix(A)


# 2. You can find all of the scalar variables present in a vector with
# `free_symbols()`.

# In[ ]:


v.free_symbols(A)


# 3. Partial derivatives of vectors can be computed in the specified reference
# frame.

# In[ ]:


v.diff(v2, A)


# 4. You can substitute numerical values for scalar expressions.

# In[ ]:


v.subs({v1: 1.34, v2: 5})


# Note that this does not alter the vector or the scalars

# In[ ]:


v


# In[ ]:


v1


# In[ ]:


v2


# Thus, we can make use of the new subsitutions by assigning it to a different
# variable.
# Let's call that `z`.

# In[ ]:


z = v.subs({v1: 1.34, v2: 5})
z.subs({5: v2})


# ## Activity
# Run the following code snippet

# In[ ]:


m = v.to_matrix(A)
m.subs({v1: 5})


# Now, probe what type of object `m`. In other words, enter `m?` in the code cell
# below and identify what its `Type`  says:

# In[ ]:


#Enter your code below
get_ipython().run_line_magic('pinfo', 'm')

