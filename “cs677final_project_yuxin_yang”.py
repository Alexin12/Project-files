# -*- coding: utf-8 -*-
"""“final project Yuxin Yang.ipynb”

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KJVOps49QFbV98pxRR8aLopDBBvmNieE
"""

import pandas as pd
import numpy as np·
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler

from google.colab import files
uploaded = files.upload()
#choose train.csv

import io
data= pd.read_csv(io.BytesIO(uploaded['train.csv']))

"""#data EDA"""

data.head()

data.info()

mising_value=data.isnull().sum().sort_values(ascending=False)
percent= (data.isnull().sum()/data.isnull().count()).sort_values(ascending=False)
missing=pd.concat([mising_value,percent],axis=1,keys=['number','percent'])
missing

categorical_indexes = [0, 1, 3, 4] + list(range(6, 20))
categorical_indexes

import seaborn as sns
plt.pie(data.satisfaction.value_counts(), labels = ["Neutral or dissatisfied", "Satisfied"], colors = sns.color_palette("YlOrBr"),
        autopct = '%.3f%%')
pass

data=data.drop(data.iloc[:,[0,1]],axis=1)#drop useless columns --Unnamed: 0 and id

category=[0,1,3,4]+[i for i in range(6,20)]

# data['Gate location']
data.iloc[:,category]=data.iloc[:,category].astype('category')

data.info()

"""##numerical data EDA"""

corr_mat = data.corr()
corr_mat

sns.heatmap(corr_mat, square = True, cmap = 'Blues')

"""there is a strong correlation between the features 'Departure delay in minutes' and 'Arrival delay in minutes'."""

plt.scatter(x=data['Arrival Delay in Minutes'],y=data['Departure Delay in Minutes'])
plt.xlabel('Arrival Delay in Minutes')
plt.ylabel('Departure Delay in Minutes')
plt.legend()

"""the scatter also shows strong relation between arrival delay time and departure delay time, and the scale of X and Y is symmetrical ,which make sense because the delay of arrival will direct cause the delay of next departure for same aircraft.Therefore, we may remove one of the them before build the model to avoid multicollinearity

## EDA between numerical and categorical feature
"""

data.info()

Q1=data['Arrival Delay in Minutes'].quantile(0.25)
Q3=data['Arrival Delay in Minutes'].quantile(0.75)

IQR=(Q3-Q1)
non_outlier_data=data.loc[(data['Arrival Delay in Minutes']>=Q1-1.5*IQR)&(data['Arrival Delay in Minutes']<=Q3+1.5*IQR)]

figure,axss = plt.subplots(2,2, figsize=[20,10])
sns.boxplot(x='satisfaction',y='Age',data=data,ax=axss[0][0])
sns.boxplot(x='satisfaction',y='Flight Distance',data=data,ax=axss[0][1])
sns.boxplot(x='satisfaction',y='Departure Delay in Minutes',data=non_outlier_data,ax=axss[1][0])
sns.boxplot(x='satisfaction',y='Arrival Delay in Minutes',data=non_outlier_data,ax=axss[1][1])

"""older people more easier to satisfied, and customer who take longer distance fight tend to satisfied.Besides, after remove mathmatical outlier, we find there is no obvious difference of delay time for satisfied and dissatisfied customer.

##relation between satisfaction and class in numeric value
"""

figure ,axxs=plt.subplots(2,2,figsize=[8,8])#subplots 记得要加s  barplot x 轴是categorical 变量 y轴一定要是 numeric 变量
#hue 是categorical

sns.barplot(x='satisfaction',y='Age',hue='Class',data=data,ax=axxs[0][0])
sns.barplot(x='satisfaction',y='Flight Distance',hue='Class',data=data,ax=axxs[0][1])
sns.barplot(x='satisfaction',y='Departure Delay in Minutes',hue='Class',data=data,ax=axxs[1][0])
sns.barplot(x='satisfaction',y='Arrival Delay in Minutes',hue='Class',data=data,ax=axxs[1][1])

"""satisfaction seems did not dependent on calss , economy customer have young age


more fight distance more satisfaction and business class flight more distance


business class tend to satisfied than Eco plus customer when delay happends
"""

