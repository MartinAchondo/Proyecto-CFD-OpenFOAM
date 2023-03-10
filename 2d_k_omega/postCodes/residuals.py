import os
import numpy as np
import pandas as pd
from io import StringIO

def get_residuals(case):

    file = 'residuals.dat'
    path_current_L = os.path.dirname(os.path.realpath(__file__)).split("\\")
    path_current_L.pop()
    path_case = "\\".join(path_current_L)
    path_file = os.path.join(path_case,'postProcessing','residuals',str(case.iniTime), file)

    with open(path_file,'r') as f:
        content = f.read()
        content = content.split('\n')
        del content[0]
        del content[1]
        contentIO = StringIO('\n'.join(content))

    data = pd.read_csv(contentIO, delimiter='\t')
    data.columns = ['Time','p','Ux','Uy','k','omega']

    return data