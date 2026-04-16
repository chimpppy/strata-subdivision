"""
extract_pdf_text.py
-------------------
Scaffold script to extract text from a PDF file using PyPDF2.

Usage:
    python extract_pdf_text.py <path_to_pdf>

Output:
    A .txt file written to the same directory as the input PDF,
    with the same base name (e.g. "document.pdf" -> "document.txt").

Install dependency before running:
    pip install PyPDF2
"""

import sys
import os


def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract all text from a PDF and return as a single string."""
    import PyPDF2

    text_parts = []
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page_num, page in enumerate(reader.pages, start=1):
            page_text = page.extract_text() or ""
            text_parts.append(f"--- Page {page_num} ---\n{page_text}")

    return "\n\n".join(text_parts)


def write_text_output(pdf_path: str, text: str) -> str:
    """Write extracted text to a .txt file alongside the PDF. Returns output path."""
    base, _ = os.path.splitext(pdf_path)
    output_path = base + ".txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path


def main():
    if len(sys.argv) != 2:
        print("Usage: python extract_pdf_text.py <path_to_pdf>")
        sys.exit(1)

    pdf_path = sys.argv[1]

    if not os.path.isfile(pdf_path):
        print(f"ERROR: File not found: {pdf_path}")
        sys.exit(1)

    if not pdf_path.lower().endswith(".pdf"):
        print(f"ERROR: Input must be a .pdf file: {pdf_path}")
        sys.exit(1)

    print(f"Extracting text from: {pdf_path}")
    text = extract_text_from_pdf(pdf_path)

    output_path = write_text_output(pdf_path, text)
    print(f"Text written to: {output_path}")


if __name__ == "__main__":
    main()
