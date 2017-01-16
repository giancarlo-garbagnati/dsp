# Question 5

'''

Bayesian (Elvis Presley twin)

Bayes' Theorem is an important tool in understanding what we really know, given 
evidence of other information we have, in a quantitative way. It helps 
incorporate conditional probabilities into our conclusions.

Elvis Presley had a twin brother who died at birth. What is the probability 
that Elvis was an identical twin? Assume we observe the following probabilities 
in the population: fraternal twin is 1/125 and identical twin is 1/300.


'''

'''

Bayes' Theorem

P(A|X) = prob of A given X

P(A|X) = P(X|A)*P(A) / P(B)


'''

frat_twin = 1/125
iden_twin = 1/300
twin_given_iden = 1
print('chance fraternal twin = 1/125 = ' + str(frat_twin))
print('chance identical twin = 1/300 = ' + str(iden_twin))
print('chance twin given identical twin = ' + str(twin_given_iden))

chance_twin = frat_twin + iden_twin
print('chance twin = ' + str(chance_twin))

iden_given_twin = iden_twin * twin_given_iden / chance_twin

print("chance identical twin, given person is a twin = " + str(iden_given_twin))
print("% chance identical twin, given person is a twin = " + str(iden_given_twin*100))


# chance identical twin, given person is a twin = 0.29411764705882354


