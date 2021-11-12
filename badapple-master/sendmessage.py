import esp8266  # 导入模块
import time
esp=esp8266.esp8266('/dev/ttyUSB0',1000000)
while True:
    text = input('>>>').split(r'\n')
    #time.sleep(0.05)
    dataS = 'AA 22'
    a=0
    for i in text:
        a=a+1
        #print(a)
        if a==1:
            esp.clearBuffer()
        esp.setCursor(0,a*15)
        esp.writeLine(i)
        #ser.write(bytes.fromhex('0d 0a'))
        time.sleep(1)
        

    # if '\n' in text:
    # time.sleep(0.1)
