from os import path
from os import environ as env
from dependency_injector import providers

def get_config():    
    if(path.exists('./appsettings.json')):                
        return providers.Configuration(json_files=['./appsettings.json'])
    else:
        return providers.Configuration({
            'printAsWarning': env['PRINT_AS_WARNING']
        })