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
dir /A:H /S
```

**Option Explanations:**
- `/A:D` – Displays only directories (folders), filtering out regular files.
- `/W` – Uses wide format, showing filenames across the screen in columns rather than a vertical list.
- `/A:H` – Shows files with the "Hidden" attribute.
- `/S` – Recursively lists contents of all subfolders.
- **Tip:** Combine `/A` with attributes: `D` (directories), `H` (hidden), `S` (system), `R` (read-only), `A` (archive).

---

### `cd` – Change directory
**Basic** – go to `C:\Windows`  
```cmd
cd C:\Windows
```

**Progressive** – go up two levels, then down to `Users\Public`  
```cmd
cd ..\..\Users\Public
```

**Option Explanations:**
- `..` – Refers to the parent directory (one level up).
- `..\..` – Moves up two directory levels.
- **Tip:** Use `cd` without parameters to display the current working directory path.

---

### `cls` – Clear the screen
```cmd
cls
```
Simply clears all text from the Command Prompt window, giving you a fresh screen.

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

**Option Explanations:**
- The `+` operator merges multiple files sequentially.
- The last filename is the destination; if omitted, files are merged into the first file.
- **Tip:** Use `/Y` to suppress confirmation prompts when overwriting, or `/V` to verify the copy.

---

### `xcopy` – Advanced copy (folders, attributes, timestamps)
**Basic** – copy all files and subfolders, preserving read‑only attribute  
```cmd
xcopy C:\Data D:\DataBackup /E /K
```

**Progressive** – copy only files modified after a certain date, with verification  
```cmd
xcopy "C:\Users\Public\*.docx" D:\Archive /D:01-01-2025 /V
```

**Option Explanations:**
- `/E` – Copies all subdirectories, including empty ones.
- `/K` – Preserves the read-only attribute on copied files (otherwise it's removed by default).
- `/D:MM-DD-YYYY` – Copies only files modified on or after the specified date.
- `/V` – Verifies each copied file against the original to ensure integrity.
- **Additional options:** `/I` assumes destination is a directory; `/S` copies subfolders  
  (but not empty ones); `/Y` suppresses overwrite prompts.

---

### `move` – Move or rename
**Basic** – move `old.txt` into `Archive\`  
```cmd
move old.txt Archive\
```

**Progressive** – rename a folder (both source and destination paths can be directories)  
```cmd
move "Project X" "Project_X_2025"
```

**Option Explanations:**
- If the destination is a directory, the source item moves into it.
- If the destination is a file path, the source is renamed.
- **Tip:** Use quotes around paths containing spaces.

---

### `del` – Delete files
**Basic** – delete all `.tmp` files quietly  
```cmd
del *.tmp /Q
```

**Progressive** – delete files recursively, prompting for each one  
```cmd
del /S /P *.log
```

**Option Explanations:**
- `/Q` – Quiet mode: suppresses confirmation prompts.
- `/S` – Recursively deletes matching files in all subfolders.
- `/P` – Prompts for confirmation before deleting each file.
- **Tip:** Use `/F` to force-delete read-only files.

---

### `mkdir` & `rmdir` – Create / remove directories
**Basic** – create `Backup` inside `Logs`  
```cmd
mkdir Logs\Backup
```

**Basic** – remove empty folder  
```cmd
rmdir OldEmptyFolder
```

**Progressive** – remove a non‑empty folder and all its contents, without confirmation  
```cmd
rmdir /S /Q TempData
```

**Option Explanations:**
- `mkdir` – Automatically creates any intermediate directories in the path.
- `rmdir /S` – Removes the specified directory and all its subdirectories and files.
- `rmdir /Q` – Quiet mode: no confirmation prompt.
- **Tip:** `rmdir` will only remove empty folders unless `/S` is used.

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

**Option Explanations:**
- The pipe (`|`) sends output from `type` to `more`, which displays one screen at a time.
- Press Space to scroll, Enter for next line, or `Q` to quit.
- **Tip:** `more longfile.txt` works as a standalone command as well.

---

### `find` – Search for a string
**Basic** – find lines containing "Error" in `app.log`  
```cmd
find "Error" app.log
```

**Progressive** – search case‑insensitively and display line numbers across multiple files  
```cmd
find /I /N "warning" *.log
```

**Option Explanations:**
- `/I` – Ignores case when matching text (so "Warning", "WARNING", etc., all match).
- `/N` – Displays line numbers alongside each matched line.
- **Tip:** Use `/C` to count matches only, or `/V` to find lines that do **not** contain the text.

---

### `fc` – Compare two files
**Basic** – ASCII comparison  
```cmd
fc old_config.ini new_config.ini
```

**Progressive** – binary comparison for non‑text files  
```cmd
fc /B image1.jpg image2.jpg
```

**Option Explanations:**
- **No flag** – Performs an ASCII text comparison, showing differences line by line.
- `/B` – Performs a byte-by-byte binary comparison, useful for executables, images, or any non-text files.
- **Additional options:** `/L` compares as ASCII text; `/N` displays line numbers; `/W` compresses whitespace during comparison.

---

## 4. Disk & File System Management

### `attrib` – View or change file attributes
**Basic** – make a file hidden and read‑only  
```cmd
attrib +h +r secret.txt
```

**Progressive** – recursively remove the "system" attribute from all files in a folder  
```cmd
attrib -s C:\Windows\Temp\*.* /S
```

**Option Explanations:**
- `+h` – Sets the "Hidden" attribute; `-h` removes it.
- `+r` – Sets the "Read-only" attribute; `-r` removes it.
- `+s` – Sets the "System" attribute (marks file as critical system file); `-s` removes it.
- `/S` – Recursively processes all files in subfolders.
- **Tip:** Use `attrib` alone to display attributes for all files in the current directory.

---

### `chkdsk` – Check disk for errors
**Basic** – check drive C: (read‑only)  
```cmd
chkdsk C:
```

**Progressive** – fix errors, locate bad sectors, and force dismount if needed  
```cmd
chkdsk C: /F /R /X
```

**Option Explanations:**
- `/F` – Fixes errors on the disk (requires exclusive access; may schedule at reboot).
- `/R` – Finds and recovers bad sectors (implies `/F`).
- `/X` – Forces the volume to dismount before scanning (ensures exclusive access).
- **Note:** If the drive is in use, you'll be prompted to schedule the scan at next system restart.

---

### `sfc` – System File Checker
**Basic** – verify and repair protected system files  
```cmd
sfc /scannow
```

**Progressive** – verify only (no repair) and scan a specific file  
```cmd
sfc /verifyonly
sfc /scanfile=C:\Windows\System32\kernel32.dll
```

**Option Explanations:**
- `/scannow` – Scans all protected system files and repairs corrupted ones (requires Administrator privileges).
- `/verifyonly` – Scans but does not repair (useful for auditing).
- `/scanfile=<path>` – Scans only the specified file.
- **Tip:** Run `sfc /scannow` first when troubleshooting system instability.

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

**Option Explanations:**
- `/all` – Shows detailed information for all network adapters (including MAC address, DHCP status, DNS servers).
- `/release` – Releases the current DHCP-assigned IP address.
- `/renew` – Requests a new IP address from the DHCP server.
- `/flushdns` – Clears the DNS resolver cache.
- **Tip:** Combine with `ipconfig /displaydns` to view cached DNS entries.

---

### `ping` – Test connectivity
**Basic** – send 4 ICMP packets to `google.com`  
```cmd
ping google.com
```

**Progressive** – ping continuously with 1500 byte packets, stop after 10 pings  
```cmd
ping -t -l 1500 8.8.8.8
```
Stop with `Ctrl+C`.

**Option Explanations:**
- `-t` – Pings continuously until manually stopped (Ctrl+C).
- `-l <size>` – Sets the size of the ICMP packet in bytes (default is 32).
- `-n <count>` – Sends a specific number of pings (e.g., `-n 10` for 10 pings).
- **Additional options:** `-w <timeout>` sets a timeout in milliseconds for each reply.

---

### `tracert` – Trace route
**Basic** – trace hops to `example.com`  
```cmd
tracert example.com
```

**Progressive** – avoid hostname resolution and use a specific timeout per hop  
```cmd
tracert -d -w 1000 192.168.1.1
```

**Option Explanations:**
- `-d` – Prevents resolution of IP addresses to hostnames (speeds up the trace).
- `-w <timeout>` – Sets the time to wait for each reply in milliseconds (default is 4000).
- **Additional options:** `-h <max_hops>` sets the maximum number of hops to trace.

---

### `netstat` – Network statistics & connections
**Basic** – show all active TCP connections and listening ports numerically  
```cmd
netstat -an
```

**Progressive** – show process IDs and refresh every 5 seconds  
```cmd
netstat -ano 5
```

**Option Explanations:**
- `-a` – Displays all connections and listening ports.
- `-n` – Shows addresses and port numbers in numerical form (no hostname resolution).
- `-o` – Displays the owning process ID (PID) for each connection.
- The trailing `5` – Refreshes the display every 5 seconds.
- **Tip:** Use with `findstr` to filter: `netstat -ano | findstr ":443"` to see connections on port 443.

---

## 6. Process & System Control

### `tasklist` – List running processes
**Basic** – show all processes with PID, memory usage  
```cmd
tasklist
```

**Progressive** – filter only `notepad.exe` instances and show detailed modules  
```cmd
tasklist /fi "imagename eq notepad.exe" /m
```

**Option Explanations:**
- `/fi` – Filters the list based on criteria (e.g., `imagename eq process.exe`, `pid eq 1234`).
- `/m` – Lists all DLL modules loaded by each process.
- **Additional filters:** `status eq running`, `memusage gt 50000` (memory > 50 MB).
- **Tip:** Use `/v` for verbose details or `/svc` to see associated Windows services.

---

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

**Option Explanations:**
- `/PID` – Specifies the process ID to terminate.
- `/IM` – Specifies the image name (process name) to terminate.
- `/F` – Forces the termination (use when a process won't close gracefully).
- **Tip:** Combine with `/T` to terminate child processes as well.

---

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

**Option Explanations:**
- `/r` – Restarts the system.
- `/s` – Shuts down the system.
- `/t <seconds>` – Sets a delay before the action (0 = immediate).
- `/c "comment"` – Adds a comment that appears in the shutdown dialog.
- `/a` – Aborts a pending shutdown or restart.
- **Additional options:** `/f` forces running applications to close without warning; `/hybrid` performs a hybrid shutdown (fast startup).

---

### `systeminfo` – Detailed system information
**Basic** – display everything (OS version, manufacturer, uptime, hotfixes)  
```cmd
systeminfo
```

**Progressive** – filter for specific values using `findstr`  
```cmd
systeminfo | findstr /i "boot"
systeminfo | findstr /i "hotfix"
```

**Option Explanations:**
- The output is piped (`|`) to `findstr` to search for specific strings.
- `/i` in `findstr` makes the search case-insensitive.
- **Tip:** Find OS version: `systeminfo | findstr "OS Name"`; find system uptime: `systeminfo | findstr "System Boot Time"`.

---

## 7. Batch Script Helpers – Echo, Set, Help

### `echo` – Output text and control command echoing
**Basic** – print "Hello World"  
```cmd
echo Hello World
```

**Progressive** – turn off command echoing in a batch file and create an empty file  
```cmd
@echo off
echo. > empty.txt
```

**Option Explanations:**
- `@echo off` – Prevents commands from being displayed in the console (only output is shown).
- `echo.` – Outputs a blank line (useful for spacing in scripts).
- `> empty.txt` – Redirects output to a file, creating an empty file.
- **Tip:** Use `echo off` (without `@`) to hide commands but show the `echo off` command itself.

---

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

**Option Explanations:**
- Variables are referenced with `%` around the name (e.g., `%MYDIR%`).
- Variables set this way last only for the current Command Prompt session.
- `%USERPROFILE%` is a built-in variable pointing to the user's home directory.
- **Tip:** Use `setx` to permanently set variables in the system or user environment.

---

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

**Option Explanations:**
- Running `help` alone shows a list of all internal commands.
- `help <command>` displays detailed syntax and options for that command.
- **Tip:** Most external commands support `/?` as an alternative to `help`.

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

**Script Explanations:**
- `@echo off` – Hides command traces for cleaner output.
- `::` – Comment lines (not executed).
- `>nul 2>&1` – Suppresses all output (both standard and error) when killing processes.
- `set /p` – Prompts the user for input.
- `/i` in the `if` statement makes the comparison case-insensitive.

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
