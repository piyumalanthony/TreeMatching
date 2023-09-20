import pickle
import matplotlib.pyplot as plt
import argparse

from constants import MIN_NUM_TAXA, MAX_NUM_TAXA, MIN_SEQ_LEN, MAX_SEQ_LEN
from tree_process import generate_br_plots, generate_hessian_plots, generate_mle_plots, load_rmse_data


def process_data_for_plots(file_path, min_taxa, max_taxa, min_seq, max_seq):
    for num_taxa_iter in range(min_taxa, max_taxa + min_taxa, min_taxa):
        for seq_len_iter in range(min_seq, max_seq + min_seq, min_seq):
            print(f'-------------- {num_taxa_iter} NUM TAXA, {seq_len_iter} SEQ LENGTH ----------------------------')
            generate_br_plots(file_path, num_taxa_iter, seq_len_iter)
            print("                Completed Branch plot generation")
            generate_hessian_plots(file_path, num_taxa_iter, seq_len_iter)
            print("                Completed Hessian plot generation")
            generate_mle_plots(file_path, num_taxa_iter, seq_len_iter)
            print("                Completed MLE plot generation\n\n")


def process_rmse_data(in_file_path_list, min_taxa, max_taxa, min_seq, max_seq):
    rmse_br_m = {}
    rmse_hessian_diag_m = {}
    rmse_hessian_off_diag_m = {}
    rmse_likelihood_m = {}
    for file_str in in_file_path_list:
        rmse_br = []
        rmse_hessian_diag = []
        rmse_hessian_off_diag = []
        rmse_likelihood = []
        for num_taxa in range(min_taxa, max_taxa + min_taxa, min_taxa):
            rmse_br_local = []
            rmse_hessian_diag_local = []
            rmse_hessian_off_diag_local = []
            rmse_likelihood_local = []
            for seq_len in range(min_seq, max_seq + min_seq, min_seq):
                br_err, hessian_diag_err, hessian_off_diag_err, likelihood_err = load_rmse_data(file_str, num_taxa,
                                                                                                seq_len)
                rmse_br_local.append(br_err)
                rmse_hessian_diag_local.append(hessian_diag_err)
                rmse_hessian_off_diag_local.append(hessian_off_diag_err)
                rmse_likelihood_local.append(likelihood_err)
            else:
                rmse_br.append(rmse_br_local)
                rmse_hessian_diag.append(rmse_hessian_diag_local)
                rmse_hessian_off_diag.append(rmse_hessian_off_diag_local)
                rmse_likelihood.append(rmse_likelihood_local)
        else:
            if file_str.endswith("JC"):
                rmse_br_m["JC"] = rmse_br
                rmse_hessian_diag_m["JC"] = rmse_hessian_diag
                rmse_hessian_off_diag_m["JC"] = rmse_hessian_off_diag
                rmse_likelihood_m["JC"] = rmse_likelihood

            elif file_str.endswith("JC_Gamma"):
                rmse_br_m["JC_Gamma"] = rmse_br
                rmse_hessian_diag_m["JC_Gamma"] = rmse_hessian_diag
                rmse_hessian_off_diag_m["JC_Gamma"] = rmse_hessian_off_diag
                rmse_likelihood_m["JC_Gamma"] = rmse_likelihood
            elif file_str.endswith("HKY"):
                rmse_br_m["HKY"] = rmse_br
                rmse_hessian_diag_m["HKY"] = rmse_hessian_diag
                rmse_hessian_off_diag_m["HKY"] = rmse_hessian_off_diag
                rmse_likelihood_m["HKY"] = rmse_likelihood
            else:
                rmse_br_m["HKY_Gamma"] = rmse_br
                rmse_hessian_diag_m["HKY_Gamma"] = rmse_hessian_diag
                rmse_hessian_off_diag_m["HKY_Gamma"] = rmse_hessian_off_diag
                rmse_likelihood_m["HKY_Gamma"] = rmse_likelihood

    with open('/home/piyumal/PHD/TreeMatching/data/error_analysis.pkl', 'wb') as f:
        pickle.dump([rmse_br_m, rmse_hessian_diag_m, rmse_hessian_off_diag_m, rmse_likelihood_m], f)


def rmse_box_plot_generation(out_file_path, model_list, min_num_taxa, max_num_taxa):
    with open('/home/piyumal/PHD/TreeMatching/data/error_analysis.pkl', 'rb') as f:
        pickle_data = pickle.load(f)
    for model in model_list:
        rmse_br = pickle_data[0][model]
        rmse_hessian_diag = pickle_data[1][model]
        rmse_hessian_off_diag = pickle_data[2][model]
        rmse_likelihood = pickle_data[3][model]
        lables = [i for i in range(min_num_taxa, max_num_taxa + min_num_taxa, min_num_taxa)]

        plt.boxplot(rmse_br, labels=lables)
        plt.title(f'RMSE Branch Lengths for {model} Substitution model')
        plt.xlabel('Number of Taxa')
        plt.ylabel('RMSE')
        plt.savefig(f'{out_file_path}/{model}/RMSE_br_{model}_box_plot.png')
        plt.clf()

        plt.boxplot(rmse_hessian_diag, labels=lables)
        plt.title(f'RMSE Hessian diagonal for {model} Substitution model')
        plt.xlabel('Number of Taxa')
        plt.ylabel('RMSE')
        plt.savefig(f'{out_file_path}/{model}/RMSE_hessian_diag_{model}_box_plot.png')
        plt.clf()

        plt.boxplot(rmse_hessian_off_diag, labels=lables)
        plt.title(f'RMSE Hessian off-diagonal for {model} Substitution model')
        plt.xlabel('Number of Taxa')
        plt.ylabel('RMSE')
        plt.savefig(f'{out_file_path}/{model}/RMSE_hessian_off_diag_{model}_box_plot.png')
        plt.clf()

        plt.boxplot(rmse_likelihood, labels=lables)
        plt.title(f'RMSE likelihood for {model} Substitution model')
        plt.xlabel('Number of Taxa')
        plt.ylabel('RMSE')
        plt.savefig(f'{out_file_path}/{model}/RMSE_likelihood_{model}_box_plot.png')
        plt.clf()




if __name__ == '__main__':
    file_str_list = [
        "/home/piyumal/PHD/Hessian_experiments_v7/JC",
        "/home/piyumal/PHD/Hessian_experiments_v7/JC_Gamma",
        "/home/piyumal/PHD/Hessian_experiments_v7/HKY",
        "/home/piyumal/PHD/Hessian_experiments_v7/HKY_Gamma"
    ]
    out_file_path = '/home/piyumal/PHD/TreeMatching/plots_v3'

    model_list = ["JC", "JC_Gamma", "HKY", "HKY_Gamma"]
    for file_path in file_str_list:
        process_data_for_plots(file_path, MIN_NUM_TAXA, MAX_NUM_TAXA, MIN_SEQ_LEN, MAX_SEQ_LEN)

    process_rmse_data(file_str_list, MIN_NUM_TAXA, MAX_NUM_TAXA, MIN_SEQ_LEN, MAX_SEQ_LEN)
    rmse_box_plot_generation(out_file_path, model_list, MIN_NUM_TAXA, MAX_NUM_TAXA)


