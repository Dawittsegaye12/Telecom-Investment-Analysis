import numpy as np
import pandas as pd

# Log Transformation Function
def log_transform_column(column):
    return np.log1p(column)

# Square Root Transformation Function
def sqrt_transform_column(column):
    return np.sqrt(np.abs(column))