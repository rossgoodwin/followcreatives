import tweepy
from time import sleep
from fc_auth import *
from followcreatives import *

name1 = raw_input("twitter user >> ")
name2 = raw_input("twitter user >> ")
name3 = raw_input("twitter user >> ")
name4 = raw_input("twitter_user >> ")

names = [name1, name2, name3, name4]

for i in names:
    try:
        main(i)
    except tweepy.TweepError:
        print "Waiting for reset...(15 min)"
        sleep(905)