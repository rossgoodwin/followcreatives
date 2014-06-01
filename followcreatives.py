import tweepy
from fc_auth import *


CONSUMER_KEY = c_k
CONSUMER_SECRET = c_s
ACCESS_KEY = a_k
ACCESS_SECRET = a_s
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


words = ['write', 'writer', 'writing', 'author', 'photographer', 'photographs' 'photograph', 'camera', 'art', 
         'music', 'musician', 'paint', 'painter', 'literary', 'literature', 'lit', 'book', 'books', 'fiction',
         'artist', 'story', 'stories', 'magazine', 'review', 'illustrator', 'documentary', 'film', 'filmmaker',
         'journal', 'create', 'creative', 'creator', 'creativity', 'design', 'designer', 'photo', 'arts',
         'gallery', 'painting', 'illustration']


main(name):
    """Follows creatives from list of friends of inputted name"""
    for i in tweepy.Cursor(api.friends, id=name).items():
        des = i._json['description']
        creative = False
        for j in words:
            if j in des.lower():
                creative = True
                break
            else:
                continue
        if creative and i._json['screen_name'] != 'Manifestists':
            i.follow()
        else:
            continue