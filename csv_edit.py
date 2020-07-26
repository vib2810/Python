import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
flag=1
# to verify correct data
if (len(sys.argv) > 2):
    print ("invalid number of arguments:   " + str(len(sys.argv)))
    print ("should be 2: 'bag2csv.py' and 'bagName'")
    sys.exit(1)
elif (len(sys.argv) == 2):
    response = pd.read_csv(sys.argv[1])
    # nresponse = pd.DataFrame()
    # nresponse = nresponse.astype(np.float64)
    # print "Size of Data: "+ str(response.shape[0])
    # for i in range(1,response.shape[0]):
    #     # if(abs(response.iat[i,1]-response.iat[i-1,1])>1):
    #     #     print str(response.iat[i,1]-response.iat[i-1,1]) + " " + str(i)
    #     #     flag=flag*-1
    #     # if(i==600 or i==1200 or i==1550 or i==2150 or i==2600 or i==3100 or i==3600 or i==4100 or i==4600 or i==5100 or i==5600 or i==6100):
    #     #     flag=-flag
    #     nresponse= nresponse.append( response.iloc[i],ignore_index=True)
    #     nresponse.iat[i-1,1]=nresponse.iat[i-1,1]*flag
    # for i in range(0,nresponse.shape[0]):
    #   if (nresponse.iat[i,1]<=-1):
    #       nresponse.iat[i,1]=-1
    #   if (nresponse.iat[i,1]>=1): 
    #       nresponse.iat[i,1]=1
    # plt.plot(nresponse.iloc[:,0])
    file1 = open("MyFile.txt","w+") 
    for i in range(1, response.shape[0]):
        str1 = str(response.iat[i,10]) + "," + str(response.iat[i,11]) + ", Kharagpur,#FFFF00\n"
        file1.write(str1)
    file1.close() 


    # print(response)
    # nresponse.to_csv("output_filename.csv", index=False, encoding='utf8')

