# jim mora bot
# Playoffs?!
import twitter
import time

c_key, c_secret, at_key, at_secret =\
(line.strip() for line in open("login.config"))

api = twitter.Api(consumer_key=c_key,
				  consumer_secret=c_secret,
				  access_token_key=at_key,
				  access_token_secret=at_secret)

results = api.GetSearch("playoffs")


while True:
	results = api.GetSearch("playoffs")
	# respond to first person on list
	print results[0].user.screen_name
	api.PostUpdate("@%s Playoffs?! Don't talk about -- Playoffs?! You "
				   "kidding me? Playoffs?! I just hope we can win a game."
		           % (results[0].user.screen_name.encode('ascii','replace')),
		           in_reply_to_status_id=results[0].id)

	# pause 45 mins
	time.sleep(2700)
