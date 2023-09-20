import pickle
import matplotlib.pyplot as plt

import numpy as np

# iqtree_jc = []
# iqtree_jc_G = []
# iqtree_hky = []
# iqtree_hky_G = []

with open("/home/piyumal/PHD/TreeMatching/time/iqtree_JC.pkl", "rb") as f:
    data = pickle.load(f)
    iqtree_jc = data[0]

with open("/home/piyumal/PHD/TreeMatching/time/iqtree_JC+G5{0.5}.pkl", "rb") as f:
    data = pickle.load(f)
    iqtree_jc_G = data[0]

with open("/home/piyumal/PHD/TreeMatching/time/iqtree_HKY.pkl", "rb") as f:
    data = pickle.load(f)
    iqtree_hky = data[0]

with open("/home/piyumal/PHD/TreeMatching/time/iqtree_HKY+G5{0.5}.pkl", "rb") as f:
    data = pickle.load(f)
    iqtree_hky_G = data[0]

with open("/home/piyumal/PHD/TreeMatching/time/mcmctree_JC.pkl", "rb") as f:
    data = pickle.load(f)
    mcmctree_jc = data[0]

with open("/home/piyumal/PHD/TreeMatching/time/mcmctree_HKY.pkl", "rb") as f:
    data = pickle.load(f)
    mcmctree_hky = data[0]

iqtree_jc = np.array(iqtree_jc)
iqtree_jc_G = np.array(iqtree_jc_G)
iqtree_hky = np.array(iqtree_hky)
iqtree_hky_G = np.array(iqtree_hky_G)
mcmctree_jc = np.array(mcmctree_jc)
mcmctree_hky = np.array(mcmctree_hky)

iqtree_jc_mean = np.mean(iqtree_jc, axis=1)
iqtree_jc_G_mean = np.mean(iqtree_jc_G, axis=1)
iqtree_hky_mean = np.mean(iqtree_hky, axis=1)
iqtree_hky_G_mean = np.mean(iqtree_hky_G, axis=1)
mcmctree_jc_mean = np.mean(mcmctree_jc, axis=1)
mcmctree_hky_mean = np.mean(mcmctree_hky, axis=1)
num_taxa = [i for i in range(10, 110, 10)]

mcmctree_jc_G = []
for i in range(10,110,10):
    with open(f'/home/piyumal/PHD/TreeMatching/time/mcmctree_local/mcmctree_JC+G5{{0.5}}_{i}.pkl', "rb") as f:
        data = pickle.load(f)
        mcmctree_jc_G_local = data[0]
    mcmctree_jc_G.append(mcmctree_jc_G_local)
mcmctree_jc_G = np.array(mcmctree_jc_G)
mcmctree_jc_G_mean = np.mean(mcmctree_jc_G, axis=1)


plt.plot(num_taxa, iqtree_jc_mean, label="IQtree + JC")
plt.plot(num_taxa, iqtree_jc_G_mean, label="IQtree + JC + Gamma")
plt.plot(num_taxa, iqtree_hky_mean, label="IQtree + HKY")
# plt.plot(num_taxa, iqtree_hky_G_mean, label="IQtree + HKY + Gamma")
plt.plot(num_taxa, mcmctree_jc_mean, label="BaseML + JC")
plt.plot(num_taxa, mcmctree_hky_mean, label="BaseML + HKY")
plt.plot(num_taxa, mcmctree_jc_G_mean, label="BaseML + JC + Gamma")
plt.ylim([0, 10])
plt.xlim([10, 100])
plt.title('Runtime comparison of tree inference and hessian calculation')
plt.xlabel('Number of species')
plt.ylabel('Time(s)')
plt.legend()
plt.savefig("/home/piyumal/PHD/TreeMatching/plots/time/plot_1.png")
plt.clf()
