#!/usr/bin/env python
# coding: utf-8

# # Forces, Moments, and Torques

# Vectors may or may not have what is called a "line of actions". This leads to two classifications of vectors:
# 
# ## Bound vector
# 
# __Bound vector__ is bound to act along a certain line in space, it is said to be bound (to its line of action, of course). As a result, it is acting on a certain point in space. The figure below illustrates an example, the force $F$ acts on the body B at a specific point $P$, which lies on the line of action of $F$. Thus, $F$ is a bound vector.
# 
# ```{figure} ./images/1.png
# ---
# name: 1
# ---
# ```
# 
# ## Free vector
# 
# __Free (or unbound) vector__ is a vector that is not bound to a line of action. A good example of this is the angular velocity vector that acts on a body. The angular velocity of a body has a magnitude and direction but does not act at a specific point; this is because the angular velocity is the same at any location on a single rigid body.
# 
# ```{figure} ./images/2.png
# ---
# name: 2
# ---
# ```

# ## Moments
# 
# If a vector is classified as a bounded one, then one can define a parameter called the moment for this bound vector about a specific point. For example, in the figure below, we can define a moment of the force, $F$, about the point $O$.
# 
# ```{figure} ./images/3.png
# ---
# name: 3
# ---
# ```
# 
# where,
# 
# - $r^{OP}$ is the position vector from $O$ to $P$.
# - $M^{F/O}$ is the moment of $F$ about $O$.
# 
# Also, the magnitude of the moment can be determined as:
# 
# ```{figure} ./images/4.png
# ---
# name: 4
# ---
# ```
# 
# where, 
# 
# - $d$ is the component of $r^{OP}$ perpendicular to $F$.
# 
# So, we can see that moment of a force yields a vector. It is obtained from the cross product between a position vector and a force. There is no such thing as a moment for free vectors.
# 
# ## Resultant of a set of vectors
# 
# Consider $S$, a set of vectors $<v_{1}, v_{2}, \ldots, v_{n}>$, 
# 
# ```{figure} ./images/5.png
# ---
# name: 5
# ---
# ```
# 
# the resultant of this set of vectors is the vector sum of the elements of the set.
# 
# ```{figure} ./images/6.png
# ---
# name: 6
# ---
# ```
# 
# If the vectors are bounded, we can find the moment of the set of vectors about some point $P$:
# 
# 
# ```{figure} ./images/7.png
# ---
# name: 7
# ---
# ```
# 
# ```{note}
# The set comprised any bound vectors and they were not necessarily a force. However, the developments do naturally apply to forces quite readily as they are bound vectors.
# ```
# 
# ## A Key Theorem on Moments
# 
# Given the sets of vectors and the point $P$ (as discussed in the preceding section), we can find the moment of the set of vectors about some other point $Q$ (see figure below) using a theorem (shown below the figure) that makes  use of the resultant of the set $R$.
# 
# ```{figure} ./images/8.png
# ---
# name: 8
# ---
# ```
# 
# ## Couple
# 
# A set of bound vectors with zero resultant is said to be a couple. It is worth reminding yourself again that a couple is not a vector; it is a set of vectors. A couple can contain as many vectors as needed to satisfy the condition of zero resultant. The minimum number of vectors in a couple is two; this is called a _simple couple_, where the two components are equal in magnitude and oppositely directed.
# 
# ### Examples
# 
# ```{figure} ./images/9.png
# ---
# name: 9
# ---
# ```
# 
# ### Torque of a couple
# 
# - It is the moment of a couple about an arbitrary point in space.
# - A torque is a vector.
# 
# 
# ## Equivalence
# 
# This is another important concept in dynamics that applies to sets of vectors. Two sets of vectors, $S_1$ and $S_2$, are said to be equivalent if and only if:
# 
# -  The resultant of $S_1$ is identical to the resultant of $S_2$.
# -  The moment of $S_1$ about some point $O$ is identical to the moemnt of $S_2$ about the same point $O$.
# 
# ```{note}
# If the sets have the same moments about $O$, they will have the same moments about any other point, as well.
# ```
# 
# ## Replacement
# 
# If we have two sets of bound vectors that are equivalent (the conditions for this are discussed above), then in the context of rigid body dynamics one of the sets can always be __replaced__ by the other __equivalent__ set. In other words, either set of vectors can eb called a __replacement__ of the other.
# 
# If two couples have equal torques, then they are replacement of each other because:
# - The resultant $s$ of couples are zero; and
# - They have the same moment (or torque) about any point.
# 
# ### Pictorial example
# 
# Consider the body $B$ with a point $P$ with only a set of forces $<F_{1}, F_{2}, F_{3}, F_{4}>$ acting on it as shown below:
# 
# ```{figure} ./images/10.png
# ---
# name: 10
# ---
# ```
# 
# These forces can be replaced by another equivalent set; this set consists of:
# - $F$ A single force through $P$, which has the same resultant as the above set of forces.
# - $T$: A torque of couple with the same moment about $P$, as the set of forces $F_{1}, F_{2}, F_{3}, F_{4}$.
# 
# ```{figure} ./images/11.png
# ---
# name: 11
# ---
# ```
# 
# Though we have described everything above in the context of forces and moments of force, the developments apply to vectors more generally. In other words, one set of bound vectors can be replaced by another set; this second set consists of one bound vector (i.e., the resultant of the first set) and a torque of a couple.
