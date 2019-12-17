# Load libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
from sklearn.metrics import accuracy_score
import pydotplus


#reading in the csv with all the data

entire_data = pd.read_csv('data/actual_test.csv')
print(entire_data)
#separating the target data from the actual data
target_data = entire_data['Posturing']

#dropping out the target from train data
train_data = entire_data.drop(columns=['Posturing'])
train_data=pd.get_dummies(train_data)


# #target_data=pd.get_dummies(target_data)
# # splitting data as train and test in 8:2 ratio

xTrain, xTest, yTrain, yTest = train_test_split(train_data, target_data, test_size=0.2, random_state=0)


#model generationn

classifier = DecisionTreeClassifier()
classifier.fit(xTrain, yTrain)
#print(yTest)
y_predict = classifier.predict(xTest)

#print(y_predict, yTrain)


#for visualising the decision tree


dot_data = StringIO()
export_graphviz(classifier, filled=True,
                out_file=dot_data, rounded=True,
                special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
Image(graph.create_png())
graph.write_png('actual_decision.png')


# printing the accuracy of the decision tree
print("Accuracy of test data - ", accuracy_score(yTest, y_predict))