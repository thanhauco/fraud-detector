import shap
import pickle
def explain(amount):
    with open('model.pkl', 'rb') as f: model = pickle.load(f)
    explainer = shap.TreeExplainer(model)
    return explainer.shap_values([[amount]])