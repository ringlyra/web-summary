from readability import Document
from markdownify import markdownify as md

def main():
    html_filepath = 'fetched_page.html'
    output_markdown_file = 'body.md'

    try:
        with open(html_filepath, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {html_filepath}")
        # Create an empty body.md or one with an error message
        with open(output_markdown_file, 'w', encoding='utf-8') as f_err:
            f_err.write(f"# Error: Source HTML file '{html_filepath}' not found.\n")
        print(output_markdown_file) # Output filename even in error case as per subtask implied requirement
        return

    # Extract main content using readability
    doc = Document(html_content)
    main_content_html = doc.summary()

    # Convert the main content HTML to Markdown
    # Options can be passed to markdownify, e.g., heading_style, bullets, etc.
    # Using default options here for simplicity.
    markdown_body = md(main_content_html, heading_style='atx')

    # (Optional) Perform any cleanup on markdown_body if necessary.
    # For example, stripping extra newlines:
    markdown_body = markdown_body.strip()

    # Save to body.md
    try:
        with open(output_markdown_file, 'w', encoding='utf-8') as f:
            f.write(markdown_body)
        print(f"Successfully converted main content to Markdown and saved to {output_markdown_file}")
    except IOError as e:
        print(f"Error writing Markdown to file: {e}")
        # Even if write fails, try to output filename
        print(output_markdown_file)
        return

    # print(output_markdown_file) # As per original script outline in prompt

if __name__ == '__main__':
    main()
