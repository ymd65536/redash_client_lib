import os

# io module

def output_sql(folder_name, result):
    """

    Args:
        folder_name (str): sql save folder name
        result (json): detail query info 
    
    """
    file_name = str(result['id']) + '_' + result['name'] + '.sql'
    dir_path = os.getcwd() + '/' + folder_name

    if os.path.isdir(dir_path) is not True:
        os.mkdir(dir_path)

    with open(dir_path + '/' + file_name, mode='w') as sql_file:
        sql_file.write(result['query'])
    
    return {"save_folder": dir_path}