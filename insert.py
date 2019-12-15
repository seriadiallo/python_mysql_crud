from connection import CONNECTION


try:
    with CONNECTION.cursor() as cursor:
        SQL = """ INSERT INTO clients (nom, prenom, age) 
            VALUES (%s, %s, %s) """
        nom = input('Donnez le nom ')
        prenom = input('Donnez le prenom ')
        age = int(input('Donnez l\'age '))
        values = (nom, prenom, age)
        cursor.execute(SQL, values)



except e:
    print('une erreur est survenue')
    # print(e)
    CONNECTION.rollback() # annuler toutes les modifications
else:
    print(' succes')
    CONNECTION.commit() # valider les modification

finally:
    CONNECTION.close() # Fermer la connexion (deconnexion)
