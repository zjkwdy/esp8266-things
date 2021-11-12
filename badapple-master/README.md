# badapple
摸索着写出来的上位机程序,给自己无聊的初三生活找一点乐趣。

需要一个esp8266(nodemcu)和一个i2c屏幕

（含 flyAkari 大佬写的下位机代码（badapple文件夹）。）

### useage:

##### 即时处理（不推荐，占用大，帧率低）

```bash
python3 main.py {ba|bilibili}
```

##### 先处理，再播放（推荐，速度快，帧率高）

###### 图片处理成json:

```bash
python3 gen.py {ba|bilibili|asus|soviet}
```

###### 播放json文件：

```bash
python3 json_pt.py {JSONFILE_NAME}
```

#### 附：本人自用的CH34x Linux驱动(CH34x.zip)，如有需要可自行编译。

```bash
cd CH34x && sudo make && sudo make load
```

