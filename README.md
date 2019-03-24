# instalike

Reads a list of users from a text file and likes the latest post from each one. If there is not a new post it will like the previous post and so on. Multiple accounts and proxies supported.

* Install instagramAPI

    pip install InstagramApi

* Configure the script at the top of run.py 

NOTE - When adding users and proxies remember that the last entry doesn't require a comma to end it.

    insta_accounts = {
        1: {'username': 'XXXX', 'password': 'XXXX', 'proxy': 'user:password@ip:port'},
        2: {'username': 'XXXX', 'password': 'XXXX', 'proxy': None},
        3: {'username': 'XXXX', 'password': 'XXXX', 'proxy': None},
        4: {'username': 'XXXX', 'password': 'XXXX', 'proxy': None},
        5: {'username': 'XXXX', 'password': 'XXXX', 'proxy': None}
    }
    
* Dump list of users instagram urls in users.txt (one per line e.g. https://instagram.com/putln2)
* Run it ```python run.py```
