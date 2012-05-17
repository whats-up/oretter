#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2
import tweepy
import re
import setting
import urllib
import logging
from BeautifulSoup import BeautifulSoup
import os
from google.appengine.ext.webapp import template
from test import TestHandler
import date_function
class MainHandler(webapp2.RequestHandler):
    def get(self):
        user_id=self.request.get("id")
        contents={}
        if user_id:
            contents["id"]=user_id
            api=get_api()
            tl=api.user_timeline(id=user_id,count=200)
            contents["keys"]=get_user_word(tl)
            contents["kousei"]=get_user_kousei(tl)
            user=tl[0].user
            contents["user"]=user
            contents["user_age"]=date_function.twitter_age(user.created_at)
        else:
            contents["id"]=None
        path = os.path.join(os.path.dirname(__file__), 'tmpl/base.html')
        self.response.out.write(template.render(path, contents))
app = webapp2.WSGIApplication(
    [
        ('/test/', TestHandler),
        ('/', MainHandler),
    ],debug=True)
def get_api():
    auth = tweepy.OAuthHandler(setting.CONSUMER_KEY,setting.CONSUMER_SECRET)
    auth.set_access_token(setting.token,setting.token_secret)
    return tweepy.API(auth_handler=auth)
def get_user_word(tl):
    s=""
    for t in tl:
        s+=t.text
    r=re.compile('@\w*')
    ss=re.sub(r,"",s)
    yahoo_url="http://jlp.yahooapis.jp/KeyphraseService/V1/extract?"
#    yahoo_url="http://jlp.yahooapis.jp/MAService/V1/parse?"
#    yahoo_url="http://jlp.yahooapis.jp/KouseiService/V1/kousei?"
    query={
    "sentence":ss,
    "appid":setting.YAHOO_APP_ID
    }
    param=urllib.urlencode(query)
    result=urllib.urlopen(yahoo_url,param)
    xml=result.read()
    soup = BeautifulSoup(xml)
    li=[]
    for item in soup.findAll("result"):
        li.append({"key":item.find("keyphrase").string,"score":item.find("score").string})
    return li
def get_user_kousei(tl):
    #yahooの校正支援APIから
    #　http://developer.yahoo.co.jp/webapi/jlp/kousei/v1/kousei.html
    s=""
    for t in tl:
        s+=t.text
    r=re.compile('@\w*')
    ss=re.sub(r,"",s)

    yahoo_url="http://jlp.yahooapis.jp/KouseiService/V1/kousei?"
    query={
        "sentence":ss,
        "appid":setting.YAHOO_APP_ID,
        "no_filter":"5,11,12,15"
    }
    param=urllib.urlencode(query)
    result=urllib.urlopen(yahoo_url,param)
    xml=result.read()
    soup = BeautifulSoup(xml)
    li=[]
    for item in soup.findAll("result"):
        li.append({"surface":item.find("surface").string,
                   "word":item.find("shitekiword").string,
                   "info":item.find("shitekiinfo").string,
                   })
    return li