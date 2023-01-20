import pandas as pd
import numpy as np

pie_df = pd.DataFrame(columns = ['apple', 'banana', 'coconut cream', 'lemon meringue', 'pumpkin', 'chocolate', 'rubarb', 'cherry'])

for i in [j for j in pie_df.columns if j != 'person']:
    listy = np.random.randint(2, size=300)
    if sum(listy) in pie_df.sum().values:
        listy = np.random.randint(2, size=300)
        pie_df[i] = listy
    else:
        pie_df[i] = listy
