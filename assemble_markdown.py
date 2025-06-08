import json

def main():
    metadata_filepath = 'metadata.json'
    summary_filepath = 'summary_ja.txt'
    body_markdown_filepath = 'body.md'
    output_filepath = 'final_article.md'

    # 1. Read metadata
    try:
        with open(metadata_filepath, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
    except FileNotFoundError:
        print(f"Error: Metadata file not found at {metadata_filepath}")
        # Create a placeholder final_article.md with error
        with open(output_filepath, 'w', encoding='utf-8') as f_err:
            f_err.write(f"# Error: Metadata file '{metadata_filepath}' not found.\n")
        print(output_filepath)
        return
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {metadata_filepath}")
        with open(output_filepath, 'w', encoding='utf-8') as f_err:
            f_err.write(f"# Error: Could not decode JSON from '{metadata_filepath}'.\n")
        print(output_filepath)
        return

    # 2. Read summary
    try:
        with open(summary_filepath, 'r', encoding='utf-8') as f:
            summary_content = f.read().strip()
    except FileNotFoundError:
        print(f"Error: Summary file not found at {summary_filepath}")
        summary_content = f"*Error: Summary file '{summary_filepath}' not found.*" # Placeholder

    # 3. Read body
    try:
        with open(body_markdown_filepath, 'r', encoding='utf-8') as f:
            body_content = f.read().strip()
    except FileNotFoundError:
        print(f"Error: Body markdown file not found at {body_markdown_filepath}")
        body_content = f"*Error: Body markdown file '{body_markdown_filepath}' not found.*" # Placeholder

    # 4. Assemble content
    # Ensure tags are comma-separated string
    tags_list = metadata.get('tags', [])
    if not isinstance(tags_list, list): # Ensure it's a list for processing
        tags_list = [] if not tags_list else [str(tags_list)]


    # Add 'codex' if not present
    if 'codex' not in [tag.lower() for tag in tags_list]: # Case-insensitive check
        tags_list.insert(0, 'codex') # Add to the beginning

    # Remove duplicates while preserving order (for Python 3.7+)
    seen_tags = set()
    unique_tags = []
    for tag in tags_list:
        if tag.lower() not in seen_tags:
            unique_tags.append(tag)
            seen_tags.add(tag.lower())

    tags_string = ", ".join(unique_tags)

    # Use .get for image URL as it was named 'og_image_url' in metadata.json
    image_url = metadata.get('og_image_url', metadata.get('image', ''))


    output_parts = [
        "<!-- metadata -->",
        f"- **title**: {metadata.get('title', '')}",
        f"- **source**: {metadata.get('source_url', '')}", # source_url in metadata.json
        f"- **author**: {metadata.get('author', '')}",
        f"- **published**: {metadata.get('published_date', '')}", # published_date in metadata.json
        f"- **fetched**: {metadata.get('fetched_utc', '')}", # fetched_utc in metadata.json
        f"- **tags**: {tags_string}",
        f"- **image**: {image_url}", # Use the retrieved image_url
        "",
        "## 要約",
        summary_content,
        "",
        "## 本文",
        body_content
    ]

    final_markdown = "\n\n".join(output_parts) # Use double newline for better paragraph separation in Markdown

    # 5. Save to final_article.md
    try:
        with open(output_filepath, 'w', encoding='utf-8') as f:
            f.write(final_markdown)
        print(f"Successfully assembled Markdown and saved to {output_filepath}")
    except IOError as e:
        print(f"Error writing final Markdown to file: {e}")
        print(output_filepath) # Still output filename
        return

    # print(output_filepath) # As per original script outline

if __name__ == '__main__':
    main()
