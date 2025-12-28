
# -*- coding: utf-8 -*-
"""
Scopesim extension

@author: Anjali Shivani
"""

#%% SECTION : LIBRARIES
import os
import pytest
import scopesim
import synphot
import numpy as np
import astropy
from astropy.io.fits import HDUList
from matplotlib import pyplot as plt
from matplotlib.colors import LogNorm
from scopesim import rc
from scopesim.source.source_templates import star_field
import scopesim_templates as sim_tp
from scopesim.optics.fov_manager import FOVManager

#%% SECTION : CALLING DREAMS PACKAGE

'''
Call the dreams

'''

PLOTS = True

if rc.__config__["!SIM.tests.run_integration_tests"] is False:
    pytestmark = pytest.mark.skip("Ignoring DREAMS integration tests")

# Set TOP_PATH to the directory containing the DREAMS package
TOP_PATH = r"C:\Users\dell\Desktop"
rc.__config__["!SIM.file.local_packages_path"] = TOP_PATH

# Adjust the PKGS dictionary to reflect the correct path
PKGS = {"DREAMS": os.path.join(TOP_PATH, "DREAMS")}

# Verify the path to the DREAMS package
if not os.path.exists(PKGS["DREAMS"]):
    raise FileNotFoundError(f"DREAMS package not found at {PKGS['DREAMS']}")
else:
    print("DREAMS package found at:", PKGS["DREAMS"])
