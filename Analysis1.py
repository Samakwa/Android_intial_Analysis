from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('ContextData_Analysis.csv')

actions=[]
for index, row in df.iterrows():

    a = []
    p = list(a)
    k = []
    #demand1 =[]
    actions.append(row[3])

#for item in actions:
#    print (actions)

"""
def count_context(seq) -> dict:
    #Tally elements from `seq`.
    hist = {}
    for i in seq:
        hist[i] = hist.get(i, 0) + 1
        return hist
"""

output1= Counter(actions)
#output1= count_context(actions)


print (output1)

with open('sorted_actions.txt','w') as file:
    file.write("Android_context = { \n")
    for k in sorted (output1.keys()):
        file.write("'%s':'%s', \n" % (k, output1[k]))
    file.write("}")
    
"""
np.random.seed(444)
np.set_printoptions(precision=3)

d = np.random.laplace(loc=15, scale=3, size=500)
# An "interface" to matplotlib.axes.Axes.hist() method
n, bins, patches = plt.hist(x=d, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('My Very Own Histogram')
plt.text(23, 45, r'$\mu=15, b=3$')
maxfreq = n.max()
# Set a clean upper y-axis limit.
plt.ylim(top=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
plt.show()
"""