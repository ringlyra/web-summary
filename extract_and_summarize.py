from readability import Document
from bs4 import BeautifulSoup
import re

def extract_plain_text(html_filepath):
    try:
        with open(html_filepath, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {html_filepath}")
        return ""

    doc = Document(html_content)
    main_text_html = doc.summary()

    soup = BeautifulSoup(main_text_html, 'html.parser')
    plain_text = soup.get_text(separator='\n', strip=True)
    return plain_text

def generate_placeholder_summary(text, num_sentences=5, max_chars=1000):
    """
    Generates a placeholder summary.
    Takes the first few sentences or up to max_chars,
    and applies some basic keyword highlighting.
    """
    if not text:
        return "コンテンツの抽出に失敗したため、要約を生成できませんでした。"

    # Simple sentence splitting (can be improved)
    sentences = re.split(r'(?<=[。！？])\s*', text)

    summary_sentences = []
    current_char_count = 0

    for sentence in sentences:
        if not sentence.strip():
            continue
        if len(summary_sentences) < num_sentences and (current_char_count + len(sentence)) <= max_chars:
            summary_sentences.append(sentence)
            current_char_count += len(sentence)
        else:
            break

    summary = "\n".join(summary_sentences)

    # Add some placeholder keyword highlighting (very basic)
    keywords = ["Vertex AI Search", "Google Cloud", "検索", "レコメンデーション", "データストア", "アプリ", "LLM"]
    for keyword in keywords:
        summary = summary.replace(keyword, f"**{keyword}**")

    if not summary.strip():
        return "抽出されたコンテンツが短すぎるため、要約を生成できませんでした。"

    return summary

if __name__ == "__main__":
    html_file = "fetched_page.html"
    output_summary_file = "summary_ja.txt"

    plain_text_content = extract_plain_text(html_file)

    if plain_text_content:
        # In a real scenario, this text would be fed to an LLM for summarization.
        # For now, we use a placeholder.
        # The prompt for an LLM would be something like:
        # "以下の日本語のテキストを包括的に要約してください。著者が伝えようとしていることをすべて捉え、
        # 重要なキーワードをMarkdownの太字（**キーワード**）で強調してください。要約は、エージェントが理解しやすいように、
        # あまり短くしすぎないでください。"

        summary_text = generate_placeholder_summary(plain_text_content)

        try:
            with open(output_summary_file, 'w', encoding='utf-8') as f:
                f.write(summary_text)
            print(f"Summary saved to {output_summary_file}")
        except IOError as e:
            print(f"Error writing summary to file: {e}")
    else:
        print("Could not extract plain text, so no summary was generated.")
        # Create an empty summary file or a file with an error message
        try:
            with open(output_summary_file, 'w', encoding='utf-8') as f:
                f.write("コンテンツの抽出に失敗したため、要約を生成できませんでした。")
            print(f"Error message saved to {output_summary_file}")
        except IOError as e:
            print(f"Error writing error message to file: {e}")
