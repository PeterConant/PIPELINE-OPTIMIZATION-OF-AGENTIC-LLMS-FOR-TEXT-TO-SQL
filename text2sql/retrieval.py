from pathlib import Path

from sentence_transformers import SentenceTransformer

import numpy as np
import faiss
import json

################## EMBEDDINGS SIMILARITY #########################

EMBEDDINGS_DIR = Path(__file__).resolve().parent.parent / 'data' / 'embeddings'

file_name = 'csv_table_descriptions'
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

embeddings = np.load(EMBEDDINGS_DIR / f'{file_name}.npy')
with open(EMBEDDINGS_DIR / f'{file_name}.json', 'r') as f:
    table_metadata = json.load(f) #list of {'table':table_name, 'chunk'=chunk_to_be(or_has_been)_embedded}

dimension = embeddings.shape[1]
index = faiss.IndexFlatIP(dimension)
index.add(embeddings.astype('float32'))

faiss.normalize_L2(embeddings)
index = faiss.IndexFlatIP(embeddings.shape[1])
index.add(embeddings.astype('float32'))

def get_tables_semantic_search(query, k=10):
    query_embedding = embedding_model.encode([query], convert_to_numpy=True)
    query_embedding = query_embedding.astype('float32')
    faiss.normalize_L2(query_embedding)

    D, I = index.search(query_embedding, k)

    retrieved_tables = []
    for rank, idx in enumerate(I[0]):

        table_name = table_metadata[idx]['table']
        retrieved_tables.append(table_name)

    return retrieved_tables