figure ,axxs=plt.subplots(2,2,figsize=[15,20])
sns.barplot(x='satisfaction',y='Age',hue='Food and drink',data=data,ax=axxs[0][0])
sns.barplot(x='satisfaction',y='Flight Distance',hue='Food and drink',data=data,ax=axxs[0][1])
sns.barplot(x='satisfaction',y='Departure Delay in Minutes',hue='Food and drink',data=data,ax=axxs[1][0])
sns.barplot(x='satisfaction',y='Arrival Delay in Minutes',hue='Food and drink',data=data,ax=axxs[1][1])

"""young age people did not satisfied by food 


long distance flight did not really satisfied by food even though they tend to satisfied by overall servcie.

customer who experienced delay more than 25 minutes tend to have higher food requirement
"""

figure ,axxs=plt.subplots(2,2,figsize=[15,20])
sns.barplot(x='satisfaction',y='Age',hue='Cleanliness',data=data,ax=axxs[0][0])
sns.barplot(x='satisfaction',y='Flight Distance',hue='Cleanliness',data=data,ax=axxs[0][1])
sns.barplot(x='satisfaction',y='Departure Delay in Minutes',hue='Cleanliness',data=data,ax=axxs[1][0])
sns.barplot(x='satisfaction',y='Arrival Delay in Minutes',hue='Cleanliness',data=data,ax=axxs[1][1])

"""young age tend to have higher displine for cleanliness 

For satisfied customer their requirement for cleanliness increase with growth of flight distance 
/On the country or not satisfied customer their requirement for cleanliness decrease with growth of flight distance

## EDA between categorical features
"""

figure,axxs=plt.subplots(5,4,figsize=[20,15])
sns.countplot(x='satisfaction',hue='Gender',data=data,ax=axxs[0][0])

sns.countplot(x='satisfaction',hue='Customer Type',data=data,ax=axxs[0][1])

sns.countplot(x='satisfaction',hue='Type of Travel',data=data,ax=axxs[0][2])

sns.countplot(x='satisfaction',hue='Class',data=data,ax=axxs[0][3])



sns.countplot(x='satisfaction',hue='Inflight wifi service',data=data,ax=axxs[1][0])

sns.countplot(x='satisfaction',hue='Departure/Arrival time convenient',data=data,ax=axxs[1][1])

sns.countplot(x='satisfaction',hue='Ease of Online booking',data=data,ax=axxs[1][2])

sns.countplot(x='satisfaction',hue='Gate location',data=data,ax=axxs[1][3])



sns.countplot(x='satisfaction',hue='Food and drink',data=data,ax=axxs[2][0])

sns.countplot(x='satisfaction',hue='Online boarding',data=data,ax=axxs[2][1])

sns.countplot(x='satisfaction',hue='Seat comfort',data=data,ax=axxs[2][2])

sns.countplot(x='satisfaction',hue='Inflight entertainment',data=data,ax=axxs[2][3])




sns.countplot(x='satisfaction',hue='On-board service',data=data,ax=axxs[3][0])

sns.countplot(x='satisfaction',hue='Leg room service',data=data,ax=axxs[3][1])

sns.countplot(x='satisfaction',hue='Baggage handling',data=data,ax=axxs[3][2])
sns.countplot(x='satisfaction',hue='Checkin service',data=data,ax=axxs[3][3])




sns.countplot(x='satisfaction',hue='Inflight service',data=data,ax=axxs[4][0])

sns.countplot(x='satisfaction',hue='Cleanliness',data=data,ax=axxs[4][1])

"""business travel more easy to satisfied maybe because the cost of travel is paid,by company which make them less picky


eco and eco plus tend to not satisfied , as opposed to Buiness class


poor inflight service may contribute a lot to dissatisfaction


poor ease of online booking service may contribute a lot to dissatisfaction


poor food and drike service may contribute a lot to dissatisfaction

poor  online boarding service may contribute a lot to dissatisfaction

poor inflight entertainment  may contribute a lot to dissatisfaction

poor leg room  may contribute a lot to dissatisfaction

poor baggage handling  service may contribute a lot to dissatisfaction

poor cleanliness may contribute a lot to dissatisfaction

#fill NA value
"""

data.info()

data['Arrival Delay in Minutes']=data['Arrival Delay in Minutes'].fillna(data['Arrival Delay in Minutes'].median)

data.isnull().sum()

"""# data preprocessing"""

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

data.drop(columns=['Arrival Delay in Minutes'],axis=1,inplace=True)

data.columns

Y=data['satisfaction']
X=data.drop(['satisfaction'],axis=1)

le=LabelEncoder()

Y=le.fit_transform(Y)

cat_cols = X.columns[X.dtypes == 'category']
num_cols=X.columns[X.dtypes=='int64']

