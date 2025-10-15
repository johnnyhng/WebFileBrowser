from flask import Blueprint, jsonify
import os

user_model_api = Blueprint('user_model_api', __name__)

@user_model_api.route('/')
def index():
    return "This is the user model API."

@user_model_api.route('/list/<user>')
def list_models(user):
    models_path = os.path.join('/data', 'users', user, 'models')
    if not os.path.isdir(models_path):
        return jsonify({"error": "User or models directory not found"}), 404

    valid_models = []
    for model_dir in os.listdir(models_path):
        model_dir_path = os.path.join(models_path, model_dir)
        if os.path.isdir(model_dir_path):
            onnx_file = os.path.join(model_dir_path, 'model.int8.onnx')
            tokens_file = os.path.join(model_dir_path, 'tokens.txt')
            if os.path.isfile(onnx_file) and os.path.isfile(tokens_file):
                valid_models.append(model_dir)

    return jsonify(valid_models)
