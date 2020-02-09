#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import random
import numpy as np
from numpy.random import default_rng
import gc
import time
import json
import math

import sys
import traceback

import requests
from requests.adapters import HTTPAdapter


class Weibo(object):
    def __init__(self):
        self.test = 0
        #self.true_user = self.load_np("/kaggle/working/user_list.npy")
        # self.random_user_id_list = np.array(random.sample(range(1000000000,5999999999), 10**8))
        #self.random_user_id_list = np.random.randint(1000000000,9999999999, size = 10**1)
        #rng = default_rng()
        #self.random_user_id_list = rng.choice(range(1000000000,9999999999), size=10**3, replace=False)
        #self.random_user_id_list = np.random.randint(10,99, size = 10**2)

    def get_json(self, params):
        url = 'https://m.weibo.cn/api/container/getIndex?'
        # print("Requesting...")
        r = requests.get(url, params=params)
        return r.json()

    def get_user_info(self, user_id):
        params = {'containerid': '107603' + str(user_id)}
        js = self.get_json(params)
        if js['ok']:
            return True
            # info = js['data']['userInfo']
            # statuses_count = info.get('statuses_count', 0)
            # page_count = int(math.ceil(statuses_count / 10.0))
            # if page_count > 1:
            #     return True
            # else:
            #     return False
    
    def write_to_txt(self, filename):
        with open(filename, 'w') as f:
            for index, item in enumerate(self.random_user_id_list):
                if index//10000 == 0:
                    print()
                f.write("%s\n" % item)
    
    def write_to_txt_np(self, filename, l):
        np.save(filename, l)
    
    def load_np(self,filename):
        randList = np.load(filename)
        return randList
    
    def check_user(self):
        # print("Load user_list", self.true_user)
        randList = list(self.load_np("../input/test.npy"))
        start_index = 72
        try:
            with open("user_list.txt", 'r') as file:
                start_line = file.readlines()[-1]
                start_index = int(start_line.split(' ')[0])
        except:
            pass
        lenRandList = len(randList)
        # print("Test Exists User", self.get_user_info("1669879400"))
        print(len(randList))
        index = start_index
        randList = randList[:-start_index]
        while index < lenRandList:
            index += 1
            user_id = randList.pop()
            print("checking", user_id)
            # print(index, user_id)
            if index%30 == 0:
                time.sleep(6)
            try:
                if self.get_user_info(user_id):
                    print("The", user_id, "is exists")
                    with open("user_list.txt", 'a') as file:
                        new = "{} {}\n".format(index, user_id)
                        file.write(new)
                    # np.save("/kaggle/working/user_list.npy", randList)

            except Exception as e:
                print('Error: ', e)
                index -= 1
                continue

    def start(self):
        # print("Load user_list", self.true_user)
        # self.write_to_txt_np("test", self.random_user_id_list)
        # randList = list(self.load_np("../input/test.npy"))
        self.check_user()


def main():
    try:
        wb = Weibo()
        wb.start()
    except Exception as e:
        print('Error: ', e)


if __name__ == '__main__':
    main()