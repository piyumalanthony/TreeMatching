import pickle
import numpy as np

with open("/home/piyumal/PHD/TreeMatching/time/mcmctree_local/mcmctree_JC+G5{0.5}_100.pkl", 'rb') as f:
    data_mcmc = pickle.load(f)

print(data_mcmc)

with open("/home/piyumal/PHD/TreeMatching/time/iqtree_JC+G5{0.5}.pkl", 'rb') as f:
    data_iqtree = pickle.load(f)

print(data_iqtree)



