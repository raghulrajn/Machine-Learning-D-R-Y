from sklearn.decomposition import PCA


def createPCA(variance = 0.95,df):
  
    pca = PCA(variance) # selecting PCA components with retaining 95% variance in dara
    principalComponents = pca.fit_transform(df) 
    cols = []
    for i in range(len(principalComponents)):
        cols.append("pc"+str(i+1))
    principalDf = pd.DataFrame(data = principalComponents
                 , columns = cols)
    return principalDf
