# Load libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.feature_extraction import DictVectorizer

entire_data = pd.read_csv('data/file1.csv')

target_data = entire_data['Posturing']
train_data = entire_data.drop(columns=['Name', 'Role Played Currently', 'Designation', 'Posturing', 'Overall'])
#encoding
train_data=pd.get_dummies(train_data)
#target_data=pd.get_dummies(target_data)
# splitting data as train and test

xTrain, xTest, yTrain, yTest = train_test_split(train_data, target_data, test_size=0.2, random_state=0)
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus



classifier = DecisionTreeClassifier()
classifier.fit(xTrain, yTrain)
print(yTest)
y_predict = classifier.predict(xTest)
from sklearn.metrics import accuracy_score
print(y_predict, yTrain)

dot_data = StringIO()
export_graphviz(classifier, filled=True,
                out_file=dot_data, rounded=True,
                special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
Image(graph.create_png())
graph.write_png('new_.png')
print(accuracy_score(yTest, y_predict))