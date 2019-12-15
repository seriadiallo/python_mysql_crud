from connection import CONNECTION


try:
    with CONNECTION.cursor() as cursor:
        SQL = """DELETE FROM clients WHERE id=%s """
        id = int(input('Donnez l\'identifiant'))
        print(V)
        nb = cursor.execute(SQL, V)



except Exception as e:
    print('une exception')
    print(e)
    CONNECTION.rollback()
else:
    print('nombre de suppression est:', nb)
    CONNECTION.commit()
finally:
    CONNECTION.close() # Fermer la connexion (deconnexion)