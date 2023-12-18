import os
from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
import sys


class service:
    def bottom_toolbar():
        return HTML(filename + '\n|Alt+Enter or Esc+Enter - Exit|')

    def prompt_continuation(width, line_number, is_soft_wrap):
        return ' ' * width

    def clear():
        if os.name == "nt":
            os.system('cls')
        elif os.name == "posix":
            os.system("clear")



def editor(filename, unnamed):
    try:
        service.clear()
        if os.path.isfile(filename):
            f = open(filename, 'r', encoding='utf-8')
            fff = f.read()
        else:
            fff = ''
        inp = prompt('',
                     multiline=True, default='%s' % "".join(fff),
                     prompt_continuation=service.prompt_continuation, bottom_toolbar=service.bottom_toolbar(), history=FileHistory('.tmp/.~history'), auto_suggest=AutoSuggestFromHistory(),
                     )

        if ("%s" % inp) == fff:
            pass
        else:
            save = input("\n\nSave file?\n (y/n)> ")
            if save == 'y':
                if unnamed == True:
                    filename = input("Filename --> ")
                else:
                    pass
                fl = open(filename, 'w', encoding='utf-8')
                fl.writelines("%s" % inp)
                fl.close()
            elif save == 'n':
                pass
    except PermissionError:
        print("[ALERT] - Bad file path")

    except UnicodeDecodeError:
        print("[ALERT] - Bad unicode")
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    try:
        unnamed = False
        filename = str(sys.argv[1])
        editor(filename, unnamed)
    except IndexError:
        unnamed = True
        filename = "*unnamed"
        editor(filename, unnamed)
