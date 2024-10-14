# RLCode3



-----------------------------------------
# Pratique et exécution du code 
-----------------------------------------

```bash
# 1. Cloner le projet (remplacez avec l'URL de votre dépôt)
git clone https://github.com/hrhouma/RLCode3.git
cd RLCode3

# 2. Créer et activer l'environnement virtuel
python3 -m venv venv
# Sur Linux, utilisez source venv/bin/activate
# Sur Windows, utilisez
venv\Scripts\activate

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



---------------------------------
# Explication
---------------------------------




### Explication des deux figures issues de l'exécution du code 

Ce code montre l'exécution d'expériences de **Q-Learning** avec différentes valeurs de **taux d'apprentissage (alpha)** et l'enregistrement des résultats sous forme de récompenses moyennes. Les figures illustrent les performances des agents entraînés avec des valeurs spécifiques d'**alpha**.

---

### **1. Première Figure : Console**


![image](https://github.com/user-attachments/assets/e00a4cc9-388f-4c20-a043-f4ef944658b9)

- **Explication** :
  - La figure montre le log d'exécution du programme dans la console. Le programme exécute des expériences pour cinq valeurs différentes de **taux d'apprentissage (alpha)** : **0.1, 0.3, 0.5, 0.7, 0.9**.
  - Pour chaque valeur d'**alpha**, un agent **Q-Learning** est entraîné sur l'environnement **MountainCar-v0** pendant **1000 épisodes**.
  - À la fin de l'exécution, les résultats sont enregistrés dans un fichier nommé **`experiment_results.pkl`**, qui contient les récompenses cumulées pour chaque agent selon la valeur d'**alpha**.

---

### **2. Seconde Figure : Graphique des Récompenses Moyennes**

![image](https://github.com/user-attachments/assets/608a0e14-339c-4761-b528-4a06bc12f3f7)


- **Explication** :
  - Ce graphique illustre l'impact du **taux d'apprentissage (alpha)** sur la performance des agents **Q-Learning**.
  - **L'axe des X** représente le **nombre d'épisodes**, c'est-à-dire le nombre de fois que l'agent a été entraîné dans l'environnement.
  - **L'axe des Y** représente la **récompense moyenne** reçue par l'agent au cours des épisodes. Les courbes ont été lissées avec une **moyenne glissante** pour lisser les fluctuations.
  - Chaque courbe représente une valeur d'**alpha** différente :
    - **Courbe bleue** pour **α = 0.1**.
    - **Courbe orange** pour **α = 0.3**.
    - **Courbe verte** pour **α = 0.5**.
    - **Courbe rouge** pour **α = 0.7**.
    - **Courbe violette** pour **α = 0.9**.

- **Interprétation** :
  - **α = 0.3** et **α = 0.5** sont les courbes qui montrent les meilleures performances, avec une convergence rapide vers des récompenses plus élevées (environ **-250**). Ces valeurs d'alpha permettent à l'agent d'apprendre de manière efficace, en équilibrant exploration et exploitation.
  - **α = 0.1** montre une courbe relativement stable, mais elle converge plus lentement, car un taux d'apprentissage plus faible signifie que l'agent met plus de temps à apprendre.
  - **α = 0.9**, quant à lui, est beaucoup plus erratique avec des récompenses très faibles, ce qui signifie que l'agent explore trop, rendant l'apprentissage inefficace. Les grandes variations montrent que l'agent n'arrive pas à stabiliser ses décisions.
  - **α = 0.7** suit une trajectoire intermédiaire, avec une performance correcte mais moins stable que **α = 0.3** et **α = 0.5**.

---

### **Explication du code**

#### 1. **Code pour l'exécution des expériences :**

- Le code suivant entraîne des agents **Q-Learning** avec différentes valeurs d'**alpha** et enregistre leurs performances dans un fichier **pickle**.
- **Fonction `run_experiment`** :
  - Cette fonction crée un environnement **MountainCar-v0** et entraîne un agent **QLearningAgent** pendant un nombre spécifié d'épisodes (par défaut, 1000). Elle renvoie les récompenses obtenues au fil des épisodes.
- **Main Script** :
  - Le programme exécute des expériences pour chaque valeur d'**alpha** dans la liste **alphas = [0.1, 0.3, 0.5, 0.7, 0.9]**.
  - Les résultats sont ensuite enregistrés dans le fichier **`experiment_results.pkl`** à l'aide de la bibliothèque **pickle**.

#### 2. **Code pour la visualisation des résultats :**

- Ce script charge les résultats enregistrés dans **`experiment_results.pkl`** et trace les **récompenses moyennes** des agents au fil des épisodes.
- **Fonction `moving_average`** : Cette fonction calcule une moyenne glissante pour lisser les récompenses et rendre les courbes plus lisibles.
- **Fonction `visualize_results`** :
  - Cette fonction charge les résultats, applique la fonction **moving_average** pour lisser les récompenses, puis trace un graphique des performances de chaque agent (pour chaque valeur d'**alpha**).
  - Le graphique montre clairement comment les différentes valeurs de **alpha** influencent la performance des agents **Q-Learning** dans l'environnement **MountainCar-v0**.

---

### **Conclusion** :

- **Impact du taux d'apprentissage (alpha)** : Le graphique montre clairement que les valeurs modérées de **alpha** (comme **0.3** et **0.5**) donnent les meilleurs résultats, en permettant à l'agent d'explorer l'environnement tout en apprenant efficacement. Des valeurs trop faibles ou trop élevées peuvent entraîner des performances sous-optimales.
- **Alpha faible (0.1)** : L'agent apprend de manière très prudente, progressant lentement vers de meilleures récompenses.
- **Alpha élevé (0.9)** : L'agent explore trop, ce qui rend difficile la stabilisation des politiques apprises, entraînant des résultats erratiques et des récompenses faibles.

Ces visualisations permettent d'analyser comment le **taux d'apprentissage (alpha)** influence la vitesse et l'efficacité de l'apprentissage dans l'environnement **MountainCar-v0**.
