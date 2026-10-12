# Nickname Atlas

from pyscript import display, document


def find_nickname (e):
    document.getElementById('display').innerHTML = " "
    nickname = document.getElementById('select_country').value
    display(nickname, target='display')