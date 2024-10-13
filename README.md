# RLCode3


```bash
# 1. Cloner le projet (remplacez avec l'URL de votre dépôt)
git clone https://github.com/votre-nom/RLCode3.git
cd mountain-car-qlearning

# 2. Créer et activer l'environnement virtuel
python -m venv venv
source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Exécuter les expériences
python experiment.py

# 5. Visualiser les résultats
python visualize_results.py
```

# Structure du projet :

```
mountain-car-qlearning/
│
├── README.md
├── requirements.txt
│
├── qlearning_agent.py
├── helpers.py
├── experiment.py
├── visualize_results.py
│
├── venv/
│   └── (contenu de l'environnement virtuel)
│
└── experiment_results.pkl  (généré après l'exécution)
```

# Explication de la structure :

- `README.md` : Instructions et explications du projet
- `requirements.txt` : Liste des dépendances du projet
- `qlearning_agent.py` : Implémentation de l'agent Q-Learning
- `helpers.py` : Fonctions utilitaires pour la discrétisation de l'état
- `experiment.py` : Script pour exécuter les expériences avec différentes valeurs d'alpha
- `visualize_results.py` : Script pour visualiser les résultats des expériences
- `venv/` : Dossier contenant l'environnement virtuel (créé lors de l'installation)
- `experiment_results.pkl` : Fichier de résultats généré après l'exécution des expériences

# Pour utiliser ce projet :

1. Suivez les commandes listées ci-dessus pour cloner, installer et exécuter le projet.
2. Après avoir exécuté `experiment.py`, un fichier `experiment_results.pkl` sera généré.
3. Exécutez ensuite `visualize_results.py` pour créer un graphique montrant l'impact des différentes valeurs d'alpha.

