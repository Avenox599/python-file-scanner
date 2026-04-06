import sys
from pathlib import Path
import json

print("Bonjour.")

# --- Sélection du dossier ---
while True:
    if len(sys.argv) >= 2:
        chemin = sys.argv[1]
    else:
        chemin = input("Entrez le chemin du dossier : ")

    dossier = Path(chemin)
    if dossier.is_dir():
        break
    elif dossier.is_file():
        print("Le chemin que vous avez inscrit dirige vers un fichier pas un dossier.")
        print("Réessayez.")
        # On vide sys.argv pour éviter la boucle infinie si l'argument était mauvais
        sys.argv = [] 
    else:
        print("Le chemin que vous avez entré n'existe pas.")
        sys.argv = []

# --- Lecture des fichiers ---
fichier_vide = 0
fichier_plein = 0
fichier_err = 0
resultats = []

# Correction : Utilisation de __file__ pour que le script s'ignore lui-même dynamiquement
nom_du_script = Path(__file__).name

for fichier in dossier.iterdir():
    # On ignore le script, le rapport txt et le rapport json
    if fichier.is_file() and fichier.name not in [nom_du_script, "rapport.txt", "rapport.json"]:
        taille = fichier.stat().st_size
        if taille == 0:
            print(f"\nLe fichier {fichier.name} est vide.")
            resultats.append((fichier.name, "VIDE"))
            fichier_vide += 1
        else:
            print(f"\nLecture du fichier {fichier.name}")
            try:
                # Lecture du texte
                print(fichier.read_text(encoding='utf-8'))
                resultats.append((fichier.name, "OK"))
                fichier_plein += 1
            except Exception as e:
                print(f"Erreur lors de la lecture de {fichier.name} : {e}")
                resultats.append((fichier.name, f"ERREUR : {e}"))
                fichier_err += 1

# --- Rédaction du rapport ---
print("\n--- Rapport de la lecture ---")
print("Rapports générés : rapport.txt et rapport.json")

# Rapport au format .txt
with open("rapport.txt", "w", encoding='utf-8') as f:
    f.write("=== Résumé ===\n")
    f.write(f"Total : {len(resultats)}\n")
    f.write(f"Nombre de fichier OK : {fichier_plein}\n")
    f.write(f"Nombre de fichier vides : {fichier_vide}\n")
    f.write(f"Nombre d'erreurs : {fichier_err}\n")
    f.write("\n=== Détails ===\n")
    for nom, statut in resultats:
        f.write(f"{nom} : {statut}\n")
    
# Affichage du rapport TXT
with open("rapport.txt", "r", encoding='utf-8') as f:
    for line in f:
        print(line.strip())

# Rapport au format .json
rapport_json = {
    "total": len(resultats),
    "vide": fichier_vide,
    "ok": fichier_plein,
    "erreur": fichier_err,
    "details": [ # Correction : "détails" -> "details" (mieux sans accent en JSON)
        {"fichier": nom, "statut": statut}
        for nom, statut in resultats
    ]
}

with open("rapport.json", "w", encoding='utf-8') as f:
    json.dump(rapport_json, f, indent=4, ensure_ascii=False)

# Affichage du rapport JSON
with open("rapport.json", 'r', encoding="utf-8") as f:
    for line in f:
        print(line.strip())