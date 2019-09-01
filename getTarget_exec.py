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

    # 追尾開始(スレッド起動)
    def run(self):
        print ("start getTarget Thread ...")
        try:
            while True:
                if self.TurretFollow:
                    # 的検出
                    self.circle = self.getTarget.getTargetPos()

                    if self.circle is not None:
                        #print 'X:'+str(circle[0])+' Y:'+str(circle[1])+' r:'+str(circle[2])
                        print('X:%d Y:%d R:%d' % (self.circle[0],self.circle[1],self.circle[2]))
                        # if (640 - self.circle[0]) > 50:
                            # self.mc.forwardMotor2A(50)
                        # elif (640 - self.circle[0]) < -50:
                            # self.mc.reverseMotor2A(50)
                        # else:
                            # self.mc.breakMotor2A()

                    print ('%d' % (self.num))
                    self.num+=1

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