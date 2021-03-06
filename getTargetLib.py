# OpenCV のインポート
# apt-get installでpython-opencv, python3-opencv,libopencv-dev
# をインストールしておくこと。
# python3-opencvが無いと、python3で動かしたときにcv2がインポートできない。
import cv2
import numpy as np
import time

class getTargetPosition:
  cap = None
  numnum = 0

  # 的検出の感度パラメータ
  minDist = 75    # 近接する円をリジェクト
  param1  = 100   # エッジ感度：大きいほうが高感度
  param2  = 20    # 円感度：小さいほうが好感度だが、誤検出増える

  # Debug用画像出力
  DebugImageOutputFlag=1  # 0:出力しない 1:出力する

  def initialize(self):
    # VideoCaptureのインスタンスを作成する。
    # 引数でカメラを選べれる。
    self.cap = cv2.VideoCapture(0)
    if True != self.cap.isOpened():
      print ("Camera Initializing Failure")
    return

  def __del__(self):
    # VideoCaptureのインスタンスを解放する。
    self.cap.release()

  def adjust(self, img, alpha = 1.0, beta = 0.0):
      dst = alpha * img + beta
      return np.clip(dst, 0, 255).astype(np.uint8)

  def getTargetPos(self):
    # 時間計測開始
    start = time.time()
    print('getTargetLib:logtime1 start')    
    # バッファにたまっているものを読み飛ばす
    for i in range(1,2):
      ret, img = self.cap.read()
    
    # time1 = time.time() - start
    # print('logtime1 %1.2f sec' %(time1))    
    
    # VideoCaptureから1フレーム読み込む
    ret = False
    cnt = 0
    while ret != True:
      ret, img = self.cap.read()
      cnt += 1
      if cnt > 10:
        ret = True
        print("Image Reading Failure")

    # time2 = time.time() - start
    # print('logtime2 %1.2f sec' %(time2))    

    # 画像の前処理
    # リサイズ
    orgHeight, orgWidth = img.shape[:2]
    size = (int(orgWidth / 4), int(orgHeight / 4))
    img = cv2.resize(img,size)
    img = self.adjust(img, alpha = 2.0, beta = 30.0)
    # 特定の色を抜く。
    # カットアンドトライだが、Gを抜くと白地に黒の円が、関係のないところを誤認識することなく、うまく検出できた
    # img[:,:,0] = 0  # Bの色を抜く
    img[:,:,1] = 0  # Gの色を抜く
    # img[:,:,2] = 0  # Rの色を抜く
    #  グレー化(R成分のみ出力)
    imgray1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #  ぼかし
    imgray = cv2.medianBlur(imgray1,5)
    # エッジング
    imedge = cv2.Canny(imgray,100,400)

    # time3 = time.time() - start
    # print('logtime3 %1.2f sec' %(time3))    

    # 的のサークル検出
    # circles = cv2.HoughCircles(imgray, cv2.cv.CV_HOUGH_GRADIENT, 1, 
    #              self.minDist, self.param1, self.param2, minRadius=10, maxRadius=200)
    circles = cv2.HoughCircles(imedge, cv2.HOUGH_GRADIENT, 2, 
                  self.minDist, self.param1, self.param2, minRadius=5, maxRadius=200)
    # cv2.cv.CV_HOUGH_GRADIENT->cv2.HOUGH_GRADIENT
    # Python2->Python3 / CV2.x->CV3.xで定義が変わることがあるので注意！
    time4 = time.time() - start
    print('getTargetLib:logtime4 %1.2f sec' %(time4))    

    if circles is not None:
       circles = np.uint16(np.around(circles))

       if self.DebugImageOutputFlag==1:
         for i in circles[0,:]:
            print ('{0}' .format(str(i[0])+","+str(i[1])+","+str(i[2])))
            # draw the outer circle
            cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

         # 加工済の画像を保存
         cv2.imwrite('DetectCircles'+str(self.numnum)+'.jpg', img)
         # cv2.imwrite('DetectCircles'+str(self.numnum)+'_gray.jpg', imgray1)
         # cv2.imwrite('DetectCircles'+str(self.numnum)+'_medi.jpg', imgray)
         # cv2.imwrite('DetectCircles'+str(self.numnum)+'_edge.jpg', imedge)

       self.numnum+=1
       return circles[0][0]

    # cv2.imwrite('DetectCircles'+str(self.numnum)+'.jpg', img)
    # cv2.imwrite('DetectCircles'+str(self.numnum)+'_gray.jpg', imgray1)
    # cv2.imwrite('DetectCircles'+str(self.numnum)+'_medi.jpg', imgray)
    # cv2.imwrite('DetectCircles'+str(self.numnum)+'_edge.jpg', imedge)

    return None
