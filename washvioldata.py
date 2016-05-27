import pandas as pd
import numpy as np

import json

with open('washing.json') as data_file:
    wash = json.load(data_file)

restn = []

for i in wash.keys():
    restn.append(i)
restn = np.array(restn)

washrestdata = np.empty(shape = (0,18) , dtype = object)

for j in range(0,len(wash)):
        for k in range (0,len(wash[restn[j]])):
            for l in range(0,len(wash[restn[j]][k]["inspections"])):
                for m in range(0, len(wash[restn[j]][k]["inspections"][l]["violations"])):

                    RestName = restn[j]

                    EstId = wash[restn[j]][k]["id"]

                    InspecId = wash[restn[j]][k]["inspections"][l]["id"]

                    violId = wash[restn[j]][k]["inspections"][l]["violations"][m]["id"]
                    observation = wash[restn[j]][k]["inspections"][l]["violations"][m]["observation"]
                    code = wash[restn[j]][k]["inspections"][l]["violations"][m]["code"]
                    correctiveAction = wash[restn[j]][k]["inspections"][l]["violations"][m]["correctiveAction"]
                    correctByDate = wash[restn[j]][k]["inspections"][l]["violations"][m]["correctByDate"]
                    violationNumber = wash[restn[j]][k]["inspections"][l]["violations"][m]["violationNumber"]
                    violation = wash[restn[j]][k]["inspections"][l]["violations"][m]["violation"]
                    points = wash[restn[j]][k]["inspections"][l]["violations"][m]["points"]
                    correctedOnSite = wash[restn[j]][k]["inspections"][l]["violations"][m]["correctedOnSite"]
                    repeatViolation = wash[restn[j]][k]["inspections"][l]["violations"][m]["repeatViolation"]
                    critical = wash[restn[j]][k]["inspections"][l]["violations"][m]["critical"]
                    priorityItem = wash[restn[j]][k]["inspections"][l]["violations"][m]["priorityItem"]
                    priorityFoundationItem = wash[restn[j]][k]["inspections"][l]["violations"][m]["priorityFoundationItem"]
                    coreItem = wash[restn[j]][k]["inspections"][l]["violations"][m]["coreItem"]
                    riskCategory = wash[restn[j]][k]["inspections"][l]["violations"][m]["riskCategory"]

                    temp = np.array([RestName,
                                     EstId,
                                     InspecId,
                                     violId,
                                     observation,
                                     code,
                                     correctiveAction,
                                     correctByDate,
                                     violationNumber,
                                     violation,
                                     points,
                                     correctedOnSite,
                                     repeatViolation,
                                     critical,
                                     priorityItem,
                                     priorityFoundationItem,
                                     coreItem,
                                     riskCategory])

                    washrestdata = np.vstack((washrestdata, temp))

columns = [ 'RestName',
            'EstId',
            'InspecId',
            'ViolId',
            'observation',
            'code',
            'correctiveAction',
            'correctByDate',
            'violationNumber',
            'violation',
            'points',
            'correctedOnSite',
            'repeatViolation',
            'critical',
            'priorityItem',
            'priorityFoundationItem',
            'coreItem',
            'riskCategory']
washrestdata = pd.DataFrame(washrestdata, columns = columns)
washrestdata.to_csv('WashRestViol.csv')