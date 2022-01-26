from pandas import *
from numpy import *
from re import *
from seaborn import *
from matplotlib.pyplot import *
from warnings import *
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix

simplefilter('ignore')

data = read_csv("Language Detection.csv")
data["Language"].value_counts()

X = data["Text"]
y = data["Language"]
le = LabelEncoder()
y = le.fit_transform(y)

dataList = []

for text in X:
    text = sub(r"[!@#$(),n\"%?:;~`0-9]", r' ', text)
    text = sub(r'[[]]', r' ', text)
    text = text.lower()
    dataList.append(text)

cv = CountVectorizer()
X = cv.fit_transform(dataList).toarray()
X.shape

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)

model = MultinomialNB()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

ac = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("Accuracy is: ", ac)

figure(figsize=(15, 10))
heatmap(cm, annot = True)
show()

def prediction(text):
    x = cv.transform([text]).toarray()
    lang = model.predict(x)
    lang = le.inverse_transform(lang)
    print("The language is in: ", lang[0])
