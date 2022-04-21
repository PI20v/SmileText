import random


def replacing_symbols(some_text):

    emoji_list = ['😀', '😃', '😄', '😁',
                  '👹','☠️','🤖','👨‍💻',
                  '🤵','👓','👌🏻','🇺🇦',
                  '🖥','🛠','⚙️','💵',
                  '🩸','💿','💈','🪦',]

    marks = '''!()-[]{};?@#$%:'"\,./^&;*_'''

    for i in some_text:
        if i in marks:
             some_text = some_text.replace(i,random.choice(emoji_list))
    return some_text


if __name__ == '__main__':

  print(  replacing_symbols('Приве! Я, Антон.'))






