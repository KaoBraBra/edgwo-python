#-------------------------------------------Algorithm area------------------------------------------------
from Algorithm.EDGWO_Kao import edgwo_kao
from Algorithm.EDGWO_Lee import edgwo_lee
from Algorithm.EDGWO_Lai import edgwo_lai
from Algorithm.PSO import PSO
from Algorithm.Gwo import gwo
#-------------------------------------------Algorithm area------------------------------------------------

#-------------------------------------------import area------------------------------------------------
import Setting as Setting , numpy as np , matplotlib.pyplot as plt 
import os , CEC2022 
#-------------------------------------------import area------------------------------------------------

#-------------------------------------------CSC2022 Function area------------------------------------------------
def CEC2022_f1(pos):    return CEC2022.Zakharov(pos + Setting.Shift_Val)
def CEC2022_f2(pos):    return CEC2022.Rosenbrock(pos + Setting.Shift_Val)
def CEC2022_f3(pos):    return CEC2022.Expanded_Schaffer(pos + Setting.Shift_Val)
def CEC2022_f4(pos):    return CEC2022.Rastrigin(pos + Setting.Shift_Val)
def CEC2022_f5(pos):    return CEC2022.Levy(pos + Setting.Shift_Val)
def CEC2022_f6(pos):    return CEC2022.Bent_Cigar(pos + Setting.Shift_Val)
def CEC2022_f7(pos):    return CEC2022.High_Conditioned_Elliptic(pos + Setting.Shift_Val)
def CEC2022_f8(pos):    return CEC2022.HGBat(pos + Setting.Shift_Val)
def CEC2022_f9(pos):    return CEC2022.Katsuura(pos + Setting.Shift_Val)
def CEC2022_f10(pos):   return CEC2022.Happycat(pos + Setting.Shift_Val)
#-------------------------------------------CSC2022 area------------------------------------------------

#-------------------------------------------Execute area------------------------------------------------
import concurrent.futures
def execute_single_run(fitness_function, max_iter, N, dim, LB, UB, run_index):
    print(f"----------------------------------Now Execution Times : {run_index+1}----------------------------------")
    all_PlotYs = []
    print("\nEDGWO_Lai Start...\n")
    all_PlotYs.append(edgwo_lai(fitness_function, max_iter, N , dim , LB , UB))
    print("\nEDGWO_Lee Start...\n")
    all_PlotYs.append(edgwo_lee(fitness_function, max_iter, N , dim , LB , UB))
    print("\nEDGWO_Kao Start...\n")
    all_PlotYs.append(edgwo_kao(fitness_function, max_iter, N , dim , LB , UB))
    print("\nGwo Start...\n")
    all_PlotYs.append(gwo(fitness_function, max_iter, N , dim , LB , UB))
    print("\nPSO Start...\n")
    all_PlotYs.append(PSO(fitness_function, max_iter, N , dim , LB , UB))
    all_PlotYs = np.array(all_PlotYs).reshape(len(os.listdir("Algorithm"))-1,Setting.max_iter)
    return all_PlotYs

def execute(fitness_function, max_iter, N, dim, LB, UB):
    all_PlotYs = np.zeros((len(os.listdir("Algorithm"))-1,Setting.max_iter))
    print(f"------------------------------Now {fitness_function.__name__} Start ------------------------------")
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [
            executor.submit(execute_single_run, fitness_function, max_iter, N, dim, LB, UB, i)
            for i in range(Setting.exe_Val)
        ]
        for future in concurrent.futures.as_completed(futures):
            Py = future.result()  # 確保每個執行緒完成
            all_PlotYs += Py
    all_PlotYs /= Setting.exe_Val
    draw(fitness_function, all_PlotYs)
    print(f"------------------------------Now {fitness_function.__name__} End ------------------------------")
    # input("Press Enter to Go next Function...")
#-------------------------------------------Execute area------------------------------------------------

#-------------------------------------------Draw area------------------------------------------------
def draw(fitness_function, all_PlotY):
    plt.figure(figsize = (10.8, 10.8), dpi = 100) # 1080 * 1080
    plt.title(fitness_function.__name__)
    plt.xlabel("Number of iteration")  
    plt.ylabel("Average Function Values (log10)")  
    PlotXs = np.arange(0,Setting.max_iter)
    line1, = plt.plot(PlotXs, np.log10(all_PlotY[0]) , color = 'red'     , linewidth = 1, label = 'EDGWO_Lai')          
    line2, = plt.plot(PlotXs, np.log10(all_PlotY[1]) , color = 'orange'  , linewidth = 1, label = 'EDGWO_Lee')   
    line3, = plt.plot(PlotXs, np.log10(all_PlotY[2]) , color = 'purple'  , linewidth = 1, label = 'EDGWO_Kao')    
    line4, = plt.plot(PlotXs, np.log10(all_PlotY[3]) , color = 'blue'    , linewidth = 1, label = 'GWO'      )           
    line5, = plt.plot(PlotXs, np.log10(all_PlotY[4]) , color = 'green'   , linewidth = 1, label = 'PSO'      )      
    plt.legend(handles = [line1, line2, line3 , line4 , line5], loc = 'upper right')
    # plt.show()
    plt.savefig(os.path.join("photo" , f"{fitness_function.__name__}.png"))
    plt.clf(); plt.cla()  
    plt.close()
#-------------------------------------------Draw area------------------------------------------------

#-------------------------------------------Main area------------------------------------------------
if __name__ == '__main__':
    print(f"Now Setting: N->{Setting.num_particles}\tTmax->{Setting.max_iter}\tDim->{Setting.dim} \t Shift Value->{Setting.Shift_Val}")
    execute(CEC2022_f1  , Setting.max_iter , Setting.num_particles , Setting.dim , Setting.LB , Setting.UB)
    execute(CEC2022_f2  , Setting.max_iter , Setting.num_particles , Setting.dim , Setting.LB , Setting.UB)
    execute(CEC2022_f3  , Setting.max_iter , Setting.num_particles , Setting.dim , Setting.LB , Setting.UB)
    execute(CEC2022_f4  , Setting.max_iter , Setting.num_particles , Setting.dim , Setting.LB , Setting.UB)
    execute(CEC2022_f5  , Setting.max_iter , Setting.num_particles , Setting.dim , Setting.LB , Setting.UB)
    execute(CEC2022_f6  , Setting.max_iter , Setting.num_particles , Setting.dim , Setting.LB , Setting.UB)
    execute(CEC2022_f7  , Setting.max_iter , Setting.num_particles , Setting.dim , Setting.LB , Setting.UB)
    execute(CEC2022_f8  , Setting.max_iter , Setting.num_particles , Setting.dim , Setting.LB , Setting.UB)
    execute(CEC2022_f9  , Setting.max_iter , Setting.num_particles , Setting.dim , Setting.LB , Setting.UB)
    execute(CEC2022_f10 , Setting.max_iter , Setting.num_particles , Setting.dim , Setting.LB , Setting.UB)
    print("Program End ...")
#-------------------------------------------Main area------------------------------------------------