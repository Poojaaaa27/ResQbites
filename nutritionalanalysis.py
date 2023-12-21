import requests
import numpy as np
import pandas as pd

# Replace 'YOUR_API_KEY' with your actual USDA API key
API_KEY ='h8F03dtkxI2mDLCLbewdVetm3BBc9a2r7vyKt11z'

def get_nutritional_info(food_name):
    # Define the base URL for the USDA API
    base_url = 'https://api.nal.usda.gov/fdc/v1/foods/search'

    # Set up the parameters for the API request
    params = {
        'query': food_name,
        'api_key': API_KEY
    }

    # Make the API request
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()

        if 'foods' in data and len(data['foods']) > 0:
            # Select the first food item from the search results
            food_item = data['foods'][0]

            # Extract the nutritional information from the food item
            nutrients = food_item['foodNutrients']
            nutrient_data = {}
            for nutrient in nutrients:
                nutrient_data[nutrient['nutrientName']] = nutrient['value']

            return nutrient_data
        else:
            print(f"Error: Unable to retrieve data for {food_name}")
            return None
    else:
        print(f"Error: Unable to retrieve data for {food_name}")
        return None

def main():
    food_name = input("Enter the name of the food: ")
    nutrient_data = get_nutritional_info(food_name)

    if nutrient_data:
        # Create a Pandas DataFrame for the nutrient data
        df = pd.DataFrame(nutrient_data, index=[0])

        # Display the nutritional information
        print("\nNutritional Information for", food_name)
        print(df)

if __name__ == '__main__':
    main()
