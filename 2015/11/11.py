from string import ascii_lowercase as alphabet
import re


class PasswordMaker:

    def __init__(self, password: str):
        self.pwd = password
        self.__alphabeta = alphabet + 'a'

    def __str__(self):
        return self.pwd

    def _increase(self):
        increment = ''
        for i, char in enumerate(reversed(self.pwd), start=1):
            char = self.__alphabeta[self.__alphabeta.index(char) + 1]
            increment = char + increment
            if char != 'a':
                break
        else:
            self.pwd = 'a' * (len(self.pwd) + 1)
        self.pwd = self.pwd[:len(self.pwd) - i] + increment
        # print(self.pwd)

    def generate(self):
        while True:
            self._increase()
            pattern_ok = (
                r'^(?=.*(?:abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz))'
                r'(?=(.*([a-z])\2){2})'
                r'(?!.*[iol])'
            )
            if bool(re.match(pattern_ok, self.pwd)):
                break
            iol = re.search(r'[iol]', self.pwd)
            if iol:
                iol_i = iol.start()
                self.pwd = (
                        self.pwd[:iol_i] 
                        + self.__alphabeta[self.__alphabeta.find(self.pwd[iol_i]) + 1] 
                        + 'a' * (len(self.pwd) - iol_i - 1)
                )


next_pwd = PasswordMaker('vzbxxyzz')
next_pwd.generate()
print(next_pwd)
