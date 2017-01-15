

'''
In the BRFSS (see Section 5.4), the distribution of heights is roughly normal 
with parameters µ = 178 cm and σ = 7.7 cm for men, and µ = 163 cm and 
σ = 7.3 cm for women.

In order to join Blue Man Group, you have to be male between 5’10” and 6’1” 
(see http://bluemancasting.com). What percentage of the U.S. male population 
is in this range? Hint: use scipy.stats.norm.cdf.
'''

'''
http://stackoverflow.com/questions/20864847/probability-to-z-score-and-vice-versa-in-python

p = 0.95
z = 1.96

>>> import scipy.stats as st
>>> st.norm.ppf(.95)
1.6448536269514722
>>> st.norm.cdf(1.64)
0.94949741652589625

scipy.stats.norm.cdf(x) gives the % under the curve

'''


import scipy.stats
#import thinkstats2
#import thinkplot



mu = 178
sigma = 7.7

# inches to cm -> 2.54 cm per inch
min_feet = 5
min_inches = 10
min_total_inches = min_feet*12 + min_inches
min_cm = min_total_inches * 2.54

max_feet = 6
max_inches = 1
max_total_inches = max_feet*12 + max_inches
max_cm = max_total_inches * 2.54

#z_min = ( min_cm - mu ) / sigma
#z_max = ( max_cm - mu ) / sigma
cdf_min = scipy.stats.norm.cdf(min_cm, loc = mu, scale = sigma)
cdf_max = scipy.stats.norm.cdf(max_cm, loc = mu, scale = sigma)
cdf_diff = cdf_max - cdf_min
cdf_diff_percent = cdf_diff * 100


print('cdf_min (5\'10\") = ' + str(cdf_min))
#print('z_min = ' + str(z_min))
print('cdf_max (6\'1\")= ' + str(cdf_max))
#print('z_max = ' + str(z_max))
print('% of the U.S. male population in this range = ' + str(cdf_diff_percent) + 
		"%")



#cdf = scipy.stats.norm.cdf(x, loc = mu, scale = sigma)
d = scipy.stats.norm(loc = mu, scale = sigma)


