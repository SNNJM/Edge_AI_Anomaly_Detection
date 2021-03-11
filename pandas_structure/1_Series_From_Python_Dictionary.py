import pandas as pd
import numpy as np

data={'student':['Tom','Jerry','Gloria','Hillary'],
      'age':[21,34,45,67],
      'gender':['male','female','female','male']}

student = pd.Series(data)
print(student)
