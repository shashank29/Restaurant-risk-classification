import pandas as pd
import numpy as np

import json

with open('washing.json') as data_file:
    wash = json.load(data_file)

restn = []

for i in wash.keys():
    restn.append(i)
restn = np.array(restn)

washrestdata = np.empty(shape = (0,39) , dtype = object)

for j in range(0,len(wash)):
        for k in range (0,len(wash[restn[j]])):
            for l in range(0,len(wash[restn[j]][k]["inspections"])):

                RestName = restn[j]

                EstId = wash[restn[j]][k]["id"]

                InspecId = wash[restn[j]][k]["inspections"][l]["id"]
                establishmentName = wash[restn[j]][k]["inspections"][l]["establishmentName"]
                addressOne = wash[restn[j]][k]["inspections"][l]["addressOne"]
                addressTwo = wash[restn[j]][k]["inspections"][l]["addressTwo"]
                city = wash[restn[j]][k]["inspections"][l]["city"]
                stateOrProvince = wash[restn[j]][k]["inspections"][l]["stateOrProvince"]
                county = wash[restn[j]][k]["inspections"][l]["county"]
                postalCode = wash[restn[j]][k]["inspections"][l]["postalCode"]
                telephone = wash[restn[j]][k]["inspections"][l]["telephone"]
                email = wash[restn[j]][k]["inspections"][l]["email"]
                inspectionDate = wash[restn[j]][k]["inspections"][l]["inspectionDate"]
                outOfBusinessDate = wash[restn[j]][k]["inspections"][l]["outOfBusinessDate"]
                outOfBusiness = wash[restn[j]][k]["inspections"][l]["outOfBusiness"]
                licenseHolder = wash[restn[j]][k]["inspections"][l]["licenseHolder"]
                licenseNumber = wash[restn[j]][k]["inspections"][l]["licenseNumber"]
                licenseStart = wash[restn[j]][k]["inspections"][l]["licenseStart"]
                licenseEnd = wash[restn[j]][k]["inspections"][l]["licenseEnd"]
                inspectionType = wash[restn[j]][k]["inspections"][l]["inspectionType"]
                establishmentType = wash[restn[j]][k]["inspections"][l]["establishmentType"]
                certifiedFoodProtectionManager = wash[restn[j]][k]["inspections"][l]["certifiedFoodProtectionManager"]
                certifiedFoodProtectionManagerLicenseEnd = wash[restn[j]][k]["inspections"][l]["certifiedFoodProtectionManagerLicenseEnd"]
                solidWasteContractor = wash[restn[j]][k]["inspections"][l]["solidWasteContractor"]
                liquidGreaseContractor = wash[restn[j]][k]["inspections"][l]["liquidGreaseContractor"]
                pestExterminator = wash[restn[j]][k]["inspections"][l]["pestExterminator"]
                inspector = wash[restn[j]][k]["inspections"][l]["inspector"]
                inspectorId = wash[restn[j]][k]["inspections"][l]["inspectorId"]
                comments = wash[restn[j]][k]["inspections"][l]["comments"]
                result = wash[restn[j]][k]["inspections"][l]["result"]
                personInChargeSignature = wash[restn[j]][k]["inspections"][l]["personInChargeSignature"]
                link = wash[restn[j]][k]["inspections"][l]["link"]
                healthDepartment = wash[restn[j]][k]["inspections"][l]["healthDepartment"]
                grade = wash[restn[j]][k]["inspections"][l]["grade"]
                score = wash[restn[j]][k]["inspections"][l]["score"]
                establishmentRiskRating = wash[restn[j]][k]["inspections"][l]["establishmentRiskRating"]
                establishmentNumber = wash[restn[j]][k]["inspections"][l]["establishmentNumber"]
                establishmentId = wash[restn[j]][k]["inspections"][l]["establishmentId"]
                inspectionArea = wash[restn[j]][k]["inspections"][l]["inspectionArea"]

                temp = np.array([RestName,
                                 EstId,
                                 InspecId,
                                 establishmentName,
                                 addressOne,
                                 addressTwo,
                                 city,
                                 stateOrProvince,
                                 county,
                                 postalCode,
                                 telephone,
                                 email,
                                 inspectionDate,
                                 outOfBusinessDate,
                                 outOfBusiness,
                                 licenseHolder,
                                 licenseNumber,
                                 licenseStart,
                                 licenseEnd,
                                 inspectionType,
                                 establishmentType,
                                 certifiedFoodProtectionManager,
                                 certifiedFoodProtectionManagerLicenseEnd,
                                 solidWasteContractor,
                                 liquidGreaseContractor,
                                 pestExterminator,
                                 inspector,
                                 inspectorId,
                                 comments,
                                 result,
                                 personInChargeSignature,
                                 link,
                                 healthDepartment,
                                 grade,
                                 score,
                                 establishmentRiskRating,
                                 establishmentNumber,
                                 establishmentId,
                                 inspectionArea])

                washrestdata = np.vstack((washrestdata,temp))

columns = [ 'RestName',
            'EstId',
            'InspecId',
            'establishmentName',
            'addressOne',
            'addressTwo',
            'city',
            'stateOrProvince',
            'county',
            'postalCode',
            'telephone',
            'email',
            'inspectionDate',
            'outOfBusinessDate',
            'outOfBusiness',
            'licenseHolder',
            'licenseNumber',
            'licenseStart',
            'licenseEnd',
            'inspectionType',
            'establishmentType',
            'certifiedFoodProtectionManager',
            'certifiedFoodProtectionManagerLicenseEnd',
            'solidWasteContractor',
            'liquidGreaseContractor',
            'pestExterminator',
            'inspector',
            'inspectorId',
            'comments',
            'result',
            'personInChargeSignature',
            'link',
            'healthDepartment',
            'grade',
            'score',
            'establishmentRiskRating',
            'establishmentNumber',
            'establishmentId',
            'inspectionArea']
washrestdata = pd.DataFrame(washrestdata, columns = columns)
washrestdata.to_csv('WashRestInspec.csv')