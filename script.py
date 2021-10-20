from pandas import *
from numpy import *
from re import *
from seaborn import *
from matplotlib.pyplot import *
from warnings import *

simplefilter('ignore')

data = read_csv("Language Detection.csv")
data.head(10)