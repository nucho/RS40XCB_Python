#!/usr/bin/env python2.6
# coding: utf-8
# author: atsushi egashira
# license: LGPLv3
"""
FutabaのRS405,RS406CB制御用ライブラリ
制御例
"""

import time
from rs40xcb_python import rs40xcb

if __name__ == '__main__':
    # メインルーチン
    servo = rs40xcb.RS40XCB(16,115200)
    print'ID1のサーボのトルクをオン'
    servo.torque(1, 1)
     
    print '最高速度で100度の位置へ回転'
    servo.move(1, 1000,0)
     
    time.sleep(1) # しばし待つ
     
    print '現在角度:%d' %servo.getAngle(1)
     
    print '1秒かけて0度の位置へ'
    servo.move(1,0,100)
     
    time.sleep(1)

    print '現在角度:%d' %servo.getAngle(1)