import faiss
import numpy as np

from sentence_transformers import SentenceTransformer

from .loader import load_documents


class DocumentRetriever:

    def __init__(self):

        self.documents = load_documents()

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        texts = [
            document["text"]
            for document in self.documents
        ]

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True
        )

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.index.add(
            np.array(embeddings).astype("float32")
        )

    def search(self, query, top_k=2):

        query_embedding = self.model.encode(
            [query],
            convert_to_numpy=True
        )

        distances, indices = self.index.search(
            np.array(query_embedding).astype("float32"),
            top_k
        )

        results = []

        for index in indices[0]:

            if index < len(self.documents):

                results.append(
                    self.documents[index]
                )

        return results