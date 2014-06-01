import tweepy
import fc_auth


CONSUMER_KEY = fc_auth.c_k
CONSUMER_SECRET = fc_auth.c_s
ACCESS_KEY = fc_auth.a_k
ACCESS_SECRET = fc_auth.a_s
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def main():
    for i in tweepy.Cursor(api.friends).items():
        sn = i._json['screen_name']
        ef = api.show_friendship(source_screen_name='Manifestists', target_screen_name=sn)[1].following
        if not ef:
            api.destroy_friendship(screen_name=sn)
        else:
            continue
        

if __name__ == '__main__':
    main()