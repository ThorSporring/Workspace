/*
 * LAB3_Alphanumeric_display.c
 *
 * Created: 07-02-2024 13:28:20
 * Author : spott
 */ 
#define F_CPU 16000000
#include <avr/io.h>
#include "lcd162.h"
#include <util/delay.h>

int main(void)
{
    /* Replace with your application code */
	LCDInit();
	LCDClear();
    while (1) 
    {
		LCDDispChar('A');
		LCDDispInteger(12);
		_delay_ms(1000);
		
    }
}

