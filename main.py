from plot_generation_v4 import generate_plots

if __name__ == '__main__':
    file_str_list = [
        "/home/piyumal/PHD/Hessian_experiments_v4/JC",
        "/home/piyumal/PHD/Hessian_experiments_v4/JC_Gamma",
        "/home/piyumal/PHD/Hessian_experiments_v4/HKY",
        "/home/piyumal/PHD/Hessian_experiments_v4/HKY_Gamma"
    ]

    for file_str in file_str_list:
        generate_plots(file_str)


