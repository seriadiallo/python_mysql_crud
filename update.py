from connection import CONNECTION


try:
    with CONNECTION.cursor() as cursor:
        SQL = """ UPDATE clients SET nom=%s, prenom=%s, age=%s 
            WHERE id=%s """
        id = int(input('donnez l\'identifiant'))
        nom = input('Donnez le nom ')
        prenom = input('Donnez le prenom ')
        age = int(input('Donnez l\'age '))
        values = (nom, prenom, age, id)
        val = cursor.execute(SQL, values)
        print('le nombre de modification', val)



except Exception as e:
    print('une erreur est survenue')
    print(e) # pour afficher les details de l'erreur
    CONNECTION.rollback() # annuler toutes les modifications
else:
    print(' succes')
    CONNECTION.commit() # valider les modification

finally:
    CONNECTION.close() # Fermer la connexion (deconnexion)
