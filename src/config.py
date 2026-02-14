import yaml


def load_cofig(config_path : str = 'configs/default.yaml'):
    with open(config_path,'r') as f:
        config = yaml.safe_load(f)
        
    return config

def save_cofig(config_path : str = 'configs/default.yaml'):
    with open(config_path,'w') as f:
        yaml.dump(f)
        

