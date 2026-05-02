import os
import re
from datetime import datetime
from openai import OpenAI

# 1. Configuration
DEEPSEEK_API_KEY = "sk-8274c2e3c1894382afdbf62f409673a5"
POSTS_DIR = "./_posts" 

client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com"
)

def slugify(text):
    """Converts a string to a URL-friendly slug for Jekyll filenames."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text

def generate_longtail_keywords(topic):
    print(f"--- Brainstorming long-tail niches for: {topic} ---")
    prompt = (
        f"Generate 50 highly specific, 'long-tail' shopping list topics for {topic}. "
        "Each should include a specific persona and a specific need. "
        "Format: Just the keywords, one per line, no numbers."
    )
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip().split('\n')

def generate_blog_post(keyword):
    print(f"--- Generating Jekyll post for: {keyword} ---")
    prompt = (
        f"Write a comprehensive shopping guide blog post for: {keyword}. "
        "Structure: \n"
        "1. Bulleted shopping list of essential items.\n"
        "2. Detailed 'Buying Guide' section explaining the logic for each item.\n"
        "Use Markdown headers (##) and bold text for readability. No intro or outro."
    )
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def save_to_jekyll(keyword, content):
    if not os.path.exists(POSTS_DIR):
        os.makedirs(POSTS_DIR)

    date_str = datetime.now().strftime("%Y-%m-%d")
    slug = slugify(keyword)
    filename = f"{date_str}-{slug}.md"
    filepath = os.path.join(POSTS_DIR, filename)

    front_matter = (
        f"---\n"
        f"layout: post\n"
        f"title: \"The Ultimate Shopping Guide for {keyword}\"\n"
        f"date: {date_str}\n"
        f"categories: guides\n"
        f"--- \n\n"
    )
    
    full_content = front_matter + content

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(full_content)
    
    print(f"Successfully saved to: {filepath}")

if __name__ == '__main__':
    main_topic = "gardening for new homeowners"
    keywords = generate_longtail_keywords(main_topic)
    for kw in keywords:
        clean_kw = kw.strip().lstrip('123456789. ')
        if clean_kw:
            post_markdown = generate_blog_post(clean_kw)
            save_to_jekyll(clean_kw, post_markdown)
