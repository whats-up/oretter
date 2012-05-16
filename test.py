#!/usr/bin/env python
# -*- coding:utf-8 -*-

import webapp2
import re
import urllib
import logging
import os

class TestHandler(webapp2.RequestHandler):
    def get(self):

        self.response.out.write("ok")

