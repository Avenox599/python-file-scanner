# 📂 File Analyser

Un outil simple et efficace en **Python** pour scanner le contenu d'un répertoire, vérifier l'intégrité des fichiers et générer des rapports détaillés.

## ✨ Fonctionnalités

* **Scan intelligent** : Analyse tous les fichiers d'un dossier spécifié.
* **Vérification d'état** : Identifie si un fichier est plein, vide ou s'il génère une erreur de lecture.
* **Lecture en direct** : Affiche le contenu des fichiers texte directement dans la console pendant le scan.
* **Génération de Rapports** : Crée automatiquement deux fichiers de synthèse :
    * `rapport.txt` : Un résumé clair et lisible.
    * `rapport.json` : Une version structurée pour une exploitation informatique.
* **Auto-exclusion** : Le script ignore intelligemment son propre fichier et les rapports générés pour éviter de fausser les statistiques.

## 🚀 Installation & Utilisation

### Prérequis
* **Python 3.x** installé sur votre système.
* Aucune bibliothèque externe n'est requise (utilise uniquement la bibliothèque standard).

### Utilisation
1. Clonez le dépôt :
   ```bash
   git clone [https://github.com/Avenox599/python-file-scanner.git](https://github.com/Avenox599/python-file-scanner.git)
   cd python-file-scanner```
2. Lancez le script:
```bash 
python file_analyzer.py chemin/du/dossier```

3. Suivez les instructions à l'écran pour entrer le chemin du dossier à analyser.

## Structure de Rapport JSON
Le fichier rapport.json généré suit cette structure:
{
    "total": 10,
    "vide": 2,
    "ok": 7,
    "erreur": 1,
    "details": [
        {"fichier": "exemple.txt", "statut": "OK"},
        {"fichier": "vide.log", "statut": "VIDE"}
    ]
}

## Technologies utilisées
### Python 3
### Pathlib
Pour une gestion robuste des chemins de fichiers.
### JSON 
Pour l'export de données structurées.

