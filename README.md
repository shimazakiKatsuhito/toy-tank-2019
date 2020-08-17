# toy-tank-2019

![サムネイル2](https://user-images.githubusercontent.com/54632092/90399098-6081da00-e0d5-11ea-805a-0aa208311b5a.jpg)

## 機能概要
  ラジコン戦車の制御プログラム。下記のような機能を有する。
    - Wifi通信<br>  ホスト側とのコマンド通信を行う。
    - モーター制御：キャタピラや砲台のモーターを制御する。
    - 画像処理：カメラ映像から標的を認識する。

## ハードウェア
    Raspberry Pi Zero
### OS
    Raspbian Buster Lite (2019/06/20版)

## 使用言語・開発環境
  Python3 with OpenCV3

構成
  getTarget_exec.py
    getTargetLib.pyを利用して目標の自動追尾を実行。
  getTargetLib.py
    目標を認識するための画像処理を実行。
  motor_controller.py
    正転・逆転・停止などモーター制御を実行
  tank_controller.py
    受信コマンドに応じて処理を実行
  tank_server.py
    Wifi接続によるコマンド通信を実行。

## 使い方
### デプロイ方法

### 起動方法
  raspberry_piの同一フォルダ内に上記の5ファイルを格納し、
  Python3でtank_server.pyを実行。
  実行コマンド"python3 tankserver.py"
  
### 終了方法
  コンソールにてCtrl + c をタイプ。

