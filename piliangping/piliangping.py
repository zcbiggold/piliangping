#!/usr/bin/env python
#coding:utf-8


from socket import gethostbyname
DOMAIN= "domain.txt"

with open(DOMAIN,'r') as f:

     for line in f.readlines():
        try:
            host = gethostbyname(line.strip('\n'))  #�����������õ���IP
        except Exception as e:
            with open('error.txt','a+') as ERR:  #error.txtΪû��IP�󶨵�����
                ERR.write(line.strip()+ '\n')
        else:
            with open('result.txt','a+') as r: #result.txt����洢��������������Ľ��  #��ʾ��ip�󶨵��������ÿո����
                r.write(host + '\n')