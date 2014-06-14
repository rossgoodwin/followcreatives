import tweepy
import fc_auth


CONSUMER_KEY = fc_auth.c_k
CONSUMER_SECRET = fc_auth.c_s
ACCESS_KEY = fc_auth.a_k
ACCESS_SECRET = fc_auth.a_s
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


words = ['write', 'writer', 'writing', 'author', 'photographer', 'photographs' 'photograph', 'camera', 'art', 
         'music', 'musician', 'paint', 'painter', 'literary', 'literature', 'lit', 'book', 'books', 'fiction',
         'artist', 'story', 'stories', 'magazine', 'review', 'illustrator', 'documentary', 'film', 'filmmaker',
         'journal', 'create', 'creative', 'creator', 'creativity', 'design', 'designer', 'photo', 'arts',
         'gallery', 'painting', 'illustration', 'poem', 'poetry', 'poet', 'novel']


def main(yn, nm):
    """Follows creatives from list of friends of inputted name"""
    for i in tweepy.Cursor(api.friends, id=nm).items():
        des = i._json['description']
        creative = False
        for j in words:
            if j in des.lower():
                creative = True
                break
            else:
                continue
        if creative and i._json['screen_name'] != yn:
            i.follow()
        else:
            continue
        

if __name__ == '__main__':
    yourname = raw_input("your twitter screenname >> ")
    name1 = raw_input("twitter user >> ")
    main(yourname, name1)
    