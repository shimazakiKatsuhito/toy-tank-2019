# 的を見つけて、砲台を旋回させる
import threading
import time
import getTargetLib
# from motor_controller import MotorController

class getTargetThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.TurretFollow = False
        self.num = 0
        self.getTarget = getTargetLib.getTargetPosition()
        # self.mc = MotorController()

        # カメラの準備
        print ("initialize ...")
        self.getTarget.initialize()

        # 標的の方向（モーターの旋回時間）
        self.TargetRight = 0
        self.TargetLeft = 0

    # 追尾開始(スレッド起動)
    def run(self):
        print ("start getTarget Thread ...")
        try:
            while True:
                if self.TurretFollow:
                    # 的検出
                    self.circle = self.getTarget.getTargetPos()

                    if self.circle is not None:
                        print('X:%d Y:%d R:%d' % (self.circle[0],self.circle[1],self.circle[2]))
                        if (self.circle[0] - 640) < -50:
                            # 左に標的あり
                            self.TargetLeft = (-1) * (self.circle[0] - 640) / 120
                            print("target is in left side")
                            # self.mc.forwardMotor2A(50)
                        elif (self.circle[0] - 640) > 50:
                            # 右に標的あり
                            self.TargetRight = (self.circle[0] - 640) / 120
                            print("target is in right side")
                            # self.mc.reverseMotor2A(50)
                        else:
                            self.TargetRight = 0
                            self.TargetLeft = 0
                            print("target is in front")
                            # self.mc.breakMotor2A()

                    print ('%d' % (self.num))
                    self.num+=1

                else:
                    self.TargetRight = 0
                    self.TargetLeft = 0
                    
            time.sleep(1)
            #MotorController.breakMotor2A()
        except  KeyboardInterrupt:
            print ("KeyboardInterrupt! stopped getTarget Thread ...")

    # 追尾開始
    def FollowStart(self):
        print ("start Detect Target ...")
        self.TurretFollow = True

    # 追尾停止
    def FollowStop(self):
        print ("Stop Detect Target ...")
        self.TurretFollow = False

    # 自動追尾方向情報取得
    def GetFollowInfo(self, left, right ):
        right = self.TargetRight
        left = self.TargetLeft