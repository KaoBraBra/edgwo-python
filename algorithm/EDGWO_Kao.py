import numpy as np
import random
import math

# X => wolves location
# f => fitness function
# X_m => average position fo all wolves
# 1. Stagnation Detection
# 2. Diversity-Driven Parameter Adaptation

def edgwo_kao(fitness, tmax, N, Dim, UB, LB):
    PlotYs_EDGWO_KAO = []
    X = np.random.uniform(LB, UB, (N, Dim))
    
    X_alpha = np.zeros(Dim)
    X_beta = np.zeros(Dim)
    X_delta = np.zeros(Dim)
    
    f_alpha = float('inf')
    f_beta = float('inf')
    f_delta = float('inf')
    
    prev_f_alpha = float('inf')  
    counter = 0        
    patient = max(5, int(tmax * 0.06)) 
    replace_num = max(1, int(N * 0.15)) 

    t = 0

    while t < tmax:
        curr_scores = np.zeros(N)

        for i in range(N):
            score = fitness(X[i])
            curr_scores[i] = score

            if score < f_alpha:
                f_delta = f_beta
                X_delta = X_beta.copy()
                f_beta = f_alpha
                X_beta = X_alpha.copy()
                f_alpha = score
                X_alpha = X[i].copy()
            elif score < f_beta:
                f_delta = f_beta
                X_delta = X_beta.copy()
                f_beta = score
                X_beta = X[i].copy()
            elif score < f_delta:
                f_delta = score
                X_delta = X[i].copy()
                
        PlotYs_EDGWO_KAO.append(f_alpha)
        
        # 1. Stagnation Detection
        tolerance = 1e-5
        if (prev_f_alpha - f_alpha) < tolerance:
            counter += 1
        else:
            counter = 0
            prev_f_alpha = f_alpha
            
        if counter >= patient:
            worst_indices = np.argsort(curr_scores)[-replace_num:]
            radius = (UB - LB) * 0.2 * (1 - t / tmax)
            X[worst_indices] = X_alpha + np.random.uniform(-radius, radius, (replace_num, Dim))
            counter = 0

        # a = 2 - t * (2 / tmax)
        # a = 2 * math.cos((math.pi / 2) * (t / tmax))
        # a = 2 * np.exp(-t / tmax)
        # a = 2 * (1 - (t / tmax)**2)

        # 2. Diversity-Driven Parameter Adaptation
        X_m = np.mean(X, axis=0)
        curr_div = np.mean(np.linalg.norm(X - X_m, axis=1))
        
        if t == 0:
            max_div = curr_div
            
        div_ratio = curr_div / (max_div + 1e-10)
        a = 2 * (1 - (t / tmax)**2)
        
        if div_ratio < 0.1 and t < 0.7 * tmax:
            a = min(2.0, a + 0.5) 
        
        for i in range(N):
            r1 = np.random.rand(3, Dim)
            r2 = np.random.rand(3, Dim)
            
            A = 2 * a * r1 - a
            C = 2 * r2
            
            p = random.random()
            
            if np.mean(np.abs(A[0])) < 1:
                D_alpha = np.abs(C[0] * X_alpha - X[i])
                X1 = X_alpha - A[0] * D_alpha
            else:
                r3, r4 = np.random.rand(Dim), np.random.rand(Dim)
                X1 = (X_alpha - X_m) - r3 * (LB + r4 * (UB - LB))

            if np.mean(np.abs(A[1])) < 1:
                D_beta  = np.abs(C[1] * X_beta - X[i])
                X2 = X_beta - A[1] * D_beta
            else:
                r3, r4 = np.random.rand(Dim), np.random.rand(Dim)
                X2 = (X_beta - X_m) - r3 * (LB + r4 * (UB - LB))

            if np.mean(np.abs(A[2])) < 1:
                D_delta = np.abs(C[2] * X_delta - X[i])
                X3 = X_delta - A[2] * D_delta
            else:
                r3, r4 = np.random.rand(Dim), np.random.rand(Dim)
                X3 = (X_delta - X_m) - r3 * (LB + r4 * (UB - LB))
            
            if p < 0.5:
                X[i] = (X1 + X2 + X3) / 3.0
            else:
                r5 = np.random.rand(Dim)
                l = -1 + 2 * r5
                X[i] = X_alpha + np.abs(X_alpha - X[i]) * np.exp(l) * np.cos(2 * np.pi * l)
                
        t += 1
        
    # print(f"EDGWO_Kao: Fitness {PlotYs_EDGWO_KAO[-1]}")
    
    return PlotYs_EDGWO_KAO