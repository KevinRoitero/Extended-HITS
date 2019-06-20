import numpy as np
from numpy import linalg

def Extended_HITS(input_matrix, epsilon):
    iter = 0
    n = len(input_matrix)
    
    x0 = np.ones( (n,1) )
    h  = np.ones( (n,1) )
    a  = np.ones( (n,1) ) 
    
    h = h / np.linalg.norm(h, ord=1)
       
    diff_auth = 1.0
    diff_hub = 1.0
    
    while  (diff_auth > epsilon)  |  (diff_hub > epsilon):
        iter +=1
        x0_auth = a
        x0_hub = h
    
        a = np.dot(np.transpose(input_matrix),h)
        h = np.dot(input_matrix,a)
        
        a = a / np.linalg.norm(a, ord=1)
        h = h / np.linalg.norm(h, ord=1)

        diff_auth = (np.absolute(x0_auth - a)).sum()
        diff_hub  = (np.absolute(x0_hub - h)).sum()

    h = [x[0,0] for x in h] 
    a = [x[0,0] for x in a] 
    return({'autority':a, 'hubness':h, 'iterations':iter} )