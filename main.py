import warnings
warnings.filterwarnings("ignore", message="pkg_resources is deprecated as an API")
#-------------------------------------------import area------------------------------------------------
import setting as Setting 
import numpy as np 
import matplotlib.pyplot as plt 
import os 
import concurrent.futures
from opfunu.cec_based import cec2021, cec2022
#-------------------------------------------import area------------------------------------------------

#-------------------------------------------Algorithm area------------------------------------------------
from algorithm.EDGWO_Kao import edgwo_kao
from algorithm.PSO import PSO
from algorithm.Gwo import gwo
from algorithm.HHO import hho
from algorithm.BES import bes
from algorithm.SCSO import scso
from algorithm.CHoA import choa
from algorithm.cHGWOSCA import chgwosca
from algorithm.MSGWO import msgwo
from algorithm.REEGWO import reegwo
from algorithm.EDGWO import edgwo

ALGORITHMS = [
    ("EDGWO", edgwo),
    ("EDGWO_Kao", edgwo_kao),
    ("GWO", gwo),
    ("cHGWOSCA", chgwosca),
    ("REEGWO", reegwo),
    ("MSGWO", msgwo),
    ("PSO", PSO),
    ("BES", bes),
    ("CHoA", choa),
    ("HHO", hho),
    ("SCSO", scso)
]
#-------------------------------------------Algorithm area------------------------------------------------

#-------------------------------------------Execute area------------------------------------------------
def execute_single_run(fitness_function, max_iter, N, dim, LB, UB, run_index):
    if (run_index + 1) % 5 == 0:
        print(f"Execution Times : {run_index+1}")
    all_PlotYs = []
    
    for name, algo_func in ALGORITHMS:
        convergence_curve = algo_func(fitness_function, max_iter, N, dim, LB, UB)
        all_PlotYs.append(convergence_curve)
        
    return np.array(all_PlotYs)

def execute(func_name, fitness_function, max_iter, N, dim, LB, UB):
    num_algos = len(ALGORITHMS)
    all_PlotYs = np.zeros((num_algos, max_iter)) 
    
    print(f"----- {func_name} -----")
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [
            executor.submit(execute_single_run, fitness_function, max_iter, N, dim, LB, UB, i)
            for i in range(Setting.exe_Val)
        ]
        for future in concurrent.futures.as_completed(futures):
            Py = future.result() 
            all_PlotYs += Py
            
    all_PlotYs /= Setting.exe_Val
    draw(func_name, all_PlotYs, max_iter)
    print()

#-------------------------------------------Draw area------------------------------------------------
def draw(func_name, all_PlotY, max_iter):
    plt.figure(figsize = (10, 8), dpi = 100) 
    plt.title(func_name)
    plt.xlabel("Number of iteration")  
    plt.ylabel("Average Function Values (log10)")  
    PlotXs = np.arange(0, max_iter)
    
    line_styles = ['-', '--', '-.', ':', '-', '--', '-.', ':', '-', '--']
    
    for idx, (name, _) in enumerate(ALGORITHMS):
        safe_y = np.maximum(all_PlotY[idx], 1e-20) 
        plt.plot(PlotXs, np.log10(safe_y), linewidth=1.5, linestyle=line_styles[idx%len(line_styles)], label=name)
        
    plt.legend(loc='upper right')
    
    if not os.path.exists("photo"):
        os.makedirs("photo")
        
    plt.savefig(os.path.join("photo" , f"{func_name}.png"))
    plt.clf(); plt.cla(); plt.close()
#-------------------------------------------Draw area------------------------------------------------

#-------------------------------------------Main area------------------------------------------------
if __name__ == '__main__':
    cec2021_funcs = [
        cec2021.F12021, cec2021.F22021, cec2021.F32021, cec2021.F42021, 
        cec2021.F52021, cec2021.F62021, cec2021.F72021, cec2021.F82021, 
        cec2021.F92021, cec2021.F102021
    ]
    
    cec2022_funcs = [
        cec2022.F12022, cec2022.F22022, cec2022.F32022, cec2022.F42022, 
        cec2022.F52022, cec2022.F62022, cec2022.F72022, cec2022.F82022, 
        cec2022.F92022, cec2022.F102022, cec2022.F112022, cec2022.F122022
    ]

    print("\n===== CEC 2021 Start =====")
    for i, FuncClass in enumerate(cec2021_funcs):
        try:
            func_obj = FuncClass(ndim=Setting.dim)
            custom_func_name = f"CEC2021_F{i+1}" 
            fitness_function = func_obj.evaluate 
            execute(custom_func_name, fitness_function, Setting.max_iter, Setting.num_particles, Setting.dim, Setting.LB, Setting.UB)
        except Exception as e:
            print(f"執行 CEC2021_F{i+1} 時發生錯誤: {e}")

    print("\n===== CEC 2022 Start =====")
    for i, FuncClass in enumerate(cec2022_funcs):
        try:
            func_obj = FuncClass(ndim=Setting.dim)
            custom_func_name = f"CEC2022_F{i+1}" 
            fitness_function = func_obj.evaluate 
            execute(custom_func_name, fitness_function, Setting.max_iter, Setting.num_particles, Setting.dim, Setting.LB, Setting.UB)
        except Exception as e:
            print(f"執行 CEC2022_F{i+1} 時發生錯誤: {e}")
#-------------------------------------------Main area------------------------------------------------