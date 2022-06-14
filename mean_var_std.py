import pandas as pd 
import numpy as np

def calculate(liste):

	flat = np.array(liste)
	mat = flat.reshape((3, 3))

	calc = {
	    'mean': [
	        list(np.mean(mat, axis=0)),
	        list(np.mean(mat, axis=1)),
	        np.mean(flat),
	    ]
	}
	calc['variance'] = [list(np.var(mat, axis=0)), list(np.var(mat, axis=1)), np.var(flat)]
	calc['standard deviation'] = [list(np.std(mat, axis=0)), list(np.std(mat, axis=1)), np.std(flat)]
	calc['minimum'] = [list(np.min(mat, axis=0)), list(np.min(mat, axis=1)), np.min(flat)]
	calc['maximum'] = [list(np.max(mat, axis=0)), list(np.max(mat, axis=1)), np.max(flat)]
	calc['summation'] = [list(np.sum(mat, axis=0)), list(np.sum(mat, axis=1)), np.sum(flat)]


	return calc