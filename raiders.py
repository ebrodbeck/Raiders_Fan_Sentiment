# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 19:31:47 2023

@author: brodbeck
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df=pd.read_csv('raiders.csv',',')
df=df.drop(['Timestamp'],axis=1)
df.columns=['sent_BB','sent_bench','sent_A49','QB1']

vals=df['QB1'].value_counts()
vals=vals.to_frame()

x=df
x=x.replace(to_replace='StidHIM',value='Stidham')
x=x.replace(to_replace='Tom Brady',value='Brady')
x=x.replace(to_replace='Both equal games',value='Nonsense Answers')
x=x.replace(to_replace='Me. ',value='Nonsense Answers')
x=x.replace(to_replace='Unfortunately Tom Brady',value='Brady')
x=x.replace(to_replace='Other',value='Nonsense Answers')
x=x.replace(to_replace='Whoever earns it ',value='Nonsense Answers')
x=x.replace(to_replace='Draft',value='Rookie')
x=x.replace(to_replace='Neither',value='Nonsense Answers')
x=x.replace(to_replace='We should reevaluate Stidham after the Chiefs game.',value='Stidham')
x=x.replace(to_replace='Dont know ',value='Stidham')
x=x.replace(to_replace='Dont know',value='Stidham')
x=x.replace(to_replace='Lamar Jackson',value='Lamar')
x=x.replace(to_replace='Neither of these two',value='Nonsense Answers')
x=x.replace(to_replace='Jamarcus Russell',value='Nonsense Answers')
x=x.replace(to_replace='Not Sure Yet. Bring in Brissett as a potential bridge or backup ',value='Nonsense Answers')
x=x.replace(to_replace='Should give Stidham a chance if he plays well against KC but with the news of Adams wanting to be involved in QB decision, i expect it to be Brady or trade for Rodgers',value='Stidham')
x=x.replace(to_replace='Too early to say, Stidham may not be a bad option',value='Stidham')
x=x.replace(to_replace='Rookie or Brady/Jimmy G/Rodgers',value='Brady')
x=x.replace(to_replace='Bridge QB',value='Nonsense Answers')
x=x.replace(to_replace='Too soon to tell',value='Nonsense Answers')
x=x.replace(to_replace='Draft pick',value='Rookie')
x=x.replace(to_replace='It doesnt matter with Josh as HC',value='Nonsense Answers')
x=x.replace(to_replace='Carr if there is no obvious upgrade',value='Carr')
x=x.replace(to_replace='proven free agent AND a developmental prospect',value='Nonsense Answers')
x=x.replace(to_replace='Brady/Rodgers',value='Rogers')
x=x.replace(to_replace='Levis ',value='Rookie')
x=x.replace(to_replace='Brady, or Stidham and a rookie.  ',value='Brady')
x=x.replace(to_replace='who knows ',value='Nonsense Answers')
x=x.replace(to_replace='Stidham but draft a QB first round ',value='Stidham')
x=x.replace(to_replace='Wreck for Williams ',value='Rookie')
x=x.replace(to_replace='Aaron Rodgers ',value='Rogers')
x=x.replace(to_replace='anyone',value='Nonsense Answers')
x=x.replace(to_replace='Competition between Stidham and somebody like Minshew, White, Heinicke, etc ',value='Stidham')
x=x.replace(to_replace='Rodgers if we want to win. Stidham if trying to build a good team beyond 2023',value='Rogers')
x=x.replace(to_replace='Brady, or Stidham and a rookie. ',value='Brady')
x=x.replace(to_replace='who knows',value='Nonsense Answers')
x=x.replace(to_replace='Rogers',value='Rodgers')
x=x.replace(to_replace='Stidham but draft a QB first round',value='Stidham')
x=x.replace(to_replace='Aaron Rodgers',value='Rodgers')
x=x.replace(to_replace='Nonsense Answers',value='Nonsense')
x=x.replace(to_replace='Lamar ',value='Lamar')


vals=vals.assign(col2=x['QB1'].value_counts())
c={'Stidham':'black','Carr':'black','Brady':'red','Nonsense':'yellow','Rookie':'pink','Rodgers':'green','Jimmy G':'red','Lamar':'purple'}

