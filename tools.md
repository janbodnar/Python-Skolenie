# Python tools


## Formatter 

Python source code formatters are  automated tools that reformat your Python code according to   
a specific style guide. They ensure consistent indentation, spacing, and other stylistic   
elements, making your code:

- More readable: Consistent formatting improves code clarity for you and other developers.
- Easier to maintain: Consistent style reduces the risk of introducing errors due to  
  formatting inconsistencies.
- Adherent to standards: Formatters can enforce project-specific coding conventions.


Here are a few commonly used Python source code formatters:

- Black: A popular opinionated formatter with a strict style guide. It enforces a single style,  
   making code very consistent.
- autopep8: A formatter that follows PEP 8, the official Python style guide. It offers more  
  flexibility than Black but still promotes consistent style.
- YAPF (Yet Another Python Formatter): Another flexible formatter with a large configuration  
  options to customize the formatting style.
- isort: Specifically formats imports in your Python code, ensuring consistent ordering and grouping.

## Linter 

A Python linter is a static code analysis tool that helps you identify and fix potential issues   
in your Python code. It's like a spell checker for your code, but instead of focusing on typos,  
it checks for:

- Syntax errors: Mistakes in the code's structure that prevent it from running at all.  
- Style inconsistencies: Violations of coding conventions like indentation or naming rules,  
  which can make code harder to read and maintain.
- Potential bugs: Issues in the code's logic that might lead to unexpected behavior or  
  errors at runtime.


Here are some key benefits of using a Python linter:  

- Improved code quality: Linters help you write cleaner, more consistent, and less error-prone code.
- Enhanced readability: Consistent style makes code easier to understand for you and other developers.
- Early bug detection: Linters can catch potential bugs before they cause problems in your application.
- Enforced coding standards: Linters can help ensure your code adheres to your team's or  
  project's specific coding guidelines.


Some popular Python linters include:

- Pylint: A powerful linter with a wide range of checks and configuration options.
- Flake8: A popular linter that combines multiple linters like Pylint and pycodestyle   
  for a comprehensive analysis.
- mypy: A linter that focuses on static type checking to catch potential type errors early on.

These linters can be integrated with code editors and IDEs to provide real-time feedback as   
you write your code. This helps you catch issues immediately and fix them before they become  
bigger problems.

Overall, using a Python linter is a valuable practice for any Python developer. It can significantly  
improve your code quality, save you time debugging, and make your codebase more maintainable.


## Ruff 

`Ruff` is a high-performance Python linter and code formatter written in Rust, offering speed and   
comprehensive code analysis.

Here are some key characteristics of Ruff:

- High Speed: It boasts speeds 10-100 times faster than traditional linters like `Flake8` or formatters like `Black`.  
- Multifunctional: Combines linting and formatting functionalities into a single tool, streamlining your workflow.  
- Wide Range of Checks: Performs over 700 built-in checks, including syntax errors, style inconsistencies,  
  and potential bugs.
- Automatic Fixes: Offers auto-fix capabilities for certain issues, saving you time correcting minor errors.
- Drop-in Replacement: Aims to replace various linters and formatters like `Flake8`, `Pylint`, `Black`, and `isort`,  
  with a single, faster solution.


## VS Code settings 

```json
{
    "editor.rulers": [
        80
    ],
    "editor.minimap.enabled": true,
    "editor.renderWhitespace": "all",
    "editor.cursorSmoothCaretAnimation": "on",
    "terminal.integrated.defaultProfile.windows": "Command Prompt",
    "workbench.editor.pinnedTabSizing": "compact",
    "[python]": {
        // "editor.defaultFormatter": "ms-python.autopep8"
    },
    "editor.occurrencesHighlight": "off",
    "editor.fontFamily": "Cascadia Code NF Regular, JetBrains Mono, Consolas, 'Courier New', monospace",
    "editor.multiCursorModifier": "ctrlCmd",
    "editor.suggest.insertMode": "replace",
    // "editor.lineHeight": 1.4,
    "editor.stickyScroll.enabled": false,
    "workbench.editor.enablePreview": true,
    "explorer.autoReveal": true,
    "workbench.tree.indent": 12,
    "emmet.triggerExpansionOnTab": true,
    "workbench.tree.renderIndentGuides": "onHover",
    "editor.fontSize": 14,
}
```



