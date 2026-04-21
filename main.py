from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk
import pandas as pd
import numpy as np

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    tokens = word_tokenize(text)
    tokens = [t.lower() for t in tokens]
    tokens = [t for t in tokens if t.isalpha() and t not in stop_words]
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return ' '.join(tokens)

data = pd.DataFrame({
    'text': ['Free money', 'This is not spam', 'Buy now', 'Not spam', 'Get free money', 'This is spam', 'Not spam at all'],
    'label': [1, 0, 1, 0, 1, 1, 0]
})

data['text'] = data['text'].apply(preprocess_text)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['text'])
y = data['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = MultinomialNB()
clf.fit(X_train, y_train)

def classify_text(text):
    text = preprocess_text(text)
    text = vectorizer.transform([text])
    return clf.predict(text)[0]

print(classify_text('Free money now'))
print(classify_text('This is not spam at all'))