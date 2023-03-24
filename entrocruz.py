# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 03:01:19 2023

@author: Mauro
"""

import matplotlib.pyplot as graf
import numpy as np
import pandas as pd




# se crea 10 datos con su respectivas validaciones

datos=np.array([[1,1,0],[1,2,0],[2,1,0],[2,2,0],[3,1,0],[2,3,1],[3,3,1],[4,3,1],[4,2,1],[3,2,1]])
print(datos)

#se grafica los puntos de los datos

for i in range(0,10):
    
    if datos[i,2]==0:
        
        graf.plot(datos[i,0],datos[i,1],"o",color="red")
        
    else:
            
        graf.plot(datos[i,0],datos[i,1],"o",color="green")
   
 # se deine la funcio sigmoide:       
   
def sigmoid(x):
    
    return 1/(1+np.exp(-x))
        
    # probando otros datos:   
     
x=datos[:,0:2]  
ysal=datos[:,2]     

# se define la prediccion:

def prediccion(X, W, b):
    return sigmoid(np.matmul(X, W) + b) 

W = np.array(np.random.rand(2,1)) 
b = np.random.rand(1)[0]

#se saca las probabiliadescon la prediccion antes definida

Probabilidades= prediccion(x, W, b)


 # utilizando probabilidades y salidas Random:      
        
Pro=np.array(np.random.rand(5,1))
ylabel=np.array(np.random.randint(0,2,5))

# se define la entropia para cualquier caso

def entropi(P,y):
    y = np.float_(y)
    P = np.float_(P)
    return -np.sum(y * np.log(P) + (1 - y) * np.log(1 - P))

# Se encuentra las entropias con los diferentes datos: 

# entropia con los datos Randon   
Entropia = entropi(Pro,ylabel)

# entropia on los datos expuestos al principio
Entropia2 = entropi(Probabilidades,ysal)

print(Entropia)
print(Entropia2)

    
        

        


            
        
        

