import numpy as np

def choa(fitness_function, max_iter, N, dim, LB, UB):
    X = np.random.uniform(LB, UB, (N, dim))
    
    Attacker_pos = np.zeros(dim)
    Attacker_score = float("inf")
    Barrier_pos = np.zeros(dim)
    Barrier_score = float("inf")
    Chaser_pos = np.zeros(dim)
    Chaser_score = float("inf")
    Driver_pos = np.zeros(dim)
    Driver_score = float("inf")
    
    Convergence_curve = np.zeros(max_iter)
    
    for t in range(max_iter):
        for i in range(N):
            X[i, :] = np.clip(X[i, :], LB, UB)
            fitness = fitness_function(X[i, :])
            
            if fitness < Attacker_score:
                Driver_score, Driver_pos = Chaser_score, Chaser_pos.copy()
                Chaser_score, Chaser_pos = Barrier_score, Barrier_pos.copy()
                Barrier_score, Barrier_pos = Attacker_score, Attacker_pos.copy()
                Attacker_score, Attacker_pos = fitness, X[i, :].copy()
            elif fitness < Barrier_score:
                Driver_score, Driver_pos = Chaser_score, Chaser_pos.copy()
                Chaser_score, Chaser_pos = Barrier_score, Barrier_pos.copy()
                Barrier_score, Barrier_pos = fitness, X[i, :].copy()
            elif fitness < Chaser_score:
                Driver_score, Driver_pos = Chaser_score, Chaser_pos.copy()
                Chaser_score, Chaser_pos = fitness, X[i, :].copy()
            elif fitness < Driver_score:
                Driver_score, Driver_pos = fitness, X[i, :].copy()

        f = 2 - t * (2 / max_iter)
        
        for i in range(N):
            for j in range(dim):
                r1, r2 = np.random.rand(), np.random.rand()
                a1 = 2 * f * r1 - f
                c1 = 2 * r2
                m1 = np.random.rand()
                d_attacker = abs(c1 * Attacker_pos[j] - m1 * X[i, j])
                x1 = Attacker_pos[j] - a1 * d_attacker
                
                r1, r2 = np.random.rand(), np.random.rand()
                a2 = 2 * f * r1 - f
                c2 = 2 * r2
                m2 = np.random.rand()
                d_barrier = abs(c2 * Barrier_pos[j] - m2 * X[i, j])
                x2 = Barrier_pos[j] - a2 * d_barrier
                
                r1, r2 = np.random.rand(), np.random.rand()
                a3 = 2 * f * r1 - f
                c3 = 2 * r2
                m3 = np.random.rand()
                d_chaser = abs(c3 * Chaser_pos[j] - m3 * X[i, j])
                x3 = Chaser_pos[j] - a3 * d_chaser
                
                r1, r2 = np.random.rand(), np.random.rand()
                a4 = 2 * f * r1 - f
                c4 = 2 * r2
                m4 = np.random.rand()
                d_driver = abs(c4 * Driver_pos[j] - m4 * X[i, j])
                x4 = Driver_pos[j] - a4 * d_driver
                
                X[i, j] = (x1 + x2 + x3 + x4) / 4
                
        Convergence_curve[t] = Attacker_score
        
    return Convergence_curve