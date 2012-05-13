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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        api=get_api()
        ss=get_user_word(api)

        self.response.out.write(ss)

app = webapp2.WSGIApplication([('/', MainHandler)],
                              debug=True)
def get_api():
    auth = tweepy.OAuthHandler(setting.CONSUMER_KEY,setting.CONSUMER_SECRET)
    auth.set_access_token(setting.token,setting.token_secret)
    return tweepy.API(auth_handler=auth)
def get_user_word(api):
    tl=api.user_timeline(id="__whats")
    s=""
    for t in tl:
        s+=t.text+"<br>"
    r=re.compile('@\w*')
    ss=re.sub(r,"",s)
    return ss