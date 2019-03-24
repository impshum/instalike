from InstagramAPI import InstagramAPI
from random import randint
from time import sleep

# DO NOT EDIT ABOVE THIS LINE

limit = 1  # How many likes per user each run
sleep_timer = 3  # In minutes (random/humanised)

# To use a proxy use --> 'user:password@ip:port' else use --> None
insta_accounts = {
    1: {'username': 'XXXX', 'password': 'XXXX', 'proxy': 'user:password@ip:port'},
    2: {'username': 'XXXX', 'password': 'XXXX', 'proxy': None}
}

# DO NOT EDIT BELOW THIS LINE

sleep_timer = sleep_timer * 60
min_sleep = sleep_timer - 60
max_sleep = sleep_timer + 60
sleep_timer = randint(min_sleep, max_sleep)


def get_users():
    with open('users.txt', 'r') as f:
        data = f.readlines()
    return [w.replace('https://instagram.com/', '') for w in list(map(str.strip, data))]


def main():
    users = get_users()
    if not users:
        print('nothing in users.txt')
    else:
        for i in range(1, len(insta_accounts) + 1):
            instauser = insta_accounts[i]['username']
            instapass = insta_accounts[i]['password']
            instaproxy = insta_accounts[i]['proxy']
            api = InstagramAPI(instauser, instapass)
            if instaproxy:
                api.setProxy(instaproxy)
            if api.login():
                print(f'logged in as {api.username}\n')
                for user in users:
                    api.searchUsername(user)
                    info = api.LastJson
                    username_id = info['user']['pk']
                    user_posts = api.getUserFeed(username_id)
                    info = api.LastJson
                    c = 0
                    if info['items']:
                        print(f'liking media by {user}')
                        for post in info['items']:
                            if not post['has_liked']:
                                print(post['pk'])
                                api.like(post['pk'])
                                c += 1
                                if c >= limit:
                                    break
                    else:
                        print(f'no media by {user}')
                    print(f'sleeping for {sleep_timer} seconds')
                    sleep(sleep_timer)


if __name__ == '__main__':
    main()
