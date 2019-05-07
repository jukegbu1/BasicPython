#Tweet length calculator

# Create a variable called tweet and put "Hear Me Code class was so much fun today!"
tweet = "Hear Me Code class was so much fun today!ar Me Code class was so much fun today!"

# Measure the length of tweet
print len(tweet)

# Was that tweet more than 140 characters?
# If so, tell the user it was too long!
# Was that tweet 140 or fewer characters?
# If so, tell the user how witty they are!

maxtweet=140

if tweet < maxtweet:
    print "You are so witty"
else:
    print "That was way to long!"
