import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold


# load dataset
dataset = pd.read_csv('data/actual_test.csv')
print(dataset)
# separating the target data from the actual data
Y = dataset['Posturing']

# dropping out the target from train data
X = dataset.drop(columns=['Posturing'])
train_data = pd.get_dummies(X)

X = pd.get_dummies(X)

dummy_Y = pd.get_dummies(Y)

# define baseline model
def baseline_model():
    # create model
    model = Sequential()
    model.add(Dense(8, input_dim=21, activation='relu'))
    model.add(Dense(4, activation='softmax'))
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


estimator = KerasClassifier(build_fn=baseline_model, epochs=200, batch_size=5, verbose=0)
kfold = KFold(n_splits=10, shuffle=True)
results = cross_val_score(estimator, X, dummy_Y, cv=kfold)
#print(results)
print("Baseline: %.2f%% (%.2f%%)" % (results.mean() * 100, results.std() * 100))