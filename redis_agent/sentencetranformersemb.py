import os
from sentence_transformers import SentenceTransformer
import numpy as np
from google.adk.tools import ToolContext

def embed_query_tool(query: str,) -> dict:
    """
    Tool per embedizzare una query usando LO STESSO MODELLO del database Redis.
    
    Args:
        query: Testo della query da embedizzare
        
    Returns:
        Dict con solo query_embedding
    """
    try:
        # USA LO STESSO MODELLO del database Redis!
        model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
        
        # Genera embedding (stesso formato del database)
        embedding = model.encode([query])
        
        # Converte in formato compatibile
        embedding_vector = embedding[0].astype(np.float32).tolist()
        
        return {'query_embedding': embedding_vector}
        
    except Exception as e:
        return {'query_embedding': []}