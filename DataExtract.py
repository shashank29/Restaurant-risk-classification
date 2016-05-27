import pandas as pd
import numpy as np
import urllib.request
import json
import scipy.stats as sc

#import florida data
flor1 = urllib.request.urlopen('https://s3.amazonaws.com/florida-restaurant-inspections/florida-restaurants-with-inspections.json')
flor2 = flor1.read().decode('utf-8')
flor = json.loads(flor2)

#import washington data
wash1 = urllib.request.urlopen('https://s3.amazonaws.com/florida-restaurant-inspections/WA-restaurants-with-inspections.json')
wash2 = wash1.read().decode('utf-8')
wash = json.loads(wash2)

#extract florida restaurant names
restf = []
for i in flor.keys():
    restf.append(i)
restf = np.array(restf)

#extract WA restaurant names
restw = []
for i in wash.keys():
    restw.append(i)
restw = np.array(restw)

#extracting required fields in FL data
FI = np.empty(shape = (0,4) , dtype = object)
for j in range(0,len(flor)):
    for k in range(0, len(flor[restf[j]])):
        for l in range(0, len(flor[restf[j]][k]["inspections"])):
            RestName = restf[j]
            InspecId = flor[restf[j]][k]["inspections"][l]["id"]
            inspectionType = flor[restf[j]][k]["inspections"][l]["inspectionType"]
            result = flor[restf[j]][k]["inspections"][l]["result"]

            temp = np.array([RestName,InspecId,inspectionType,result])

            FI = np.vstack((FI,temp))

columns = [ 'RestName','InspecId','inspectionType','result']
FI = pd.DataFrame(FI, columns = columns)

#extracting required fields in WA data
WI = np.empty(shape = (0,4) , dtype = object)
for j in range(0,len(wash)):
    for k in range(0, len(wash[restw[j]])):
        for l in range(0, len(wash[restw[j]][k]["inspections"])):
            RestName = restw[j]
            InspecId = wash[restw[j]][k]["inspections"][l]["id"]
            inspectionType = wash[restw[j]][k]["inspections"][l]["inspectionType"]
            result = wash[restw[j]][k]["inspections"][l]["result"]

            temp = np.array([RestName,InspecId,inspectionType,result])

            WI = np.vstack((WI,temp))

columns = [ 'RestName','InspecId','inspectionType','result']
WI = pd.DataFrame(WI, columns = columns)

#extracting required fields in FL data
FInew = np.empty(shape = (0,9) , dtype = object)
for j in range(0,len(flor)):
    for k in range(0, len(flor[restf[j]])):
        for l in range(0, len(flor[restf[j]][k]["inspections"])):
            for m in range(0, len(flor[restf[j]][k]["inspections"][l]["violations"])):
                RestName = restf[j]
                violId = flor[restf[j]][k]["inspections"][l]["violations"][m]["id"]
                correctedOnSite = flor[restf[j]][k]["inspections"][l]["violations"][m]["correctedOnSite"]
                repeatViolation = flor[restf[j]][k]["inspections"][l]["violations"][m]["repeatViolation"]
                critical = flor[restf[j]][k]["inspections"][l]["violations"][m]["critical"]
                priorityItem = flor[restf[j]][k]["inspections"][l]["violations"][m]["priorityItem"]
                priorityFoundationItem = flor[restf[j]][k]["inspections"][l]["violations"][m]["priorityFoundationItem"]
                coreItem = flor[restf[j]][k]["inspections"][l]["violations"][m]["coreItem"]
                riskCategory = flor[restf[j]][k]["inspections"][l]["violations"][m]["riskCategory"]

                temp = np.array([RestName,violId,correctedOnSite,repeatViolation,critical,priorityItem,priorityFoundationItem,coreItem, riskCategory ])

                FInew = np.vstack((FInew,temp))

columns = [ 'RestName','violId','correctedOnSite','repeatViolation','critical','priorityItem','priorityFoundationItem','coreItem', 'riskCategory' ]
FInew = pd.DataFrame(FInew, columns = columns)
FInew.fillna('missing')
#FInew.ix[:,2:8]=FInew.ix[:,2:8].str.lower()

#extracting required fields in WA data
WInew = np.empty(shape = (0,4) , dtype = object)
for j in range(0,len(wash)):
    for k in range(0, len(wash[restw[j]])):
        for l in range(0, len(wash[restw[j]][k]["inspections"])):
            for m in range(0, len(wash[restw[j]][k]["inspections"][l]["violations"])):
                RestName = restw[j]
                violId = wash[restw[j]][k]["inspections"][l]["violations"][m]["id"]
                points = wash[restw[j]][k]["inspections"][l]["violations"][m]["points"]
                critical = wash[restw[j]][k]["inspections"][l]["violations"][m]["critical"]

                temp = np.array([RestName,violId,points,critical])

                WInew = np.vstack((WInew,temp))

columns = [ 'RestName','violId','points','critical']
WInew = pd.DataFrame(WInew, columns = columns)
WInew['critical']=WInew['critical'].str.lower()
WInew.fillna('missing')
WInew['points'] = pd.to_numeric(WInew['points'])
WInew['points'] = np.array(WInew['points'])

FLinspec  = pd.DataFrame(FI)
FLinspec.to_csv('Flinspec.csv',index=False)

WLinspec  = pd.DataFrame(WI)
WLinspec.to_csv('Wlinspec.csv',index=False)

FLviol  = pd.DataFrame(FInew)
FLviol.to_csv('Flviol.csv',index=False)

WLviol  = pd.DataFrame(WInew)
WLviol.to_csv('Wlviol.csv',index=False)