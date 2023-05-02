import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn import svm
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import Ridge
import pickle

df = pd.read_csv('mieszkania_z_wspolrzedne.csv', index_col=0)
dataset = df
X = dataset.drop(['cena', 'adres'], axis=1)
Y = dataset['cena']
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, train_size=0.85, test_size=0.15, random_state=0)
model = RandomForestRegressor(n_estimators=1600, min_samples_split=10, min_samples_leaf=1, max_features='sqrt',
                              max_depth=20, bootstrap=False, n_jobs=-1)
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)
error = mean_absolute_percentage_error(Y_test, Y_pred)
error1 = mean_absolute_error(Y_test, Y_pred)
pickle.dump(model, open('model.sav', 'wb'))
print(error)
print(error1)





