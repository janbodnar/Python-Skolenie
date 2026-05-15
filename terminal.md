# Classic Windows Command Line Tools – Progressive Guide

This guide covers essential legacy command-line tools available in the Windows Command Prompt (`cmd.exe`).  
Each tool is introduced with a basic example, then followed by more advanced usage and real‑world scenarios.

---

## 1. Getting Started – Navigating & Viewing Files

### `dir` – List directory contents
**Basic** – show files in current folder  
```cmd
dir
```
**Progressive** – show only directories, wide format, including hidden/system files  
```cmd
dir /A:D /W
dir /A:H /S   (find hidden files in all subfolders)
```

### `cd` – Change directory
**Basic** – go to `C:\Windows`  
```cmd
cd C:\Windows
```
**Progressive** – go up two levels, then down to `Users\Public`  
```cmd
cd ..\..\Users\Public
```

### `cls` – Clear the screen
```cmd
cls
```

---

## 2. Working with Files – Copy, Move, Delete

### `copy` – Simple file copy
**Basic** – copy one file to another location  
```cmd
copy report.txt D:\Backup\
```
**Progressive** – concatenate multiple text files into one  
```cmd
copy file1.txt + file2.txt combined.txt
```

### `xcopy` – Advanced copy (folders, attributes, timestamps)
**Basic** – copy all files and subfolders (`/E`), preserving read‑only attribute (`/K`)  
```cmd
xcopy C:\Data D:\DataBackup /E /K
```
**Progressive** – copy only files modified after a certain date, with verification  
```cmd
xcopy "C:\Users\Public\*.docx" D:\Archive /D:01-01-2025 /V
```

### `move` – Move or rename
**Basic** – move `old.txt` into `Archive\`  
```cmd
move old.txt Archive\
```
**Progressive** – rename a folder (both source and destination paths can be directories)  
```cmd
move "Project X" "Project_X_2025"
```

### `del` – Delete files
**Basic** – delete all `.tmp` files quietly  
```cmd
del *.tmp /Q
```
**Progressive** – delete files recursively, prompting for each one  
```cmd
del /S /P *.log
```

### `mkdir` & `rmdir` – Create / remove directories
**Basic** – create `Backup` inside `Logs`  
```cmd
mkdir Logs\Backup
```
**Basic** – remove empty folder  
```cmd
rmdir OldEmptyFolder
```
**Progressive** – remove a non‑empty folder and all its contents (`/S`), without confirmation (`/Q`)  
```cmd
rmdir /S /Q TempData
```

---

## 3. Viewing & Searching File Content

### `type` – Display text file
**Basic** – show `readme.txt`  
```cmd
type readme.txt
```
**Progressive** – use with `more` to paginate long files  
```cmd
type longfile.txt | more
```

### `find` – Search for a string
**Basic** – find lines containing “Error” in `app.log`  
```cmd
find "Error" app.log
```
**Progressive** – search case‑insensitively (`/I`) and display line numbers (`/N`) across multiple files  
```cmd
find /I /N "warning" *.log
```

### `fc` – Compare two files
**Basic** – ASCII comparison  
```cmd
fc old_config.ini new_config.ini
```
**Progressive** – binary comparison (`/B`) for non‑text files  
```cmd
fc /B image1.jpg image2.jpg
```

---

## 4. Disk & File System Management

### `attrib` – View or change file attributes
**Basic** – make a file hidden and read‑only  
```cmd
attrib +h +r secret.txt
```
**Progressive** – recursively remove the “system” attribute from all files in a folder  
```cmd
attrib -s C:\Windows\Temp\*.* /S
```

### `chkdsk` – Check disk for errors
**Basic** – check drive C: (read‑only)  
```cmd
chkdsk C:
```
**Progressive** – fix errors (`/F`), locate bad sectors (`/R`), and force dismount if needed (`/X`)  
```cmd
chkdsk C: /F /R /X
```
> **Note**: `/R` implies `/F`. The drive may need to be dismounted – answer `Y` to run at next reboot.

### `sfc` – System File Checker
**Basic** – verify and repair protected system files  
```cmd
sfc /scannow
```
**Progressive** – verify only (no repair) and write logs to a custom path  
```cmd
sfc /verifyonly
sfc /scanfile=C:\Windows\System32\kernel32.dll
```

---

## 5. Networking Tools – From Ping to Route Tracing

### `ipconfig` – IP configuration
**Basic** – show all adapters’ IP, subnet mask, default gateway  
```cmd
ipconfig /all
```
**Progressive** – release and renew DHCP lease, then flush DNS cache  
```cmd
ipconfig /release
ipconfig /renew
ipconfig /flushdns
```

### `ping` – Test connectivity
**Basic** – send 4 ICMP packets to `google.com`  
```cmd
ping google.com
```
**Progressive** – ping continuously (`-t`), with 1500 byte packets (`-l`), stop after 10 pings  
```cmd
ping -t -l 1500 8.8.8.8
```
Stop with `Ctrl+C`.

### `tracert` – Trace route
**Basic** – trace hops to `example.com`  
```cmd
tracert example.com
```
**Progressive** – avoid hostname resolution (`-d`) and use a specific timeout per hop  
```cmd
tracert -d -w 1000 192.168.1.1
```

### `netstat` – Network statistics & connections
**Basic** – show all active TCP connections and listening ports numerically (`-an`)  
```cmd
netstat -an
```
**Progressive** – show process IDs (`-o`) and refresh every 5 seconds  
```cmd
netstat -ano 5
```
Then use `taskkill` (see next section) to close a connection’s owning process.

---

## 6. Process & System Control

### `tasklist` – List running processes
**Basic** – show all processes with PID, memory usage  
```cmd
tasklist
```
**Progressive** – filter only `notepad.exe` instances and show detailed modules (`-m`)  
```cmd
tasklist /fi "imagename eq notepad.exe" /m
```

### `taskkill` – Terminate processes
**Basic** – end a process by PID (ask nicely, then force)  
```cmd
taskkill /PID 1234
taskkill /PID 1234 /F
```
**Progressive** – kill all processes that match a name (e.g., all `calc.exe`)  
```cmd
taskkill /IM calc.exe /F
```

### `shutdown` – Restart or shut down the system
**Basic** – restart after 60 seconds with a comment  
```cmd
shutdown /r /t 60 /c "Scheduled restart"
```
**Progressive** – abort a pending shutdown, then perform an immediate shutdown  
```cmd
shutdown /a
shutdown /s /t 0
```

### `systeminfo` – Detailed system information
**Basic** – display everything (OS version, manufacturer, uptime, hotfixes)  
```cmd
systeminfo
```
**Progressive** – filter for specific values using `findstr`  
```cmd
systeminfo | findstr /i "boot"    (find boot time)
systeminfo | findstr /i "hotfix"   (list installed updates)
```

---

## 7. Batch Script Helpers – Echo, Set, Help

### `echo` – Output text and control command echoing
**Basic** – print “Hello World”  
```cmd
echo Hello World
```
**Progressive** – turn off command echoing in a batch file (use `@echo off`) and create an empty file  
```cmd
@echo off
echo. > empty.txt
```

### `set` – Environment variables
**Basic** – show all variables  
```cmd
set
```
**Progressive** – create a temporary variable and use it in a path  
```cmd
set MYDIR=C:\Temp\Work
mkdir %MYDIR%
copy %USERPROFILE%\*.txt %MYDIR%
```

### `help` – Built‑in command reference
**Basic** – list all available commands  
```cmd
help
```
**Progressive** – get detailed syntax for `xcopy`  
```cmd
help xcopy
```
(Alternative: `xcopy /?` works for most commands.)

---

## Putting It All Together – A Real‑World Batch Example

The following script demonstrates several tools together:  
- Check disk health,  
- Copy logs,  
- Kill a stuck process,  
- Restart the machine if needed.

```batch
@echo off
echo === Starting maintenance ===

