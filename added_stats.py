# print("Hello World!")

# plotly standard imports
import plotly.graph_objs as go
import chart_studio.plotly as py

# Cufflinks wrapper on plotly
import cufflinks

# Data science imports
import pandas as pd
import numpy as np

# Options for pandas
pd.options.display.max_columns = 999

# Display all cell outputs
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

# from __future__ import print_function, division
import matplotlib as mpl
import matplotlib.pyplot as plt


from plotly.offline import iplot
cufflinks.go_offline()

# Set global theme
cufflinks.set_config_file(world_readable=True, theme='pearl')

# Get slugging percentages from Batting data
slugpct = pd.read_csv("https://raw.githubusercontent.com/chadwickbureau/baseballdatabank/master/core/Batting.csv",sep=',')
# Get batters who are sluggers from People data
slugppl = pd.read_csv("https://raw.githubusercontent.com/chadwickbureau/baseballdatabank/master/core/People.csv",sep=',')

# print(slugpct)
# print("Hello World! Py file")

sluggers = slugpct.to_numpy()

# Print players from 2012 San Francisco Giants
for a in sluggers:
    if a[1] == 2012 and a[3] == 'SFN':
        # Take Buster Posey's ('poseybu01') stats, 2012 NL MVP
        if a[0] == 'poseybu01' or a[0] == 'crawfbr01':
            print(a)

# print(slugpct.yearID == 2012)
