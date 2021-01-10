import tweepy


class tweets_service(object):

    def __init__(self,tweetsCount,amountOfTweets):
        super(tweets_service, self).__init__()
        self.CONSUMER_KEY="BLAz4UpWcAwQhlTd9v7JOHc1L"
        self.CONSUMER_SECRET="BZzv6A2cnZcDDx3YNEu1OivX27i6yRrngN5irvWAgFsjXmSuNE"
        self.ACCESS_TOKEN="1334878703667605505-nA7XjVZiYbsSaUKFMXi4HZfvFLfhTd"
        self.ACCESS_TOKEN_SECRET="qONfS57DIW0J9JMM31eExGc0QAiLnPCc8zxp8SFV9b3ua"
        self.auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        self.auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(self.auth)
        self.tweetsCount=tweetsCount
        self.amountOfTweets=amountOfTweets


    def extract_tweet(self):
        self.all_tweetsFromUser_list = []
        try:
            user=self.api.get_user( self.tweetsCount)
        except tweepy.TweepError as err:
            print("User dose not exist")
            self.all_tweetsFromUser_list.append(-1)
            return self.all_tweetsFromUser_list



        ID = user.id_str
        user = self.api.get_user(ID)
        statuses_count = user.statuses_count
        if statuses_count==0:
            self.all_tweetsFromUser_list.append(0)
            return self.all_tweetsFromUser_list
        elif statuses_count<self.amountOfTweets:
            for tweet in tweepy.Cursor(self.api.user_timeline, screen_name= self.tweetsCount, tweet_mode='extended').items(statuses_count):
                self.all_tweetsFromUser_list.append(str(tweet._json['full_text'] + '\n'))
                print(self.all_tweetsFromUser_list)
                return self.all_tweetsFromUser_list
        else:
            for tweet in tweepy.Cursor(self.api.user_timeline, screen_name= self.tweetsCount, tweet_mode='extended').items(self.amountOfTweets):
             self.all_tweetsFromUser_list.append(str(tweet._json['full_text'] + '\n'))
            print(self.all_tweetsFromUser_list)
            return self.all_tweetsFromUser_list



