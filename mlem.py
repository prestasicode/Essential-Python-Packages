from mlem.api import save

#instead of joblib.dump(model, 'diabetes_model')
save(model, 'diabetes_model', sample_data=X_test)
