import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
response = pd.read_csv("_slash_throttle.csv")
a=0
print(response.shape[0]-1)
for i in range(0,response.shape[0]-1):
	if response.iat[i,0] == response.iat[i+1,0]:
		response.iat[i,0]=0
		a=a+1
print(a)
nresponse = pd.DataFrame()
nresponse = nresponse.astype(np.float64)

for i in range(0,response.shape[0]-1):
	if response.iat[i,0] != 0:
		nresponse= nresponse.append( response.iloc[i],ignore_index=True)
		# response=response.drop(i,axis=0)
		# i=i-1
a=0
for i in range(0,nresponse.shape[0]-1):
	nresponse.iat[i,1]=a
	a=a+response.iat[i,1]
plt.plot(nresponse.iloc[:,1])
plt.plot(26*nresponse.iloc[:,2])
plt.show()


print(nresponse)
nresponse.to_csv("output_filename.csv", index=False, encoding='utf8')

