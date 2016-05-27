import pandas as pd
import numpy as np
import scipy.stats as sc
import math as mt

#import data
FLins = pd.read_csv('Flinspec.csv')
WAins = pd.read_csv('WLinspec.csv')
FLviol = pd.read_csv('Flviol.csv')
WAviol = pd.read_csv('Wlviol.csv')

#converting to required format for FL data
a = pd.pivot_table(FLins,index=["RestName"],columns=["inspectionType"],aggfunc={"InspecId":len},fill_value=0)
b = pd.pivot_table(FLins,index=["RestName"],columns=["result"],aggfunc={"InspecId":len},fill_value=0)
c= pd.merge(a,b,how='outer',left_index=True, right_index=True)
nfi = pd.pivot_table(FLins,index=["RestName"],aggfunc={"InspecId":len},fill_value=0)
FInew= pd.merge(c,nfi,how='outer',left_index=True, right_index=True)
FInew = (FInew.ix[:,0:9].T/FInew.ix[:,9]).T
#FInew.to_csv('FInew.csv')

#converting to required format for WA data
a = pd.pivot_table(WAins,index=["RestName"],columns=["inspectionType"],aggfunc={"InspecId":len},fill_value=0)
b = pd.pivot_table(WAins,index=["RestName"],columns=["result"],aggfunc={"InspecId":len},fill_value=0)
c= pd.merge(b,a,how='outer',left_index=True, right_index=True)
nwi = pd.pivot_table(WAins,index=["RestName"],aggfunc={"InspecId":len},fill_value=0)
WInew= pd.merge(c,nwi,how='outer',left_index=True, right_index=True)
WInew = (WInew.ix[:,0:16].T/WInew.ix[:,16]).T
#WInew.to_csv('WInew.csv')

#converting to required format for FL data
cos = pd.pivot_table(FLviol,index=["RestName"],columns=["correctedOnSite"],aggfunc={"violId":len},fill_value=0)
rv = pd.pivot_table(FLviol,index=["RestName"],columns=["repeatViolation"],aggfunc={"violId":len},fill_value=0)
cr = pd.pivot_table(FLviol,index=["RestName"],columns=["critical"],aggfunc={"violId":len},fill_value=0)
pi = pd.pivot_table(FLviol,index=["RestName"],columns=["priorityItem"],aggfunc={"violId":len},fill_value=0)
pfi = pd.pivot_table(FLviol,index=["RestName"],columns=["priorityFoundationItem"],aggfunc={"violId":len},fill_value=0)
ci = pd.pivot_table(FLviol,index=["RestName"],columns=["coreItem"],aggfunc={"violId":len},fill_value=0)
rc = pd.pivot_table(FLviol,index=["RestName"],columns=["riskCategory"],aggfunc={"violId":len},fill_value=0)
cosrv= pd.merge(cos,rv,how='outer',left_index=True, right_index=True)
crpi= pd.merge(cr,pi,how='outer',left_index=True, right_index=True)
pfici= pd.merge(pfi,ci,how='outer',left_index=True, right_index=True)
pficirc= pd.merge(pfici,rc,how='outer',left_index=True, right_index=True)
cosrvpficirc= pd.merge(cosrv,pficirc,how='outer',left_index=True, right_index=True)
cosrvpficirccrpi= pd.merge(cosrvpficirc,crpi,how='outer',left_index=True, right_index=True)
vc = pd.pivot_table(FLviol,index=["RestName"],aggfunc={"violId":len},fill_value=0)
FVnew= pd.merge(cosrvpficirccrpi,vc,how='outer',left_index=True, right_index=True)
FVnew = (FVnew.ix[:,0:15].T/FVnew.ix[:,15]).T
#FVnew.to_csv('FVnew.csv')

#converting to required format for WA data
a = pd.pivot_table(WAviol,index=["RestName"],columns=["critical"],aggfunc={"violId":len},fill_value=0)
b = pd.pivot_table(WAviol,index=["RestName"],values=["points"],aggfunc=[np.sum])
c= pd.merge(a,b,how='outer',left_index=True, right_index=True)
wc = pd.pivot_table(WAviol,index=["RestName"],aggfunc={"violId":len},fill_value=0)
WVnew= pd.merge(c,wc,how='outer',left_index=True, right_index=True)
WVnew = (WVnew.ix[:,0:3].T/WVnew.ix[:,3]).T
#WVnew.to_csv('WVnew.csv')

