from time import sleep
import tweepy
import unfollow


while True:
    try:
        unfollow.main()
    except tweepy.error.TweepError:
        print "Waiting for reset...(15 min)"
        sleep(905)