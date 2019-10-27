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
                        # 1280×720画素の画像にて基準(中心？)から右か左かで
                        # 砲台の旋回方向と旋回時間を決定する
                        # 現状はカメラが上下逆転してセットされているので、
                        # 左上原点の画像と現実は左右逆と考える。
                        if (self.circle[0] - 640) < -50:
                            # 左に標的あり
                            self.TargetRight = abs(((self.circle[0] - 640) / 120) * 0.5)
                            time.sleep(self.TargetRight)
                            print('target Right %d sec' %(self.TargetRight))
                        elif (self.circle[0] - 640) > 50:
                            # 右に標的あり
                            self.TargetLeft = abs(((self.circle[0] - 640) / 120) * 0.5)
                            time.sleep(self.TargetLeft)
                            print('target Left %d sec' %(self.TargetLeft))
                        else:
                            # 正面に標的あり
                            self.TargetRight = 0
                            self.TargetLeft = 0
                            print("target is in front")
                    else:
                        # 標的情報初期化
                        self.TargetRight = 0
                        self.TargetLeft = 0

                    print ('%d' % (self.num))
                    self.num+=1

                else:
                    self.TargetRight = 0
                    self.TargetLeft = 0
                    
                time.sleep(0.5)
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

    # 砲台の左旋回方向情報取得
    def GetInfoTurretTurnLeft(self):
        return self.TargetLeft

    # 砲台の右旋回方向情報取得
    def GetInfoTurretTurnRight(self):
        return self.TargetRight
