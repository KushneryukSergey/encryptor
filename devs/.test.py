import json
from modules.frequencies import count_frequencies

with open("../texts/The_Breathing_Method-Stephen_King.txt", "r") as file:
    count_frequencies(file.read(), "en", "freq.json")
with open("freq.json", "r") as freq:
    kings_frequencies = json.load(freq)
print(kings_frequencies)

print(len("\n"))
