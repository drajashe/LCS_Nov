import pandas as pd
import numpy as np

import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import  accuracy_score
from sklearn.svm import SVC


dataset = pd.read_csv('data/actual_test.csv')
#print(dataset)
# separating the target data from the actual data
y = dataset['Posturing']

# dropping out the target from train data
X = dataset.drop(columns=['Posturing'])
train_data = pd.get_dummies(X)

X = pd.get_dummies(X)

y = pd.get_dummies(y)



from sklearn import datasets


from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
import numpy as np


#Splitting the dataset into the Training set and Test set

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
print(y_train.shape)
# Parameters

log_clf=GaussianNB()
random_clf=RandomForestClassifier()
#svm_clf= SVC()
voting_clf=VotingClassifier(estimators=[('lr',log_clf),('rnd',random_clf)],voting='hard')
voting_clf.fit(X_train,y_train)
for clf in (log_clf,random_clf,voting_clf):
    clf.fit(X_train,y_train)
    y_pred=clf.predict(X_test)
    print(clf.__class__,accuracy_score(y_test,y_pred))
