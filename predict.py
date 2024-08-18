import pandas as pd
import waste_detect as w
def predict_waste_category(user_quantity_in_grams, user_ingredient_count, user_food):
    # Create a DataFrame with user input
    user_input = pd.DataFrame({
        'quantity_in_grams': [user_quantity_in_grams],
        'ingredient_count': [user_ingredient_count],

    })
    # Encode 'food_type' feature using one-hot encoding
    for food_type in w.data['food_type'].unique():
        user_input[f'food_type_{food_type}'] = 0
    if user_food in w.data['food_type'].unique():
        user_input[f'food_type_{user_food}'] = 1
    # user_input = pd.get_dummies(user_input, columns=['food_type'])

    # Ensure that the user input DataFrame has the same columns as the training data
    missing_cols = set(w.X.columns) - set(user_input.columns)
    for col in missing_cols:
        user_input[col] = 0
    # Ensure the feature columns are in the same order as during training
    user_input = user_input[w.X_train.columns]
    # Make the prediction
    user_prediction = w.clf.predict(user_input)

    if user_prediction[0] == 'High':
        return "This food item is producing high waste. Consider reducing the number of ingredients used or the quantity in which this food item is being prepared."
    else:
        return "Relax, this food item is producing low waste. You can go ahead preparing it. No changes required."




