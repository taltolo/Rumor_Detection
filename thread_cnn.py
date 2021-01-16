import pickle
import numpy
from tensorflow import keras
from PyQt5.QtCore import QThread, pyqtSignal
import numpy as np
from cnn_rumor_detection import cnn_rumor_detection
from tweets_service import tweets_service


class thread_cnn_model(QThread):
    commit=pyqtSignal()

    def __init__(self,embedding_dim=400,max_sequence_length=150,optimizer='AdaGrad',epochs=10, batch_size=10,filters_number=250,model_name='AdaGrad_model'):
        QThread.__init__(self)
        self.cnn=cnn_rumor_detection(embedding_dim,max_sequence_length,optimizer,epochs,batch_size,filters_number,model_name)

    def run(self):
        self.cnn.pre_processing_dataset()
        self.commit.emit()

class thread_cnn_analyze(QThread):
    commit_analyze = pyqtSignal(numpy.ndarray)
    def __init__(self,tweet,model_name, filters_number,optimizer,epochs,batch_size):
        QThread.__init__(self)
        self.word_dictionary = pickle.load(open("word_dictionary.pkl", 'rb'))
        self.cnn = cnn_rumor_detection(400,140,optimizer,epochs,batch_size,filters_number,model_name)
        self.cnn.pre_processing_tweets(tweet)
        self.cnn.model=keras.models.load_model("models/"+model_name+".h5")

    def run(self):
        tweet2vector = []
        temp_tweet_spilt = []
        for tweet in self.cnn.tweet_to_analyze:
            temp = []
            temp_tweet_spilt=tweet.split()
            for word in temp_tweet_spilt:
                 temp.append(self.word_dictionary.get(word, 12001))
            tweet2vector.append(temp)
        for tweet in tweet2vector:
            for i in range(0, (self.cnn.max_sequence_length - len(tweet))):
                tweet.append(self.word_dictionary['PAD'])
        tweet2nparry = np.array(tweet2vector,dtype=np.float64)
        print(tweet2nparry.shape)
        self.analyze = self.cnn.model.predict([tweet2nparry])
        print(type(self.analyze))
        self.commit_analyze.emit(self.analyze)


class thread_cnn_twiteer(QThread):
    commit_tweets=pyqtSignal(list)

    def __init__(self,user_name,amount_tweets):
        QThread.__init__(self)
        self.twiteer_api=tweets_service(user_name, amount_tweets)

    def run(self):
        tweets_list=[]
        tweets_list=self.twiteer_api.extract_tweet()
        self.commit_tweets.emit(tweets_list)


