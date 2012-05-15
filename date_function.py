#! /usr/bin/env python
# coding: utf-8
import datetime
date=datetime.date(2010,11,1)

def twitter_age(created_at):
    if isinstance(created_at,datetime.datetime):
        created_at=created_at.date()
    d1=datetime.date(2008,4,28)#twitter日本語版サービス開始日
    now=datetime.date.today()
    max_age=now-d1
    this_age=now-created_at
    return int(1.0*this_age.days/max_age.days*100)

def main():
    print twitter_age(date)
if __name__ == '__main__':
    main()