from sklearn.model_selection import RandomizedSearchCV
from pprint import pprint
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('mieszkania_z_wspolrzedne.csv', index_col=0)
dataset = df
X = dataset.drop(['cena', 'adres'], axis=1)
Y = dataset['cena']
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, train_size=0.85, test_size=0.15, random_state=0)
n_estimators = [int(x) for x in np.linspace(start=200, stop=2000, num=10)]
max_features = ['auto', 'sqrt']
max_depth = [int(x) for x in np.linspace(10, 200, num=20)]
max_depth.append(None)
min_samples_split = [2, 5, 10]
min_samples_leaf = [1, 2, 4]
bootstrap = [True, False]
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}

rf = RandomForestRegressor()
rf_random = RandomizedSearchCV(estimator=rf, param_distributions=random_grid, n_iter=100, cv=5, verbose=2, random_state=42, n_jobs=-1)
rf_random.fit(X_train, Y_train)
print(rf_random.best_params_)