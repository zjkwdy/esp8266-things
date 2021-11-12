import serial  # 导入模块


class esp8266:
    portx=''
    bps=0
    timex=None
    tryR=3
    def __init__(self,portx:str,bps:int,tryR=3):
        # 端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
        # 波特率，标准值之一：50 75 110 134 150 200 300 600 1200 1800 2400 4800 9600 19200 38400 57600 115200
        # 超时设置 None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
        timex = None
        self.portx=portx
        self.bps=bps
        self.timex=None
        self.tryR=tryR
        self.ser = serial.Serial(self.portx, self.bps, timeout=self.timex)
        # 打开串口，并得到串口对象
    def getserial(self):
        return self.ser
    def setCursor(self,cursorX,cursorY):
        ser=self.ser
        message=f'AA 4D {hex(cursorX).split("0x")[-1].rjust(2,"0")} {hex(cursorY).split("0x")[-1].rjust(2,"0")} 00'
        #print(message)
        for i in range(self.tryR):
            ser.write(bytes.fromhex(message))
    def clearBuffer(self):
        ser=self.ser
        message='AA 4A'
        for i in range(self.tryR):
            ser.write(bytes.fromhex(message))
    def writeLine(self,message:str):
        ser=self.ser
        dataS = 'AA 22'
        ser.write(bytes.fromhex(dataS)+message.encode('utf-8'))
        #ser.write()