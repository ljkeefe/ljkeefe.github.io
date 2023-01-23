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

        
MD_agg_df = pd.DataFrame(columns = ['Item', 'Item #', 'MaxDiff Score'])

MD_agg_df['Item'] = item_list
MD_agg_df['Item #'] = list(range(1,len(item_list)+1))

perc = 1
for i in item_list:
    j = np.random.uniform(0,perc)
    MD_agg_df.loc[MD_agg_df[''] == i, 'MaxDiff Score'] = j
    perc -= j
MD_agg_df.sort_values('MaxDiff Score', ascending=False)

MD_resp_df = pd.DataFrame(columns = item_list)

for i in list(range(500)):
    perc = 1
    for j in item_list:
        k = np.random.uniform(0,perc)
        MD_resp_df.loc[i, j] = k
        perc -= k
