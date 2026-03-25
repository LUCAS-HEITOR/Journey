import json
import os

Archive = "keys.json"

def read_keys():
    if not os.path.exists(Archive):
        return {}
    with open(Archive, "r") as f:
        return json.load(f)
    
def save_key(name_ai, value):
    keys = read_keys()
    keys[name_ai] = value
    with open(Archive, "w") as f:
        json.dump(keys, f, indent=4)

def erase_key(name_ai):
    keys = read_keys()
    if name_ai in keys:
        del keys[name_ai]
        with open(Archive, "w") as f:
            json.dump(keys, f, indent=4)

def listen_keys():
    keys = read_keys()
    return list(keys.keys())            

# Função para buscar uma chave específica
def get_key(name_ai):
    keys = read_keys()
    return keys.get(name_ai)