import pymysql.cursors

# Connect to the database
CONNECTION = pymysql.connect(host='localhost', # localisation de la base de donnees
                             user='root', #nom d'utilisateur
                             password='password',   # mot de passe
                             port=3306, # port
                             db='python_db',   # nom de la base de donnees
                             charset='utf8mb4', # encodage 
                             cursorclass=pymysql.cursors.DictCursor) # methode de recuperation des donnees
