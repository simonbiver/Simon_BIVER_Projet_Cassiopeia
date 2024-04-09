#coding:utf-8

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Class for machine learning
class Ml_Tools():
    def __init__(self, columns : pd.DataFrame, target : pd.DataFrame):
        self.columns = columns
        self.target = target

    def calibrate_RFC(self):
        """Create a dataframe use randomforestclassifier algorithm with all criterions in range of depht 20-200 step by 10."""

        x = self.columns
        y = self.target
        
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0, stratify = y)

        numeric_columns = x.select_dtypes(include = "number").columns.to_list()
        categorical_columns = x.select_dtypes(include = "category").columns.to_list()
        
        transformers = []
        if numeric_columns:
            scalar = StandardScaler()
            transformers.append(('num', scalar, numeric_columns))
        if categorical_columns:
            encode = OneHotEncoder(drop='first')
            transformers.append(('cat', encode, categorical_columns))

        transformer = ColumnTransformer(transformers=transformers)    
        x_train = transformer.fit_transform(x_train)

        criterion = ["gini", "entropy", "log_loss"]
        r_estimators = range(20,210,10)
        df_RFC_temp = []
        for c in criterion:
            for e in r_estimators:

                classifier = RandomForestClassifier(n_estimators = e, criterion = c)
                classifier.fit(x_train, y_train)
                score_train = classifier.score(x_train, y_train)
                score_test = classifier.score(x_test, y_test)

                parametres = {"Criterion Type" : c, "Depth" : e, "Score train" : score_train, "Score Test" : score_test}

                df_temp = pd.DataFrame([parametres])
                df_RFC_temp.append(df_temp)
        df_RFC = pd.concat(df_RFC_temp, ignore_index=True)
        return df_RFC