import pickle
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

model = pickle.load(open('model.pkl','rb'))

tf_idf = TfidfVectorizer(stop_words = 'english', max_df = 0.7)
df = pd.read_csv("csv_files/train.csv")
df = df.dropna()
df.reset_index(inplace=True)
X = df['title']
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=0)

def fake_result(news_title):
    X_train_tfidf = tf_idf.fit_transform(X_train)
    X_test_tfidf = tf_idf.transform(X_test)
    input_news = [news_title]
    vectorized_input_news = tf_idf.transform(input_news)
    prediction = model.predict(vectorized_input_news)
    return prediction
