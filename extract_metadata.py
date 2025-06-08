import json
from bs4 import BeautifulSoup
import datetime

def extract_metadata(html_filepath, source_url):
    metadata = {
        "title": "",
        "author": "cloud.google.com", # Default author
        "published_date": "",
        "og_image_url": "",
        "source_url": source_url,
        "fetched_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "tags": ["codex"]
    }

    try:
        with open(html_filepath, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {html_filepath}")
        return metadata # Return default metadata with error indication or handle as preferred

    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract Title
    if soup.title and soup.title.string:
        metadata["title"] = soup.title.string.strip()
    else:
        h1_tag = soup.find('h1')
        if h1_tag and h1_tag.string:
            metadata["title"] = h1_tag.string.strip()
        else:
            # Fallback for title if no <title> or <h1> is found
            og_title = soup.find("meta", property="og:title")
            if og_title and og_title.get("content"):
                metadata["title"] = og_title.get("content").strip()
            else:
                twitter_title = soup.find("meta", attrs={"name": "twitter:title"})
                if twitter_title and twitter_title.get("content"):
                    metadata["title"] = twitter_title.get("content").strip()


    # Extract Author
    author_meta_selectors = [
        {"name": "author"},
        {"property": "article:author"},
        {"name": "twitter:creator"}
    ]
    for selector in author_meta_selectors:
        author_tag = soup.find("meta", attrs=selector)
        if author_tag and author_tag.get("content"):
            metadata["author"] = author_tag.get("content").strip()
            break

    # Extract Published Date
    # Order of preference for date extraction
    date_selectors = [
        {"property": "article:published_time"},
        {"property": "og:article:published_time"},
        {"name": "publishdate"},
        {"name": "date"},
        {"name": "DC.date.issued"},
        {"itemprop": "datePublished"}
    ]

    found_date = None
    for selector in date_selectors:
        date_tag = soup.find("meta", attrs=selector)
        if date_tag and date_tag.get("content"):
            found_date = date_tag.get("content").strip()
            break

    if not found_date:
        time_tag = soup.find("time")
        if time_tag and time_tag.get("datetime"):
            found_date = time_tag.get("datetime").strip()

    if found_date:
        try:
            # Attempt to parse and reformat to ISO 8601
            # This handles various common date formats but might need to be more robust
            # For now, we'll assume it's close to ISO or directly usable if parsable
            # A more robust solution would try multiple parsing patterns
            dt_object = datetime.datetime.fromisoformat(found_date.replace("Z", "+00:00"))
            metadata["published_date"] = dt_object.isoformat()
        except ValueError:
            # If parsing fails, store the original string if it's not empty
            # Or decide on a specific format like YYYY-MM-DD
            # For now, keeping it simple and storing as found if not parsable
            # but we aim for ISO 8601, so if it's not that, it might be better to leave it empty or log an error
            # For this task, we'll try to extract just date part if it's a complex string
            try:
                # Simplistic attempt to get YYYY-MM-DD
                parsed_date = datetime.datetime.strptime(found_date.split("T")[0], "%Y-%m-%d")
                metadata["published_date"] = parsed_date.strftime("%Y-%m-%d")
            except ValueError:
                 # Try another common format like "Month D, YYYY"
                try:
                    parsed_date = datetime.datetime.strptime(found_date, "%B %d, %Y")
                    metadata["published_date"] = parsed_date.strftime("%Y-%m-%d")
                except ValueError:
                    # If specific parsing fails, keep as is if it's a simple YYYY-MM-DD
                    if len(found_date) == 10 and found_date.count('-') == 2:
                         metadata["published_date"] = found_date
                    else:
                        # Try to find a date in a class like 'article-timestamp' or similar
                        date_span = soup.find(lambda tag: tag.name == 'span' and 'date' in tag.get('class', []))
                        if date_span and date_span.string:
                             metadata["published_date"] = date_span.string.strip() # Store as is for now
                        else:
                            # Final attempt looking for text like "最終更新日 YYYY-MM-DD"
                            import re
                            # Try to find any <p> tag containing the date string
                            p_date_tags = soup.find_all(lambda tag: tag.name == 'p' and "最終更新日" in tag.get_text())
                            for p_tag in p_date_tags:
                                match = re.search(r"最終更新日 (\d{4}-\d{2}-\d{2})", p_tag.get_text())
                                if match:
                                    metadata["published_date"] = match.group(1)
                                    break # Found, no need to check other p_tags

                            if not metadata["published_date"]: # If not found in any <p> tag
                                # Fallback to searching all text if specific <p> tag doesn't match format
                                page_text = soup.get_text()
                                match = re.search(r"最終更新日 (\d{4}-\d{2}-\d{2})", page_text)
                                if match:
                                    metadata["published_date"] = match.group(1)
                                elif found_date: # only print warning if a candidate date was found but not parsed
                                    print(f"Warning: Could not parse found date string: {found_date}")
                            # Ensure found_date warning is only printed if nothing was assigned and a candidate existed
                            elif not metadata["published_date"] and found_date:
                                print(f"Warning: Could not parse found date string: {found_date}")


    # Extract Open Graph Image URL
    og_image_tag = soup.find("meta", property="og:image")
    if og_image_tag and og_image_tag.get("content"):
        metadata["og_image_url"] = og_image_tag.get("content").strip()
    else:
        # Fallback to other image meta tags if og:image is not found
        twitter_image_tag = soup.find("meta", attrs={"name": "twitter:image"})
        if twitter_image_tag and twitter_image_tag.get("content"):
            metadata["og_image_url"] = twitter_image_tag.get("content").strip()
        else:
            # Fallback to the first large image if no meta tags are found
            # This is a heuristic and might not always pick the best image
            img_tag = soup.find("img", {"src": True}) # A very generic fallback
            if img_tag:
                 metadata["og_image_url"] = img_tag["src"]


    return metadata

if __name__ == "__main__":
    html_file = "fetched_page.html"
    source = "https://cloud.google.com/generative-ai-app-builder/docs/enterprise-search-introduction?hl=ja"

    extracted_data = extract_metadata(html_file, source)

    output_filename = "metadata.json"
    with open(output_filename, 'w', encoding='utf-8') as f_json:
        json.dump(extracted_data, f_json, ensure_ascii=False, indent=4)

    print(f"Metadata extracted and saved to {output_filename}")
