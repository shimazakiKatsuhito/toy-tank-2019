# -*- coding:utf-8 -*-
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from tank_controller import TankController

# 参考
# https://www.e-tinkers.com/2018/04/how-to-control-raspberry-pi-gpio-via-http-web-server/
# 追記（嶋）
# 当ファイルを実行時は'python3 tank_server.py'で実行しましょう！
# 'python tank_server.py'とするとpython2で動くので実行できません。

host_name = ''
host_port = 8000

class TankServer(HTTPServer):
   def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.tc = TankController()
        # getTargetスレッド起動
        self.tc.gt.start()
        print ("finish initialize TankServer...")

class TankServerHandler(BaseHTTPRequestHandler):
    """ タンクコントロールサーバー """

    def do_HEAD(self):
        """ do_HEAD() can be tested use curl command 
            'curl -I http://server-ip-address:port' 
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        """ 基本的に全部GETでいける """
        html_all = '''
            <html>
            <body style="width:960px; margin: 20px auto;">
            <div>tank:
            <a href="/tank/go_forward">go</a> 
            <a href="/tank/go_backward">back</a> 
            <a href="/tank/stop">stop</a> 
            <a href="/tank/turn_left">left</a> 
            <a href="/tank/turn_right">right</a>
            <hr />
            <div>turret:
            <a href="/turret/follow">follow</a>
            <a href="/turret/unfollow">unfollow</a>
            <a href="/turret/shoot">shoot</a>
            </div>
            <hr />
            <div id="status"></div>
            <script>
              document.getElementById("status").innerHTML="{}";
            </script>
            </body>
            </html>
        '''

        reqs = (self.path.split("/"))[1:]
        # print(reqs)

        if reqs[0] == 'tank':
            status= "tank: {}".format(reqs[1])
            if reqs[1] == 'go_forward':
                self.server.tc.tank_go_forward()
            elif reqs[1] == 'stop':
                self.server.tc.tank_stop()
            elif reqs[1] == 'turn_left':
                self.server.tc.tank_turn_left()
            elif reqs[1] == 'turn_right':
                self.server.tc.tank_turn_right()
            elif reqs[1] == 'go_backward':
                self.server.tc.tank_go_backward()
            else: # elseのときはstopにする
                status= "tank: {} => stop".format(reqs[1])
                self.server.tc.tank_stop()
        elif reqs[0] == 'turret':
            status= "turrel: {}".format(reqs[1])
            if reqs[1] == 'follow':
                self.server.tc.turret_follow()
            elif reqs[1] == 'unfollow':
                self.server.tc.turret_unfollow()
            elif reqs[1] == 'shoot':
                self.server.tc.turret_shoot()
            else: # elseのときはunfollowにする
                status= "tank: {} => stop".format(reqs[1])
                self.server.tc.turret_unfollow()
        else:
            status='error'
        self.do_HEAD()
        self.wfile.write(html_all.format(status).encode("utf-8"))

#
# main
#
if __name__ == '__main__':
    tank_server = TankServer((host_name, host_port), TankServerHandler)
    try:
        tank_server.serve_forever()
    except KeyboardInterrupt:
        # getTargetスレッドが終了するまで待つ
        tank_server.tc.gt.join()
        tank_server.server_close()
