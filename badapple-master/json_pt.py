import json
import sys
import serial  # 导入模块
import time

# 端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
portx = "/dev/ttyUSB0"
# 波特率，标准值之一：50 75 110 134 150 200 300 600 1200 1800 2400 4800 9600 19200 38400 57600 115200
bps = 1000000
# 超时设置 None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
timex = None
# 打开串口，并得到串口对象
ser = serial.Serial(portx, bps, timeout=timex)

dirs=sys.argv[1]
with open(dirs,'rb+') as fp:
    frames=json.load(fp)
    while True:
        try:
            for data in frames:
                #发三遍
                for i in range(2):
                    ser.write(bytes.fromhex(frames[data]))
                time.sleep(0.0215)
        except Exception as e:
            print(e)
