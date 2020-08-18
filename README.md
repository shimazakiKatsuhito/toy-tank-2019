# toy-tank-2019 ラジコン側プログラム

![サムネイル2](https://user-images.githubusercontent.com/54632092/90399098-6081da00-e0d5-11ea-805a-0aa208311b5a.jpg)
![img_20190819_185839_nakami](https://user-images.githubusercontent.com/54632092/90507816-7ce34c80-e191-11ea-8e22-36c0b01022c5.jpg)

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
  raspberry_piの同一フォルダ内に上記の5ファイルを格納し、
  Python3でtank_server.pyを実行。
  実行コマンド"python3 tankserver.py"
  
### 終了方法
  コンソールにてCtrl + c をタイプ。