counts_x_QB1=x['QB1'].value_counts().reset_index()
counts_x_QB1=counts_x_QB1.rename(columns={'index':'QB','QB1':'Count'})
counts_x_QB1['color']=counts_x_QB1['QB'].map(c)
counts_x_QB1['pct']=counts_x_QB1['Count'].apply(lambda x: 100*x / counts_x_QB1['Count'].sum())
counts_x_QB1['pct']=counts_x_QB1['pct'].apply(lambda x: round(x,1))


plt.figure()
sns.barplot(x='QB',y='pct',data=counts_x_QB1,palette=counts_x_QB1.color)
plt.xticks(rotation=45)
plt.xlabel(' ')
plt.title('General Preferred QB1 - 2023/24 Season')
for i, value in enumerate(counts_x_QB1['pct']):
    plt.annotate(value, (i,value),ha='center',va='bottom')


#==================================================================

dickriders=x[x['sent_BB']=='Positive']
haters=x[x['sent_BB']=='Negative']

drs_sad=dickriders[dickriders['sent_bench']=='Carr should still be QB1']
drs_happy=dickriders[dickriders['sent_bench']=='Carr needed to be benched']

drs_sad_JSgood=drs_sad[drs_sad['sent_A49']=='Glad we moved to Stidham']
drs_sad_DCgood=drs_sad[drs_sad['sent_A49']=='Should have kept Carr']



drs=x['sent_BB'].value_counts().reset_index()
drs=drs.rename(columns={'index':'Sentiment','sent_BB':'Count'})
drs['pct']=drs['Count'].apply(lambda x: 100*x / drs['Count'].sum())
drs['pct']=drs['pct'].apply(lambda x: round(x,1))

g_b=x['sent_bench'].value_counts().reset_index()
g_b=g_b.rename(columns={'index':'Reaction','sent_bench':'Count'})
g_b['pct']=g_b['Count'].apply(lambda x: 100*x / g_b['Count'].sum())
g_b['pct']=g_b['pct'].apply(lambda x: round(x,1))

g_49=x['sent_A49'].value_counts().reset_index()
g_49=g_49.rename(columns={'index':'Reaction','sent_A49':'Count'})
g_49['pct']=g_49['Count'].apply(lambda x: 100*x / g_49['Count'].sum())
g_49['pct']=g_49['pct'].apply(lambda x: round(x,1))

drs_qb1=dickriders['QB1'].value_counts().reset_index()
drs_qb1=drs_qb1.rename(columns={'index':'QB','QB1':'Count'})
drs_qb1['pct']=drs_qb1['Count'].apply(lambda x: 100*x / drs_qb1['Count'].sum())
drs_qb1['pct']=drs_qb1['pct'].apply(lambda x: round(x,1))

h_qb1=haters['QB1'].value_counts().reset_index()
h_qb1=h_qb1.rename(columns={'index':'QB','QB1':'Count'})
h_qb1['pct']=h_qb1['Count'].apply(lambda x: 100*x / h_qb1['Count'].sum())
h_qb1['pct']=h_qb1['pct'].apply(lambda x: round(x,1))
#ss['pct']=ss['Count'].apply(lambda x: 100*x / ss['Count'].sum())

drs_bench_counts=dickriders['sent_bench'].value_counts().reset_index()
drs_bench_counts=drs_bench_counts.rename(columns={'index':'Reaction','sent_bench':'Count'})
drs_bench_counts['pct']=drs_bench_counts['Count'].apply(lambda x: 100*x / drs_bench_counts['Count'].sum())
drs_bench_counts['pct']=drs_bench_counts['pct'].apply(lambda x: round(x,1))

drs_stid_cts=dickriders['sent_A49'].value_counts().reset_index()
drs_stid_cts=drs_stid_cts.rename(columns={'index':'Reaction','sent_A49':'Count'})
drs_stid_cts['pct']=drs_stid_cts['Count'].apply(lambda x: 100*x / drs_stid_cts['Count'].sum())
drs_stid_cts['pct']=drs_stid_cts['pct'].apply(lambda x: round(x,1))

