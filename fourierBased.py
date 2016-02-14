import cv2
import numpy as np
import dicom
import json
import os
import shutil
import sys
import random
from matplotlib import image
from scipy.ndimage import label
from scipy.ndimage.morphology import binary_erosion
from scipy.fftpack import fftn, ifftn
from scipy.signal import argrelmin, correlate
from scipy.spatial.distance import euclidean
from scipy.stas import linregress
from scipy.optimize import curve_fit
from scipy.interpolate import UnivariateSpline 

NUM_BINS = 100
STD_MULTIPLIER = 2
THRESHOLD_AREA = 250
COMPONENT_INDEX_TOLERANCE = 20
ANGLE_SLICES = 36

#Output Progress
def log_ouput(msg, lvl):
  string = ""
  for in in range(lvl):
    string += " "
  string += msg
  print string
  
#Load Datasets-Short-Axis: Top-Level
def segment_all_datasets():
  
