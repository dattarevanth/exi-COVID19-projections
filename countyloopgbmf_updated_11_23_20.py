#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  15 11:54:15 2020

@author: revanth Datta

gbm loop: county
"""
n=5
if n<10:
	n=input('How many of the highest population counties in the US do you want to project? Please use numerical input:')
	n=int(n)
	if n > 10:
		print('That will take a long time due to API limitations. Are you sure?')
		answer=str(input('Y/N:'))
		if answer == 'N' or 'n':
			n=input('How many of the highest population counties in the US do you want to project? Please use numerical input:')
			n=int(n)
			if int(n) > 10: print('Ok. Please be patient.')

		else:
			print('Ok, please be patient.')
proj=input('How far out would you like to project? Please enter numerical days as input.')
proj=int(proj)
projlb=proj-5
for name in [proj,projlb]:
	name=str(name)
print(f"Projecting the total new cases until '{proj}' days in the future for the top '{n}' most populated US counties.")
answer2=input('Are you ready? Y/N:')
if str(answer2)== 'Y' or 'y':
	print('Prepare for a quantum leap. Please do not interrupt me.')
else:
	print('Sorry, science waits for no one.')
n=int(n)
proj=int(proj)
##############################################################################
import os
import pandas as pd
os.getcwd()
os.chdir('/Users/revanth/Documents/Datta_Fund/c3ai/')
#os.chdir() #need locids.csv and api pkg in wd, also install h2o
import c3aidatalake
import h2o
from h2o.estimators.gbm import H2OGradientBoostingEstimator
import bottleneck as bn
import numpy as np
from pyfinance import ols
##############################################################################
dfp = c3aidatalake.fetch(
		"populationdata",
	    {
		  "spec": {
		    "filter": "contains(parent, 'UnitedStates') && populationAge == 'Total' && gender == 'Male/Female' && year == 2019 && value >= '1000000'",
		    "limit": -1
		  }
	     },
	)
#&& value >= '500000'
countypops=dfp[[dfp.columns[-1],dfp.columns[-5]]]
countypops=countypops.copy()
countypops.sort_values(by='value',ascending=False,inplace=True)
countypops.reset_index(inplace=True,drop=True)
countypops.drop(8, inplace=True, axis=0)
l_o_c=countypops.iloc[0:n,0].tolist()
print('toppers')
#
##################CODE TO FETCH AND CALCULATE AVERAGE INTENT SCORES PER STATE###################
#fetch all survey data
survey = c3aidatalake.fetch(
    "surveydata",
    {
        "spec": {
            
        }
    },
    get_all = True
)

#filter it for the intent metrics - mask, 6 feet, stay home, wash hands
#put data in to dictionary
d = {
    'State': np.array(list(map(lambda a: a.split('_')[0], list(survey.iloc[:]['location.id'])))),
    'Mask': np.array(survey.iloc[:]['coronavirusIntent_Mask']),
    'SixF': np.array(survey.iloc[:]['coronavirusIntent_SixFeet']),
    'StayH': np.array(survey.iloc[:]['coronavirusIntent_StayHome']),
    'WashH': np.array(survey.iloc[:]['coronavirusIntent_WashHands'])
    }

#turn dictionary into dataframe and calculate averages by state
intent_by_state = pd.DataFrame(d).groupby("State").mean()

#delete dictionary and survey data because it is not needed
del d, survey
##############################################################################allmobilitycode
#####get cc, mob, dex
piqli=pd.read_csv('/Users/revanth/Documents/Datta_Fund/c3ai/piqlabels.csv')
pl=piqli.iloc[:,0].tolist()
del pl[26:] #remove device counts and non adjusted
del pl[1:13]
del pl[2:] #these deletions bc only count and exposure populated for harris, can check for otherse later
#only ones that come through for Harris are adjusted count and exposure

mob=['Apple_WalkingMobility', 
'Apple_DrivingMobility',
'Apple_TransitMobility',
'Google_GroceryMobility',
'Google_ParksMobility',
'Google_TransitStationsMobility',
'Google_RetailMobility',
'Google_ResidentialMobility',
'Google_WorkplacesMobility']
cl=['JHU_ConfirmedCases',
'JHU_ConfirmedDeaths',
'JHU_ConfirmedRecoveries',]
main=pl+mob+cl
print('lists')
train=pd.DataFrame()
test=pd.DataFrame()
traincombo=pd.DataFrame()
testcombo=pd.DataFrame()
loopcount=0
results=pd.DataFrame(columns=['Location', 'Mean Absolute Error',f"Mean Absolute Prediction: % new population infected from now till day '{proj}'" , '(MAE/y)*100'],
                     index=list(range(0,n,1)))
today = pd.Timestamp.now().strftime("%Y-%m-%d")

for i in l_o_c:
	#data pull
	loi=i
	df = c3aidatalake.evalmetrics(
	    "outbreaklocation",
	    {
	        "spec" : {
	            "ids" : [loi],
	            "expressions" : main,
	            "start" : "2020-02-15",
	            "end" : today,
	            "interval" : "DAY",
	        }
	    },
	    get_all = True
	)
	#data processing
	for i in list(range(28,0,-2)):
		df.drop(labels=df.columns[i], axis=1, inplace=True)
	dfs=df.copy(deep=True) #savepoint, don't call API again.
	df=dfs.copy(deep=True) #load save
	#tma 4 and 7 for mob and pl lists
	predlist = dfs.columns.tolist()
	del predlist[-2:]
	del predlist[0]
	del predlist[0]
	del predlist[8]
	for i in predlist:
		for x in [4,7,15]:
			df[i]=df[i].astype(float)
			df[i+'tma'+ str(x)]=bn.move_mean(df[i], window = x)

			df[str(i)+'_n'+str(x)]=df[i+'tma'+ str(x)]/df[i+'tma'+ str(x)].mean() * 100 
	print('tmas1')#print(i, x, sep=' , ')
            #may want to normalize this to a universal constant later
	npop = 300000000 #us pop, one column to quantify county size as an anchor, all values normalized to county
	#target loc size
	#
	#oldpop=dfp.iloc[0,8]
	pop=countypops.iloc[n,1]
	print(i, 'pop')
		#ppl currently infected estimate
	od=df.columns.tolist()[0:15] #original data column names
	#all((df[od[-6]] - (
    #    df[i+'.JHU_ConfirmedRecoveries.data']/df[i+'.JHU_ConfirmedCases.data']
    #    )*df[od[-6]] - df[od[-2]]) >=0)
	#sum((df[od[-6]] - (rr*df[od[-6]]) - df[od[-2]]) >=0)/271
	df=df[df[loi+'.JHU_ConfirmedCases.data'] > 0]
	df['ace']=(df[od[-6]]- df[od[-2]]) #active cases estimate
	df['ace_pn']=df['ace']/pop *100

	df['ncd']=df[loi+'.JHU_ConfirmedCases.data'].diff()
	df['ncd_pn']=df['ncd']/pop * 100 #new cases each day normalized by population of harris county


	df.reset_index(inplace=True, drop=True)
	df['n']=df.index #time equalizer across any loc bc we use n=0 as start of cases
	rolling = ols.PandasRollingOLS(y=df['ncd_pn'], x=df['n'], window=5)
	df['ncd_pn_s'] = rolling.beta
	df['ncd_pn_s'] = df['ncd_pn_s'].astype(float)
	df['ncd_pn_s_tma']=bn.move_mean(df['ncd_pn_s'], window=5) 

	#model prep
	df['ncd_pn']=df['ncd_pn'].astype(np.float64)
	df['ncd_pn_tma']=bn.move_mean(df['ncd_pn'], window=5)
	#df['ncd_pn_tma_f'+str(proj)]=df['ncd_pn_tma'].shift(proj)
	#df=df[df['ncd_pn_tma_f'+str(proj)].notnull()]
	#df['ncd_pn_tma_f'+str(proj)]=df['ncd_pn_tma_f'+str(proj)].astype(np.float64)
	#normalize to us pop 300mil
	#cum cases outcome
	df['cumcases'+str(proj)]=((df[loi+'.JHU_ConfirmedCases.data'].shift(-proj))-df[loi+'.JHU_ConfirmedCases.data'])/pop
	df=df[df['cumcases'+str(proj)].notnull()]
	df['cumcases'+str(proj)]=df['cumcases'+str(proj)].astype(np.float64)
	df['popn']=(pop/npop)*100
	#df['popoldn']=oldpop/pop
	#rr, aces
	for i in ['ace_pn']:
		for x in [4,7,15]:
			df[i]=df[i].astype(float)
			df[i+'tma'+ str(x)]=bn.move_mean(df[i], window = x)
			df[i+'tma'+ str(x)]=df[i+'tma'+ str(x)].astype(float)
			print('tmas2')
			df[str(i)+'_n'+str(x)]=df[i+'tma'+ str(x)]/df[i+'tma'+ str(x)].mean() * 100
		for ytime in [5,15,30]:
			rolling = ols.PandasRollingOLS(y=df[i], x=df['n'], window=ytime)
			df[i+str(ytime)] = rolling.beta
			df[i+str(ytime)]=df[i+str(ytime)].astype(float)
			print('slopes2')
		for i in [5,15,30]:
			rolling=rolling = ols.PandasRollingOLS(y=df['ace_pn'], x=df['n'], window=i)
			df['ace_pn'+str(i)+'^2']=rolling.beta
			df['ace_pn'+str(i)+'^2']=df['ace_pn'+str(i)+'^2'].astype(float)
			print(i)
		for i in [5,15,30]:
			df=df[df['ace_pn'+str(i)+'^2'].notnull()]
	##################CODE TO CALL INTENT SCORE###################    
	state_loi = loi.split('_')[-2]
	for i in intent_by_state.columns.tolist():
		df[i]=intent_by_state[i][state_loi]
    #df=df.tail(len(df.index)-35)
    #predictorsm=df.columns.tolist()
	#predictorsm=list(range(0,len(predictorsm),1))
	#df.columns=predictorsm
	#bigdf
	train=pd.DataFrame()
	test=pd.DataFrame()
	train=train.append(
		df.tail(int(.9*len(df.index))).head(
		int(
		len(df.index*.8))))
	test=test.append(df.tail(int(.1*len(df.index))))
	train.reset_index(inplace=True, drop=True)
	test.reset_index(inplace=True, drop=True)
	if loopcount==0:
		predictorsm=df.columns.tolist()
		for i in list(range(1,len(predictorsm),1)):
			if predictorsm[i]=='cumcases'+str(proj):
				respid=i
				response=predictorsm[respid]
				print(loopcount)
		predictorsm=list(range(0,len(predictorsm)))
		del predictorsm[16]
		del predictorsm[15]
		del predictorsm[11]
		del predictorsm[0]
	else:
		print(loopcount)
		print(i, 'Data processing successful. Check out my code to change how far back in time I look to make predictions.')
	print('Now training a GBM. My GBM framework is noisy please enjoy a look under the hood.')
	h2o.init()
	dftr = h2o.H2OFrame(train)
	dfte = h2o.H2OFrame(test)
	gbm=H2OGradientBoostingEstimator()
	gbm.train(x=predictorsm, y='cumcases'+str(proj), training_frame=dftr)
	perf = gbm.model_performance(dfte)
	results.iloc[loopcount,1]=abs(test[response]).mean()
	results.iloc[loopcount,2]=perf.mae()
	results.iloc[loopcount,0]=loi
	results.iloc[loopcount,3]=str((perf.mae()/abs(test[response]).mean())*100)+'% error'
	print(results)
	loopcount=loopcount+1

    
        
            

#h2o.init()
#dftr = h2o.H2OFrame(train)
#dfte = h2o.H2OFrame(test)
#gbm=H2OGradientBoostingEstimator()
#gbm.train(x=predictorsm, y=response, training_frame=dftr)
#perf = gbm.model_performance(dfte)
#print(perf)
#abs(test[response]).mean()

#gbmpredictions=gbm.predict(dfte)
#gbmpredictions=pd.DataFrame(gbmpredictions)

#del predictorsm[-9:]
#predictorsm

#del predictorsm[0]
#del predictorsm[14:16]
#del predictorsm[0]
#del predictorsm[8]
#response=predictorsm[-2]
#del predictorsm[-2]



#train.to_csv('traindata_varun.csv')
#test.to_csv('testdata_varun.csv')

