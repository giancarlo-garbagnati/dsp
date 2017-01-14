# Work/solution for exercise 2-4 of "Think Stats"

'''
Using the variable totalwgt_lb, investigate whether first babies are lighter
or heavier than others. Compute Cohen’s d to quantify the difference between
the groups. How does it compare to the difference in pregnancy length?
'''

'''

'''

import nsfg
import first
import math

'''
Cohen's d

Another way to convey the size of the effect is to compare the difference
between groups to the variability within groups. Cohen’s d is a statistic 
intended to do that; it is defined

d = (x_1 − x_2) / s
  
where x_1 and x_2 are the means of the groups and s is the “pooled standard 
deviation”. 
'''

'''
Pooled Standard Deviation

SD_pooled = sqrt( (SD1^2 + SD2^2) / 2 )

http://www.statisticshowto.com/pooled-standard-deviation/
'''

'''
Numpy.series information:
http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.html

Pandas.DataFrame information:
http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html
'''

# from the book
def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d

# calculates the effect size using's Cohen's d using a different formula
#  I just ended up using the book formula because the solution is close but
#  different than what's provided in the book
def cohenD(g1, g2):
	# first we calculate the difference between means                          
	meanDiff = g1.mean() - g2.mean()

	# now we calculate the pooled standard deviation:
	# SD_pooled = sqrt( (SD1^2 + SD2^2) / 2 )
	SD_pooled = math.sqrt( ( g1.std()**2 + g2.std()**2 ) / 2 )
	#SD_pooled = math.sqrt( ( g1.var() + g2.var() ) / 2 )
	'''
	SD1 = g1.std()
	SD2 = g2.std()
	n1 = len(g1)
	n2 = len(g2)
	SD_pooled = math.sqrt( ( (n1-1)*SD1 + (n2-1)*SD2 ) / (n1+n2-2) )
	'''

	# return the difference of means divided by the pooled standard deviation
	return meanDiff / SD_pooled


# makes three dataframes with data for live births, 
#  first babies, and all others
live, firstD, others = first.MakeFrames()

# print(first.totalwgt_lb)
# print(type(first))
# print(type(first.totalwgt_lb))
# print(first.totalwgt_lb.mean())

firstTotalWgt = firstD.totalwgt_lb
othersTotalWgt = others.totalwgt_lb
firstPregLen = firstD.prglngth
othersPregLen = others.prglngth

'''
Using the variable totalwgt_lb, investigate whether first babies are lighter
or heavier than others. Compute Cohen’s d to quantify the difference between
the groups. How does it compare to the difference in pregnancy length?
'''

#print(live.axes)
CohenDTotalWgt = CohenEffectSize(firstTotalWgt, othersTotalWgt)
print("Cohen's d for total weight between first babies and others (in lb): ")
print(CohenDTotalWgt)
print("Cohen's d for total weight between first babies and others (in oz): ")
print(CohenDTotalWgt*16)
#print(cohenD(firstTotalWgt, othersTotalWgt))

print("Cohen's d for pregnancy length between first babies and others: ")
print(CohenEffectSize(firstPregLen, othersTotalWgt))


# resp = ReadFemResp()