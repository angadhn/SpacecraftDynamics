#!/usr/bin/env python
# coding: utf-8

# # Introduction

# In the most general sense, *dynamics* is the study of properties or parameters that evolve or change with respect to some other parameter. For example, the field of population dynamics studies the change of animal or human populations. In the context of this text and class, we will study parameters describing the motion of bodies. More often than not, we will be interested in the changes of parameters with respect to time.
# 
# At a physical level, our focus will be on the motion of bodies, which we assume can be categorized under two classes: 
# 
# 1. **Particles**: These are objects that can be modeled as point masses. They have negligible dimension. 
# 
# 2. **Rigid bodies**: These are objects that have some predefined constant shape. The distances between all points of a rigid body remain constant for all time, even when a force is applied to them. 
# 
# This module could also be called _Computational Rigid Body Dynamics_. Studying the dynamics involving the motion of particles and bodies has two distinct parts:
# 
# 1. **Kinematics**: the study of the geometry or mathematics of motion, without taking into consideration any forces that cause said motion. The parameters of interest here are positions, velocities, and accelerations. This is also called rigid body motion or rigid body kinematics.
# 
# 2. **Kinetics**: the study of motion while accounting for any forces causing the motion by using Newton's laws.
# 
# ```{figure} ./images/1.png
# ---
# name: 1
# ---
# ```
