
/*--------------------------------------------------------------
  File name: "lcd162.h"

  Driver for "LCD Keypad Shield" alphanumeric display.
  Display controller = HD44780U (LCD-II).
  
  Max. uC clock frequency = 16 MHz (Tclk = 62,5 ns)

  Connection : PORTx (4 bit mode) :
  [LCD]        [Portx]
  RS   ------  PH 5
  RW   ------  GND
  E    ------  PH 6
  DB4  ------  PG 5
  DB5  ------  PE 3
  DB6  ------  PH 3
  DB7  ------  PH 4

  Henning Hargaard
  Modified Michael Alrøe
--------------------------------------------------------------*/
#ifndef LCD167_H_
#define LCD167_H_

//PORT DEFINES
#define E_PULSE_PORT PORTH
#define E_PULSE_PIN	 6

// Defining the used port pin numbers
// (The ports and pins used for the 4 bit data are not definable)
#define CONTROL_PORT PORTH
#define CONTROL_DDR DDRH
#define RS_BIT 5
#define E_BIT  6

//Instruction defines

#define LCD_CLEAR_DISPLAY 0x01
#define LCD_DISPLAY_CURSOR_HOME 0x02
#define LCD_CHARACTER_ENTRY_MODE 0x04
#define LCD_DISPLAY_ON_OFF_CURSOR 0x08
#define LCD_DISPLAY_CURSOR_SHIFT 0x10
#define LCD_FUNCTION_SET 0x20
#define LCD_SET_CGRAM_ADDRESS 0x40
#define LCD_SET_DISPLAY_ADDRESS 0x80

//LCD module signal Mega2560 port pin
//D7 PORT H, bit 4
//D6 PORT H, bit 3
//D5 PORT E, bit 3
//D4 PORT G, bit 5
//E PORT H, bit 6
//RS PORT H, bit 5
//RW Ground (fixed Write)
//Backlight ON/OFF PORT B, bit 4 (=OC2A)

//PORT DEFINES END
#pragma once
void LCDInit();
void LCDClear();
void LCDGotoXY(unsigned char x, unsigned char y);
void LCDDispChar(char ch);
void LCDDispString(char *str);
void LCDDispInteger(int i);
void LCDLoadUDC(unsigned char UDCNo, const unsigned char *UDCTab);
void LCDOnOffControl(unsigned char cursor, unsigned char blink);
void LCDCursorLeft();
void LCDCursorRight();
void LCDShiftLeft();
void LCDShiftRight();
void setBacklight(unsigned char percent);
unsigned char readKeys();
//-------------------------------------------------------------


#endif /* LCD167_H_ */