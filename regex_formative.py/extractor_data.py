import re

# Improved regex patterns with better edge-case handling
patterns = {
    "Valid Emails": r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b",
    "Valid URLs": r"https?://(?:www\.)?[a-zA-Z0-9-]+(?:\.[a-zA-Z]+)+[/\S]*",
    "Valid Phone Numbers": r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",
    "Valid Credit Card Numbers": r"\b(?:\d{4}[-\s]?){3}\d{4}\b",
    "Valid Time Formats": r"\b(?:[01]?\d|2[0-3]):[0-5]\d\b|\b(?:1[0-2]|0?[1-9]):[0-5]\d (?:AM|PM)\b",
    "HTML Tags": r"<\s*[\w]+(?:\s+[^>]*)?>",
    "Hashtags": r"#\w+",
    "Valid Currency Amounts": r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?",
}

# Sample text for testing
sample_text = """
Emails:
 - user@example.com
 - firstname.lastname@company.co.uk
 - invalid@.com
 - @example.com
 - user@com
 - valid.email+alias@domain.org

URLs:
 - https://www.example.com
 - https://subdomain.example.org/page
 - www.example.com
 - http:/example.com

Phone Numbers:
 - (123) 456-7890
 - 123-456-7890
 - 123.456.7890
 - (123 456-7890
 - 123-4567-890

Credit Card Numbers:
 - 1234 5678 9012 3456
 - 1234-5678-9012-3456

Time Formats:
 - 14:30
 - 2:30 PM
 - 23:59
 - 12:60 PM

HTML Tags:
 - <p>
 - <div class="example">
 - <img src="image.jpg" alt="description">

Hashtags:
 - #example
 - #ThisIsAHashtag

Currency Amounts:
 - $19.99
 - $1,234.56
 - $1,234,56
 - 19.99$
"""

# Function to extract and display results
def extract_data(patterns, text):
    for label, pattern in patterns.items():
        matches = re.findall(pattern, text)
        print(f"\n{label}:")
        if matches:
            for match in matches:
                print(" -", match)
        else:
            print(" - No valid matches found.")

# Run the extraction
if __name__ == "__main__":
    extract_data(patterns, sample_text)
