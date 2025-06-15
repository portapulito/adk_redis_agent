# redis_agent/agent.py
import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, SseServerParams
from . genai_query_tool import embed_query_tool
# Configurazione dell'agente Redis
root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='redis_assistant_agent',
    instruction='''Sei un assistente Redis che aiuta gli utenti a gestire e cercare dati in Redis in modo efficiente. 
    Puoi aiutare con:
    - Memorizzazione e recupero di stringhe, hash, liste, set, sorted set
    - Gestione di Redis streams e pub/sub
    - Lavoro con documenti JSON
    - Operazioni di ricerca vettoriale
    - Gestione generale del server Redis
    
    Usa il linguaggio naturale per interagire con le strutture dati Redis.''',
    tools=[
        MCPToolset(
            connection_params=SseServerParams(
                url="http://127.0.0.1:8000/sse"
            )
        ), embed_query_tool
    ]
)
