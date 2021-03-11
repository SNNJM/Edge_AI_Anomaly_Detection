import pandas as pd
import numpy as np

data={'name':['kaido','ichigo','rei','yuki'],
      'age':[20,19,22,21],
      'favourite_colour':['red','orange','green','blue'],
      'grade':[67,78,90,12],}

df = pd.DataFrame(data)
print(df)
