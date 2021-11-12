import os
import sys
import serial  # 导入模块
from PIL import Image
frame = {}
# 端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
portx = "/dev/ttyUSB0"
# 波特率，标准值之一：50 75 110 134 150 200 300 600 1200 1800 2400 4800 9600 19200 38400 57600 115200
bps = 1000000
# 超时设置 None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
timex = None
# 打开串口，并得到串口对象
ser = serial.Serial(portx, bps, timeout=timex)

dirs=sys.argv[1]
ls_dir = os.listdir(dirs)
ls_dir.sort()
while True:
    try:
        for n in ls_dir:
            path = dirs+'/'+n
            print(path)
            im = Image.open(path)
            w, h = im.width, im.height
            p = []#一帧画面的变量
            for hi in range(h):
                hm=[]
                for hw in range(w):
                    ri = im.convert('RGB')
                    r, g, b = ri.getpixel((hw, hi))
                    #白
                    if(r >= 100 or g >=100 or b >=100):
                        hm.append('1')
                    else:
                    #黑
                        hm.append('0')
                    #八个一组
                    if (hw+1) % 8==0:
                        p.append(hm)
                        hm=[]
                    if hw == w-1:
                        hw = 0
            #数据帧起始
            data='AA 55 '
            for h in p:
                #大端排列
                h.reverse()
                a=hex(int(''.join(h),2)).split('0x')[-1]
                if len(a)==1:
                    #不够用0补齐
                    data= data+'0'+a+' '
                else:
                    data= data+a+' '
                #line=''.join(h)
            #发三遍
            ser.write(bytes.fromhex(data))
    except Exception as e:
        print(e)