#importing weights
fi = pd.read_csv('Input1.csv')
fi = np.array(fi.ix[:,0])
wi = pd.read_csv('Input2.csv')
wi = np.array(wi.ix[:,0])
fv = pd.read_csv('Input3.csv')
fv = np.array(fv.ix[:,0])
wv = pd.read_csv('Input4.csv')
wv = np.array(wv.ix[:,0])

#obtaining score for FL
FInew  = FInew.ix[:,0:9]*fi
scoreF = FInew.sum(axis=1)
scoreF11 = scoreF

FVnew = FVnew.ix[:,0:15]*fv
scoreFV = FVnew.sum(axis=1)
scoreFV11 =scoreFV

#obtaining score for WA
WInew  = WInew.ix[:,0:16]*wi
scoreW = WInew.sum(axis=1)
scoreW11 = scoreW

WVnew  = WVnew.ix[:,0:3]*wv
scoreWV = WVnew.sum(axis=1)
scoreWV11 = scoreWV

#adjusting scores

nfi1 = np.array(nfi)
nfi2 = np.array(vc)
nwi = np.array(nwi)
wc = np.array(wc)

scoreF = pd.DataFrame(scoreF,index=FInew.index)
scoreFV = pd.DataFrame(scoreFV,index=FVnew.index)
scoreW = pd.DataFrame(scoreW,index=WInew.index)
scoreWV = pd.DataFrame(scoreWV,index=WVnew.index)

scoreF1 = np.array(scoreF)
scoreFV1 = np.array(scoreFV)
scoreW1 = np.array(scoreW)
scoreWV1 = np.array(scoreWV)

#FL inspec score
M=np.mean(scoreF1)
SD = np.std(scoreF1)
for i in range(0,len(scoreF1)):
    m = scoreF1[i]
    sd = SD/mt.sqrt(nfi1[i])
    c = 1
    u=0
    if (m < M):
        a= np.arange(m,M,0.01)
        for k in range(0, len(a)):
            y = 1-sc.norm.cdf(a[k], m, sd)
            z = sc.norm.cdf(a[k], M, SD)
            q = abs(z-y)
            if q < c:
                c = q
                u = a[k]
        scoreF1[i]=u
    else:
        a = np.arange(M,m,0.01)
        for k in range(0,len(a)):
                y =sc.norm.cdf(a[k],m,sd)
                z=1-sc.norm.cdf(a[k],M,SD)
                q = abs(z-y)
                if q<c:
                    c=q
                    u= a[k]
        scoreF1[i] = u

sdf = np.std(scoreF1)
mf= scoreF1.mean(0)
scoreF1 = 100*(1-sc.norm.cdf(scoreF1,mf,sdf))
scoreF1 = pd.DataFrame(scoreF1,columns=['ScoreF'])
scoreF1[scoreF1 <1] = 1
scoreF1  = np.array(scoreF1)
#scoreF1 = mt.ceil(scoreF1)
scoreF1 = pd.DataFrame(scoreF1,index=scoreF.index)

#FL viol score
M=np.mean(scoreFV1)
SD = np.std(scoreFV1)
for i in range(0,len(scoreFV1)):
    m = scoreFV1[i]
    sd = SD/mt.sqrt(nfi2[i])
    c = 1
    u=0
    if (m < M):
        a= np.arange(m,M,0.01)
        for k in range(0, len(a)):
            y = 1-sc.norm.cdf(a[k], m, sd)
            z = sc.norm.cdf(a[k], M, SD)
            q = abs(z-y)
            if q < c:
                c = q
                u = a[k]
        scoreFV1[i]=u
    else:
        a = np.arange(M,m,0.01)
        for k in range(0,len(a)):
                y =sc.norm.cdf(a[k],m,sd)
                z=1-sc.norm.cdf(a[k],M,SD)
                q = abs(z-y)
                if q<c:
                    c=q
                    u= a[k]
        scoreFV1[i] = u

sdf = np.std(scoreFV1)
mf= scoreFV1.mean(0)
scoreFV1 = 100*(1-sc.norm.cdf(scoreFV1,mf,sdf))
scoreFV1 = pd.DataFrame(scoreFV1,columns=['ScoreFV'])
scoreFV1[scoreFV1 <1] = 1
scoreFV1  = np.array(scoreFV1)
#scoreFV1 = mt.ceil(scoreFV1)
scoreFV1 = pd.DataFrame(scoreFV1,index=scoreFV.index)

