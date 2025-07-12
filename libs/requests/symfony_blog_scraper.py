#!/usr/bin/python

import requests
import re
from html.parser import HTMLParser


class BlogTitleParser(HTMLParser):
    """HTML parser to extract blog post titles"""
    
    def __init__(self):
        super().__init__()
        self.titles = []
        self.current_tag = None
        self.capture_text = False
        
    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        
        # Look for common blog title patterns
        if tag in ['h1', 'h2', 'h3']:
            # Check if this heading might be a blog title
            attr_dict = dict(attrs)
            class_name = attr_dict.get('class', '')
            
            # Common blog title CSS classes
            title_classes = ['post-title', 'entry-title', 'blog-title', 'article-title']
            if any(cls in class_name for cls in title_classes):
                self.capture_text = True
            elif tag == 'h2':  # H2 tags are commonly used for blog titles
                self.capture_text = True
                
        elif tag == 'a' and self.current_tag in ['h1', 'h2', 'h3']:
            # Title links within headings
            self.capture_text = True
    
    def handle_endtag(self, tag):
        if tag in ['h1', 'h2', 'h3', 'a']:
            self.capture_text = False
        self.current_tag = None
    
    def handle_data(self, data):
        if self.capture_text:
            title = data.strip()
            if title and len(title) > 5:  # Filter out very short text
                self.titles.append(title)


def get_symfony_blog_titles():
    """
    Get the latest three blog post titles from symfony.com/blog
    
    This function demonstrates web scraping techniques to extract
    blog post titles from the Symfony website.
    """
    
    try:
        # Make HTTP request to Symfony blog
        url = 'https://symfony.com/blog'
        response = requests.get(url)
        
        # Check if request was successful
        if response.status_code != 200:
            print(f"Error: Failed to fetch page. Status code: {response.status_code}")
            return []
        
        # Parse HTML content using our custom parser
        parser = BlogTitleParser()
        parser.feed(response.text)
        
        # Also try regex patterns as fallback
        if not parser.titles:
            # Look for common blog title patterns with regex
            patterns = [
                r'<h2[^>]*>(.*?)</h2>',          # H2 tags
                r'<h2[^>]*><a[^>]*>(.*?)</a></h2>',  # Links in H2
                r'class="[^"]*title[^"]*"[^>]*>(.*?)<',  # Elements with "title" class
                r'<article[^>]*>.*?<h[23][^>]*>(.*?)</h[23]>',  # Headers in articles
            ]
            
            for pattern in patterns:
                matches = re.findall(pattern, response.text, re.IGNORECASE | re.DOTALL)
                if matches:
                    # Clean up the matched titles
                    for match in matches[:3]:
                        # Remove HTML tags from the match
                        clean_title = re.sub(r'<[^>]+>', '', match).strip()
                        if clean_title and len(clean_title) > 5:
                            parser.titles.append(clean_title)
                    break
        
        return parser.titles[:3]  # Return only the latest 3 titles
        
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return []
    except Exception as e:
        print(f"Error parsing HTML: {e}")
        return []


def demo_with_local_html():
    """
    Demonstration with sample HTML content showing how the parser works
    """
    
    # Sample HTML that mimics a typical blog structure
    sample_html = """
    <!DOCTYPE html>
    <html>
    <head><title>Sample Blog</title></head>
    <body>
        <main>
            <article>
                <h2><a href="/post1">How to Build Better Web Applications with Symfony 7</a></h2>
                <p>Published on January 15, 2024</p>
            </article>
            <article>
                <h2><a href="/post2">Symfony UX: Creating Interactive User Interfaces</a></h2>
                <p>Published on January 10, 2024</p>
            </article>
            <article>
                <h2><a href="/post3">Performance Optimization in Symfony Applications</a></h2>
                <p>Published on January 5, 2024</p>
            </article>
            <article>
                <h2><a href="/post4">Getting Started with Symfony Components</a></h2>
                <p>Published on December 28, 2023</p>
            </article>
        </main>
    </body>
    </html>
    """
    
    print("Demo with sample blog HTML:")
    print("===========================")
    
    # Parse with our custom parser
    parser = BlogTitleParser()
    parser.feed(sample_html)
    
    if parser.titles:
        print("Extracted blog titles:")
        for i, title in enumerate(parser.titles[:3], 1):
            print(f"{i}. {title}")
    else:
        # Fallback to regex
        h2_pattern = r'<h2><a[^>]*>(.*?)</a></h2>'
        titles = re.findall(h2_pattern, sample_html)
        print("Extracted blog titles (using regex):")
        for i, title in enumerate(titles[:3], 1):
            print(f"{i}. {title}")


def demo_with_alternative_site():
    """
    Demonstration using an alternative site that is accessible
    This shows the same technique that would work for Symfony blog
    """
    
    try:
        # Use a demo blog site for testing the scraping technique
        url = 'https://httpbin.org/html'
        response = requests.get(url)
        
        if response.status_code == 200:
            # Parse with our custom parser
            parser = BlogTitleParser()
            parser.feed(response.text)
            
            # Also extract h1 using regex as demo
            h1_pattern = r'<h1>(.*?)</h1>'
            h1_matches = re.findall(h1_pattern, response.text)
            
            print("Demo extraction from test site:")
            if h1_matches:
                for i, title in enumerate(h1_matches[:3], 1):
                    print(f"{i}. {title.strip()}")
            else:
                print("No titles found in demo site")
        
        print("\nNote: This demonstrates the technique.")
        print("For Symfony blog, you would:")
        print("1. Replace URL with 'https://symfony.com/blog'")
        print("2. Inspect the page to find correct HTML patterns")
        print("3. Update the regex patterns or parser logic")
        
    except Exception as e:
        print(f"Demo error: {e}")


if __name__ == "__main__":
    print("Symfony Blog Scraper")
    print("===================")
    
    # Try to get actual Symfony blog titles
    print("\nAttempting to fetch Symfony blog titles...")
    titles = get_symfony_blog_titles()
    
    if titles:
        print("\nLatest 3 Symfony Blog Posts:")
        for i, title in enumerate(titles, 1):
            print(f"{i}. {title}")
    else:
        print("Could not fetch Symfony blog titles.")
        print("This might be due to:")
        print("- Network connectivity issues")
        print("- Site blocking automated requests")
        print("- Changes in site structure")
        
        # Show local demo instead
        print("\n" + "="*50)
        demo_with_local_html()
        
        print("\n" + "="*50)
        demo_with_alternative_site()
    
    print("\nHow to use this script for any blog:")
    print("1. Replace the URL with your target blog")
    print("2. Inspect the page HTML to find title patterns")
    print("3. Update the regex patterns or parser logic")
    print("4. Run the script to extract the titles")