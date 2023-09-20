import os
import time
import pickle
import psutil
import numpy as np

iqtree_path = '/home/piyumal/PHD/TreeMatching/iqtree2'


def process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss


def time_mcmctree(min_taxa, max_taxa, gap, file_str, model):
    time_global = []
    memory_global = []
    for i in range(min_taxa, max_taxa + min_taxa, gap):
        time_local = []
        memory_local = []
        for j in range(1000, 11000, 1000):
            print("____________________________________________")
            print(i, j)
            os.chdir(f'{file_str}/mcmctree_output/{i}/{j}')
            cmd_mcmctree = f'mcmctree {file_str}/simulated_data/{i}/{j}_mcmctree.ctl'
            mem_before = process_memory()
            start = time.time()
            os.system(cmd_mcmctree)
            end = time.time()
            mem_after = process_memory()
            time_local.append(end - start)
            memory_local.append(mem_after - mem_before)
        time_global.append(time_local)
        memory_global.append(memory_local)
        with open(f'/home/piyumal/PHD/TreeMatching/time/mcmctree_local/mcmctree_{model}_{i}.pkl', 'wb') as f:
            pickle.dump([time_local, memory_local], f)
    with open(f'/home/piyumal/PHD/TreeMatching/time/mcmctree_{model}.pkl', 'wb') as f:
        pickle.dump([time_global, memory_global], f)


def time_iqtree(min_taxa, max_taxa, gap, iqtree_path, file_str, model):
    time_global = []
    memory_global = []
    for i in range(min_taxa, max_taxa + min_taxa, gap):
        time_local = []
        memory_local = []
        for j in range(1000, 11000, 1000):
            print(i, j)
            cmd_iqtree = (
                f'{iqtree_path} -s {file_str}/simulated_data/{i}/{j}.phy --redo  -nt 1 -m {model} --dating mcmctree '
                f'-seed 1 -te {file_str}/simulated_data/{i}/{j}.nw --prefix {file_str}/iqtree_output/{i}/{j}/output')
            mem_before = process_memory()
            start = time.time()
            os.system(cmd_iqtree)
            end = time.time()
            mem_after = process_memory()
            time_local.append(end - start)
            memory_local.append(mem_after - mem_before)
        time_global.append(time_local)
        memory_global.append(memory_local)
    with open(f'/home/piyumal/PHD/TreeMatching/time/iqtree_{model}.pkl', 'wb') as f:
        pickle.dump([time_global, memory_global], f)


def time_iqtree_AA(min_taxa, max_taxa, gap, iqtree_path, file_str, model):
    time_global = []
    memory_global = []
    for i in range(min_taxa, max_taxa + gap, gap):
        time_local = []
        memory_local = []
        for j in range(1000, 11000, 1000):
            print(i, j)
            cmd_iqtree = f'{iqtree_path} -s {file_str}/simulated_data/{i}/{j}.phy --redo  -nt 1 -m WAG+G5{{0.5}} --dating mcmctree -seed 1 -te {file_str}/simulated_data/{i}/{j}.nw --prefix {file_str}/iqtree_output/{i}/{j}/output'
            mem_before = process_memory()
            start = time.time()
            os.system(cmd_iqtree)
            end = time.time()
            mem_after = process_memory()
            time_local.append(end - start)
            memory_local.append(mem_after - mem_before)
        time_global.append(time_local)
        memory_global.append(memory_local)
    with open(f'/home/piyumal/PHD/TreeMatching/time/AA/iqtree_{model}.pkl', 'wb') as f:
        pickle.dump([time_global, memory_global], f)


if __name__ == '__main__':
    # time_iqtree(10, 100, 10, iqtree_path, "/home/piyumal/PHD/Hessian_experiments_v6/JC", "JC")
    # time_iqtree(10, 100, 10, iqtree_path, "/home/piyumal/PHD/Hessian_experiments_v6/JC_Gamma", "JC+G5{0.5}")
    # time_iqtree(10, 100, 10, iqtree_path, "/home/piyumal/PHD/Hessian_experiments_v6/HKY", "HKY")
    # time_iqtree(10, 100, 10, iqtree_path, "/home/piyumal/PHD/Hessian_experiments_v6/HKY_Gamma", "HKY+G5{0.5}")

    # time_mcmctree(10, 100, 10, "/home/piyumal/PHD/Hessian_experiments_v6/JC", "JC")
    # time_mcmctree(50, 100, 10, "/home/piyumal/PHD/Hessian_experiments_v6/JC_Gamma", "JC+G5{0.5}")
    # time_mcmctree(10, 100, 10, "/home/piyumal/PHD/Hessian_experiments_v6/HKY", "HKY")
    # time_mcmctree(10, 100, 10, "/home/piyumal/PHD/Hessian_experiments_v6/HKY_Gamma", "HKY+G5{0.5}")

    # time_iqtree_AA(100, 100, 10, iqtree_path, "/home/piyumal/PHD/Hessian_experiments_v7/AA", "WAG")

    # with open('/home/piyumal/PHD/TreeMatching/time/iqtree_HKY.pkl', 'rb') as f:
    #     time_data = pickle.load(f)
    #     # print(time_data)
    #     # print(len(time_data))
    #     # print(len(time_data[0]))
    #     print(np.sum(np.array(time_data[0])))

    # with open(f'/home/piyumal/PHD/TreeMatching/time/iqtree_JC+G5{{0.5}}.pkl', 'rb') as f:
    #     time_data = pickle.load(f)
    #     # print(time_data)
    #     # print(len(time_data))
    #     # print(len(time_data[0]))
    #     print(np.sum(np.array(time_data[0])))
    #     print(np.sum(time_data[0][-1]))
    # data = []
    # for i in range(10, 110, 10):
    #     with open(f'/home/piyumal/PHD/TreeMatching/time/mcmctree_local/mcmctree_JC+G5{{0.5}}_{i}.pkl', 'rb') as f:
    #         time_data = pickle.load(f)
    #         # print(time_data)
    #         # print(len(time_data))
    #         # print(len(time_data[0]))
    #         # print(np.sum(np.array(time_data[0])))
    #         data.append(np.sum(np.array(time_data[0])))
    # print(data)
    # print(np.sum(np.array(data)))

    with open(f'/home/piyumal/PHD/TreeMatching/time/AA/iqtree_WAG.pkl', 'rb') as f:
        time_data = pickle.load(f)
        # print(time_data)
        # print(len(time_data))
        # print(len(time_data[0]))
        print(np.sum(np.array(time_data[0])))
        # print(np.sum(time_data[0][-1]))