# VS Code

Great tutorial: https://code.visualstudio.com/docs/editor/codebasics

- `Ctrl + P` - search for symbols
- `Ctrl + Shift + P` - open command palette

## Formatting

- format document `Shift+Alt+F` - Format the entire active file.
- format selection `Ctrl+K Ctrl+F` - Format the selected text.

## Basic shortcuts

- `Ctrl + Shift + Enter` - insert line above
- `Ctrl + Enter` - insert line below
- `Ctrl + Shift + K` - delete line
- `Ctrl + Shift + L` - highlight all occurrences
- `Ctrl + D` - highlight next occurrence
- `Ctrl + C` - copy line without highlighting it first
- `Alt + Up/Down arrow` - move line up/down
- `Alt + Shift + Up/Down arrow` - duplicate line up/down


## Multi-cursor

Add `f` and remove `!` from the example with multicursor (`Ctrl + Alt + Up/Down` on Windows.)  
Also `Ctrl + Click`.  (Toggle MultiCursor modifier command).

Trim trailing whitespaces.  

```python
vals = (-5, 10, 55, 12, -7, 11, 22)

print('minimum je: {min(vals)}!') 
print('maximum je: {max(vals)}!')   
print('pocet prvkov je: {len(vals)}!')            
print('suma je: {sum(vals)}!')
```

## Selections

Swap the occupation & last name columns.  

```
first name   occupation     last name  
John         gardener       Doe
Roger        driver         Roe
Paul         teacher        Novak
Jane         accountant     Smith
Lucia        programmer     Dorak
Robert       soldier        Williams
```

## Commands 

The commands palette is started with `Ctrl + Shift + P`.  

Common useful commands: 

- Trim Trailing Whitespace
- Help: Welcome
- Developer: Reload window
- Python: Select Interpreter
- Preferences: Color Theme


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
"editor.multiCursorModifier": "ctrlCmd",
"editor.suggest.insertMode": "replace",
"workbench.editor.pinnedTabSizing": "compact",
"editor.occurrencesHighlight": "off",
"workbench.iconTheme": "file-icons",
"workbench.editor.enablePreview": true,
"explorer.autoReveal": true,
"workbench.tree.indent": 12,
"emmet.triggerExpansionOnTab": true,
"workbench.tree.renderIndentGuides": "onHover",
"editor.fontSize": 13,
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

