"""Convert docx file to plain text."""

from pathlib import Path

from docx import Document


def docx_to_text(docx_path: str | Path) -> str:
    """Extract all paragraph text from a docx file."""
    doc = Document(docx_path)
    return "\n".join(p.text for p in doc.paragraphs)


def main():
    docx_path = Path("/Users/dev/git/cv/past_cv/PromptEngineer_CV.docx")
    out_path = docx_path.with_suffix(".txt")
    text = docx_to_text(docx_path)
    out_path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
