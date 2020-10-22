import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASES = {
    'atlas' : {
        "client" : "mongodb+srv://snoozy:deadoralive@cluster0.cbx9i.mongodb.net/<otaku_center>?retryWrites=true&w=majority",
        "database" : "Otaku_center"
    },

    'local' : {
        "client" : "192.168.1.14:27017",
        "database" : "Otaku_center"
    },

    'mongo_docker': {
        "client": "mongodb://0.0.0.0:27019/?readPreference=primary&appname=MongoDB%20Compass&ssl=false",
        "database": "Otaku_center"
    }
}

# valeur par default de la ligne de commande
Command_line = {'-d' : "local", # database, correspond à une des clefs de DATABASES
                '-f' : "none"   # fonction à lancer
                }

RETURN_STATEMENT = {'scan_downloaded' : [],
                    'error_scan_downloaded' : []
                    }