# toy-tank-2019
A toy tank radio control using raspberry pi.
![サムネイル](https://user-images.githubusercontent.com/54632092/90398486-7ba01a00-e0d4-11ea-9d85-63631d08e69d.jpg)

## 機能概要
  下記のようにラジコン戦車を制御する。
    ・Wifi通信にてコマンドを受け付ける。
    ・キャタピラや砲台のモーターを制御する。
    ・カメラ映像から標的を認識する。

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

