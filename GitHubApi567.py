"""
    Developed by: Jose Lara
    Class: SSW 567 - Software Quality Assurance and Testing
    Date: Tues. Feb. 13, 2018

"""
import requests
from requests.exceptions import HTTPError

class Repo:
    '''Githhub interface script'''

    _data = {}

    def __init__(self, user_name):
        self.user_name = user_name

    def requestRepos(self):
        try:
            self._data = requests.get('https://api.github.com/users/' + self.get_user() + '/repos')
        except HTTPError:
            print('Error Happened with API request')

    def requestCommits(self, repo_name):
        return len(requests.get('https://api.github.com/repos/' + self.get_user() + '/'+repo_name+'/commits').json())

    def get_user_repo(self):
        return self._data.json()

    def get_all_data(self):
        value = []
        for d in self.get_user_repo():
            value.append('Repo: '+d['name'] +" - number of commits "+ str(self.requestCommits(d['name'])))
        return value

    def get_user(self):
        return self.user_name

    def get_status_code(self):
        return self._data.status_code


# Program Running
if __name__ == '__main__':
    newRepo = Repo('jlara567')
    newRepo.requestRepos()
    for x in newRepo.get_all_data():
        print(x)







