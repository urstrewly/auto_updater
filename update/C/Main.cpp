#include <iostream>
#include "Mem.h"

MemoryManager* Process = new MemoryManager;

int main()
{
	


	if (!Process->kill("alpha.exe"))
		return -1;

	
}
