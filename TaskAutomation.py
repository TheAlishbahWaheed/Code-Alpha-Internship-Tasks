import re
import os

INPUT_FILE = "data.txt"
OUTPUT_FILE = "emails.txt"

EMAIL_PATTERN = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

def extract_emails(text):
    """Extract unique email addresses from text."""
    emails = re.findall(EMAIL_PATTERN, text)
    return sorted(set(emails))  # remove duplicates + sort


def read_file(file_path):
    """Read file safely."""
    if not os.path.exists(file_path):
        print(f"❌ Error: {file_path} not found!")
        return None

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def write_emails(file_path, emails):
    """Write emails to output file."""
    with open(file_path, "w", encoding="utf-8") as file:
        for email in emails:
            file.write(email + "\n")


def main():
    content = read_file(INPUT_FILE)

    if content is None:
        return

    emails = extract_emails(content)

    if not emails:
        print("⚠️ No email addresses found.")
        return

    write_emails(OUTPUT_FILE, emails)

    print("✅ Email extraction completed successfully!")
    print(f"📧 Total unique emails found: {len(emails)}")
    print(f"📁 Saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> 45eb687dea236f23616506b3be9f552e95444886
