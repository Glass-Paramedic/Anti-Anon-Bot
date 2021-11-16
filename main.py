import praw
import threading
#from keep_alive import keep_alive #This is only needed if you want to do the same as anonbot and host for free on replit 

# I would highly recommend you host on a vps instead as replit is extemely unreliable
# Can't afford a vps? Dm me and if your bot is intresting enough I can host it for you

# Create a reddit instance and login #Note: you should use an environment variable for the credentials if you are hosting on replit
reddit = praw.Reddit(
    user_agent="Anti_Anon",
    client_id="96hc68l4iXGXXXXXXXXXX",
    client_secret="JQgXXXX-XXXXXXXXX",
    username="anti-anon-bot",
    password="XXXXX"
)

# Get all posts from r/AnonReddit if the author is not AnonBot
def posts():
    for submission in reddit.subreddit("AnonReddit").stream.submissions(skip_existing=True):
        try:
            if submission.author != "Anon-Bot":
                title = submission.title
                post = submission.selftext
                author = submission.author

                reddit.subreddit("AntiAnonReddit").submit(title, selftext = post + f""" 

    **Original Author** = u/{author}""")
        except Exception as e:
            print(e)
def comments():
    #Get all comments from r/AnonReddit if the author is not AnonBot
    for comment in reddit.subreddit("AnonReddit").stream.comments(skip_existing=True):
        try:
            if comment.author != "Anon-Bot":
                body = comment.body
                author = comment.author
                parent = comment.parent()

                submission = reddit.submission(url="https://www.reddit.com/r/AntiAnonReddit/comments/qv9b46/comment_stream/") #Get the post to stream replies to
                submission.reply(f"""{body}
                
    **Original Author** = u/{author}

    **Parent** = https://www.reddit.com/{parent.permalink}""")
        except Exception as e:
            print(e)

#Create a thread for post and comment functions in order to run both concurrently 
def main():
    threading.Thread(target=posts).start()
    threading.Thread(target=comments).start()
    #threading.Thread(target=keep_alive).start() #This is only needed if are hsoting on replit

#run
if __name__ == '__main__':
    main()
