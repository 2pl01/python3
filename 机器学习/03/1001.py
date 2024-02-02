# coding=utf-8
"""
    @project: python3
    @Author："东家“
    @file： 1001.py
    @date：2023/02/14 11:29
    @Python 机器学习 第三章
    
"""
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import  LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

filename='iris.data.csv'
names=['separ-length','separ-width','petal-length','petal-width','class']
dataset = read_csv(filename, names=names)
print('数据维度: 行 %s，列 %s' % dataset.shape)
# 查看数据的前10行
print(dataset.head(10))

print(dataset.describe())

#分布情况
print(dataset.groupby('class').size())

dataset.plot(kind='box', subplots=True, layout=(2,2),sharex=False, sharey=False)
# pyplot.show()
# dataset.hist()
# pyplot.show()
scatter_matrix(dataset)
pyplot.show()