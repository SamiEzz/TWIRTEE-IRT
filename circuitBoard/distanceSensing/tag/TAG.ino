
//libraries
#include <SPI.h>
#include "DW1000Ranging.h"


// connection pins
const uint8_t PIN_RST = 9; // reset pin
const uint8_t PIN_IRQ = 2; // irq pin
const uint8_t PIN_SS = SS; // spi select pin

//declare variables
int tagID;
float tagRange;
float tagPower;


void setup() {
  
  Serial.begin(9600);
  delay(1000);
  DW1000Ranging.initCommunication(PIN_RST, PIN_SS, PIN_IRQ);
  DW1000Ranging.attachNewRange(newRange);
  DW1000Ranging.attachNewDevice(newDevice);
  DW1000Ranging.attachInactiveDevice(inactiveDevice);
  //DW1000Ranging.useRangeFilter(true);
  DW1000Ranging.startAsTag("7D:00:22:EA:82:60:3B:9C", DW1000.MODE_LONGDATA_RANGE_ACCURACY);
  // Wire.begin();
}

void loop() {
  DW1000Ranging.loop();

}

void newRange() {

  tagID = (int) (DW1000Ranging.getDistantDevice()->getShortAddress());
  tagRange = (float) DW1000Ranging.getDistantDevice()->getRange();
  tagPower = (float) DW1000Ranging.getDistantDevice()->getRXPower();
  // Serial.print("FROM: ");Serial.print(tagID);Serial.print("Range: ");Serial.println(tagRange);
  Serial.print("\n");
  Serial.print(tagID);Serial.print(",");Serial.print(tagRange);
}

void newDevice(DW1000Device* device) {
  //Serial.print("\nAnchorID,");
  //Serial.print((int) (DW1000Ranging.getDistantDevice()->getShortAddress()));

}

void inactiveDevice(DW1000Device* device) { }

