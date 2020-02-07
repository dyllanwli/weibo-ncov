#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import random
import numpy as np

import json
import math

import sys
import traceback

import requests
from requests.adapters import HTTPAdapter


class Weibo(object):
    def __init__(self):
        # self.random_user_id_list = random.sample(range(1000000000,9999999999), 10**8)
        self.random_user_id_list = np.random.randint(1000000000,9999999999, size = 10**2)

    def get_json(self, params):
        url = 'https://m.weibo.cn/api/container/getIndex?'
        r = requests.get(url, params=params)
        return r.json()

    def get_user_info(self, user_id):
        params = {'containerid': '107603' + str(user_id)}
        js = self.get_json(params)
        if js['ok']:
            return True
    
    def write_to_txt(self, filename):
        with open(filename, 'w') as f:
            for index, item in enumerate(self.random_user_id_list):
                if index//10000 == 0:
                    print()
                f.write("%s\n" % item)
    
    def write_to_txt_np(self, filename):
        np.save(filename, self.random_user_id_list)

    def start(self):
        try:
            self.write_to_txt_np("test.txt")

                # if self.get_user_info(user_id):
                #     print("User exists")
                # else:
                #     print("User non exists")
        except Exception as e:
            print('Error: ', e)
            traceback.print_exc()


def main():
    try:
        wb = Weibo()
        wb.start()
    except Exception as e:
        print('Error: ', e)
        traceback.print_exc()


if __name__ == '__main__':
    main()
