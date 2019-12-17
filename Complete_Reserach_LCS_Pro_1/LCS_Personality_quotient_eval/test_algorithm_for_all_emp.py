# Load libraries
import pandas as pd
#from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
import pydotplus
import numpy as np

def main():
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

    # Program to find most frequent
    # element in a list
    def most_frequent(List):
        return max(set(List), key=List.count)

    test_data = pd.read_excel("data/DETAILS_EMP.xlsx")
    def read_data_for_pro(test_data,feature_cols):
        # test_data['Speed']= test_data['Speed'].split(",")
        # print(test_data['Speed'][0])

        def most_frequent(List):
            return max(set(List), key=List.count)
        for i in col_names:
            test_data[i] = test_data[i].apply(lambda x: x.split(','))

        for every_col in feature_cols:
            for i,each in enumerate(test_data[every_col]):
                test_data[every_col][i]=most_frequent(each)


        for i,each in enumerate(test_data['Posturing']):
            #print(most_frequent(each))
            test_data['Posturing'][i] = most_frequent(each)
            #print(test_data['Posturing'])
        X_test = test_data[feature_cols]
        y_test = test_data[target_col]
            #print(test_data,every_col)
        label_encoder_2 = preprocessing.LabelEncoder()
        for i in feature_cols:
            X_test[i] = label_encoder_2.fit_transform(X_test[i])
        # cAlling decision tree
        Decision_tree_model(X, y, y_predict,X_test,y_test,grnd_truth)



    #decision tree model generationn
    def Decision_tree_model(X,y,y_predict,X_test,y_test,grnd_truth):
        classifier = DecisionTreeClassifier()
        classifier.fit(X,y)
        y_predict = classifier.predict(X_test)
        dot_data = StringIO()
        export_graphviz(classifier, filled=True,
                        out_file=dot_data, rounded=True,
                        special_characters=True)
        graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
        Image(graph.create_png())
        graph.write_png('actual_decision.png')
        # printing the accuracy of the decision tree

        y_pred_df=pd.DataFrame({'Predicted Posture of an employee':y_predict})
        y_pred_df=pd.concat([y_pred_df, y_test], ignore_index=True, axis=1)
        name_cols=['Name','Designation','Role']
        emp_details=test_data[name_cols]

        y_pred_df=pd.concat([emp_details,y_pred_df],ignore_index=True,axis=1)

        y_pred_df.columns= ['Name','Designation','Role','Actual posture feedback','Correct Predicted Posture of an employee']
        y_pred_df.to_excel("data/emp_details_analysis.xlsx")

    read_data_for_pro(test_data,feature_cols)



if __name__ == '__main__':
    main()
