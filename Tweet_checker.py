#Tweet_Checker.py

tweet = input("Enter your tweet: ")
tweet_length = len(tweet)

#The accepted twitter length is 140.
max_chars = 140

if tweet_length < max_chars:
    print(f"That {tweet_length} character tweet will work!")
else:
    print(f"Your {tweet_length} character tweet is {tweet_length - max_chars} chars too long")
