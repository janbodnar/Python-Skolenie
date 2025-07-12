#!/usr/bin/python

"""
Simple script to get the latest three blog post titles from symfony.com/blog

This script demonstrates web scraping using only Python standard library modules:
- requests for HTTP requests
- re for regular expressions  
- html.parser for HTML parsing

Usage: python3 get_symfony_titles.py
"""

import requests
import re


def get_latest_symfony_blog_titles():
    """
    Fetch and extract the latest 3 blog post titles from symfony.com/blog
    
    Returns:
        list: List of blog post titles (up to 3)
    """
    
    url = 'https://symfony.com/blog'
    
    try:
        print("Fetching Symfony blog page...")
        response = requests.get(url, timeout=10)
        
        if response.status_code != 200:
            print(f"Error: HTTP {response.status_code}")
            return []
        
        html_content = response.text
        print("Page fetched successfully, extracting titles...")
        
        # Try different patterns to extract blog post titles
        patterns = [
            # H2 tags with links (common pattern)
            r'<h2[^>]*>\s*<a[^>]*>(.*?)</a>\s*</h2>',
            
            # H2 tags without links
            r'<h2[^>]*class="[^"]*title[^"]*"[^>]*>(.*?)</h2>',
            
            # Any element with title-related class
            r'class="[^"]*(?:post-title|entry-title|blog-title)[^"]*"[^>]*>(.*?)<',
            
            # Article headings
            r'<article[^>]*>.*?<h[23][^>]*>(.*?)</h[23]>',
        ]
        
        titles = []
        
        for pattern in patterns:
            matches = re.findall(pattern, html_content, re.IGNORECASE | re.DOTALL)
            
            if matches:
                for match in matches:
                    # Clean the title text
                    clean_title = re.sub(r'<[^>]+>', '', match).strip()
                    clean_title = re.sub(r'\s+', ' ', clean_title)  # Normalize whitespace
                    
                    if clean_title and len(clean_title) > 10:  # Filter short/empty titles
                        titles.append(clean_title)
                
                if titles:
                    break  # Stop after finding titles with first working pattern
        
        return titles[:3]  # Return only the latest 3
        
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []


def main():
    """Main function to run the blog title extraction"""
    
    print("Symfony Blog Title Extractor")
    print("=" * 30)
    
    titles = get_latest_symfony_blog_titles()
    
    if titles:
        print(f"\nFound {len(titles)} blog post titles:")
        print("-" * 40)
        
        for i, title in enumerate(titles, 1):
            print(f"{i}. {title}")
            
        print("-" * 40)
        print("✅ Successfully extracted Symfony blog titles!")
        
    else:
        print("\n❌ Could not extract blog titles.")
        print("\nPossible reasons:")
        print("- Network connectivity issues")
        print("- Website structure has changed")
        print("- Site is blocking automated requests")
        print("- Temporary server issues")
        
        print("\nTo fix this issue:")
        print("1. Check your internet connection")
        print("2. Try running the script again later")
        print("3. Inspect the page HTML to update the regex patterns")


if __name__ == "__main__":
    main()