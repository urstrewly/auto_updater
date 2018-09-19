#ifndef _MEMORY_GUARD_ // !_MEMORY_GUARD_
#define _MEMORY_GUARD_
#include "includes.h"


class MemoryManager
{
public:
	MemoryManager();
	~MemoryManager();

	bool	 kill(const char*);

private:
	bool	 GetProcessByName(const char*);

	int ProcessId;
};

extern HANDLE	hProcess;

extern MemoryManager* Process;

#endif  // !_MEMORY_GUARD_
