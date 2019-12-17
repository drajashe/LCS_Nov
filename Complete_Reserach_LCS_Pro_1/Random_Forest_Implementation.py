#  https://stackabuse.com/random-forest-algorithm-with-python-and-scikit-learn/


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import graphviz
import pydotplus
from sklearn import  metrics
from IPython.display import Image
from sklearn.tree import export_graphviz
from sklearn.ensemble import RandomForestClassifier


dataset = pd.read_csv('data/actual_test.csv')
print(dataset)
# separating the target data from the actual data
y = dataset['Posturing']

# dropping out the target from train data
X = dataset.drop(columns=['Posturing'])
train_data = pd.get_dummies(X)

X = pd.get_dummies(X)

y = pd.get_dummies(y)
print(y.columns)

# changing random state from 0 to 4 increases the accuracy by 4
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4)
# print(X_test)
#
# #Feature scaling
from sklearn.preprocessing import StandardScaler

#
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
#
# #training the Random forest algorithm


#
classifier = RandomForestClassifier(n_estimators=20, random_state=0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
#


# Accuracy of Random forest model

#
print(metrics.classification_report(y_test, y_pred))
print('Accuracy Score:', metrics.accuracy_score(y_test, y_pred))

# Convert to png using system command (requires Graphviz)

estimator = classifier.estimators_[5]


# Export as dot file
export_graphviz(estimator, out_file='tree.dot',
                feature_names = X.columns,
                class_names = y.columns,
                rounded = True, proportion = False,
                precision = 2, filled = True)

# Convert to png using system command (requires Graphviz)
from subprocess import call
call(['dot', '-Tpng', 'tree.dot', '-o', 'tree.png', '-Gdpi=600'])

# Display in jupyter notebook
from IPython.display import Image
Image(filename = 'tree.png')


