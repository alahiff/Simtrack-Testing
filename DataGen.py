#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 15:24:08 2022

@author: vgopakum
"""

# %%
import os
import numpy as np
from pyDOE import lhs 
from tqdm import tqdm 

from matplotlib import pyplot as plt 
from SimRun import run_sim

# %%

n_sims = 10000  
lb = np.asarray([np.pi, 0.1, 1.0, 0.25])
ub = np.asarray([4*np.pi, 1.0, 8.0, 0.75])

params = lb + (ub - lb) * lhs(4, n_sims)

# %%

u_dataset = []
for ii in tqdm(range(n_sims)):
    u_dataset.append(run_sim(ii, params[ii,0], params[ii,1], params[ii,2], params[ii,3]))

u_dataset = np.asarray(u_dataset)

# %%
# np.savez(os.getcwd() + '/Data/' + 'ConvDiff_u.npz', u = u_dataset, params=params)