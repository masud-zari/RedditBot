import requests
import json
import pprint

#Getting username and password
print "Hello and welcome \n"
print "Please enter your username and password to login \n"

user = raw_input("Username: ")
passwd = raw_input("Password: ")

whatToDo = int(raw_input("What would you like to do? \n 1.Download all Imgur files in the first 100 posts \n 2.Post a comment on my subreddit \n Please enter choice: ")); 


username = user
password = passwd

payload = {'user' : user, 'passwd' : passwd, 'api_type' : 'json'}

#Requesting Session
headers = {'user-agent' : '/u/mxz087000 API bot try.',}
client = requests.session()
client.headers = headers
reddit = client.post('https://ssl.reddit.com/api/login', data=payload)
j = json.loads(reddit.content)
mh = j['json']['data']['modhash']


#Post comment on comment  
def postCommentOnComment(mh, comment):
    payload_comment = {'api_type' : 'json', 'text' : commentOnComment, 'thing_id' : 't1_clhmmgy', 'uh' : mh}
    reddit_comment = client.post('https://ssl.reddit.com/api/comment' ,data=payload_comment)
    jreddit_comment = (reddit_comment.content)


if whatToDo == 2 :
    commentOnComment = raw_input("Please enter your comment: ");
    postCommentOnComment(mh, commentOnComment);

