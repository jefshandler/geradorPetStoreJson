import os
import json
import csv

project_dir = os.path.dirname(os.path.abspath(__file__))

json_dir = os.path.join(project_dir, 'jsons')
csv_dir = os.path.join(project_dir, 'csvs')

json_file_path = os.path.join(json_dir, 'jsons.json')

csv_file_path = os.path.join(csv_dir, 'pets.csv')

with open(json_file_path) as file:
    data = json.load(file)


with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(["petId", "categoryId", "categoryName", "petName", "photoUrls", "tagsIds", "tagsNames", "status"])

    for item in data:
        photo_urls = ";".join(item["photoUrls"])
        tags_ids = ";".join([str(tag["id"]) for tag in item["tags"]])
        tags_names = ";".join([tag["name"] for tag in item["tags"]])

        csv_row = [
            item["id"],
            item["category"]["id"],
            item["category"]["name"],
            item["name"],

            photo_urls,
            tags_ids,
            tags_names,
            item["status"]
        ]
        writer.writerow(csv_row)

print("JSON to CSV conversion completed.")

