# PredictiCode
# IA Prédictive pour l'Impact d'un Commit et la Probabilité de Régression

## Contexte

Ce projet a pour objectif de concevoir et de développer une intelligence artificielle (IA) prédictive permettant d’évaluer l’impact d’un commit sur le reste du code source, ainsi que de prédire la probabilité de régression associée. Ce travail s’inscrit dans le contexte des défis rencontrés par les équipes de développement logiciel qui, au fil du temps, doivent faire face à la complexité croissante du code et à l’augmentation du nombre de modifications.

Les équipes de développement sont souvent confrontées à des problèmes où les modifications apportées au code (les *commits*) introduisent des régressions, c’est-à-dire des défauts dans des fonctionnalités précédemment stables. Ce projet vise à fournir une solution permettant d'identifier ces risques avant que les changements ne soient intégrés au code principal.

## Objectif

L’objectif principal de ce projet est de développer une IA qui analyse les commits effectués sur un dépôt de code et prédit leur impact potentiel sur le comportement global du logiciel. En particulier, l’IA devrait pouvoir :
- Prédire si un commit pourrait entraîner des régressions.
- Estimer la probabilité qu'une modification introduise un bug ou une anomalie dans le code.

## Approches et Méthodologie

Pour réaliser cet objectif, plusieurs approches sont mises en œuvre, telles que :
1. **Analyse statique du code** : Extraction de caractéristiques du code pour identifier les parties les plus susceptibles d’être affectées par une modification.
2. **Modélisation de l’historique des commits** : Utilisation de l’historique des commits pour comprendre les modèles de modification dans le code et leur impact passé.
3. **Machine Learning & IA** : Application d’algorithmes prédictifs pour analyser les modifications du code, tels que des modèles basés sur :
   - TensorFlow
   - scikit-learn

Les modèles utilisent les données provenant de l’historique des commits, les caractéristiques des fichiers modifiés, les fonctions modifiées, ainsi que d’autres paramètres pertinents.

## Fonctionnalités

- **Prédiction de régression** : Détecte les commits susceptibles d’introduire des régressions dans le code.
- **Évaluation de l’impact** : Calcule l'impact d'un commit sur d’autres parties du code source.
- **Visualisation des risques** : Fournit une interface pour visualiser les commits à risque et évaluer la probabilité de régression.

## Technologies Utilisées

- **Python** : Langage de programmation principal utilisé pour la conception de l'IA et des algorithmes.
- **TensorFlow** : Bibliothèque pour le machine learning, utilisée pour entraîner les modèles prédictifs.
- **scikit-learn** : Bibliothèque pour l’analyse des données et l’entraînement des modèles de machine learning.
- **Git** : Système de gestion de version pour récupérer les commits et analyser les modifications.
- **Flask** : Framework web pour déployer l'API prédictive et interagir avec les utilisateurs.