len(cat_cols)
len(num_cols)

X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=48)

X_train[cat_cols]

"""##categorical data encoding"""

X_train=pd.get_dummies(X_train,columns=cat_cols)
X_test=pd.get_dummies(X_test,columns=cat_cols)

X_test

print(X_train.shape,X_test.shape)

"""##numeric standalize"""

sca=StandardScaler()
sca.fit(X_train[num_cols])
X_train[num_cols]=sca.transform(X_train[num_cols])
X_test[num_cols]=sca.transform(X_test[num_cols])

print(X_train.shape,X_test.shape)

X_train

"""# train model"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

from sklearn import neighbors
# Logistic Regression
classifier_logistic = LogisticRegression()

# K Nearest Neighbors
classifier_KNN = KNeighborsClassifier(n_neighbors=6)

# Random Forest
classifier_RF = RandomForestClassifier()

# Train the model
classifier_logistic.fit(X_train, y_train)

classifier_logistic.predict(X_test)

classifier_logistic.score(X_test,y_test)

classifier_RF.fit(X_train, y_train)

classifier_RF.score(X_test,y_test)

classifier_KNN.fit(X_train, y_train)

classifier_KNN.score(X_test,y_test)

"""#find optimal hyper paramaters"""

from sklearn.model_selection import GridSearchCV

# helper function for printing out grid search results 
def print_grid_search_metrics(gs):
    print ("Best score: " + str(gs.best_score_))
    print ("Best parameters set:")
    best_parameters = gs.best_params_
    for param_name in sorted(best_parameters.keys()):
        print(param_name + ':' + str(best_parameters[param_name]))

# Possible hyperparamter options for Logistic Regression Regularization
# Penalty is choosed from L1 or L2
# C is the 1/lambda value(weight) for L1 and L2
# solver: algorithm to find the weights that minimize the cost function

# ('l1', 0.01)('l1', 0.05) ('l1', 0.1) ('l1', 0.2)('l1', 1)
# ('12', 0.01)('l2', 0.05) ('l2', 0.1) ('l2', 0.2)('l2', 1)
parameters = {
    'penalty':('l2','l1'), 
    'C':(0.01, 0.05, 0.1, 0.2,0.5,0.8,0.9,0.92,0.94,0.96,1)
}
Grid_LR =GridSearchCV(LogisticRegression(solver='liblinear'),parameters,cv=5)#solver 这个参数是代表logistics regression？

Grid_LR.fit(X_train, y_train)

print_grid_search_metrics(Grid_LR)

best_LR_model = Grid_LR.best_estimator_
best_LR_model.predict(X_test)
best_LR_model.score(X_test, y_test)

# Possible hyperparamter options for KNN
# Choose k
parameters = {
    'n_neighbors':[1,3,5,7,9,11,13]
}
Grid_KNN = GridSearchCV(KNeighborsClassifier(),parameters, cv=5)
Grid_KNN.fit(X_train, y_train)

# best k
print_grid_search_metrics(Grid_KNN)
best_KNN_model = Grid_KNN.best_estimator_

# Possible hyperparamter options for Random Forest
# Choose the number of trees
parameters = {
    'n_estimators' : [60,80,100],
    'max_depth': [1,5,10]
}
Grid_RF = GridSearchCV(RandomForestClassifier(),parameters, cv=5)
Grid_RF.fit(X_train, y_train)

print_grid_search_metrics(Grid_RF)

best_RF_model = Grid_RF.best_estimator_

best_RF_model

"""#performance evaluation"""

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

plot_confusion_matrix(best_RF_model,X_test,y_test)

classification_report(y_test,best_RF_model.predict(X_test))

plot_confusion_matrix(best_LR_model,X_test,y_test)

best_LR_prediction=best_LR_model.predict(X_test)
classification_report(y_test,best_LR_prediction)

plot_confusion_matrix(best_KNN_model,X_test,y_test)

classification_report(y_test,best_KNN_model.predict(X_test))



feature_imp_df = pd.DataFrame(list(zip(best_RF_model.feature_importances_, X_train)))
feature_imp_df.columns = ['feature importance', 'feature']
feature_imp_df=feature_imp_df.sort_values(by='feature importance',ascending=False)

feature_imp_df.head(10)

coee_df=pd.DataFrame(data=best_LR_model.coef_.transpose(),index=X_train.columns,columns=['Coef'])

coee_df.sort_values(by=['Coef']).head(10)

