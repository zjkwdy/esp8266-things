import esp8266  # 导入模块
import time
import platform
import psutil as ps
esp=esp8266.esp8266('/dev/ttyUSB0',1000000,5)
p=platform.uname()
system,release=p.system,p.release.split('-')[0]
esp.clearBuffer()
while True:
    text = [
        f'{system} {release}',
        f'CPU:{ps.cpu_percent()/ps.cpu_count()}%'.ljust(20,' '),
        f'MEM:{ps.virtual_memory().percent}%'.ljust(20,' '),
        f'DISK:{ps.disk_usage("/").percent}%'.ljust(20,' ')
    ]
    a=0
    #esp.clearBuffer()
    for i in text:
        a=a+1
        print(i)
        #print(a)
        esp.setCursor(0,a*14)
        esp.writeLine(i)
        #ser.write(bytes.fromhex('0d 0a'))
        time.sleep(0.7)
        

    # if '\n' in text:
    # time.sleep(0.1)
