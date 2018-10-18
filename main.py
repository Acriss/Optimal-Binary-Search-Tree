from optimalTree import OptimalTree
import numpy as np
from random import seed
from random import random
# seed random number generator
seed(1)

def initialize(n):
    # let's generate a random success probability between 0.4 and 0.6
    # and then have a binomial distribution of probabilities
    success = 0.2 + (random() * 0.6)
    # n trials, random success probability, n values given as output
    p = np.random.binomial(n, success, n)
    np.random.shuffle(p)
    p = p/sum(p)
    # Note that because of float issues, the elements inside p or q don't
    # exactly sum up to one, but very close
    return (p)

def build_tree(p):
    tree = OptimalTree(p)
    tree.create_tree()
    return(tree.get_parents_from_roots())

(p) = initialize(10)
print(build_tree(p))
