from pandas import *
from numpy import *
from re import *
from seaborn import *
from matplotlib.pyplot import *
from warnings import *

simplefilter('ignore')

data = read_csv("X:\projects\Language Detection in Python\Language Detection.csv")
data.head(10)