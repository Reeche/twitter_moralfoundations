# Part 1
# Specify which group these follower ID's will belong to
# user = 'cdu'
# Speccify the usernames of the accounts you are searching follower lists for
cdu = 'CDU'

# Enter your own KEY, SECRET, TOKEN and TOKEN_SECRET codes here
APP_KEY = '1LkXJ9SqzQm7an39boqQ5AW0v'
APP_SECRET = 'eEDlvPcEEfJPKVR1HkIYCmR0BcsISQWXhzjudaNHvMYj3cGgh7'
OAUTH_TOKEN = '911681697577611264-lQDqG7lcZGjvL1vIvrR3qKTlaPZH3Xp'
OAUTH_TOKEN_SECRET = 'AZqWtegYKM7GrsN0AVmwaqMHQH72R85lzaEwQvpflam8x'

from twython import Twython, TwythonError
import time
import random
import re
import unicodedata

# Authentication required as of Twitter API v1.1
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

print('Twython initialized...')

# Write all the follower ID's of the specified users to a text file
# Rate limited to 15 requests per 15 minutes
# file outputs: <user>FollowersIDs.txt

print('Collecting'+ CDU + "'s followers ids...")

iter = 0
fout = open(user + 'FollowersIDs.txt','w')
cursor_id = -1
while cursor_id != 0 and iter != 15:
 try:
  iter += 1
  print(iter)
  if iter == 15:
   print('waiting 15 mins for new rate limit window...')
   time.sleep(910)
   iter=0
  followers = twitter.get_followers_ids(screen_name = CDU, cursor = cursor_id)
  for id in followers['ids']:
   fout.write(str(id)+'\n')
  cursor_id = followers ['next_cursor']
 except TwythonError as e:
  print(e)
fout.close()

# Read the text file and eliminate duplicates
# File outputs: <user>FollowersIDsCleaned.txt
lines_seen = set()
fin = open(user + 'FollowersIDs.txt','r')
final = open(user + 'FollowersIDsCleaned.txt','w')
followerlist = []
followerlistfinal = []
for id in fin:
 re.sub('\n',"",id)
 followerlist.append(int(id))
 if id not in lines_seen:
  followerlistfinal.append(int(id))
  lines_seen.add(id)
  final.write(id)
fin.close()
final.close()
print('Total follower IDs =', len(followerlist))
print('Cleaned total follower IDs =', len(followerlistfinal))
random.shuffle(followerlist)
print('done')

# Repeat this code for all parties so the output should be one set of <user>FollowersIDsCleaned.txt for each group
