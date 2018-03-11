import unittest
from unittest.mock import Mock

from GitHubApi567 import Repo

class RepoTest(unittest.TestCase):
    """This class is to test the GitHubApi567 project with Mock."""

    def test_getUserRepos(self):
        mock_repo = Mock()
        newRepo = Repo(mock_repo)
        mock_repo.return_value.ok = True

if __name__ == '__main__':
    unittest.main()
