# Finding Large Files in Windows: A Comprehensive Guide

This document covers methods for locating large files using File Explorer, Command Prompt, and PowerShell. These techniques work on Windows 10, Windows 11, and earlier versions.

---

## Table of Contents
1. [File Explorer – Advanced Query Syntax](#file-explorer--advanced-query-syntax)
2. [File Explorer – Using the Size Filter Menu](#file-explorer--using-the-size-filter-menu)
3. [Command Prompt (CMD) – `forfiles` Command](#command-prompt-cmd--forfiles-command)
4. [PowerShell – Advanced and Fast Searches](#powershell--advanced-and-fast-searches)
5. [Important Limitations & How to Overcome Them](#important-limitations--how-to-overcome-them)
6. [Quick Reference Card](#quick-reference-card)

---

## File Explorer – Advanced Query Syntax

The search bar in File Explorer supports **Advanced Query Syntax (AQS)**, allowing you to find files by size quickly .

### Step-by-step Guide:
1.  Press **Windows Key + E** to open File Explorer.
2.  Navigate to `This PC` or a specific drive (e.g., `C:\`) to broaden the search.
3.  Click in the search box (top right).
4.  Type one of the following commands and press **Enter**:

### Available Keywords:
| Keyword | File Size Range |
| :--- | :--- |
| `size:empty` | 0 KB |
| `size:tiny` | 0 – 10 KB (or 0-16 KB depending on version)  |
| `size:small` | 10 KB – 100 KB  |
| `size:medium` | 100 KB – 1 MB  |
| `size:large` | **1 MB – 16 MB**  |
| `size:huge` | **16 MB – 128 MB**  |
| `size:gigantic` | **> 128 MB** (often > 4 GB in newer UI)  |

### Searching with Custom Sizes:
For more control, use comparison operators:
- **Greater than:** `size:>500MB` (finds files larger than 500 MB) .
- **Range:** `size:500MB..2GB` (finds files between 500 MB and 2 GB) .
- **Combine with other criteria:**
    - `kind:video size:>1GB`
    - `ext:.iso size:>2GB` 
    - `size:>1GB datemodified:<2024/01/01` 

---

## File Explorer – Using the Size Filter Menu

If you can't remember the keywords, you can use the built-in filter menu .

1.  In File Explorer, click in the search box.
2.  The **Search** tab will appear in the ribbon at the top.
3.  Click the **Search** tab.
4.  In the **Refine** section, click the **Size** dropdown.
5.  Select a pre-defined size category (e.g., "Gigantic").
6.  The filter will automatically apply the `size:` syntax to your search.

---

## Command Prompt (CMD) – `forfiles` Command

For users who prefer the command line or need to export results quickly, the `forfiles` command is a useful built-in tool .

### Syntax:
```cmd
forfiles /S /C "cmd /c if @fsize GTR [SIZE_IN_BYTES] echo @path"
```

- `GTR` means "Greater Than". You can also use `GEQ` ("Greater Than or Equal To") .
- Replace `[SIZE_IN_BYTES]` with the size threshold.

### Examples:
1.  **Find files larger than 1 GB (1,073,741,824 bytes) on drive C:** 
    ```cmd
    cd C:\
    forfiles /S /C "cmd /c if @fsize GTR 1073741824 echo @path"
    ```

2.  **Save the results to a text file:**
    ```cmd
    forfiles /S /C "cmd /c if @fsize GTR 1073741824 echo @path > LargeFilesList.txt"
    ```
    *(This saves the list to a file in the current directory)* .

---

## PowerShell – Advanced and Fast Searches

PowerShell is significantly faster than Command Prompt for searching large directories. You can filter, sort, and format the output easily .

### Basic Command to List Largest Files:
To find the 20 largest files in the `C:\` drive, run the following in PowerShell (run as Administrator for best results) :
```powershell
Get-ChildItem -Path C:\ -Recurse -ErrorAction SilentlyContinue | 
Sort-Object -Property Length -Descending | 
Select-Object -First 20 Name, FullName, Length
```

### Advanced Command with Human-Readable Sizes:
This command finds the 50 largest files and displays their size in Gigabytes (GB) .
```powershell
Get-ChildItem -Path C:\ -File -Recurse -Force -ErrorAction SilentlyContinue |
Sort-Object -Property Length -Descending |
Select-Object -First 50 @{Name='Size(GB)';Expression={[math]::Round($_.Length/1GB,2)}}, FullName
```

### Export to CSV for Analysis:
```powershell
Get-ChildItem -Path C:\ -Recurse -ErrorAction SilentlyContinue |
Sort-Object -Property Length -Descending |
Select-Object -First 100 Name, FullName, Length |
Export-Csv -Path C:\largest_files.csv -NoTypeInformation
```

### Finding Large Directories (Folder Sizes):
PowerShell can be used to find large folders, which is often more useful than finding individual files, as large folders usually contain many small files .

```powershell
Get-ChildItem C:\ -Directory -Force -ErrorAction SilentlyContinue | ForEach-Object {
    $size = [math]::Round((Get-ChildItem $_.FullName -Recurse -File -Force -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum).Sum / 1GB, 2)
    [PSCustomObject]@{ Folder = $_.FullName; SizeGB = $size }
} | Sort-Object SizeGB -Descending | Select-Object -First 15
```

---

## Important Limitations & How to Overcome Them

When using File Explorer or standard commands, you may miss large files due to three critical blind spots .

| Blind Spot | Description | Solution |
| :--- | :--- | :--- |
| **Hidden/System Files** | System files like `pagefile.sys`, `hiberfil.sys`, or memory dumps are hidden by default. | In File Explorer, go to **View → Options → View** and enable **Show hidden files, folders, and drives** and disable **Hide protected operating system files**.  |
| **Permission Denied** | You may not have access to folders like `System Volume Information`. | Run Command Prompt or PowerShell **as Administrator**.  |
| **Individual Files vs. Folders** | A folder can be massive even if it contains no single large file (e.g., browser cache). | Use the PowerShell script provided above to sort folders by total size.  |

---

## Quick Reference Card

- **File Explorer (Pre-defined):** Type `size:gigantic` or use the Search tab → Size dropdown.
- **File Explorer (Custom):** Type `size:>500MB` or `size:>1GB`.
- **Command Prompt:** `forfiles /S /C "cmd /c if @fsize GTR 1073741824 echo @path"` (1 GB threshold).
- **PowerShell (Files):** `Get-ChildItem -Path C:\ -Recurse | Sort-Object Length -Descending | Select-Object -First 50 FullName, Length` (Run as Admin).
- **PowerShell (Folders):** Use the script in the PowerShell section to find the largest directories by total size.
