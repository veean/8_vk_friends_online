import vk
import getpass

APP_ID = 5793481  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    return input("Please enter your VK login : ")


def get_user_password():
    return getpass.getpass(prompt="Please enter your VK password : ")


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    friends_id = api.friends.getOnline()
    friends_list = api.users.get(user_ids=friends_id)
    return friends_list


def output_friends_to_console(friends_online_):
    for friend in friends_online_:
        print("{} {} is online right now.".format(friend['first_name'], friend['last_name']))


if __name__ == '__main__':

    login_ = get_user_login()
    password_ = get_user_password()

    if login_ and password_:
        friends_online = get_online_friends(login_, password_)
        output_friends_to_console(friends_online)
    else:
        print("Invalid Login or Password !")
