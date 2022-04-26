from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

features = "[<INDEPENDENT FEATURES>]"

X = df.loc[:,features].values
y = df.loc[:,[TARGET]].values

_X = StandardScaler().fit_transform(X)

components = 2
def createPCA(components,df=_X):
  
    pca = PCA(n_components = components) # selecting PCA components with retaining 95% variance in dara
    principalComponents = pca.fit_transform(df) 
    cols = []
    for i in range(len(components)):
        cols.append("pc"+str(i+1))
    principalDf = pd.DataFrame(data = principalComponents
                 , columns = cols)
    return principalDf
