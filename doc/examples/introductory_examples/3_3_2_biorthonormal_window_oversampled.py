#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 jaidev <jaidev@newton>
#
# Distributed under terms of the MIT license.

"""
Example from section 3.3.2 of the tutorial.
"""

from tftb.generators.api import fmlin
from tftb.processing.linear import gabor
import matplotlib.pyplot as plt
import numpy as np

N1 = 256
Ng = 33
Q = 4
sig = fmlin(N1)[0]
window = np.exp(np.log(0.005) * np.linspace(-1, 1, Ng) ** 2)
window = window / np.linalg.norm(window)
tfr, dgr, h = gabor(sig, 32, Q, window)
time = np.arange(256)
freq = np.linspace(0, 0.5, 128)
plt.matshow(tfr, aspect='auto', extent=[0, 255, 0, 0.5])
plt.xlabel('Time')
plt.ylabel('Normalized frequency')
plt.title('Squared modulus of the Gabor coefficients')
plt.show()