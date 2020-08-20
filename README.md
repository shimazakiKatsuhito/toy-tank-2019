# toy-tank-2019 ラジコン戦車制御プログラム
自動で的に照準を合わせたり、音声で動いたりするラジコン戦車です。<br>  既存のおもちゃを改造しました。<br>  次のようなことができます。まだ未完成の部分もありますが…(^-^;
- 移動　　：前進／後退／右旋回／左旋回／停止します。
- 自動追尾：標的を見つけて砲台の照準を合わせます（未完）
- 砲弾発射：BB弾を発射します。

![サムネイル2](https://user-images.githubusercontent.com/54632092/90399098-6081da00-e0d5-11ea-805a-0aa208311b5a.jpg)
![img_20190819_185839_nakami_2](https://user-images.githubusercontent.com/54632092/90508719-2e36b200-e193-11ea-9100-7753fa51c446.jpg)

## 機能概要
ラジコン戦車の制御プログラム。下記のような機能を有する。
- Wifi通信 : ホスト側とのコマンド通信を行う。
- モーター制御 : キャタピラや砲台のモーターを制御する。
- 画像処理 : カメラ映像から標的を認識する。

## 装置構成
### 筐体(戦車本体)
バトルタンク－陸上自衛隊74式戦車
### マイコン
Raspberry Pi Zero
### MEM
MicroSD 32GB
### OS
Raspbian Buster Lite (2019/06/20版)
### カメラ
usbカメラ
### モータードライバ
デュアルモータードライバDRV8835 × 2個

## ソース(ラジコン戦車制御アプリ)
### プログラミング言語
Python3
### ライブラリ
OpenCV3

## 使い方
### デプロイ方法

### 起動方法
raspberry_piの同一フォルダ内に下記のファイルを格納し、コマンドを実行。
- getTarget_exec.py
- getTargetLib.py
- motor_controller.py
- tank_controller.py
- tank_server.py
    
実行コマンド  ```python3 tankserver.py```
  
### 終了方法
  コンソールにてCtrl + c をタイプ。

