# agent.py
import argparse
import importlib
import pandas as pd
import subprocess
import sys
import os

MAX_ATTEMPTS = 3

def run_agent(target: str):
    pdf_path = r"C:\Users\srima\ai-agent-challenge\data\icici\icici sample.pdf"
    csv_path = r"C:\Users\srima\ai-agent-challenge\data\icici\result.csv"
    parser_module = r"C:\Users\srima\ai-agent-challenge\pdf_parser.py"

    # Check input files exist
    if not os.path.exists(pdf_path) or not os.path.exists(csv_path):
        print(f"❌ Missing required files for target '{target}'")
        sys.exit(1)

    # Agent Loop: plan → generate (import parser) → run test → self-fix
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            print(f"\n🔄 Attempt {attempt}...")
            parser = importlib.import_module(parser_module)
            df = parser.parse(pdf_path)

            # Save output for inspection
            out_csv = f"result_{target}.csv"
            df.to_csv(out_csv, index=False)
            print(f"✅ Parser ran successfully, saved {out_csv}")

            # Run test script
            subprocess.run([sys.executable, "test_parser.py", "--target", target], check=True)
            print("🎉 All tests passed! Agent finished.")
            return
        except Exception as e:
            print(f"⚠ Error during attempt {attempt}: {e}")
            if attempt == MAX_ATTEMPTS:
                print("❌ Agent failed after maximum attempts.")
                sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Agent Challenge Runner")
    parser.add_argument("--target", required=True, help="icici")
    args = parser.parse_args()


    run_agent(args.target)
