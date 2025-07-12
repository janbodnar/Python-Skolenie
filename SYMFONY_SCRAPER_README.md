# Symfony Blog Title Scraper

This repository contains scripts to extract the latest three blog post titles from `symfony.com/blog` using Python web scraping techniques.

## Files

### `get_symfony_titles.py`
A simple, focused script that extracts the latest 3 blog post titles from Symfony's blog.

**Features:**
- Uses only Python standard library (requests, re)
- Multiple regex patterns to handle different HTML structures
- Proper error handling and user feedback
- Clean, readable output

**Usage:**
```bash
python3 get_symfony_titles.py
```

### `libs/requests/symfony_blog_scraper.py`
A more comprehensive example that demonstrates various web scraping techniques.

**Features:**
- Custom HTML parser class using `html.parser`
- Multiple extraction methods (parser + regex fallback)
- Demo functionality with sample HTML
- Educational comments and documentation

**Usage:**
```bash
python3 libs/requests/symfony_blog_scraper.py
```

## How It Works

1. **HTTP Request**: Makes a GET request to `https://symfony.com/blog`
2. **HTML Parsing**: Extracts blog post titles using regex patterns
3. **Title Extraction**: Looks for common blog title patterns:
   - `<h2><a>Title</a></h2>` - Linked headings
   - `class="post-title"` - Title CSS classes  
   - `<article><h2>Title</h2>` - Article headings
4. **Cleaning**: Removes HTML tags and normalizes whitespace
5. **Output**: Returns the latest 3 titles

## Common Blog Title Patterns

The scripts use these regex patterns to find blog titles:

```python
patterns = [
    r'<h2[^>]*>\s*<a[^>]*>(.*?)</a>\s*</h2>',                    # H2 with links
    r'<h2[^>]*class="[^"]*title[^"]*"[^>]*>(.*?)</h2>',          # H2 with title class
    r'class="[^"]*(?:post-title|entry-title|blog-title)[^"]*"[^>]*>(.*?)<',  # Title classes
    r'<article[^>]*>.*?<h[23][^>]*>(.*?)</h[23]>',               # Article headings
]
```

## Customization

To adapt these scripts for other blogs:

1. Change the URL in the script
2. Inspect the target blog's HTML structure
3. Update the regex patterns to match the specific HTML structure
4. Test and refine the patterns

## Error Handling

The scripts handle common issues:
- Network connectivity problems
- HTTP errors (404, 500, etc.)
- Parsing errors
- Empty or malformed responses

## Dependencies

- Python 3.6+
- `requests` library (install with `pip install requests`)

## Example Output

```
Symfony Blog Title Extractor
==============================
Fetching Symfony blog page...
Page fetched successfully, extracting titles...

Found 3 blog post titles:
----------------------------------------
1. How to Build Better Web Applications with Symfony 7
2. Symfony UX: Creating Interactive User Interfaces  
3. Performance Optimization in Symfony Applications
----------------------------------------
✅ Successfully extracted Symfony blog titles!
```