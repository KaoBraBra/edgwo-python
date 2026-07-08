import numpy as np
import random

# X => wolves location
# f => fitness function
# X_m => average position fo all wolves
def edgwo(fitness, tmax, N, Dim, UB, LB):
    PlotYs_EDGWO_KAO = []
    
    X = np.random.uniform(LB, UB, (N, Dim))
    
    X_alpha = np.zeros(Dim)
    X_beta = np.zeros(Dim)
    X_delta = np.zeros(Dim)
    
    f_alpha = float('inf')
    f_beta = float('inf')
    f_delta = float('inf')
    
    t = 0

    while t < tmax:
        for i in range(N):
            
            score = fitness(X[i])
            
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
        
        a = 2 - t * (2 / tmax)
        X_m = np.mean(X, axis=0)
        
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
        
    # print(f"EDGWO: Fitness {PlotYs_EDGWO_KAO[-1]}")
    
    return PlotYs_EDGWO_KAO