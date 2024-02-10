/*-------------------------------------------------------------------
  File name: "lcd162.c"

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
---------------------------------------------------------------------*/
#include <avr/io.h>

#define F_CPU 16000000
#include <util/delay.h>

#include <avr/cpufunc.h>  // Enabling macro _NOP() to insert the NOP instruction
#include <stdlib.h>  // Enabling itoa()

#include "lcd162.h"

//*********************** PRIVATE (static) operations *********************

static void waitBusy(unsigned char instruction)
{
    // "Clear display" and "Return Home" executes 1,52 ms
    if (instruction < 4)
    _delay_ms(2);
    // - all other instructions executes 37 us
    else
    _delay_us(50);
}  

static void pulse_E()
{
	
	E_PULSE_PORT |= (1 << E_PULSE_PIN);
	
	for (int i = 0; i <= 4; i++)
	{
		_NOP();
	}
	
	E_PULSE_PORT &= ~(1 << E_PULSE_PIN);
}

// Sets the display data pins according to the 4 lower bits of data
static void set4DataPins(unsigned char data)
{
  PORTH = (PORTH & 0b11100111) | ((data<<1) & 0b00011000);
  PORTE = (PORTE & 0b11110111) | ((data<<2) & 0b00001000);
  PORTG = (PORTG & 0b11011111) | ((data<<5) & 0b00100000);  
}

static void sendInstruction(unsigned char instruction)
{      	
    // Write high nibble ::
    // RS = 0, E = 0, DB7-DB4 = Data high nibble
    CONTROL_PORT &= ~((1<<RS_BIT) | (1<<E_BIT));
    set4DataPins(instruction>>4);
    // Generate E pulse
    pulse_E();
    // Write low nibble ::
    // RS = 0, E = 0, DB7-DB4 = Data low nibble
    set4DataPins(instruction);
    // Generate E pulse
    pulse_E();
    // Wait for instruction executed
    waitBusy(instruction);
}

static void sendData(unsigned char data)
{      
    // Write high nibble ::
    // RS = 1, E = 0, DB7-DB4 = Data high nibble
    CONTROL_PORT |= (1<<RS_BIT);
    CONTROL_PORT &= ~(1<<E_BIT);
    set4DataPins(data>>4);
    // Generate E pulse
    pulse_E();
    // Write low nibble ::
    // RS = 1, E = 0, DB7-DB4 = Data low nibble
    set4DataPins(data);
    // Generate E pulse
    pulse_E();
    // Wait > 37 us
    _delay_us(50);
}

//*********************** PUBLIC functions *****************************
// Initializes the display, blanks it and sets "current display position"
// at the upper line, leftmost character (cursor invisible)
// Reference: Page 46 in the HD44780 data sheet
void LCDInit()
{
  // Initializing the used port
  DDRH |= 0b01111000;  // Outputs
  DDRE |= 0b00001000;
  DDRG |= 0b00100000;
  
  // Wait 50 ms (min. 15 ms demanded according to the data sheet)
  _delay_ms(50);
  // Function set (still 8 bit interface)
  PORTG |= 0b00100000;
  PORTE |= 0b00001000;
  pulse_E();
  
  // Wait 10 ms (min. 4,1 ms demanded according to the data sheet)
  _delay_ms(10);
  // Function set (still 8 bit interface)
  pulse_E();

  // Wait 10 ms (min. 100 us demanded according to the data sheet)
  _delay_ms(10);
  // Function set (still 8 bit interface)
  pulse_E();

  // Wait 10 ms (min. 100 us demanded according to the data sheet)
  _delay_ms(10);
  // Function set (now selecting 4 bit interface !)
  PORTG &= 0b11011111;
  pulse_E();

  // Function Set : 4 bit interface, 2 line display, 5x8 dots
  sendInstruction( 0b00101000 );
  // Display, cursor and blinking OFF
  sendInstruction( 0b00001000 );
  // Clear display and set DDRAM adr = 0	
  sendInstruction( 0b00000001 );
  // By display writes : Increment cursor / no shift
  sendInstruction( 0b00000110 );
  // Display ON, cursor and blinking OFF
  sendInstruction( 0b00001100 );
}

// Blanks the display and sets "current display position" to
// the upper line, leftmost character
void LCDClear()
{
  sendInstruction(LCD_CLEAR_DISPLAY);
  sendInstruction(LCD_DISPLAY_CURSOR_HOME);
  sendInstruction(0x0D);
}

// Sets DDRAM address to character position x and line number y
void LCDGotoXY( unsigned char x, unsigned char y )
{
  // To be implemented
}

// Display "ch" at "current display position"
void LCDDispChar(char ch)
{
	sendData(ch);
}

// Displays the string "str" starting at "current display position"
void LCDDispString(char* str)
{
  // To be implemented
}

// Displays the value of integer "i" at "current display position"
void LCDDispInteger(int i)
{
	 sendData(i+'0');
}

// Loads one of the 8 user definable characters (UDC) with a dot-pattern,
// pre-defined in an 8 byte array in FLASH memory
void LCDLoadUDC(unsigned char UDCNo, const unsigned char *UDCTab)
{
  // To be implemented		
}

// Selects, if the cursor has to be visible, and if the character at
// the cursor position has to blink.
// "cursor" not 0 => visible cursor.
// "blink" not 0 => the character at the cursor position blinks.
void LCDOnOffControl(unsigned char cursor, unsigned char blink)
{
  // To be implemented
}

// Moves the cursor to the left
void LCDCursorLeft()
{
  // To be implemented
}

// Moves the cursor to the right
void LCDCursorRight()
{
  // To be implemented
}

// Moves the display text one position to the left
void LCDShiftLeft()
{
  // To be implemented
}

// Moves the display text one position to the right
void LCDShiftRight()
{
  // To be implemented
}

// Sets the backlight intensity to "percent" (0-100)
void setBacklight(unsigned char percent)
{
  // To be implemented
}

// Reads the status for the 5 on board keys
// Returns 0, if no key pressed
unsigned char readKeys()
{
  // To be implemented
}