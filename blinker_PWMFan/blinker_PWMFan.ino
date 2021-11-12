#define BLINKER_WIFI
#define BLINKER_WITHOUT_SSL
#include <Blinker.h>

#define BUTTON_POWER "button_power"
#define SLIDER_RANGE "ranger_fan"
#define FAN_PC "fan_pc"
const int ControlPin = 12;
BlinkerButton PowerButton(BUTTON_POWER);
BlinkerSlider FanRanger(SLIDER_RANGE);
BlinkerNumber FanPC(FAN_PC);
int Havepercent=0;
int percent=0;
void setup() {
  Serial.begin(115200);
  BLINKER_DEBUG.stream(Serial);
  BLINKER_DEBUG.debugAll();
  setPWM(0);
  // put your setup code here, to run once:
  Blinker.begin("authKey","WiFiName","WiFiPass");
  analogWriteFreq(25000);
  Blinker.attachHeartbeat(heartbeat);
  PowerButton.attach(changeONOFF);
  FanRanger.attach(sliderControl);
  FanRanger.print(percent);
  FanPC.print(percent);
}

void heartbeat()
{
  FanPC.print(percent);
}
void setPWM(int Npercent)
{
  analogWrite(ControlPin,(int)(0+(Npercent*2.55)));
  percent=Npercent;
  Havepercent=!Havepercent;
  FanPC.print(percent);
}
void loop() {
  Blinker.run();
}
void changeONOFF(const String & state)
{
  setPWM((!Havepercent)*100);
  if(Havepercent==0){
    PowerButton.print("off");
  }else{
    PowerButton.print("on");
  }
}
void sliderControl(int32_t value)
{
  setPWM(value);
  FanRanger.print(percent);
}
