from pathlib import Path


DOCUMENTS_PATH = Path("data/documents")


def load_documents():

    documents = []

    for file_path in DOCUMENTS_PATH.glob("*.txt"):

        text = file_path.read_text(
            encoding="utf-8"
        )

        documents.append({
            "filename": file_path.name,
            "text": text
        })

    return documents