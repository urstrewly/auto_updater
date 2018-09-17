#include <iostream>
#include "Mem.h"

int main()
{
	MemoryManager* mem = new MemoryManager;


	if (!mem->kill("alpha.exe"))
		return -1;

	
}