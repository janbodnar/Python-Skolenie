# VS Code

## Shortcuts

- `Ctrl + Shift + Enter` - insert line above
- `Ctrl + Enter` - insert line below
- `Ctrl + Shift + K` - delete line

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

