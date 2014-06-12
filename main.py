from time import sleep
import tweepy
import followcreatives

yourname = raw_input("your twitter screenname >> ")
name1 = raw_input("twitter user >> ")
name2 = raw_input("twitter user >> ")
name3 = raw_input("twitter user >> ")
name4 = raw_input("twitter user >> ")
name5 = raw_input("twitter user >> ")

names = [name1, name2, name3, name4, name5]

for i in names:
    try:
        followcreatives.main(yourname, i)
    except tweepy.error.TweepError:
        print "Waiting for reset...(15 min)"
        sleep(905)