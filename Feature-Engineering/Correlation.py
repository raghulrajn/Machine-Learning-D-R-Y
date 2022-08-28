import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def drawCorrelationMatrix(df):
    
    cmap = sns.diverging_palette(250, 15, s=75, l=40,
                                 n=9, center="light", as_cmap=True)
    matrix = df.corr()
    mask = np.triu(np.ones_like(matrix, dtype=bool))
    plt.figure(figsize=(16,12))
    plt.title("Correlation heatmap between all parameters")
    fig = sns.heatmap(matrix, mask=mask, center=0, annot=True,
                 fmt='.2f', square=True, cmap=cmap)    
    
def getRedundantPairs(df):
    '''Get diagonal and lower triangular pairs of correlation matrix'''
    pairs_to_drop = set()
    cols = df.columns
    for i in range(0, df.shape[1]):
        for j in range(0, i+1):
            pairs_to_drop.add((cols[i], cols[j]))
    return pairs_to_drop

def getTopAbsCorrelations(df, n=5,method = 'pearson'):
#   ''' Get top 5 most correlated features in the given dataset. Method can be 'pearson', 'spearman', 'kendall' ''''
    au_corr = df.corr(method = method).abs().unstack()
    labels_to_drop = getRedundantPairs(df)
    au_corr = au_corr.drop(labels=labels_to_drop).sort_values(ascending=False)
    print("Top {} Correlated features in given dataset".format(n))
    return au_corr[0:n]
