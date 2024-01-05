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

file_name_prefix = "./ImgOfEat/"
url_prefix = "http://185.128.106.222:3000/"

for data_i, filename in zip(data_in, filenames):
    url = url_prefix + "dish/"
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
    if '{"query":"INSERT INTO' in response.text:
        print("Images already loaded")
        break
    print(response.text)

for kitchen in "Американская Итальянская Русская".split():
    url = url_prefix + "kitchen/"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJyb2xlIjowfQ.bQoM-YvgvSYMcASgpMpgI5-JtaZSDu3lzGjH2soiK3s",
    }
    response = requests.request("PUT", url, headers=headers, data=json.dumps({"name": kitchen}))
    print(response.text)