#WA inspec score
M=np.mean(scoreW1)
SD = np.std(scoreW1)
for i in range(0,len(scoreW1)):
    m = scoreW1[i]
    sd = SD/mt.sqrt(nwi[i])
    c = 1
    u=0
    if (m < M):
        a= np.arange(m,M,0.01)
        for k in range(0, len(a)):
            y = 1-sc.norm.cdf(a[k], m, sd)
            z = sc.norm.cdf(a[k], M, SD)
            q = abs(z-y)
            if q < c:
                c = q
                u = a[k]
        scoreW1[i]=u
    else:
        a = np.arange(M,m,0.01)
        for k in range(0,len(a)):
                y =sc.norm.cdf(a[k],m,sd)
                z=1-sc.norm.cdf(a[k],M,SD)
                q = abs(z-y)
                if q<c:
                    c=q
                    u= a[k]
        scoreW1[i] = u

sdf = np.std(scoreW1)
mf= scoreW1.mean(0)
scoreW1 = 100*(1-sc.norm.cdf(scoreW1,mf,sdf))
scoreW1 = pd.DataFrame(scoreW1,columns=['ScoreW'])
scoreW1[scoreW1 <1] = 1
scoreW1  = np.array(scoreW1)
#scoreW1 = mt.ceil(scoreW1)
scoreW1 = pd.DataFrame(scoreW1,index=scoreW.index)

#WA inspec score
M=np.mean(scoreWV1)
SD = np.std(scoreWV1)
for i in range(0,len(scoreWV1)):
    m = scoreWV1[i]
    sd = SD/mt.sqrt(wc[i])
    c = 1
    u=0
    if (m < M):
        a= np.arange(m,M,0.01)
        for k in range(0, len(a)):
            y = 1-sc.norm.cdf(a[k], m, sd)
            z = sc.norm.cdf(a[k], M, SD)
            q = abs(z-y)
            if q < c:
                c = q
                u = a[k]
        scoreWV1[i]=u
    else:
        a = np.arange(M,m,0.01)
        for k in range(0,len(a)):
                y =sc.norm.cdf(a[k],m,sd)
                z=1-sc.norm.cdf(a[k],M,SD)
                q = abs(z-y)
                if q<c:
                    c=q
                    u= a[k]
        scoreWV1[i] = u

mf= scoreWV1.mean(0)
sdf = np.std(scoreWV1)
scoreWV1 = 100*(1-sc.norm.cdf(scoreWV1,mf,sdf))
scoreWV1 = pd.DataFrame(scoreWV1,columns=['ScoreWV'])
scoreWV1[scoreWV1 <1] = 1
scoreWV1  = np.array(scoreWV1)
#scoreWV1 = mt.ceil(scoreWV1)


scoreWV1 = pd.DataFrame(scoreWV1,index=scoreWV.index)

FloridaScore = pd.concat([scoreF1, scoreFV1], axis=1)
WAScore = pd.concat([scoreW1, scoreWV1], axis=1)


mf1= scoreF11.mean(0)
sdf1 = np.std(scoreF11)
mf2= scoreFV11.mean(0)
sdf2 = np.std(scoreFV11)
mf3= scoreW11.mean(0)
sdf3 = np.std(scoreW11)
mf4= scoreWV11.mean(0)
sdf4 = np.std(scoreWV11)

scoreF11 = 100*(1-sc.norm.cdf(scoreF11,mf1,sdf1))
scoreFV11 = 100*(1-sc.norm.cdf(scoreFV11,mf2,sdf2))
scoreW11 = 100*(1-sc.norm.cdf(scoreW11,mf3,sdf3))
scoreWV11 = 100*(1-sc.norm.cdf(scoreWV11,mf4,sdf4))

scoreF11 = pd.DataFrame(scoreF11,index=scoreF.index)
scoreFV11 = pd.DataFrame(scoreFV11,index=scoreFV.index)
scoreW11 = pd.DataFrame(scoreW11,index=scoreW.index)
scoreWV11 = pd.DataFrame(scoreWV11,index=scoreWV.index)

#scoreF11 = mt.ceil(scoreF11)
#scoreFV11 = mt.ceil(scoreFV11)
#scoreW11 = mt.ceil(scoreW11)
#scoreWV11 = mt.ceil(scoreWV11)



FloridaScoreNA = pd.concat([scoreF11, scoreFV11], axis=1)
WAScoreNA = pd.concat([scoreW11, scoreWV11], axis=1)

FinalScore1 = FloridaScore.append(WAScore)
FinalScoreNA = FloridaScoreNA.append(WAScoreNA)

FinalScore = pd.concat([FinalScore1, FinalScoreNA], axis=1)



FinalScore.columns = ['Inspection Score','Violation Score','Inspection ScoreNA','Violation ScoreNA']


FinalScore.to_csv('FinalScore.csv')