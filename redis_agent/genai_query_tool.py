import os
import google.genai as genai
from google.genai.types import EmbedContentConfig
from google.adk.tools import ToolContext

def embed_query_tool(query: str,) -> dict:
    """
    Tool per embedizzare una query usando Google AI.
    
    
    Args:
        query: Testo della query da embedizzare
    
    Returns:
        Dict con embedding e metadati
    """
    try:
        # Configura client
        client = genai.Client()
        
        # Genera embedding
        response = client.models.embed_content(
            model="gemini-embedding-001",
            contents=query,
            config=EmbedContentConfig(
                task_type="RETRIEVAL_QUERY",
                output_dimensionality=3072
            )
        )
        
        # Estrai embedding
        embedding = response.embeddings[0].values
        
        return {'query': embedding}
        
    except Exception as e:
        return []