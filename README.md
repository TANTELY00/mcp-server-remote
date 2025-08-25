INSTALLATION DES DEPENDANCES  : 

- installation de uv : pip install uv
- initialiser uv dans un proje : uv init 
- pour installer les dependances definie dans le projet : uv sync 

CREATION et ACTIVATION DE LA VARIABLE D'ENVIRONNEMENT 
- uv venv 
- source .venv/bin/activate

DEMANDE A UV D'AJOUTER LES COMMANDE MCP 
- uv add "mcp[cli]"

INSTALLATION DE LA DEPENDANCE DOTENV POUR AVOIR ACCEDER DANS LE FICHIER .ENV COMME VARIABLE D'ENVIRONNEMENT 
- uv add python-dotenv 

INSTALLATION DE LA DEPENDANCE TAVILY POUR AVOIR ACCEDER A LAL RECHERCHE SUR WEB 
- uv add tavily-python 

POUR FAIRE UN TESTE DES TOOLS DANS LE SERVEUR , il faut installer 
-  npx @modelcontextprotocol/inspector@0.15  



