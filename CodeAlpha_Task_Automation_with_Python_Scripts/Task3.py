import re
import os
import csv

def extract_emails_from_file():
    print("=" * 60)
    print("Email Address Extractor")
    print("=" * 60)
    
    input_file = input("\nEnter input file path (with .txt extension): ").strip()
    
    if not os.path.exists(input_file):
        print(f"❌ File '{input_file}' not found.")
        return
    
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            content = file.read()
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return
    
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(email_pattern, content)
    
    if not emails:
        print("⚠️  No emails found in the file.")
        return
    
    unique_emails = list(set(emails))
    unique_emails.sort()
    
    print(f"\n✅ Found {len(unique_emails)} unique email(s):\n")
    for idx, email in enumerate(unique_emails, 1):
        print(f"{idx}. {email}")
    
    output_file = input("\nEnter output file name (without extension): ").strip()
    
    save_option = input("\nChoose format:\n1. Text file (.txt)\n2. CSV file (.csv)\n3. Both\n\nEnter choice (1/2/3): ").strip()
    
    if save_option in ["1", "3"]:
        output_txt = f"{output_file}.txt"
        try:
            with open(output_txt, "w", encoding="utf-8") as file:
                file.write("EXTRACTED EMAILS\n")
                file.write("=" * 50 + "\n")
                file.write(f"Total Emails: {len(unique_emails)}\n")
                file.write(f"Date: {__import__('datetime').datetime.now()}\n")
                file.write("=" * 50 + "\n\n")
                for idx, email in enumerate(unique_emails, 1):
                    file.write(f"{idx}. {email}\n")
            print(f"✅ Saved to {output_txt}")
        except Exception as e:
            print(f"❌ Error saving to txt: {e}")
    
    if save_option in ["2", "3"]:
        output_csv = f"{output_file}.csv"
        try:
            with open(output_csv, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Email", "Index"])
                for idx, email in enumerate(unique_emails, 1):
                    writer.writerow([email, idx])
            print(f"✅ Saved to {output_csv}")
        except Exception as e:
            print(f"❌ Error saving to csv: {e}")

if __name__ == "__main__":
    extract_emails_from_file()