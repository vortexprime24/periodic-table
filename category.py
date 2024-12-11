import json

def extract_unique_categories(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    unique_categories = set()

    for key, value in data.items():
        if key != "order" and isinstance(value, dict) and "category" in value:
            unique_categories.add(value['category'])
    
    print("Unique categories:")
    for category in unique_categories:
        print(category)

file_path = 'table.json'
extract_unique_categories(file_path)

