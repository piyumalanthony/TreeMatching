import os

from constants import MIN_NUM_TAXA, MAX_NUM_TAXA, MIN_SEQ_LEN, MAX_SEQ_LEN, IQTREE_PATH, AA_FILE_PATH


def run_iqtree(path):
    os.chdir(path)
    print(os.getcwd())
    for i in range(MIN_NUM_TAXA, MAX_NUM_TAXA + MIN_NUM_TAXA, MIN_NUM_TAXA):
        os.system(f'mkdir iqtree_output/{i}')
        for j in range(MIN_SEQ_LEN, MAX_SEQ_LEN + MIN_SEQ_LEN, MIN_SEQ_LEN):
            # os.system(f'mkdir iqtree_output')
            os.system(f'mkdir iqtree_output/{i}/{j}')
            # os.mkdir(f'iqtree_output/{i}')
            # os.mkdir(f'iqtree_output/{i}/{j}')
            cmd_iqtree = f'{IQTREE_PATH} -s {path}/simulated_data/{i}/{j}.phy --redo  -nt 1 -m WAG+G5{{0.5}} --dating mcmctree -seed 1 -te {path}/simulated_data/{i}/{j}.nw --prefix {path}/iqtree_output/{i}/{j}/output'
            os.system(cmd_iqtree)
            print(i, j)
            print("____________________________________________________________________________")


def generate_ctl_file(path):
    for i in range(MIN_NUM_TAXA, MAX_NUM_TAXA + MIN_NUM_TAXA, MIN_NUM_TAXA):
        os.system(f"mkdir {path}/mcmctree_output/{i}")
        for j in range(MIN_SEQ_LEN, MAX_SEQ_LEN + MIN_SEQ_LEN, MIN_SEQ_LEN):
            os.system(f"mkdir {path}/mcmctree_output/{i}/{j}")
            file_str = [
                "seed = -1\n"
                f"seqfile = {path}/simulated_data/{i}/{j}.phy\n",
                f"treefile = {path}/simulated_data/{i}/{j}_mcmc.treefile\n",
                "outfile = out.txt\n",
                "ndata = 1\n",
                "seqtype = 2\n",
                "usedata = 3\n",
                "clock = 2\n",
                "RootAge = <1.0\n",
                "model = 0\n",
                "alpha = 0.5\n",
                "ncatG = 5\n",
                "cleandata = 0\n",
                "BDparas = 1 1 0\n",
                "kappa_gamma = 6 2\n",
                "alpha_gamma = 1 1\n",
                "rgene_gamma = 2 2\n",
                "sigma2_gamma = 1 10\n",
                "finetune = 1: 0.1  0.1  0.1  0.01 .5\n",
                "print = 1\n",
                "burnin = 2000\n",
                "sampfreq = 2\n",
                "nsample = 20000\n"

            ]
            with open(f"{path}/simulated_data/{i}/{j}_mcmctree.ctl", "w+") as f:
                f.write("".join(file_str))


def generate_mcmctree_file(path):
    for i in range(MIN_NUM_TAXA, MAX_NUM_TAXA + MIN_NUM_TAXA, MIN_NUM_TAXA):
        for j in range(MIN_SEQ_LEN, MAX_SEQ_LEN + MIN_SEQ_LEN, MIN_SEQ_LEN):
            with open(f"{path}/simulated_data/{i}/{j}.nw") as f:
                tree_str = f.readline()
                with open(f"{path}/simulated_data/{i}/{j}_mcmc.treefile", "w+") as f:
                    f.write("{} {}\n".format(i, 1))
                    f.write(tree_str)


def run_mcmctree(path):
    for i in range(MIN_NUM_TAXA, MAX_NUM_TAXA + MIN_NUM_TAXA, MIN_NUM_TAXA):
        for j in range(MIN_SEQ_LEN, MAX_SEQ_LEN + MIN_SEQ_LEN, MIN_SEQ_LEN):
            os.chdir(f"{path}/mcmctree_output/{i}/{j}")
            cmd_mcmctree = f"mcmctree {path}/simulated_data/{i}/{j}_mcmctree.ctl"
            os.system(cmd_mcmctree)


if __name__ == '__main__':
    # run_iqtree(AA_FILE_PATH)
    # generate_ctl_file(AA_FILE_PATH)
    # generate_mcmctree_file(AA_FILE_PATH)
    run_mcmctree(AA_FILE_PATH)
