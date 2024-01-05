import requests
import json

with open("dish-data.json", "r", encoding="utf-8") as data_in_file:
    data_in = json.load(data_in_file)

file_names_data_in = [
    ["drinks", "coffe.png", "Cola.png", "limonade.png", "orangesok.png", "tea.png"],
    ["Fastfood", "burger.png", "chips.png", "free.png", "hotdog.png", "sandwich.png"],
    ["Italian", "Lazania.png", "PastaKarbonara.png", "Pizza.png", "Pizza4sira.png", "PizzaMargarita.png"],
    ["Russian", "blin.png", "borstch.png", "Pelmen.png", "Pirogsmyasom.png", "Pure.png"],
]
filenames = [f"{line[0]}/{val}" for line in file_names_data_in for val in line[1:]]

url = "http://localhost:3000/dish/"
file_name_prefix = "./ImgOfEat/"

for data_i, filename in zip(data_in, filenames):
    files = [
        (
            "image",
            (filename.split("/")[-1], open(file_name_prefix + filename, "rb"), "image/png"),
        )
    ]
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJyb2xlIjowfQ.bQoM-YvgvSYMcASgpMpgI5-JtaZSDu3lzGjH2soiK3s"
    }
    response = requests.request("PUT", url, headers=headers, data={"data": json.dumps(data_i)}, files=files)
    print(response.text)
