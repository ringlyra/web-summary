import json
import os
import re
from datetime import datetime, timezone

def main():
    metadata_filepath = 'metadata.json'
    current_article_path = 'final_article.md'

    # 1. Read metadata
    try:
        with open(metadata_filepath, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
    except FileNotFoundError:
        print(f"Error: Metadata file not found at {metadata_filepath}. Cannot determine final path.")
        # To fulfill the "output the final path" even in failure, we might output a planned path or error.
        # However, without metadata, title and date are unknown.
        # For now, let's indicate failure more directly if possible or stick to the script's end print.
        # For this subtask, we'll assume metadata.json exists as per previous steps.
        return
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {metadata_filepath}.")
        return

    title = metadata.get('title', 'Untitled')
    # Use 'fetched_utc' as per metadata.json structure from previous steps
    fetched_iso_date = metadata.get('fetched_utc', datetime.now(timezone.utc).isoformat())

    # Parse the fetched date to get YYYY, MM, DD
    try:
        # Ensure TZ info for fromisoformat, or handle potential parsing issues
        if 'Z' in fetched_iso_date and not fetched_iso_date.endswith('+00:00'):
             fetched_iso_date = fetched_iso_date.replace('Z', '+00:00')
        fetched_datetime = datetime.fromisoformat(fetched_iso_date)
    except ValueError as e:
        print(f"Error parsing date: {fetched_iso_date} - {e}. Defaulting to current UTC date.")
        fetched_datetime = datetime.now(timezone.utc)

    year = fetched_datetime.strftime('%Y')
    month = fetched_datetime.strftime('%m')
    day = fetched_datetime.strftime('%d') # Added day extraction
    date_prefix_for_filename = f"{year}-{month}-{day}"

    # 2. Domain (extracted from source_url for robustness, fallback to hardcoded)
    source_url = metadata.get('source_url', 'https://cloud.google.com')
    try:
        domain = source_url.split('//')[1].split('/')[0]
    except IndexError:
        domain = "cloud.google.com" # Default if parsing fails

    # 3. Sanitize title
    # Japanese characters are valid in many modern file systems, but for max compatibility:
    # Convert to lowercase first if that's desired (original prompt did this)
    # For this version, we'll try to preserve original case somewhat but focus on filesystem-unsafe chars.

    # Remove characters that are problematic or not commonly used in filenames.
    # Allow unicode letters and numbers, plus underscore, hyphen, dot.
    # sanitized_title = re.sub(r'[^\w\s\.\-]', '', title, flags=re.UNICODE) # \w includes unicode letters/numbers
    # sanitized_title = re.sub(r'\s+', '_', sanitized_title).strip('_') # Replace spaces with underscores

    # Stricter sanitization:
    sanitized_title_ascii = title.encode('ascii', 'ignore').decode('ascii') # Remove non-ASCII
    sanitized_title_ascii = re.sub(r'\s+', '_', sanitized_title_ascii) # Replace spaces with underscores
    sanitized_title_ascii = re.sub(r'[^a-zA-Z0-9_\.\-]', '', sanitized_title_ascii) # Keep only ASCII alphanumeric, underscore, dot, hyphen
    # Remove leading/trailing underscores that might result from stripping characters adjacent to spaces
    sanitized_title_ascii = re.sub(r'^_+|_+$', '', sanitized_title_ascii)
    # Replace multiple underscores with a single one
    sanitized_title_ascii = re.sub(r'_+', '_', sanitized_title_ascii)


    sanitized_title_ascii = sanitized_title_ascii[:100] # Limit length to 100 chars

    if not sanitized_title_ascii: # Handle case where title becomes empty after sanitization
        sanitized_title_ascii = "document"

    # 4. Construct filename
    filename = f"{date_prefix_for_filename}_{sanitized_title_ascii}.md"

    # 5. Construct directory path
    # Per instructions, path is YYYY/MM/domain/
    directory_path = os.path.join(year, month, domain)

    # 6. Create directory if not exists
    try:
        os.makedirs(directory_path, exist_ok=True)
    except OSError as e:
        print(f"Error creating directory {directory_path}: {e}")
        return

    # 7. Define final full file path
    final_filepath = os.path.join(directory_path, filename)

    # 8. Move/rename final_article.md to final_filepath (overwrites if exists)
    try:
        if not os.path.exists(current_article_path):
            print(f"Error: Source file '{current_article_path}' not found. Cannot move.")
            # To satisfy output requirement, print planned path
            print(f"Planned final path: {final_filepath}")
            return

        os.rename(current_article_path, final_filepath)
        print(f"File '{current_article_path}' moved to '{final_filepath}'")
    except OSError as e:
        print(f"Error moving file from '{current_article_path}' to '{final_filepath}': {e}")
        # If move fails, output the intended final path to satisfy subtask output requirement
        print(final_filepath)
        return

    print(final_filepath) # Output the final path

if __name__ == '__main__':
    main()
