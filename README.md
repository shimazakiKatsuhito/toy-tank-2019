# toy-tank-2019

![サムネイル2](https://user-images.githubusercontent.com/54632092/90399098-6081da00-e0d5-11ea-805a-0aa208311b5a.jpg)

## 機能概要
ラジコン戦車の制御プログラム。下記のような機能を有する。
- Wifi通信 : ホスト側とのコマンド通信を行う。
- モーター制御 : キャタピラや砲台のモーターを制御する。
- 画像処理 : カメラ映像から標的を認識する。

## 装置構成
### マイコン
    Raspberry Pi Zero
### OS
    Raspbian Buster Lite (2019/06/20版)
### カメラ

### モータードライバ

## 使用言語・開発環境
  Python3 with OpenCV3

## 使い方
### デプロイ方法

### 起動方法
  raspberry_piの同一フォルダ内に上記の5ファイルを格納し、
  Python3でtank_server.pyを実行。
  実行コマンド"python3 tankserver.py"
  
### 終了方法
  コンソールにてCtrl + c をタイプ。

