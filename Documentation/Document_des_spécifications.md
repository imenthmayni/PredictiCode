# Document des spécifications

## Epic 1: Définition des spécifications et de la portée du projet

### User Story 1.1: Définir les spécifications du projet

**Description:** En tant que développeur, je veux définir les spécifications du projet pour clarifier les objectifs et les attentes.

**Tâches:**

- Organiser une réunion avec le client pour discuter des besoins et des objectifs.
- Rédiger un document de spécifications.
- Obtenir l'approbation des spécifications par le client.

### User Story 1.2: Définir les métriques de succès

**Description:** En tant que chef de projet, je veux définir les métriques de succès pour évaluer l'efficacité de l'IA prédictive.

**Tâches:**

- Identifier les métriques clés (précision, rappel, F1-score, etc.).
- Définir des seuils de performance acceptables.
- Documenter les métriques et les seuils.

## Epic 2: Collecte et préparation des données

### User Story 2.1: Collecter des données

**Description:** En tant que développeur, je veux collecter des données historiques de commits, la base de tickets de Jira et la liste des spécifications pour entraîner le modèle prédictif.

**Tâches:**

- Identifier les dépôts de code pertinents.
- Extraire les données de commits (messages de commit, modifications de fichiers, etc.).
- Extraire les données de tickets de Jira :
  - Extraire les données des tickets (titres, descriptions, statuts, etc.)
  - Récupérer les métadonnées associées aux tickets (auteur, date de création, date de clôture, etc.).
- Extraire les données de spécifications.
- Stocker les données dans une base de données :
  - Choisir le type de base de données adapté à nos trois types de données et assurant la liaison entre eux.
  - Implémenter les scripts de stockage pour insérer les données extraites dans la base de données.
  - Vérifier l'intégrité et la cohérence des données stockées.

### User Story 2.2: Nettoyer et préparer les données

**Description:** En tant que data scientist, je veux nettoyer et préparer les données pour m'assurer qu'elles sont utilisables pour l'entraînement du modèle.

**Tâches:**

- Nettoyer les données.
- Effectuer une analyse exploratoire des données pour visualiser les données et détecter les anomalies.
- Créer des jeux de données d'entraînement, de validation et de test.
- Documenter le processus de préparation des données.

## Epic 3: Développement du modèle prédictif

### User Story 3.1: Choisir un algorithme de machine learning

**Description:** En tant que data scientist, je veux choisir un algorithme de machine learning approprié pour la prédiction de l'impact des commits.

**Tâches:**

- Rechercher et évaluer différents algorithmes (régression linéaire, forêts aléatoires, réseaux de neurones, etc.).
- Comparer les performances des algorithmes sur un jeu de données d'échantillon.
- Sélectionner l'algorithme le plus performant.

### User Story 3.2: Entraîner le modèle prédictif

**Description:** En tant que data scientist, je veux entraîner le modèle prédictif en utilisant le dataset qu’on a préparé.

**Tâches:**

- Configurer l'environnement d'entraînement.
- Entraîner le modèle en utilisant les données d'entraînement.
- Évaluer les performances du modèle sur le jeu de validation.

## Epic 4: Déploiement

### User Story 4.1: Déployer le modèle prédictif

**Description:** En tant que data scientist, je veux déployer le modèle prédictif afin qu'il soit accessible pour prédire l'impact des commits.

**Tâches:**

1. Préparer l'infrastructure de déploiement :
   - Choisir la plateforme et configurer l'environnement de production.
2. Emballer et déployer le modèle :
   - Convertir le modèle et créer des scripts de déploiement.
3. Développer et tester l'API :
   - Créer une API pour les prédictions et effectuer des tests en production.
4. Documenter le déploiement :
   - Documenter le processus de déploiement.

## Epic 5: Tests et validation

### User Story 5.1: Tester le modèle sur des commits réels

**Description:** En tant que développeur, je veux tester le modèle prédictif sur des commits réels pour valider sa précision et sa fiabilité.

**Tâches:**

- Sélectionner un échantillon de commits récents.
- Analyser l'impact prédit par le modèle.
- Comparer les prédictions avec les résultats réels.

### User Story 5.2: Obtenir des retours des développeurs

**Description:** En tant que développeur, je veux obtenir des retours des développeurs sur l'utilisation du modèle prédictif pour l'améliorer continuellement.

**Tâches:**

- Organiser des sessions de feedback avec les développeurs.
- Collecter et analyser les retours.
- Prioriser et implémenter les améliorations suggérées.
