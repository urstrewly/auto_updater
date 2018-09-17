#include "Mem.h"


extern DWORD client		= NULL;
extern DWORD engine		= NULL;
extern HANDLE hProcess  = NULL;


MemoryManager::MemoryManager()
{

}

MemoryManager::~MemoryManager()
{
	client = NULL;
	engine = NULL;
	hProcess = INVALID_HANDLE_VALUE;
	ProcessId = NULL;
}


bool MemoryManager::MemoryManager::kill(const char* pp)
{

	if (GetProcessByName(pp)) 
		if (TerminateProcess(hProcess, NULL))
			return true;
	
		return false;
}

bool MemoryManager::GetProcessByName(const char * p)
{
	PROCESSENTRY32 entry;
	entry.dwSize = sizeof(PROCESSENTRY32);

	HANDLE snapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, NULL);

	if (snapshot == INVALID_HANDLE_VALUE)
		return false;

	if (Process32First(snapshot, &entry) == TRUE)
	{
		while (Process32Next(snapshot, &entry) == TRUE)
		{

			if (strcmp(entry.szExeFile, p) == 0)
			{
				ProcessId = entry.th32ProcessID;

				if (!ProcessId)
					return false;

				hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, ProcessId);

				if (hProcess == INVALID_HANDLE_VALUE)
					return false;

				CloseHandle(snapshot);
				return true;
			}
		}
	}

	CloseHandle(snapshot);
	return false;
}

