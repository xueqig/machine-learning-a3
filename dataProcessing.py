import csv
from ast import literal_eval
import numpy as np
import pandas as pd
from scipy.sparse import lil_matrix


class TwitterDataProcessing:
    def read_count_tfidf_data(self, file_path):
        print("Reading " + file_path + " ...")
        data = pd.read_csv(file_path, dtype={"sentiment": str, "tweet_id": int}, converters={"tweet": literal_eval})
        labels = np.array(list(data["sentiment"]))
        tweet_ids = np.array(list(data["tweet_id"]))
        tweets = list(data["tweet"])

        tweets_sparse_matrix = lil_matrix((len(tweets), 5000))

        for i in range(len(tweets)):
            tweet = tweets[i]
            for j in range(len(tweet)):
                word = tweet[j]
                tweets_sparse_matrix[i, word[0]] = word[1]

        return labels, tweet_ids, tweets_sparse_matrix

    def read_glove_data(self, file_path):
        print("Reading " + file_path + " ...")
        data = pd.read_csv(file_path, dtype={"sentiment": str, "tweet_id": int}, converters={"tweet": literal_eval})
        labels = list(data["sentiment"])
        tweet_ids = list(data["tweet_id"])
        tweets = list(data["tweet"])
        return labels, tweet_ids, tweets

    def read_raw_data(self, file_path):
        print("Reading " + file_path + " ...")
        data = pd.read_csv(file_path, dtype={"sentiment": str, "tweet_id": int, "tweet": str})
        labels = np.array(list(data["sentiment"]))
        tweet_ids = np.array(list(data["tweet_id"]))
        tweets = np.array(list(data["tweet"]))
        return labels, tweet_ids, tweets

    def write_predictions(self, tweet_ids, predictions, file_path):
        print("Writing " + file_path + "...")
        pred_file = open(file_path, "w")
        writer = csv.writer(pred_file)
        writer.writerow(["tweet_id", "sentiment"])
        for i in range(len(tweet_ids)):
            writer.writerow([tweet_ids[i], predictions[i]])
        pred_file.close()
        print("Finish writing " + str(i + 1) + " testing")