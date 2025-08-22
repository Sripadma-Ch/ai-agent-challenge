import os
import pandas as pd
from pdf_parser import parse

def test_parse_creates_dataframe():
    pdf_path = "data/icici/icici Sample.pdf"
    df = parse(pdf_path)
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0   # At least one row should be extracted

def test_parse_saves_csv():
    pdf_path = "data/icici/icici Sample.pdf"
    csv_path = "data/icici/test_output.csv"
    
    df = parse(pdf_path)
    df.to_csv(csv_path, index=False)
    
    assert os.path.exists(csv_path)
    os.remove(csv_path)  # cleanup