#!/usr/bin/env python
# -*- coding:utf-8 -*-

import webapp2
import re
import urllib
import logging
import os

class TestHandler(webapp2.RequestHandler):
    def get(self):
        br="<br>"
        links=[
            '<a href="/test/?o=12345">test :1</a>',
            '<a href="/test/?o=12345&p=abcde&q=hogehoge">test :2-1</a>',
            '<a href="/test/?o=12345&o=abcde&o=hogehoge">test :2-2</a>',
        ]
        s='<a href="https://developers.google.com/appengine/docs/python/tools/webapp/requestclass?hl=ja">Doc</a>%s'%br
        s+="<h3>test</h3>"
        for l in links:
            s+=l+br
        #test1
        obj1=self.request.get("o")
        if obj1:
            s+='self.request.get("o") →'+obj1+br
        else:
            s+='self.request.get("o") →:not object'+br
        #test2
        obj2=self.request.get_all("o")
        if obj2:
            s+='self.request.get_all("o") →%s%s'%(obj2,br)
        else:
            s+='self.request.get_all("o") →→:not object'+br
        s+="<h3>WebOb Request </h3>"
        s+='<h5>self.request.body</h5> %s%s'%(self.request.body,br)
        s+='<h5>self.request.body_file</h5> %s%s'%(self.request.body_file,br)
        s+='<h5>self.request.remote_addr</h5> %s%s'%(self.request.remote_addr,br)
        s+='<h5>self.request.url</h5> %s%s'%(self.request.url,br)
        s+='<h5>self.request.path</h5> %s%s'%(self.request.path,br)
        s+='<h5>self.request.query_string</h5> %s%s'%(self.request.query_string,br)
        #headers
        s+='<h5>self.request.headers</h5>'

        for k,v in self.request.headers.items():
            s+="%s : %s%s"%(k,v,br)

        s+='<h5>self.request.cookies</h5> %s%s'%(self.request.cookies,br)

        self.response.out.write(s)

