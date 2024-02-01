#define F_CPU 16000000
#include <util/delay.h>
#include <avr/io.h>

int main()
{
	DDRA = 0;
	DDRB = 0xFF;
	while (1)
	{
		if ((PINA & 0b10000000) == 0){
		int i = 0;
		
		}

		if (PINA != 0xFF)
		PORTB = ~PINB;
	}
}