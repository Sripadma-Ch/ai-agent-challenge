****AI-AGENT-CHALLENGE**** 

1. Project Title & Description

AI Agent Challenge – PDF Bank Statement Parser

This project extracts structured data (Date, Description, Debit, Credit, Balance) from ICICI bank PDF statements and saves it as a CSV file.  
It also includes automated tests written with pytest.


2. Folder Structure

Show users where key files are.

 📂 Project Structure

ai-agent-challenge/ 
├── pdf_parser.py        # Main script for parsing PDFs 
├── test_parser.py       # Unit tests using pytest 
├── data/ │  
 └── icici/ │       
 ├── icici Sample.pdf   # Example input PDF │       
 └── result.csv         # Extracted CSV output 
 └── README.md



3. Installation Instructions

 🔧 Installation

Clone the repo and install dependencies:

bash
git clone https://github.com/Sripadma-Ch/ai-agent-challenge.git
cd ai-agent-challenge
pip install -r requirements.txt

(Create `requirements.txt` with: `pdfplumber`, `pandas`, `pytest`)


4. Usage

🚀 Usage

Run the parser on the sample ICICI PDF:

python pdf_parser.py

This will generate:

data/icici/result.csv

Preview the data in Python:

import pandas as pd
df = pd.read_csv("data/icici/result.csv")
print(df.head())



5. Running Tests

🧪 Running Tests

To verify the parser works correctly:

python -m pytest -v

Expected output:

test_parser.py::test_parse_creates_dataframe PASSED
test_parser.py::test_parse_saves_csv PASSED


6. Future Work / Notes (optional)

 📌 Future Improvements
- Handle more banks (HDFC, SBI, etc.)
- Improve text extraction accuracy
- Add an AI agent to categorize expenses




---

✅ With this, anyone visiting your repo can:

Understand what it does

Install dependencies

Run code and tests



