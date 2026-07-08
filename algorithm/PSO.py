import random , copy , sys 
import numpy as np 


def PSO(fitness ,tmax , N ,Dim , LB , UB ):
    PlotYs_PSO = []
    class Particle:
        def __init__(self):
            self.rnd = random.Random()
            self.position = [0.0 for i in range(Dim)]
            self.velocity = [0.0 for i in range(Dim)]
            self.best_part_pos = [0.0 for i in range(Dim)]
        
            for i in range(Dim):
                self.position[i] = ((UB - LB) *
                self.rnd.random() + LB)
                self.velocity[i] = ((UB - LB) *
                self.rnd.random() + LB)

            self.fitness = fitness(np.array(self.position))
            self.best_part_pos = copy.copy(self.position) 
            self.best_part_fitnessVal = self.fitness

    w = 0.729 
    c1 = 1.49445
    c2 = 1.49445

    rnd = random.Random()
    swarm = [Particle() for i in range(N)] 

    best_swarm_pos = [0.0 for i in range(Dim)]
    best_swarm_fitnessVal = sys.float_info.max

    for i in range(N):
        if swarm[i].fitness < best_swarm_fitnessVal:
            best_swarm_fitnessVal = swarm[i].fitness
            best_swarm_pos = copy.copy(swarm[i].position) 

    Iter = 0
    while Iter < tmax:
        PlotYs_PSO.append(best_swarm_fitnessVal)

        for i in range(N):
            for k in range(Dim): 
                r1 = rnd.random()
                r2 = rnd.random()
            
                swarm[i].velocity[k] = ( 
                                        (w * swarm[i].velocity[k]) +
                                        (c1 * r1 * (swarm[i].best_part_pos[k] - swarm[i].position[k])) +
                                        (c2 * r2 * (best_swarm_pos[k] -swarm[i].position[k])) 
                                    ) 

                if swarm[i].velocity[k] < LB:
                    swarm[i].velocity[k] = LB
                elif swarm[i].velocity[k] > UB:
                    swarm[i].velocity[k] = UB

            for k in range(Dim): 
                swarm[i].position[k] += swarm[i].velocity[k]

            swarm[i].fitness = fitness(np.array(swarm[i].position))

            if swarm[i].fitness < swarm[i].best_part_fitnessVal:
                swarm[i].best_part_fitnessVal = swarm[i].fitness
                swarm[i].best_part_pos = copy.copy(swarm[i].position)

            if swarm[i].fitness < best_swarm_fitnessVal:
                best_swarm_fitnessVal = swarm[i].fitness
                best_swarm_pos = copy.copy(swarm[i].position)
        
        Iter += 1
    return PlotYs_PSO