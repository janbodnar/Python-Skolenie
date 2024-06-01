# VS Code

## Shortcuts

- `Ctrl + Shift + Enter` - insert line above
- `Ctrl + Enter` - insert line below
- `Ctrl + Shift + K` - delete line
- `Ctrl + Shift + L` - highlight all occurrences
- `Ctrl + D` - highlight next occurrence
- `Ctrl + C` - copy line without highlighting it first


## Multi-cursor

Add `f` and remove `!` from the example with multicursor (`Ctrl + Alt + Up/Down` on Windows.)  
Also `Ctrl + Click`.  

Trim trailing whitespaces.  

```python
vals = (-5, 10, 55, 12, -7, 11, 22)

print('minimum je: {min(vals)}!') 
print('maximum je: {max(vals)}!')   
print('pocet prvkov je: {len(vals)}!')            
print('suma je: {sum(vals)}!')
```


## Extensions

- Rewrap
- Hex editor
- file-icons
- TabOut
- SQLite viewer
- REST Client


## Settings 

```json
"editor.rulers": [
    80
],
"editor.renderWhitespace": "all",
"editor.cursorSmoothCaretAnimation": "on",
"terminal.integrated.defaultProfile.windows": "Command Prompt",
"terminal.integrated.enableMultiLinePasteWarning": false,
"editor.stickyScroll.enabled": false,
"editor.fontFamily": "'JetBrains Mono', Consolas, 'Courier New', monospace",
"workbench.editor.pinnedTabSizing": "compact",
"editor.occurrencesHighlight": "off",
"workbench.iconTheme": "file-icons",
```

## REST client

Create `client.http` file.  

```
get http://webcode.me/words.txt
get http://webcode.me/users.csv
get http://webcode.me/users.json
get http://webcode.me/users.xml
get http://webcode.me/thermopylae.txt
get http://webcode.me/os.html
get http://webcode.me/countries.html
```

