import json

with open("firebase_key.json", "r") as f:
    key_data = json.load(f)

key_data["private_key"] = key_data["private_key"].replace("\n", "\\n")
minified = json.dumps(key_data)

print("\n🔥 Copy this output and paste it into Vercel as FIREBASE_KEY:\n")
print(minified)
