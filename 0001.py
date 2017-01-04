#! /usr/bin/env python
# coding: utf-8

# 生成激活码（或者优惠券）

import uuid

def create_num(num,length=16):
    result = []
    while num > 0:
        uuid_id = uuid.uuid1()
        # 删去字符串中的'-',取出前length 个字符
        temp = str(uuid_id).replace('-', '')[:length]
        if temp not in result:
            result.append(temp)
            num -= 1
    return result

if __name__ == '__main__':
    print(create_num(2,32))
