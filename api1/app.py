from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Charger les modèles de régression et de classification
regression_model = joblib.load('regression_model.pkl')  # Remplacez par votre fichier de modèle
classification_model = joblib.load('classification_model.pkl')  # Remplacez par votre fichier de modèle

# Liste des colonnes attendues par le modèle
expected_columns = ['Year', 'Month', 'Day', 'Author', 'message', 'functions']

@app.route('/', methods=['GET'])
def home():
    return "API Flask fonctionne correctement !"

@app.route('/predict/regression', methods=['POST'])
def predict_regression():
    try:
        # Récupérer les données envoyées par l'utilisateur
        data = request.get_json()

        # Vérification de la présence de "features"
        if 'features' not in data:
            return jsonify({'error': 'Les données doivent contenir une clé "features"'}), 400

        # Extraire les features
        features = data['features']
        if not isinstance(features, dict):
            return jsonify({'error': 'Les "features" doivent être un objet JSON'}), 400

        # Vérification que toutes les colonnes attendues sont présentes
        missing_columns = [col for col in expected_columns if col not in features]
        if missing_columns:
            return jsonify({'error': f'Colonnes manquantes : {", ".join(missing_columns)}'}), 400

        # Créer un DataFrame à partir des features
        features_df = pd.DataFrame([features])  # Crée un DataFrame à partir d'une ligne de données

        # Vérifier que l'objet modèle est bien un modèle avec la méthode 'predict'
        if not hasattr(regression_model, 'predict'):
            return jsonify({'error': 'Le modèle de régression ne contient pas la méthode "predict"'}), 500

        # Préparer les données pour la prédiction
        prediction = regression_model.predict(features_df)

        return jsonify({'prediction': prediction.tolist()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/predict/classification', methods=['POST'])
def predict_classification():
    try:
        # Récupérer les données envoyées par l'utilisateur
        data = request.get_json()

        # Vérification de la présence de "features"
        if 'features' not in data:
            return jsonify({'error': 'Les données doivent contenir une clé "features"'}), 400

        # Extraire les features
        features = data['features']
        if not isinstance(features, dict):
            return jsonify({'error': 'Les "features" doivent être un objet JSON'}), 400

        # Vérification que toutes les colonnes attendues sont présentes
        missing_columns = [col for col in expected_columns if col not in features]
        if missing_columns:
            return jsonify({'error': f'Colonnes manquantes : {", ".join(missing_columns)}'}), 400

        # Créer un DataFrame à partir des features
        features_df = pd.DataFrame([features])  # Crée un DataFrame à partir d'une ligne de données

        # Préparer les données pour la prédiction
        prediction = classification_model.predict(features_df)

        # Retourner la classe prédite
        return jsonify({'prediction': int(prediction[0])}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
