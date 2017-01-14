# Work/solution for exercise 3-1 of "Think Stats"

'''
Something like the class size paradox appears if you survey children and ask 
how many children are in their family. Families with many children are more 
likely to appear in your sample, and families with no children have no chance 
to be in the sample.

Use the NSFG respondent variable NUMKDHH to construct the actual distribution 
for the number of children under 18 in the household.

Now compute the biased distribution we would see if we surveyed the children 
and asked them how many children under 18 (including themselves) are in their 
household.

Plot the actual and biased distributions, and compute their means. As a 
starting place, you can use chap03ex.ipynb.
'''

import nsfg
import first
import math
import numpy
import pandas
import thinkstats2
import thinkplot


# makes three dataframes with data for live births, first babies, and all 
#	others
#live, firstD, others = first.MakeFrames()

'''
dataframes
As we saw in the previous chapter, simple indexing selects a column, returning
a Series:
>>> df['A']
To select a row by label, you can use the loc attribute, which returns a Series:
>>> df.loc['a']
'''

resp = nsfg.ReadFemResp()
numKidsSeries = resp['numkdhh']
nkPMF = thinkstats2.Pmf(numKidsSeries, label='actual')

# plotting the pre-biased histogram
thinkplot.PrePlot()
thinkplot.Hist(nkPMF)
thinkplot.Config(xlabel='kids/household', ylabel='probability')
# thinkplot.Config(xlabel='weeks', ylabel='probability', axis=[27, 46, 0, 0.6])
thinkplot.Show()

# now we bias the set
biasedPMF = nkPMF.Copy(label='biased')
for x, p in nkPMF.Items():
	biasedPMF.Mult(x, x)
biasedPMF.Normalize()

# plotting the biased histogram
thinkplot.PrePlot()
thinkplot.Hist(biasedPMF)
thinkplot.Config(xlabel='kids/household', ylabel='probability')
# thinkplot.Config(xlabel='weeks', ylabel='probability', axis=[27, 46, 0, 0.6])
thinkplot.Show()

'''
Something like the class size paradox appears if you survey children and ask 
how many children are in their family. Families with many children are more 
likely to appear in your sample, and families with no children have no chance 
to be in the sample.

Use the NSFG respondent variable NUMKDHH to construct the actual distribution 
for the number of children under 18 in the household.

Now compute the biased distribution we would see if we surveyed the children 
and asked them how many children under 18 (including themselves) are in their 
household.

Plot the actual and biased distributions, and compute their means. As a 
starting place, you can use chap03ex.ipynb.
'''

# plotting both in the same graph
width = 0.5
thinkplot.PrePlot()
thinkplot.Hist(nkPMF, align='right', width = width)
thinkplot.Hist(biasedPMF, align='left', width = width)
thinkplot.Config(xlabel='kids/household', ylabel='probability')
thinkplot.Show()

#print(type(resp))
#print(type(numKidsSeries))

#axes = resp.axes
#cols = resp.axes[1]
#print(type(cols))
#print(list(cols))

meanActual = nkPMF.Mean()
meanBiased = biasedPMF.Mean()

print("Mean of actual PMF = " + str(meanActual))
print("Mean of biased PMF = " + str(meanBiased))





