# © 2022 Gakuto Seyama
# SPDX-License-Identifier: BSD-3-Clause

import rclpy                     #ROS2のクライアントのためのライブラリ
from rclpy.node import Node 
from std_msgs.msg import Int16   #通信の型（16ビットの符号付き整数）

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Int16, "countup", 10)
n = 0
def cb():          #17行目で定期実行されるコールバック関数
    global n
    msg = Int16()
    msg.data = n
    pub.publish(msg)
    n += 1

node.create_timer(0.5, cb)
rclpy.spin(node)
