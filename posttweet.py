import tweepy
auth = tweepy.OAuthHandler('CONSUMER KEY', 'CONSUMER SECRET')
auth.set_access_token('ACCESS TOKEN', 'ACCESS TOKEN SECRET')
api=tweepy.API(auth, wait_on_rate_limit=True)
f=open('/PATH/TO/TWEET/FILE', 'r')
api.update_status(f.read())
f.close()
