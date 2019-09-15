# -*- coding:utf-8 -*-
import sys
import time
import concurrent.futures
from motor_controller import MotorController
from getTarget_exec import getTargetThread

class TankController():
    """ タンクコントローラー """
    def __init__(self):
        self.mc = MotorController()
        self.gt = getTargetThread()
        self.TurretLeft = 0
        self.TurretRight = 0
        self.excutor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
        self.excutor.submit(self.turret_move)
        #
        # 以下戦車の動作
        #
    def tank_go_forward(self):
        # 前進
        print("exec: " , sys._getframe().f_code.co_name)
        self.mc.forwardMotor1A(50)
        self.mc.forwardMotor1B(50)

    def tank_go_backward(self):
        # 後退
        print("exec: " , sys._getframe().f_code.co_name)
        self.mc.reverseMotor1A(50)
        self.mc.reverseMotor1B(50)
        
    def tank_stop(self):
        # 停止
        print("exec: " ,sys._getframe().f_code.co_name)
        self.mc.breakMotor1A()
        self.mc.breakMotor1B()

    def tank_turn_right(self):
        # 右旋回
        print("exec: " ,sys._getframe().f_code.co_name)
        self.mc.reverseMotor1A(50)
        self.mc.forwardMotor1B(50)

    def tank_turn_left(self):
        # 左旋回
        print("exec: " ,sys._getframe().f_code.co_name)
        self.mc.forwardMotor1A(50)
        self.mc.reverseMotor1B(50)

        #
        # 以下砲台
        #
    def turret_follow(self):
        # 標的追尾開始
        print("exec: " ,sys._getframe().f_code.co_name)
        self.gt.FollowStart()

    def turret_unfollow(self):
        # 標的追尾停止
        print("exec: " ,sys._getframe().f_code.co_name)
        self.gt.FollowStop()

    def turret_shoot(self):
        # BB弾発射
        print("exec: " ,sys._getframe().f_code.co_name)
        self.mc.forwardMotor2B(100)
        time.sleep(5)
        self.mc.breakMotor2B()

    def turret_move(self):
        self.gt.GetFollowInfo(self.TurretLeft,self.TurretRight)
        while True:
            if self.TurretLeft != 0:
                self.mc.forwardMotor2A(50)
                time.sleep(self.TurretLeft)
                print("turret:turnning left")
            elif self.TurretRight != 0:
                self.mc.reverseMotor2A(50)
                time.sleep(self.TurretRight)
                print("turret:turnning Right")
            else:
                time.sleep(1)
