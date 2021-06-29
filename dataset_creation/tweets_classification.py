from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from nltk.corpus import stopwords
from pathlib import Path
import pandas as pd
import unidecode
import argparse
import os
import re


# Function to avoid unwanted paths
def checked(path, unwanted=["ipynb_checkpoints", ".DS_Store", "__Interval.csv", "Json", "Classified", "Logistic predictor.ipynb", "Untitled.ipynb"]):
    unwanted = [".DS_Store", "__Interval.csv", "Json", "Classified", "Logistic predictor.ipynb"]
    return (f for f in os.listdir(path) if f not in unwanted)


def normalize_string(to_normalize):
    # Normalize text given a string,
    text = str(to_normalize).lower()       # lowering text
    text = unidecode.unidecode(text)
    text = re.sub(r'[^\\w\\s]', '', text)  # removing all the punctuations
    last_text = text.split()
    stopwords_set = set(stopwords.words("spanish"))
    last_text = ' '.join([x for x in last_text if (x not in stopwords_set)])
    return last_text


# FEATURE EXTRACTION
# returns train, test and CountVectorizer object
def extract_features(df, field, training_data, testing_data):

    # binary feature representation
    cv = CountVectorizer()
    cv.fit_transform(training_data[field].values)               # creates a vocabulary based on the training set

    # transforms the text according to the vocabulary in the training set
    train_feature_set=cv.transform(training_data[field].values)
    test_feature_set=cv.transform(testing_data[field].values)

    return train_feature_set,test_feature_set,cv

#TRAINING FUNCTION
def train(df):
    # split training / test data
    training_data, testing_data = train_test_split(df, random_state = 2000, test_size = 0.1)
    # get labels
    Y_train = training_data["sexual_assault"].values
    Y_test = testing_data["sexual_assault"].values
    # get features
    X_train, X_test, feature_transformer = extract_features(df, "text", training_data, testing_data)
    # logistic regression classifier
    scikit_log_reg = LogisticRegression(verbose=1, solver='liblinear', C=5, penalty='l2',max_iter=1000)

    model = scikit_log_reg.fit(X_train, Y_train.astype(int))
    score = model.score(X_test, Y_test.astype(int))
    print("Testing accuracy = ", score)
    return(model, feature_transformer)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_arguments("-data", nargs='*', help='Absolute path to data directories')
    parser.add_argument("-train", nargs='*', help='Path to directories with CSV files containing labeled tweets')
    parser.add_argument("-predict", nargs='*', help='Path to directories with CSV files containing tweets to be predicted')
    args = parser.parse_args()

    train_set = args.train
    predict_set = args.test
    tweets_path = args.data

    # IMPORT CLASSIFIED DATASET
    classified_df = pd.DataFrame()

    for directory in train_set:
        training_path = os.path.abspath(tweets_path+directory)
        for file in checked(training_path):
            if file[:10] == "classified":
                f_path = training_path + "/" + file
                aux = pd.read_csv(f_path, sep=";")[["sexual_assault", "text"]]
                aux['text'] = aux['text'].apply(lambda x: normalize_string(x))
                classified_df = classified_df.append(aux)

    # Ambiguous strings labeled as 2 must be dropped out
    classified_df.drop(classified_df[ classified_df['sexual_assault'] == 2].index , inplace=True)

    # TRAIN
    model, feature_transf = train(classified_df)

    # PREDICT
    for directory in predict_set:
        predicting_path = os.path.abspath(tweets_path+directory)
        for f in checked(predicting_path):
            df = pd.read_csv(predicting_path +"/"+ f)
            tweets_list = []
            for t in df["text"]:
                tweets_list.append(str(t))
            tweets = feature_transf.transform(tweets_list)
            df.insert(0, "predicted_proba", model.predict_proba(tweets), True)
            Path(f'{predicting_path}/Classified').mkdir(parents=True, exist_ok=True)  # Check if the output directory exists, else create it
            df.to_csv(predicting_path+"/Classified/predicted_"+f)
