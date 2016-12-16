#
# Tools for retrieving content from webpages
#

#import struct
#from datetime import datetime as dt

import requests
import re


def getTopPosts():
    r = requests.get()


def getUser(*user, **params):
    """ Get user page in requests query format """

    # Make sure input is in right format
    if ('url' in params):
        url = params['url']
    elif type(user[0]) is str:
        url = 'https://www.reddit.com/user/'+user[0]
    else:
        print('Input should be like: getComments("username") or getComments(url="url")')

    # Retrieve webpage
    r = requests.get(url)

    # Check if user exists
    if r.status_code is 200:
        return r
    else:
        print('User does not exist')
        return r


def getComments(r):
    """ Get all comments listed on first page of user
    By default comments are sorted by newest
    """

    # Get all div elements that correspond to comments
    #strlist = re.split('<div', r.text )
    strlist = re.split('noncollapsed', r.text )
    #indices = [i for i,x in enumerate(divlist) if re.search('noncollapsed',x) ]
    #jindices = [i for i,x in enumerate(divlist) if re.search('class="md"',x) ]

    commentData = []
    #print( len(indices))
    #print( len(jindices))
    
    for splitpart in strlist[1:]:
        
        # Get Comment ID
        thing_id = re.split('thing_t1_',splitpart)
        thing_id = re.split('"',thing_id[1])
        thing_id = thing_id[0]
        # Get Comment Permalink
        permalink = re.split('>permalink<',splitpart)
        permalink = re.split('<a href="',permalink[0])
        permalink = re.split('"',permalink[-1])
        permalink = permalink[0]
        # Get Comment text
        ctext = re.split(' class="md">',splitpart)
        ctext = re.split('</div>',ctext[1])
        ctext = ctext[0]
        
        commentData = commentData + [{'id':thing_id, 'permalink':permalink, 'text':ctext}]

    return commentData
    

