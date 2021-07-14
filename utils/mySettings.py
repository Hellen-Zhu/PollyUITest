import yaml


# def load_yaml_data1(file_name):
#     files = open(file_name,'r',encoding='utf-8')
#     data = yaml.load(files,Loader=yaml.FullLoader)
#     return data

def load_yaml_data_by_key(file_name, key):
    files = open(file_name, 'r', encoding='utf-8')
    data = yaml.safe_load(files)[key]
    return data


