import csv, json

def convert_from_csv_to_json(csv_filename, json_filename):
    csv_file = open("src/mock_db/"+csv_filename, 'r')
    json_file = open("src/mock_db/"+json_filename, 'w')
    columns = ("Ingredient", "IsVegan")
    
