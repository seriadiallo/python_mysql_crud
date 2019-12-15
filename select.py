from connection import CONNECTION


try:
    with CONNECTION.cursor() as cursor:
        SQL = """ SELECT * FROM clients """
        cursor.execute(SQL)
        clients = cursor.fetchall() # recupere toutes les lignes renvoyees par le select
        # print(clients)
        for client in clients: #
            for key, value in client.items():
                print(f"{key}: {value}")
            print('-----------------')



except Exception as e:
    print('une erreur est survenue')
    print(e) # pour afficher les details de l'erreur

finally:
    CONNECTION.close() # Fermer la connexion (deconnexion)