:: 1. Check disk C: (read-only)
chkdsk C:

:: 2. Find any "crash" entries in system logs
find /I "crash" C:\Windows\Logs\System.log

:: 3. Kill any hanging notepad processes
taskkill /IM notepad.exe /F >nul 2>&1

:: 4. Backup current user's documents to D:\Backup
xcopy "%USERPROFILE%\Documents\*" D:\Backup /E /Y /Q

:: 5. Ask user to restart
set /p answer="Restart now? (Y/N): "
if /i "%answer%"=="Y" shutdown /r /t 10 /c "Restart after maintenance"

echo === Maintenance complete ===
```

Save as `maintenance.cmd` and run as Administrator for full effect.

---

## Quick Reference Table (Updated)

| Tool | Basic Task | Progressive Example |
|------|------------|----------------------|
| `dir` | List files | `dir /A:D /S` – list all folders recursively |
| `xcopy` | Copy folders | `xcopy src dst /E /K /D:01-01-2025` – copy newer files |
| `fc` | Compare files | `fc /B file1.bin file2.bin` – binary compare |
| `attrib` | Change file attributes | `attrib +h +r *.* /S` – hide & protect all files in tree |
| `chkdsk` | Check disk | `chkdsk C: /F /R` – fix errors and scan bad sectors |
| `ipconfig` | Show IP | `ipconfig /release && ipconfig /renew` |
| `ping` | Test host | `ping -t 8.8.8.8` – continuous ping |
| `tracert` | Trace route | `tracert -d example.com` – fast trace without DNS |
| `netstat` | Show connections | `netstat -ano 5` – live update with PIDs |
| `taskkill` | Kill process | `taskkill /IM virus.exe /F` |
| `shutdown` | Restart PC | `shutdown /r /t 0` – immediate restart |
| `systeminfo` | System details | `systeminfo \| findstr "OS Name"` |
| `set` | Manage variables | `set TEMP=C:\FastTemp` – change temp folder for session |
| `help` | Command help | `help copy` |

---

## Final Notes

- Use `command /?` for built‑in documentation of any tool.
- Most tools accept redirection: `dir > filelist.txt`, `find "text" < input.txt`.
- These commands are still fully functional on Windows 10/11, though PowerShell offers more power.  
  For scripting on modern Windows, consider PowerShell – but the classics remain lightweight and omnipresent.

Keep this guide handy – you now have a progressive reference from simple commands to batch automation.
