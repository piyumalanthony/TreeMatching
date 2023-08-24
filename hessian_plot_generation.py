import matplotlib.pyplot as plt
import pickle


def generate_hessian_plots(file_path):
    for i in range(10, 110, 10):
        for j in range(1000, 11000, 1000):
            print(file_path)
            print(i,j)
            with open(f'{file_path}/pickle/br_idx_mapping_{i}_{j}.pkl', 'rb') as f:
                pickle_data = pickle.load(f)
            index_list = pickle_data[0]

            for l in index_list:
                iqtree_hessian = f'{file_path}/iqtree_output/{i}/{j}/output_hessian.gh'
                baseml_hessian = f'{file_path}/mcmctree_output/{i}/{j}/hessian.txt'
                iqtree_hessian_values = []
                iqtree_h = open(iqtree_hessian, 'r')
                lines = iqtree_h.readlines()
                iqtree_h.close()

                for line in lines:
                    values = line.strip().split()
                    values = [float(i) for i in values]
                    iqtree_hessian_values.append(values)

                baseml_hessian_values = []
                baseml_h = open(baseml_hessian, 'r')
                lines_1 = baseml_h.readlines()
                baseml_h.close()

                for line in lines_1:
                    values = line.strip().split()
                    values = [float(i) for i in values]
                    baseml_hessian_values.append(values)

                baseml_hessian_global = []
                for m in range(len(index_list)):
                    baseml_hessian_local = []
                    for n in range(len(index_list)):
                        baseml_hessian_local.append(baseml_hessian_values[index_list[m]][index_list[n]])
                    else:
                        baseml_hessian_global.append(baseml_hessian_local)

                iqtree_hessian_diagonal = []

                for u, v in enumerate(iqtree_hessian_values):
                    iqtree_hessian_diagonal.append(v[u])

                baseml_hessian_diagonal = []

                for u, v in enumerate(baseml_hessian_global):
                    baseml_hessian_diagonal.append(v[u])

                iqtree_hessian_off_diagonal = []
                for u, v in enumerate(iqtree_hessian_values):
                    for k, l in enumerate(v):
                        if k != i:
                            iqtree_hessian_off_diagonal.append(l)

                baseml_hessian_off_diagonal = []
                for u, v in enumerate(baseml_hessian_global):
                    for k, l in enumerate(v):
                        if k != i:
                            baseml_hessian_off_diagonal.append(l)

                plt.plot(iqtree_hessian_diagonal, baseml_hessian_diagonal, 'bo')
                plt.plot([min(iqtree_hessian_diagonal), max(iqtree_hessian_diagonal)],
                         [min(iqtree_hessian_diagonal), max(iqtree_hessian_diagonal)], 'r--', label='x=y')
                plt.title(f'IQTree vs Baseml hessian diagonal values for {i} taxa and {j} seq length')
                plt.xlabel('IQtree hessian')
                plt.ylabel('Baseml hessian')
                plt.savefig(f'{file_path}/plots/hessian_plots/hessian_diagonal_{i}_{j}.png')
                plt.clf()

                plt.plot(iqtree_hessian_off_diagonal, baseml_hessian_off_diagonal, 'bo')
                plt.plot([min(iqtree_hessian_off_diagonal), max(iqtree_hessian_off_diagonal)],
                         [min(iqtree_hessian_off_diagonal), max(iqtree_hessian_off_diagonal)], 'r--', label='x=y')
                plt.title(f'IQTree vs Baseml hessian off diagonal values for {i} taxa and {j} seq length')
                plt.xlabel('IQtree hessian')
                plt.ylabel('Baseml hessian')
                plt.savefig(f'{file_path}/plots/hessian_plots/hessian_off_diagonal_{i}_{j}.png')


file_str_list = [
    # "/home/piyumal/PHD/Hessian_experiments_v4/JC",
    # "/home/piyumal/PHD/Hessian_experiments_v4/JC_Gamma",
    "/home/piyumal/PHD/Hessian_experiments_v4/HKY",
    "/home/piyumal/PHD/Hessian_experiments_v4/HKY_Gamma"
]

for file_str in file_str_list:
    generate_hessian_plots(file_str)
