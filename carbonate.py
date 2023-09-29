import os
from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import HTML


def bottom_toolbar():
    return HTML(filename + ' | Alt+Enter or Esc+Enter - Exit')

def prompt_continuation(width, line_number, is_soft_wrap):
    return ' ' * width

def clear():
    os.system('cls')

def file(filename):
    try:
        clear()
        if os.path.isfile(filename):
            f = open(filename, 'r', encoding='utf-8')
            fff = f.read()
        else:
            fff = ''
        inp = prompt('~ ', multiline=True, default='%s' % "".join(fff), prompt_continuation=prompt_continuation, bottom_toolbar=bottom_toolbar())

        if ("%s" % inp) == fff:
            pass
        else:
            save = input("\n\nSave file?\n (y/n)> ")
            if save == 'y':
                fl = open(filename, 'w', encoding='utf-8')
                fl.writelines("%s" % inp)
                fl.close()
            elif save == 'n':
                pass
    except PermissionError:
        print("[ALERT] - Bad file path")

    except UnicodeDecodeError:
        print("[ALERT] - Bad unicode")


if __name__ == '__main__':
    filename = input("Filename >> ")
    file(filename)