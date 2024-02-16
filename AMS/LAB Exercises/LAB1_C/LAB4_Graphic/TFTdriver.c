/************************************************************
File name: "TFTdriver.c"

Driver for "ITDB02 320 x 240 TFT display module, Version 2"
mounted at "ITDB02 Arduino Mega2560 Shield".
Display controller = ILI 9341.

Max. uC clock frequency = 16 MHz (Tclk = 62,5 ns)

Connections:
DB15-DB8:   PORT A
DB7-DB0:    PORT C

RESETx:     PORT G, bit 0
CSx:        PORT G, bit 1
WRx:        PORT G, bit 2
RS (=D/Cx): PORT D, bit 7

Henning Hargaard
Modified Michael Alrøe
************************************************************/
#include <avr/io.h>

#define F_CPU 16000000
#include <util/delay.h>

#include <avr/cpufunc.h>  // _NOP()
#include "TFTdriver.h"

// Data port definitions:
#define DATA_PORT_HIGH PORTA
#define DATA_PORT_LOW  PORTC

// Control port definitions:
#define WR_PORT PORTG
#define WR_BIT 2
#define DC_PORT PORTD
#define DC_BIT  7  //"DC" signal is at the shield called RS
#define CS_PORT PORTG
#define CS_BIT  1
#define RST_PORT PORTG
#define RST_BIT 0

// Defineable commands
#define TFT_SLEEP_OUT 0x11
#define TFT_DISPLAY_OFF 0x28
#define TFT_DISPLAY_ON 0x29
#define TFT_MEM_ACCESS_CTRL 0x36
#define TFT_PIXEL_FORMAT_SET 0x3a
#define TFT_MEM_WRITE 0x2c
#define TFT_SET_COLUMNS_ADR 0x2a
#define TFT_SET_PAGE_ADR 0x2b



// LOCAL FUNCTIONS /////////////////////////////////////////////////////////////

// ILI 9341 data sheet, page 238
void WriteCommand(unsigned char command)
{
	// Data set up (commands only use the lower byte of the data bus)
	DATA_PORT_LOW = command;
	// DC low
	DC_PORT &= ~(1<<DC_BIT);
	// CS low
	CS_PORT &= ~(1<<CS_BIT);
	// WR low
	WR_PORT &= ~(1<<WR_BIT);
	// twr0 > 15 ns
	_NOP();
	// WR high
	WR_PORT |= (1<<WR_BIT);
	// tcfs > 0
	_NOP();
}

// ILI 9341 data sheet, page 238
void WriteData(unsigned int data)
{
	// Data set up
	DATA_PORT_HIGH = data >> 8;
	DATA_PORT_LOW = data;
	// DC high
	DC_PORT |= (1<<DC_BIT);
	// CS low
	CS_PORT &= ~(1<<CS_BIT);
	// WR low
	WR_PORT &= ~(1<<WR_BIT);
	// twr0 > 15 ns
	_NOP();
	// WR high
	WR_PORT |= (1<<WR_BIT);
	// tcfs > 0
	_NOP();
}
// PUBLIC FUNCTIONS ////////////////////////////////////////////////////////////

// Initializes (resets) the display
void DisplayInit()
{
	// Control pins are outputs
	DDRG |= 0b00000111;
	DDRD |= 0b10000000;
	// Data pins are outputs
	DDRA = 0xFF;
	DDRC = 0xFF;
	// All control pins high;
	PORTG |= 0b00000111;
	PORTD |= 0b10000000;
	// RST low
	RST_PORT &= ~(1<<RST_BIT);
	// Wait 500 ms
	_delay_ms(500);
	// RST high
	RST_PORT |= (1<<RST_BIT);
	_delay_ms(130);
	// Exit sleep mode
	SleepOut();
	// Display on
	DisplayOn();
	// Set bit BGR (scanning direction)
	MemoryAccessControl(0b00001000);
	// 16 bits (2 bytes) per pixel
	InterfacePixelFormat(0b00000101);
}

void DisplayOff()
{
	WriteCommand(TFT_DISPLAY_OFF);
}

void DisplayOn()
{
	WriteCommand(TFT_DISPLAY_ON);
}

void SleepOut()
{
	WriteCommand(TFT_SLEEP_OUT);
}

void MemoryAccessControl(unsigned char parameter)
{
	WriteCommand(TFT_MEM_ACCESS_CTRL);
	WriteData(parameter);
}

void InterfacePixelFormat(unsigned char parameter)
{
	WriteCommand(TFT_PIXEL_FORMAT_SET);
	WriteData(parameter);
}

void MemoryWrite()
{
	WriteCommand(TFT_MEM_WRITE);
}

// Red 0-31, Green 0-63, Blue 0-31
void WritePixel(RGB_t rgb)
{
	//MemoryWrite();
	unsigned int combined_color = (rgb.Red << 11) | (rgb.Green << 5) | rgb.Blue;
	WriteData(combined_color);
}

// Set Column Address (0-239), Start > End
void SetColumnAddress(unsigned int Start, unsigned int End)
{
	WriteCommand(TFT_SET_COLUMNS_ADR);

	WriteData(Start>>8);
	WriteData(Start);
	WriteData(End>>8);
	WriteData(End);
}

// Set Page Address (0-319), Start > End
void SetPageAddress(unsigned int Start, unsigned int End)
{
	WriteCommand(TFT_SET_PAGE_ADR);

	WriteData(Start>>8);
	WriteData(Start);
	WriteData(End>>8);
	WriteData(End);
}

// Fills rectangle with specified color
// (StartX,StartY) = Upper left corner. X horizontal (0-319) , Y vertical (0-239).
// Height (1-240) is vertical. Width (1-320) is horizontal.
// R-G-B = 5-6-5 bits.
void FillRectangle(unsigned int StartX, unsigned int StartY, unsigned int Width, unsigned int Height, unsigned char Red, unsigned char Green, unsigned char Blue)
{
	RGB_t rgb = {Red, Green, Blue};
	SetPageAddress(StartX, StartX + Width);
	SetColumnAddress(StartY, StartY + Height);
	MemoryWrite();
	
	for(int i = StartX; i < StartX + Width; i++)
	{
		for(int i = StartY; i < StartY + Height; i++)
		{
			_delay_us(100);
			WritePixel(rgb);
		}
	}
	
}