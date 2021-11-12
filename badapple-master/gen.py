import os
from posixpath import dirname
import sys
import serial  # 导入模块
import json
from PIL import Image
frame = {}
dirs = sys.argv[1]
ls_dir = os.listdir(dirs)
ls_dir.sort()

try:
    for n in ls_dir:
        path = dirs+'/'+n
        print(path)
        im = Image.open(path)
        w, h = im.width, im.height
        p = []  # 一帧画面的变量
        for hi in range(h):
            hm = []
            for hw in range(w):
                ri = im.convert('RGB')
                r, g, b = ri.getpixel((hw, hi))
                # 白
                if(r >= 100 or g >= 100 or b >= 100):
                    hm.append('1')
                else:
                    # 黑
                    hm.append('0')
                # 八个一组
                if (hw+1) % 8 == 0:
                    p.append(hm)
                    hm = []
                if hw == w-1:
                    hw = 0
        # 数据帧起始
        data = 'AA 55 '
        for h in p:
            # 大端排列
            h.reverse()
            a = hex(int(''.join(h), 2)).split('0x')[-1]
            if len(a) == 1:
                # 不够用0补齐
                data = data+'0'+a+' '
            else:
                data = data+a+' '
            # line=''.join(h)
        frame[n] = data
    with open(dirs+'.json', 'w+') as fp:
        json.dump(frame, fp)
except Exception as e:
    print(e)
