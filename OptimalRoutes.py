
# coding: utf-8

# In[14]:


import pandas as pd
import os
import glob


# In[ ]:


get_ipython().system('head -n 100 ')


# In[4]:


a=pd.read_csv('a_example.in')
b=pd.read_csv('b_should_be_easy.in')
c=pd.read_csv('c_no_hurry.in')
d=pd.read_csv('d_metropolis.in')
e=pd.read_csv('e_high_bonus.in')


# In[23]:


f = open("b_should_be_easy.in", 'r')
rides = f.read().split("\n")
rides_df = pd.DataFrame([ride.split(" ") for ride in rides],
                  dtype=float,
                  columns=['start_row', 'start_col', 'end_row', 'end_col', 'time_earliest', 'time_latest'])
header_df=rides_df.iloc[1]
# remove last row 
rides_df = rides_df[2:-1]
rides_df['start_row'] = rides_df['start_row'].astype(float)

# sort by earliest time
rides_df.sort_values(by='time_earliest', inplace=True)
print(rides_df.head())
#rideRow[rideID]


# In[16]:


rides_df['distance']=rides_df['time_latest']-rides_df['time_earliest']


# In[26]:


get_ipython().system('head -n 1 a_example.in')


# In[ ]:


df_vehicles=pd.DataFrame({'vehicleID':[range(nVehicles)].'rideID':[].'steps_available':[],'steps_needed':[],'status':[],'rideToComplete':[]})
# rowVehicle='vehicleID':''.'rideID':[].'steps_available':'','status':'','rideToComplete':''

#df_vehicles functions
def stepSubstract(row):
    row['steps_available']=row['steps_available']-1
    row['steps_needed']=row['steps_needed']-1
    if row['steps_available']==0:
        row['status']='available'
        row['rideID']=row['rideID'].append(row['rideToComplete'])
        row['rideToComplete']=''
def assignRideToVehicle(dfVehicles,rideRow,dfRides):
    #get first vehicle capable
    vehicleID=dfVehicles[dfVehicles['steps_available']=>rideRow['steps_needed']].iloc[1,'vehicleID']
    #assign it rideID
    dfVehicles[dfVehicles['vehicleID']==vehicleID]['rideID']=rideRow['rideID']
    #drop ride from ridesDF
    dfRides.drop(dfRides[dfRides['vehicleId']==vehicleID].index)
    
    

