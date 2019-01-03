#!/usr/bin/env python
#coding:utf-8


from socket import gethostbyname
DOMAIN= "domain.txt"

with open(DOMAIN,'r') as f:

     for line in f.readlines():
        try:
            host = gethostbyname(line.strip('\n'))  #域名反解析得到的IP
        except Exception as e:
            with open('error.txt','a+') as ERR:  #error.txt为没有IP绑定的域名
                ERR.write(line.strip()+ '\n')
        else:
            with open('result.txt','a+') as r: #result.txt里面存储的是批量解析后的结果  #显示有ip绑定的域名，用空格隔开
                r.write(host + '\n')