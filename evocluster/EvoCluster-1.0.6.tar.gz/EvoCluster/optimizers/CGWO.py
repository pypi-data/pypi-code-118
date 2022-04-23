# -*- coding: utf-8 -*-
"""
Created on Mon May 16 00:27:50 2016

@author: Hossam Faris
"""

import random
import numpy
import math
from .._solution import solution
import time


    

def GWO(objf,lb,ub,dim,SearchAgents_no,Max_iter, k, points, metric):
    
    
    #Max_iter=1000
    #lb=-100
    #ub=100
    #dim=30  
    #SearchAgents_no=5
    
    # initialize alpha, beta, and delta_pos
    Alpha_score=float("inf")
    Alpha_pos=numpy.zeros(dim)
    Alpha_labels=numpy.zeros(dim)
    
    Beta_score=float("inf")
    Beta_pos=numpy.zeros(dim)
    Beta_labels=numpy.zeros(dim)
    
    Delta_score=float("inf")
    Delta_pos=numpy.zeros(dim)
    Delta_labels=numpy.zeros(dim)

    #Initialize the positions of search agents
    Positions = numpy.zeros((SearchAgents_no, dim))
    Positions=numpy.random.uniform(0,1,(SearchAgents_no,dim)) *(ub-lb)+lb
    labelsPred=numpy.zeros((SearchAgents_no,len(points)))
    
    Convergence_curve=numpy.zeros(Max_iter)
    s=solution()

     # Loop counter
    print("GWO is optimizing  \""+objf.__name__+"\"")    
    
    timerStart=time.time() 
    s.startTime=time.strftime("%Y-%m-%d-%H-%M-%S")
    # Main loop
    for l in range(0,Max_iter):
        for i in range(0,SearchAgents_no):
            
            # Return back the search agents that go beyond the boundaries of the search space
            Positions[i,:]=numpy.clip(Positions[i,:], lb, ub)

            # Calculate objective function for each search agent
            startpts = numpy.reshape(Positions[i,:], (k,(int)(dim/k)))
            if objf.__name__ == 'SSE' or objf.__name__ == 'SC' or objf.__name__ == 'DI':
                fitnessValue, labelsPredValues=objf(startpts, points, k, metric) 
            else:
                fitnessValue, labelsPredValues=objf(startpts, points, k) 
            fitness = fitnessValue
            labelsPred[i,:] = labelsPredValues
            
            # Update Alpha, Beta, and Delta
            if fitness<Alpha_score :
                Delta_score=Beta_score  # Update delte
                Delta_pos=Beta_pos.copy()
                Delta_labels=Beta_labels.copy()
                Beta_score=Alpha_score  # Update beta
                Beta_pos=Alpha_pos.copy()
                Beta_labels=Alpha_labels.copy()
                Alpha_score=fitness; # Update alpha
                Alpha_pos=Positions[i,:].copy()
                Alpha_labels=labelsPred[i,:].copy()
                        
            if (fitness>Alpha_score and fitness<Beta_score ):
                Delta_score=Beta_score  # Update delte
                Delta_pos=Beta_pos.copy()
                Delta_labels=Beta_labels.copy()
                Beta_score=fitness  # Update beta
                Beta_pos=Positions[i,:].copy()
                Beta_labels=labelsPred[i,:].copy()            
            
            if (fitness>Alpha_score and fitness>Beta_score and fitness<Delta_score):                 
                Delta_score=fitness # Update delta
                Delta_pos=Positions[i,:].copy()
                Delta_labels=labelsPred[i,:].copy()           
                
        
        a=2-l*((2)/Max_iter); # a decreases linearly fron 2 to 0
        
        # Update the Position of search agents including omegas
        for i in range(0,SearchAgents_no):
            for j in range (0,dim):     
                           
                r1=random.random() # r1 is a random number in [0,1]
                r2=random.random() # r2 is a random number in [0,1]
                
                A1=2*a*r1-a; # Equation (3.3)
                C1=2*r2; # Equation (3.4)
                
                D_alpha=abs(C1*Alpha_pos[j]-Positions[i,j]); # Equation (3.5)-part 1
                X1=Alpha_pos[j]-A1*D_alpha; # Equation (3.6)-part 1
                           
                r1=random.random()
                r2=random.random()
                
                A2=2*a*r1-a; # Equation (3.3)
                C2=2*r2; # Equation (3.4)
                
                D_beta=abs(C2*Beta_pos[j]-Positions[i,j]); # Equation (3.5)-part 2
                X2=Beta_pos[j]-A2*D_beta; # Equation (3.6)-part 2       
                
                r1=random.random()
                r2=random.random() 
                
                A3=2*a*r1-a; # Equation (3.3)
                C3=2*r2; # Equation (3.4)
                
                D_delta=abs(C3*Delta_pos[j]-Positions[i,j]); # Equation (3.5)-part 3
                X3=Delta_pos[j]-A3*D_delta; # Equation (3.5)-part 3             
                
                Positions[i,j]=(X1+X2+X3)/3  # Equation (3.7)
                
            
        
        
        Convergence_curve[l]=Alpha_score;

        if (l%1==0):
               print(['At iteration '+ str(l)+ ' the best fitness is '+ str(Alpha_score)]);
    
    timerEnd=time.time()  
    s.endTime=time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime=timerEnd-timerStart
    s.convergence=Convergence_curve
    s.optimizer="GWO"
    s.objfname=objf.__name__
    s.labelsPred = numpy.array(Alpha_labels, dtype=numpy.int64)
    s.bestIndividual = Alpha_pos
    
    
    
    
    return s