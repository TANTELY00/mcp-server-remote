from mcp.server.fastmcp import FastMCP
from tavily import TavilyClient
from dotenv import load_dotenv
import os
from typing import List, Dict

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

mcp = FastMCP('http-mcp-server', host='127.0.0.1', port=23000)
tavily_api_key = os.environ.get("TAVILY_API_KEY")

if tavily_api_key is None:
    raise ValueError("La variable d'environnement TAVILY_API_KEY n'est pas définie !")

web_search_client = TavilyClient(api_key=tavily_api_key)

# get informations about the employe 
@mcp.tool()
def get_employee_info(name: str) -> Dict:
    """
    Get information about  given employee  .
    Args:
        name (str): The name of the employee.
    Returns:
        Dict: A dictionary containing employee information.    
    """
    return {
        "name": name,
        "age": 30,
        "position": "Software Engineer"
    }


# search the web for recent information
@mcp.tool()
def web_search(query: str) -> List[Dict]:
    """
    Search the web for given query.ra
    Args:
        query (str): The search query.
    Returns:
        List[Dict]: A list of search results.
    """
    try:
        response = web_search_client.search(query=query)
        return response["results"]
    except :
        return "No results found"
    
if __name__ == '__main__':
    mcp.run(transport='sse') 

