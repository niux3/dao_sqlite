from src.user_dao import UserDAO

def main():
    user_dao = UserDAO()
    user_dao.create_table()

    # Création d'un nouvel utilisateur
    # user_id = user_dao.create_user("Bob Doe", "bob.doe@i.com")
    # print(f"Utilisateur créé avec l'ID {user_id}")

    # Récupération de l'utilisateur
    # user_id = 2
    # user = user_dao.get_user(user_id)
    # print(f"Utilisateur récupéré : {user.name} - {user.email}")

    # Mise à jour de l'utilisateur
    # user_dao.delete_user(user_id)

    # Liste des utilisateurs
    # users = user_dao.list_users()
    # print("Liste des utilisateurs :")
    # for user in users:
        # print('*' * 80)
        # print(f'id : {user.id}')
        # print(f'name : {user.name}')
        # print(f'email : {user.email}')
        # print('')

    # Suppression de l'utilisateur
    # user_dao.delete_user(user_id)
    # print(f"Utilisateur supprimé. Liste actuelle : {user_dao.list_users()}")

if __name__ == "__main__":
    main()
