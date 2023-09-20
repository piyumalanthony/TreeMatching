import os
import ete3

from constants import MIN_NUM_TAXA, MAX_NUM_TAXA, MIN_SEQ_LEN, MAX_SEQ_LEN, IQTREE_PATH, AA_FILE_PATH


def generate_tree(path):
    print(os.getcwd())
    os.chdir(path)
    for i in range(MIN_NUM_TAXA, MAX_NUM_TAXA + MIN_NUM_TAXA, MIN_NUM_TAXA):
        os.system(f'mkdir simulated_data/{i}')
        taxa = ["T" + str(i) for i in range(1, i + 1)]
        for j in range(MIN_SEQ_LEN, MAX_SEQ_LEN + MIN_SEQ_LEN, MIN_SEQ_LEN):
            t = ete3.Tree()
            t.populate(i, taxa, random_branches=True, branch_range=[0.0005, 0.4])
            # polynode = t.get_common_ancestor("T1")
            # polynode.resolve_polytomy(recursive=False)
            t.write(format=1,
                    outfile=f'simulated_data/{i}/{j}.nw')


def run_alisim_aa(path):
    os.chdir(path)
    for i in range(MIN_NUM_TAXA, MAX_NUM_TAXA + MIN_NUM_TAXA, MIN_NUM_TAXA):
        for j in range(MIN_SEQ_LEN, MAX_SEQ_LEN + MIN_SEQ_LEN, MIN_SEQ_LEN):
            cmd_alisim_v2 = f'{IQTREE_PATH} --alisim simulated_data/{i}/{j} -m WAG+G5{{0.5}} -t simulated_data/{i}/{j}.nw -seed 1 --length {j}'
            os.system(cmd_alisim_v2)


if __name__ == '__main__':
    generate_tree(AA_FILE_PATH)
    run_alisim_aa(AA_FILE_PATH)