h_bench_counts=haters['sent_bench'].value_counts().reset_index()
h_bench_counts=h_bench_counts.rename(columns={'index':'Reaction','sent_bench':'Count'})
h_bench_counts['pct']=h_bench_counts['Count'].apply(lambda x: 100*x / h_bench_counts['Count'].sum())
h_bench_counts['pct']=h_bench_counts['pct'].apply(lambda x: round(x,1))

h_stid_cts=haters['sent_A49'].value_counts().reset_index()
h_stid_cts=h_stid_cts.rename(columns={'index':'Reaction','sent_A49':'Count'})
h_stid_cts['pct']=h_stid_cts['Count'].apply(lambda x: 100*x / h_stid_cts['Count'].sum())
h_stid_cts['pct']=h_stid_cts['pct'].apply(lambda x: round(x,1))

plt.figure()
a1=sns.barplot(x='Sentiment',y='pct',data=drs,palette='Accent',edgecolor='black')
plt.title('Derek Carr Fan Sentiment - Pre Benching')
plt.xticks(rotation=20)
for i, value in enumerate(drs['pct']):
    plt.annotate(value, (i,value),ha='center',va='bottom')
    
plt.figure()
a1=sns.barplot(x='Reaction',y='pct',data=g_b,palette='Greens',edgecolor='black')
plt.title('General Fan Sentiment to Carr Benching')
plt.xticks(rotation=20)
for i, value in enumerate(g_b['pct']):
    plt.annotate(value, (i,value),ha='center',va='bottom')
    
plt.figure()
a1=sns.barplot(x='Reaction',y='pct',data=g_49,palette='Greens',edgecolor='black')
plt.title('General Fan Sentiment After 49ers Game')
plt.xticks(rotation=20)
for i, value in enumerate(g_49['pct']):
    plt.annotate(value, (i,value),ha='center',va='bottom')
    
plt.figure()
a1=sns.barplot(x='Reaction',y='pct',data=drs_bench_counts,palette='Greys',edgecolor='black')
plt.title('Carr Fans Reaction to Benching')
plt.xticks(rotation=20)
for i, value in enumerate(drs_bench_counts['pct']):
    plt.annotate(value, (i,value),ha='center',va='bottom')
    
plt.figure()
a1=sns.barplot(x='Reaction',y='pct',data=h_bench_counts,palette='Reds',edgecolor='black')
plt.title('Carr Critics Reaction to Benching')
plt.xticks(rotation=20)
for i, value in enumerate(h_bench_counts['pct']):
    plt.annotate(value, (i,value),ha='center',va='bottom')
    
plt.figure()
a1=sns.barplot(x='Reaction',y='pct',data=drs_stid_cts,palette='Greys',edgecolor='black')
plt.title('Carr Fans Reaction to Stidham v 49ers')
plt.xticks(rotation=20)
for i, value in enumerate(drs_stid_cts['pct']):
    plt.annotate(value, (i,value),ha='center',va='bottom')
    
plt.figure()
a1=sns.barplot(x='Reaction',y='pct',data=h_stid_cts,palette='Reds',edgecolor='black')
plt.title('Carr Critics Reaction to Stidham v 49ers')
plt.xticks(rotation=20)
for i, value in enumerate(h_stid_cts['pct']):
    plt.annotate(value, (i,value),ha='center',va='bottom')
    
plt.figure()
a1=sns.barplot(x='QB',y='pct',data=drs_qb1,palette='Greys',edgecolor='black')
plt.title('Carr Fans Preferred QB1')
plt.xticks(rotation=20)
for i, value in enumerate(drs_qb1['pct']):
    plt.annotate(value, (i,value),ha='center',va='bottom')
    
plt.figure()
a1=sns.barplot(x='QB',y='pct',data=h_qb1,palette='Reds',edgecolor='black')
plt.title('Carr Critics Preferred QB1')
plt.xticks(rotation=20)
for i, value in enumerate(h_qb1['pct']):
    plt.annotate(value, (i,value),ha='center',va='bottom')