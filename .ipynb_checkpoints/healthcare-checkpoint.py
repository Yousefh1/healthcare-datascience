import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Read in the data
healthcare = pd.read_csv('healthcare.csv')

# Examine the data
print(healthcare.head())