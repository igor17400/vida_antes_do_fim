import pandas as pd

def preprocess_data(pop_data_path):
    # Load and preprocess your data
    pop = pd.read_csv(pop_data_path)
    pop['V'] = pd.to_numeric(pop['V'], errors='coerce')
    return pop
