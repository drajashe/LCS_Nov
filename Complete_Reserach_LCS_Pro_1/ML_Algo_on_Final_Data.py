# Load libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
import pydotplus
#column variables
col_names = ['Reliability','Responsibility','Accountability','Creativity','Quality','Speed','Expression','Posturing']
grnd_truth = pd.read_csv("data/actual_test.csv", header=None, names=col_names)

#split dataset in features and target variable
feature_cols =['Reliability','Responsibility','Accountability','Creativity','Quality','Speed','Expression']
target_col=['Posturing']
X = grnd_truth[feature_cols] # Features
y = grnd_truth[target_col]# Target variable

# Import label encoder
y_predict=0

# label_encoder object knows how to understand word labels.
label_encoder = preprocessing.LabelEncoder()
for i in feature_cols:
    X[i] = label_encoder.fit_transform(X[i])

test_data = pd.read_excel("data/excel.xlsx")

X_test=test_data[feature_cols]
y_test=test_data[target_col]
label_encoder_2 = preprocessing.LabelEncoder()
for i in feature_cols:
    X_test[i] = label_encoder_2.fit_transform(X_test[i])




#decision tree model generationn
def Decision_tree_model(X,y,y_predict):
    classifier = DecisionTreeClassifier()
    classifier.fit(X, y)
    y_predict = classifier.predict(X_test)
    dot_data = StringIO()
    export_graphviz(classifier, filled=True,
                    out_file=dot_data, rounded=True,
                    special_characters=True)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    Image(graph.create_png())
    graph.write_png('actual_decision.png')
    # printing the accuracy of the decision tree
    print("Accuracy of test data - ", accuracy_score(y_test , y_predict))



#cAlling decision tree
Decision_tree_model(X,y,y_predict)