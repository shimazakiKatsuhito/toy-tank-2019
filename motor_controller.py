# coding: utf-8
import sys

# GPIOおよびtimeライブラリをインポート
import RPi.GPIO as GPIO, time

# 使用するピン番号を代入
# MTDのピン番号
# MTD-1A (EN=GPIO12, PH=GPIO25)　キャタピラ　右側 
EN1A = 32
PH1A = 22
# MTD-1B (EN=GPIO18, PH=GPIO17)　キャタピラ　左側
EN1B = 12
PH1B = 11
# MTD-2A (EN=GPIO19, PH=GPIO16)　砲台旋回
EN2A = 35
PH2A = 36
# MTD-2B (EN=GPIO13, PH=GPIO22)　大砲発射
EN2B = 33
PH2B = 15

class MotorController():

    # デューティ比を変化させるステップを定義
    c_step = 10

    def __init__(self):
        # ピン番号の割り当て方式を「コネクタのピン番号」に設定
        GPIO.setmode(GPIO.BOARD)
        
        # 各ピンを出力ピンに設定
        GPIO.setup(EN1A, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(PH1A, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(EN1B, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(PH1B, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(EN2A, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(PH2A, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(EN2B, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(PH2B, GPIO.OUT, initial=GPIO.LOW)

        # PWM オブジェクトのインスタンスを作成
        # 出力ピン：12 番、周波数：100Hz
        self.p1a = GPIO.PWM(EN1A, 100)
        # 出力ピン：18 番、周波数：100Hz
        self.p1b = GPIO.PWM(EN1B, 100)
        # 出力ピン：19 番、周波数：100Hz
        self.p2a = GPIO.PWM(EN2A, 100)
        # 出力ピン：13 番、周波数：100Hz
        self.p2b = GPIO.PWM(EN2B, 100)

        # PWM信号を出力
        self.p1a.start(0)
        self.p1b.start(0)
        self.p2a.start(0)
        self.p2b.start(0)

    #モータを前進方向へ回転する関数
    def forwardMotor1A(self, val):
        self.p1a.ChangeDutyCycle(0)
        GPIO.output(PH1A, GPIO.HIGH)
        self.p1a.ChangeDutyCycle(val)
    def forwardMotor1B(self, val):
        self.p1b.ChangeDutyCycle(0)
        GPIO.output(PH1B, GPIO.HIGH)
        self.p1b.ChangeDutyCycle(val)
    def forwardMotor2A(self, val):
        self.p2a.ChangeDutyCycle(0)
        GPIO.output(PH2A, GPIO.HIGH)
        self.p2a.ChangeDutyCycle(val)
    def forwardMotor2B(self, val):
        self.p2b.ChangeDutyCycle(0)
        GPIO.output(PH2B, GPIO.HIGH)
        self.p2b.ChangeDutyCycle(val)
    #モータを反転方向へ回転する関数
    def reverseMotor1A(self, val):
        self.p1a.ChangeDutyCycle(0)
        GPIO.output(PH1A, GPIO.LOW)
        self.p1a.ChangeDutyCycle(val)
    def reverseMotor1B(self, val):
        self.p1b.ChangeDutyCycle(0)
        GPIO.output(PH1B, GPIO.LOW)
        self.p1b.ChangeDutyCycle(val)
    def reverseMotor2A(self, val):
        self.p2a.ChangeDutyCycle(0)
        GPIO.output(PH2A, GPIO.LOW)
        self.p2a.ChangeDutyCycle(val)
    def reverseMotor2B(self, val):
        self.p2b.ChangeDutyCycle(0)
        GPIO.output(PH2B, GPIO.LOW)
        self.p2b.ChangeDutyCycle(val)
    #モータをブレーキかけて停止する関数
    def breakMotor1A(self):
        self.p1a.ChangeDutyCycle(0)
    def breakMotor1B(self):
        self.p1b.ChangeDutyCycle(0)
    def breakMotor2A(self):
        self.p2a.ChangeDutyCycle(0)
    def breakMotor2B(self):
        self.p2b.ChangeDutyCycle(0)
    def __del__(self):
        # PWM を停止
        self.p1a.stop()
        self.p1b.stop()
        self.p2a.stop()
        self.p2b.stop()

        # GPIO を解放
        GPIO.cleanup()