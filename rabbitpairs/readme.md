- in 1202, Leonardo of Pisa considered a mathematical exercise regarding the reproduction of a population of rabbits. 
- He made the following simplifying assumptions about the population:
    1. the population begins in the first month with a pair of newborn rabbits. 
    2. rabbits reach reproductive age after one month. 
    3. in any given month, every rabbit of reproductive age mates with another rabbit of reproductive age. 
    4. exactly one month after two rabbits male, they produce noe male and one female rabbit. 
    5. rabbits never die or stop reproducing. 
- fibonacci's exercise was to calculate how many pairs would remain in one year. We can see that in the second month, the first pair of rabbits reach reproductive age and mate. 
- in the third month, another pair of rabbits is born, and we have two rabbit pairs; our first pair or rabbits mates again. 
- in the fourth month, another pair of rabbits is born to the original pair while the second pair reach maturity and mate with three total pairs. 

Problem

- a sequence is an ordered collection of objects which are allowed to repeat. they can be finite or infinite. 
- a recurrence relation is a way of defining the terms of a sequence with respect to values of previous terms. 
- when finding the n-th term of a sequence is defined by a recurrence relation, we can simple use the recurrence relation to generate terms for progressively larger values of n. 
- this problem introduces us to the computational technique of dynamic programming which succesively builds up solutions by using the answers to smaller cases. 

given positive enters n (less than or equal to) 40 and k (less than equal to) 5, return the total number of rabbit pairs that will be present after n months. if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits provides a litter of k rabbit pairs (instead of only 1 pair)