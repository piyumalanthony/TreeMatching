import os
import time
import ete3

iqtree_path = '/home/piyumal/PHD/TreeMatching/iqtree2'
start = time.time()
cmd = ("{0} -s examples/example_8.phy --redo  -nt 1 -m JC --dating mcmctree -seed 123 -te examples/mtCDNApri_v2.trees "
       "-o gibbon --prefix ./examples/test").format(
    iqtree_path)
os.system(cmd)
end = time.time()

print(end - start)


def simulate_data(min_taxa, max_taxa, gap, file_str):
    for i in range(min_taxa, max_taxa + min_taxa, gap):
        os.system(f'mkdir {file_str}/simulated_data/{0}')
        taxa = ["T" + str(i) for i in range(1, i + 1)]
        for j in range(1000, 11000, 1000):
            t = ete3.Tree()
            t.populate(i, taxa, random_branches=True, branch_range=[0.0005, 0.4])
            # polynode = t.get_common_ancestor("T1")
            # polynode.resolve_polytomy(recursive=False)
            t.write(format=1,
                    outfile=f'{file_str}/simulated_data/{0}/{1}.nw')


def generate_alignments(min_taxa, max_taxa, gap, file_str):
    pass


def run_iqtree(file_path, iqtree_path, model, model_param, num_taxa, seq_len):
    dir_1 = f'{file_path}/{model}/iqtree_output/{num_taxa}'
    dir_2 = f'{file_path}/{model}/iqtree_output/{num_taxa}/{seq_len}'
    if not (os.path.exists(dir_1)):
        os.system(f'mkdir {file_path}/{model}/iqtree_output/{num_taxa}')
    if not (os.path.exists(dir_2)):
        os.system(f'mkdir {file_path}/{model}/iqtree_output/{num_taxa}/{seq_len}')

    tree_string = ""

    with open(f'{file_path}/{model}/mcmctree_output/{num_taxa}/{seq_len}/out.BV') as f:
        for k, line in enumerate(f.readlines()):
            if k == 3:
                tree_string = line

    with open(f'{file_path}/{model}/iqtree_output/{num_taxa}/{seq_len}/tree.nwk', "w") as f:
        f.write(tree_string)
    if "Gamma" in model:
        cmd_iqtree = f'{iqtree_path} -s {file_path}/{model}/simulated_data/{num_taxa}/{seq_len}.phy --redo  -nt 1 -m {model_param} -gmedian --dating mcmctree -seed 1 -te {file_path}/{model}/iqtree_output/{num_taxa}/{seq_len}/tree.nwk --prefix {file_path}/{model}/iqtree_output/{num_taxa}/{seq_len}/output'
    else:
        cmd_iqtree = f'{iqtree_path} -s {file_path}/{model}/simulated_data/{num_taxa}/{seq_len}.phy --redo  -nt 1 -m {model_param} --dating mcmctree -seed 1 -te {file_path}/{model}/iqtree_output/{num_taxa}/{seq_len}/tree.nwk --prefix {file_path}/{model}/iqtree_output/{num_taxa}/{seq_len}/output'
    print(cmd_iqtree)
    os.system(cmd_iqtree)



if __name__ == '__main__':
    file_path = '/home/piyumal/PHD/Hessian_experiments_v7'
    iqtree_path = '/home/piyumal/PHD/TreeMatching/iqtree2'
    model_list = ["JC", "JC_Gamma", "HKY", "HKY_Gamma"]
    for model in model_list:
        for i in range(10, 110, 10):
            for j in range(1000, 11000, 1000):
                print(f' Model: {model}, Num taxa: {i}, Seq len: {j} ')
                print('IQTREE running...')
                if model == 'JC':
                    s_model = 'JC'
                elif model == 'JC_Gamma':
                    s_model = 'JC+G5{0.5}'
                elif model == 'HKY':
                    s_model = 'HKY'
                else:
                    s_model = 'HKY+G5{0.5}'

                run_iqtree(file_path, iqtree_path, model, s_model, i, j)
                print('IQTREE optimization completed.')
