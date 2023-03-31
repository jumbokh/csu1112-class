# import libraries
import numpy as np
import matplotlib.pyplot as plt 

import pandas as pd  
import seaborn as sns 

%matplotlib inline

# import dataset from: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html
from sklearn.datasets import load_boston

# load boston_dataset
boston_dataset = load_boston()

# check out boston_dataset
print(boston_dataset.keys())

# check each column's description
print(boston_dataset.DESCR)


# convert loaded dataset into pandas dataframe
boston = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)
boston.head()

# append column 'target' into dataframe
boston['MEDV'] = boston_dataset.target

# check if any null values
boston.isnull().sum()

# check distribution of target variable
# set the size of the whole plot
sns.set(rc={'figure.figsize':(10,10)})
sns.distplot(boston['MEDV'])
plt.show()

# create correlation matrix for all variables to see if there's any linearity relationship 
correlation_matrix = boston.corr().round(2)
# annot = True to print the values inside the square
sns.heatmap(data=correlation_matrix, annot = True)

# visualize the relationship of LSTAT vs MEDV and RM vs MEDV
plt.figure(figsize=(20, 5))

features = ['LSTAT', 'RM']
target = boston['MEDV']

for i, col in enumerate(features):
    # format plots as 1 row, 2 columns, nth plot    
    plt.subplot(1, len(features) , i+1)
    # add data column into plot
    x = boston[col]
    y = target
    plt.scatter(x, y, marker='o')
    plt.title(col)
    plt.xlabel(col)
    plt.ylabel('MEDV')
    
# Use LSTAT and RM as feature variables and MEDV as target variable
X = pd.DataFrame(np.c_[boston['LSTAT'], boston['RM']], columns = ['LSTAT','RM'])
Y = boston['MEDV']

# train_test_split
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=5)

print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

# Modeling - using LinearRegression
from sklearn.linear_model import LinearRegression
reg = LinearRegression()

# Fitting linear model
reg.fit(X_train,Y_train)

# redicting using the linear model
reg.predict(X_test)

# Real target data：Y_test

# Use R2-score: return the coefficient of determination R^2 of the prediction
# The best possible score is 1.0 
print('R2: ', reg.score(X_test, Y_test))

# whole plot size
plt.figure(figsize=(8, 5))

# plotting the y_test vs y_pred
# ideally should have been a straight line
Y_pred = reg.predict(X_test)
plt.scatter(Y_pred, Y_test)
plt.xlabel('Y_pred')
plt.ylabel('Y_test')
plt.show()

# check the model details: intercept and coefficients
reg.intercept_
coeff_df = pd.DataFrame(reg.coef_, X_train.columns, columns=['Coefficient'])  
coeff_df