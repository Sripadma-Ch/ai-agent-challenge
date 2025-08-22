import pandas as pd
import pdfplumber

def parse(pdf_path):
    rows = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text().splitlines()
            for line in text:
                # Splitting line into words (basic parsing)
                parts = line.split()
                rows.append(parts)
    df = pd.DataFrame(rows)
    return df


if __name__ == "__main__":
    input_pdf = r"C:\Users\srima\ai-agent-challenge\data\icici\icici sample.pdf"
    output_csv = r"C:\Users\srima\ai-agent-challenge\data\icici\result.csv"

    df = parse(input_pdf)
    df.to_csv(output_csv, index=False)
    print(f"✅ Extracted data saved to {output_csv}")