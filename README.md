# toy-tank-2019
A toy tank radio control using raspberry pi.

機能概要
  下記のようにラジコン戦車を制御する。
    ・Wifi通信にてコマンドを受け付ける。
    ・キャタピラや砲台のモーターを制御する。
    ・カメラ映像から標的を認識する。

動作環境
  ハードウェア
    Raspberry Pi Zero
  OS
    Raspbian Buster Lite (2019/06/20版)

開発環境
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

起動方法
  Python3でtank_server.pyを実行。
  
終了方法
  コンソールにてCtrl + c をタイプ。

