import pandas as pd
import numpy as np

df = pd.read_excel(<FILE>)

grp_df = df.groupby(['COL_A','COL_B']).agg({'Quantity': 'sum'})
grp_df = grp_df.groupby(level=1).apply(lambda x:100 * x / float(x.sum())).reset_index()

# grp_df = df.groupby(['COL_A','COL_B']).agg({'Quantity': 'sum'})
# df['%'] = 100 * df['sales'] / df.groupby('state')['sales'].transform('sum')

grp_df['pct'] = grp_df['Quantity'].apply(lambda x: float("{:.2f}".format(x)))
grp_df['>75%'] = grp_df['pct'].apply(lambda x: x>75)
grp_df['75%-50%'] = grp_df['pct'].apply(lambda x: x>50 and x<75)
grp_df['25%-50%'] = grp_df['pct'].apply(lambda x: x<50 and x>25)
grp_df['<25%'] = grp_df['pct'].apply(lambda x: x<25)

grp_df_export_new = grp_df.reset_index()
grp_df_export_new.to_excel(<FILE-NAME>)
