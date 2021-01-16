import pickle
import re
from collections import Counter
from tensorflow.keras import losses
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.layers import Conv1D, Dense, Input, Embedding, Dropout, Activation, MaxPooling1D, Flatten
import ftfy
import nltk
import pandas as pd
from nltk.corpus import stopwords
from gensim.models import KeyedVectors
import numpy as np



class cnn_rumor_detection():
 def __init__(self,embedding_dim=400,max_sequence_length=150,optimizer='AdaGrad',epochs=10, batch_size=10,filters_number=250,model_name='AdaGrad_model'):
     self.embedding_dim=embedding_dim
     self.max_sequence_length=max_sequence_length
     self.epochs=epochs
     self.batch_size=batch_size
     self.filters=filters_number
     self.model_name=model_name
     self.optimizer=optimizer


 def pre_processing_tweets(self, input):
    def deEmojify(inputString):
        return inputString.encode('ascii', 'ignore').decode('ascii')
    df = pd.read_csv("contractions.csv", usecols=['col1', 'col2'])
    contractions_dict = dict(zip(list(df.col1), list(df.col2)))
    self.message_list , self.label_list = [] , []
    c_re = re.compile('(%s)' % '|'.join(contractions_dict.keys()))
    def expand_contractions(text, c_re=c_re):
        def replace(match):
            return contractions_dict[match.group(0)]
        return c_re.sub(replace, text)
    self.tweet_to_analyze =[]
    for msg in input:
        tweet =msg
        tweet = deEmojify(tweet)
        tweet = re.sub("(@[A-Za-z0-9]+)|(\#[A-Za-z0-9]+)|(<Emoji:.*>)|(pic\.twitter\.com\/.*)",'', tweet)
        tweet = re.sub(r'http\S+', '', tweet)
        tweet = re.sub(r'#\S+', '', tweet)
        tweet = re.sub(r'@\S+', '', tweet)
        tweet = re.sub('\n','', tweet)
        tweet = re.sub("([^0-9A-Za-z \t])", " ", tweet)
        tweet.lower()
        tweet = expand_contractions(tweet)
        self.tweet_to_analyze.append(tweet)
    print(self.tweet_to_analyze)

 def pre_processing_dataset(self):
        self.tweets = pd.read_csv("mydatasetnew.csv", usecols=['author', 'sentence', 'type'])
        df = pd.read_csv("contractions.csv", usecols=['col1', 'col2'])
        contractions_dict = dict(zip(list(df.col1), list(df.col2)))
        self.sentence_list, self.type_list, self.author_list = [], [], []
        c_re = re.compile('(%s)' % '|'.join(contractions_dict.keys()))
        def expand_contractions(text, c_re=c_re):
            def replace(match):
                return contractions_dict[match.group(0)]
            return c_re.sub(replace, text)

        self.word2vec = KeyedVectors.load_word2vec_format("word2vec_twitter_tokens.bin", unicode_errors='ignore',
                                                          binary=True)

        count = Counter()
        for author, sentence, type in zip(self.tweets['author'], self.tweets['sentence'], self.tweets['type']):
            if re.match("(\w+:\/\/\S+)", sentence) == None:
                sentence = ' '.join(
                    re.sub("(@[A-Za-z0-9]+)|(\#[A-Za-z0-9]+)|(<Emoji:.*>)|(pic\.twitter\.com\/.*)", " ",
                           sentence).split())
                author = ' '.join(
                    re.sub("(@[A-Za-z0-9]+)|(\#[A-Za-z0-9]+)|(<Emoji:.*>)|(pic\.twitter\.com\/.*)", " ",
                           author).split())

                sentence = re.sub('<.*?>', '', sentence)
                author = re.sub('<.*?>', '', author)
                sentence = ftfy.fix_text(sentence)
                author = ftfy.fix_text(author)
                sentence = expand_contractions(sentence)
                author = expand_contractions(author)
                sentence = ' '.join(re.sub("([^0-9A-Za-z \t])", " ", sentence).split())
                author = ' '.join(re.sub("([^0-9A-Za-z \t])", " ", author).split())
                stop_words = set(stopwords.words('english'))
                word_tokens = nltk.word_tokenize(sentence)
                filtered_sentence = [w for w in word_tokens if not w in stop_words and w in self.word2vec.vocab]
                print(filtered_sentence)
                count.update(filtered_sentence)
                self.sentence_list.append(filtered_sentence)
                self.type_list.append(type)
                self.author_list.append(author)
        self.clean_tweets_dict = {j[0]: i for i, j in enumerate(count.most_common(12000))}
        self.clean_tweets_dict['UNK'] = 12001
        self.clean_tweets_dict['PAD'] = 12002
        pickle.dump(self.clean_tweets_dict, open('word_dictionary.pkl', 'wb'))
        self.spliting_data()
        self.build_word_embedding_matrix()
        self.build_model()

 def spliting_data(self):
     self.train_dataset, self.train_dataset_type, self.test_dataset, self.test_dataset_type = [], [], [], []
     for i in range(0, len(self.sentence_list)):
         if np.random.uniform(0, 1) < (80 / 100):
             self.train_dataset.append(self.sentence_list[i])
             self.train_dataset_type.append(self.type_list[i])
         else:
             self.test_dataset.append(self.sentence_list[i])
             self.test_dataset_type.append(self.type_list[i])

 def build_model(self):

     self.model = Sequential()
     self.model.add(Embedding(len(self.embedding_matrix), int(400), weights=[self.embedding_matrix],
                         input_length=int(self.max_sequence_length), trainable=False))
     self.model.add(Dropout(0.3))
     self.model.add(Conv1D(filters=int(self.filters), kernel_size=3, padding='same', activation='relu'))
     self.model.add(MaxPooling1D(pool_size=2))
     self.model.add(Dropout(0.3))
     self.model.add(Dense(200, activation='relu'))
     self.model.add(Flatten())
     self.model.add(Dense(1, activation='sigmoid'))

     print(self.model.summary())

     train_sents, test_sents = self.generate_data_to_train()
     self.model.compile(loss=losses.mean_squared_error, optimizer=str(self.optimizer), metrics=['acc'])
     self.hist = self.model.fit(np.array(train_sents), np.array(self.train_dataset_type), \
                      validation_data=(np.array(test_sents), np.array( self.test_dataset_type)), \
                      epochs=int(self.epochs), batch_size=int(self.batch_size))
     print(self.model.summary())
     self.model.save("models/"+self.model_name+".h5")

     train_loss = self.hist.history['loss']
     train_val_loss=self.hist.history['val_loss']
     train_acc=self.hist.history['acc']
     train_acc_val=self.hist.history['val_acc']

     dict_history={
         "train_loss": train_loss,
         "train_val_loss": train_val_loss,
         "train_acc":train_acc,
         "train_val_acc":train_acc_val
     }

     pickle.dump(dict_history,open('models/history'+self.model_name+'.pkl', 'wb'))

 def generate_data_to_train(self):
     train_sents_list_vector = []
     for list in self.train_dataset:
         temp_list = []
         for word in list:
             temp_list.append(self.clean_tweets_dict.get(word, 12001))
         for i in range(0, (self.max_sequence_length - len(temp_list))):
             temp_list.append(self.clean_tweets_dict['PAD'])
         train_sents_list_vector.append(temp_list)

     test_sents_list_vector = []
     for list in self.test_dataset:
         temp_list = []
         for word in list:
             temp_list.append(self.clean_tweets_dict.get(word, 12001))
         for i in range(0, (self.max_sequence_length - len(temp_list))):
             temp_list.append(self.clean_tweets_dict['PAD'])
         test_sents_list_vector.append(temp_list)

     return train_sents_list_vector,test_sents_list_vector


 def build_word_embedding_matrix(self):
        self.embedding_matrix = pd.np.zeros((len(self.clean_tweets_dict) + 1, self.embedding_dim))

        for (word, idx) in self.clean_tweets_dict.items():
                self.embedding_matrix[idx] = self.word2vec.word_vec(word)
        self.embedding_matrix[len(self.embedding_matrix)-1] = [0]*400

        print(self.embedding_matrix.shape)
        return self.embedding_matrix





