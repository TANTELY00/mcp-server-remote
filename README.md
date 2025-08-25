

## INSTALLATION DES DÉPENDANCES

* Installation de **uv** :

  ```bash
  pip install uv
  ```

* Initialiser un projet avec **uv** :

  ```bash
  uv init
  ```

* Installer les dépendances définies dans le projet :

  ```bash
  uv sync
  ```

---

## CRÉATION ET ACTIVATION DE L’ENVIRONNEMENT VIRTUEL

* Créer un environnement virtuel :

  ```bash
  uv venv
  ```

* Activer l’environnement virtuel :

  ```bash
  source .venv/bin/activate
  ```

---

## AJOUT DES COMMANDES MCP

* Ajouter les commandes **MCP CLI** :

  ```bash
  uv add "mcp[cli]"
  ```

---

## GESTION DES VARIABLES D’ENVIRONNEMENT

* Installer **python-dotenv** pour accéder aux variables définies dans un fichier `.env` :

  ```bash
  uv add python-dotenv
  ```

---

## INSTALLATION DE LA DÉPENDANCE TAVILY

* Installer **tavily-python** pour effectuer des recherches sur le web :

  ```bash
  uv add tavily-python
  ```

---

## TEST DES TOOLS DU SERVEUR MCP

* Pour tester les outils disponibles sur le serveur MCP, installer **mcp-inspector** :

  ```bash
  npx @modelcontextprotocol/inspector@0.15
  ```

---

