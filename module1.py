#!/bin/python3

import math
import os
import random
import re
import sys


import urllib.parse
import urllib.request
import json
#
# Complete the 'getUsernames' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts INTEGER threshold as parameter.
#

def getUsernamesPage(url, page, users):

    req = urllib.request.Request(url+str(page))
    response = urllib.request.urlopen(req)
    str_res = response.read().decode('utf8').replace("'", '"')
    res = json.loads(str_res)

    tot_pages = res['total_pages']
    # per_page = res['per_page']

    for i in range(0, len(res['data'])):
        if res['data'][i]['submission_count'] > threshold:
            users.append(res['data'][i]['username'])
    
    if (page==tot_pages):
        return users
    else:
        return getUsernamesPage(url,page+1,users)

def getUsernames(threshold):
    # Write your code here
    url = 'https://jsonmock.hackerrank.com/api/article_users/search?page='
    users = []

    return getUsernamesPage(url,1,users)


if __name__ == '__main__':
    threshold = int(10)
    result = getUsernames(threshold)
    print(result)