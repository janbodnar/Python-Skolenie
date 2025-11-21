# VS Code

Visual Studio Code (VS Code) is a free, open-source code editor developed by Microsoft.  
It has become one of the most popular development environments for Python programming due to  
its lightweight nature, extensive extension ecosystem, and powerful features. VS Code provides  
intelligent code completion, built-in Git integration, debugging capabilities, and excellent  
Python support through extensions.

Unlike full IDEs, VS Code strikes a balance between simplicity and functionality, making it  
ideal for both beginners and experienced developers. Its customizable interface and keyboard-centric  
workflow allow developers to work efficiently without leaving the keyboard.

This guide covers essential shortcuts, tips, and configurations to help you become productive  
with VS Code for Python development.

Great tutorial: https://code.visualstudio.com/docs/editor/codebasics

## Essential shortcuts

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

## Python-specific features

VS Code offers powerful Python-specific features through the Python extension:

- **IntelliSense**: Autocomplete suggestions for variables, functions, and modules
- **Linting**: Automatic code analysis to catch errors and style issues (pylint, flake8)
- **Type checking**: Static type checking with mypy or Pyright
- **Auto-imports**: Automatically add import statements when using modules
- **Refactoring**: Rename symbols across files, extract methods, and more

Select Python interpreter with `Ctrl + Shift + P` → "Python: Select Interpreter"


## Debugging

VS Code has excellent built-in debugging support:

- `F5` - Start debugging
- `F9` - Toggle breakpoint
- `F10` - Step over
- `F11` - Step into
- `Shift + F11` - Step out
- `Shift + F5` - Stop debugging

Create a `.vscode/launch.json` file for custom debug configurations. You can debug:
- Python scripts
- Django/Flask applications
- Unit tests
- Remote applications


## Terminal integration

Integrated terminal shortcuts:

- `Ctrl + backtick` - Toggle integrated terminal
- `Ctrl + Shift + backtick` - Create new terminal
- `Ctrl + Shift + 5` - Split terminal
- `Ctrl + PageUp/PageDown` - Switch between terminals

Run Python files directly:
- Right-click in editor → "Run Python File in Terminal"
- Or use the play button in the top-right corner


## File navigation tips

- `Ctrl + Tab` - Switch between open files
- `Ctrl + \` - Split editor
- `Ctrl + W` - Close current file
- `Ctrl + K Ctrl + W` - Close all files
- `Ctrl + Shift + T` - Reopen closed file
- `Ctrl + K R` - Reveal active file in Explorer
- `Alt + Left/Right` - Navigate backward/forward
- `Ctrl + G` - Go to line number
- `Ctrl + Shift + O` - Go to symbol in file
- `Ctrl + T` - Go to symbol in workspace


## Code editing productivity

- `Ctrl + Space` - Trigger IntelliSense/autocomplete
- `Ctrl + .` - Quick fix (show code actions)
- `Shift + Alt + I` - Insert cursor at end of each selected line
- `Ctrl + U` - Undo last cursor operation
- `Ctrl + /` - Toggle line comment
- `Shift + Alt + A` - Toggle block comment
- `Ctrl + K Ctrl + C` - Add line comment
- `Ctrl + K Ctrl + U` - Remove line comment
- `Ctrl + ]` - Indent line
- `Ctrl + [` - Outdent line
- `Ctrl + Shift + [` - Fold code block
- `Ctrl + Shift + ]` - Unfold code block
- `Ctrl + K Ctrl + 0` - Fold all
- `Ctrl + K Ctrl + J` - Unfold all


## Search and replace

- `Ctrl + F` - Find in current file
- `Ctrl + H` - Replace in current file
- `Ctrl + Shift + F` - Find in all files
- `Ctrl + Shift + H` - Replace in all files
- `Alt + Enter` (during search) - Select all occurrences of find match
- `F3` / `Shift + F3` - Find next/previous


## Zen mode and focus

- `Ctrl + K Z` - Enter Zen mode (distraction-free coding)
- `Ctrl + B` - Toggle sidebar visibility
- `Ctrl + J` - Toggle panel (terminal, problems, output)
- `F11` - Toggle full screen

These shortcuts help you focus on code by hiding UI elements.


## Useful productivity tips

1. **Peek definition**: `Alt + F12` - View function/class definition in a popup
2. **Go to definition**: `F12` - Jump to where a symbol is defined
3. **Find all references**: `Shift + F12` - Find all usages of a symbol
4. **Rename symbol**: `F2` - Rename variable/function across entire project
5. **Breadcrumbs**: Enable breadcrumbs to navigate code structure (View → Show Breadcrumbs)
6. **Minimap**: The minimap on the right side helps navigate large files
7. **Problems panel**: `Ctrl + Shift + M` - View linting errors and warnings
8. **Output panel**: View extension outputs and logs
9. **Sticky scroll**: Shows nested scopes at the top while scrolling


## Working with Python virtual environments

VS Code automatically detects virtual environments:

1. Create venv: `python -m venv venv`
2. VS Code will detect it and offer to select it
3. Or manually select: `Ctrl + Shift + P` → "Python: Select Interpreter"
4. Activate in terminal: `.\venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Linux/Mac)

The selected environment appears in the status bar (bottom-left).


## Snippets

Type these prefixes and press `Tab` to expand:

- `for` - for loop
- `if` - if statement
- `def` - function definition
- `class` - class definition
- `try` - try-except block
- `with` - with statement
- `ifmain` - if __name__ == '__main__'

Create custom snippets: File → Preferences → Configure User Snippets


## Version control (Git)

- `Ctrl + Shift + G` - Open Source Control panel
- Stage changes by clicking `+` next to files
- Commit with message in the Source Control panel
- View diffs by clicking modified files

**Recommended extensions:**
- **GitLens**: Provides inline blame, file/line history, and advanced Git features
- **Git History**: Browse and search Git log, view file history, compare branches

