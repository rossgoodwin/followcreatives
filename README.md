FollowCreatives
===============

FollowCreatives is a simple script written by [Ross Goodwin](http://rossgoodwin.com) in Python 2.7 that follows other creative folks on Twitter. Tweepy is required. 

You must create a new Twitter application at [dev.twitter.com](http://dev.twitter.com) to generate the necessary API keys and access tokens. Once acquired, place the API keys and access tokens into a new file named "fc\_auth.py" in the same directory as followcreatives.py, using the variable names c\_k, c\_s, a\_k, and a\_s.

To run FollowCreatives, enter the following in the terminal from the directory containing the python files:

    $ python main.py

You will then be prompted to enter your Twitter screenname followed by five other Twitter screennames. Creative individuals from entered screennames' Twitter friends will be followed, with 15 minute breaks to account for API rate limiting.



