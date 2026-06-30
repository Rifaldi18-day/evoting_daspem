import json
import os

def load_data(filepath):
    """Fungsi untuk membaca data dari file JSON"""
    folder = os.path.dirname(filepath)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)
        
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(filepath, data):
    """Fungsi untuk menyimpan data kembali ke file JSON"""
    folder = os.path.dirname(filepath)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)
        
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)