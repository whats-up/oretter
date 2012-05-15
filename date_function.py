#! /usr/bin/env python
# coding: utf-8
import datetime
date=datetime.date(2010,11,1)

def twitter_age(_date):
    if isinstance(_date,datetime.datetime):
        _date=_date.date()
    d1=datetime.date(2008,4,28)#twitter日本語版サービス開始日
    now=datetime.date.today()
    max_age=now-d1
    this_age=now-_date
    return int(1.0*this_age.days/max_age.days*100)

def main():
    pass
if __name__ == '__main__':
    main()