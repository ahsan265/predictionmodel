# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 20:58:56 2020

@author: Huniya Sohail
"""

import sys
import pandas as pd
import numpy as np
import pickle
from collections import OrderedDict, defaultdict
import json
import requests
import sys


# road_name = input("Enter your road name : ") 
# month=input("Enter month :")
# hour=input("Enter hour : ")
# day=input("Enter day: ") 
 
# road="IJP_road"

# datetime='10/7/2019,3:38 pm'

# nodes="[{'start_node':370705004,'end_node':1369956654},{'start_node':42469049,'end_node':42469053},{'start_node':34984482,'end_node':36201913}]"

nodes=sys.argv[1]
nodes= eval(nodes)

datetime=sys.argv[2]
token=datetime.split(',')
date=token[0].split('/')
month=date[0]
day=date[1]
year=date[2]
# timing=token[1].split(' ')
# time=timing[1].split(':')
time=token[1].split(':')
hour=int(time[0])
time=time[1].split(' ')
minutes=int(time[0])
dayTime=time[1]
if (minutes>=30):
    hour=hour+1
if(dayTime=='pm'):
    hour=hour+12


#ijp_2019 = pd.read_csv('F:\\Huniya\\DataSets\\Tracking World\\Sample Data\\start_node_ways_end_node_ijp_April_2019_tw_dateTime_speed_agg.csv') # returns a dataframe

#reader2=reader2.loc[:, ~reader2.columns.str.contains('^Unnamed')]

#speed=ijp_2019.groupby(['start_node', 'end_node'])['tracker_speed'].mean().reset_index()
'''
nodes=ijp_2019[['start_node','end_node']]
nodes=nodes.drop_duplicates(subset=['start_node', 'end_node'])
start_node=nodes['start_node'].values.tolist()
end_node=nodes['end_node'].values.tolist()
mergedStuff = pd.merge(speed, nodes, on=['start_node','end_node'], how='inner')
'''
start_node=[]
end_node=[]
for i in range(len(nodes)):
    start=''
    if "start_node" in nodes[i]:
        start=nodes[i]["start_node"]
    end=''
    if "end_node" in nodes[i]:
        end=nodes[i]["end_node"]
    start_node.append(start)
    end_node.append(end)
#way_id=reader3[reader3['osmname']==road_name]
#way_id= way_id['osm_way_id'].values.tolist()
data = {'start_node': start_node,
        'end_node':end_node,
}


X_test = pd.DataFrame(data)
X_test['month']= month
X_test['day']=day
X_test['hour']=hour
X_test=X_test.to_numpy()

filename = 'C:\\Users\\ahsan\\Desktop\\predtionwithislamabad\\p_model v1\\files\\finalized_model_segment_reg.sav'

loaded_model = pickle.load(open(filename, 'rb'))
y_pred=loaded_model.predict(X_test)
#y_pred1=np.array(mergedStuff['tracker_speed'].values)
#y_pred1=np.around(y_pred1)


bins = [0, 35, 50,np.inf]
labels = ['1', '2', '3']

len(y_pred)
y_pred = np.random.uniform(low=0, high=99.99, size=(len(y_pred),))
reponse = {'start_node': start_node,
        'end_node':end_node,
        'predicted_speed':y_pred,
}

Y_pred = pd.DataFrame(reponse)
Y_pred['level']=0


Y_pred['level'] = pd.cut(Y_pred['predicted_speed'], bins, labels=labels)
#Y_pred["level"] = pd.cut(mergedStuff["tracker_speed"], bins, labels=labels)


data_res=Y_pred.to_dict('records') 

  
resp=json.dumps(data_res)
print(resp)

# headers = {'Content-Type': 'application/json'}
# post = requests.post('http://localhost:5000/postdata', json=data_res,verify=False) # the POST request
#print(post)







