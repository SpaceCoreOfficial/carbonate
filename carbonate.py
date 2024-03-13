import os, sys

from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

from prompt_toolkit.shortcuts import input_dialog
from prompt_toolkit.shortcuts import yes_no_dialog
from prompt_toolkit.shortcuts import message_dialog



save_dialog = input_dialog(
    title='Saving...',
    text='Please type filename:')
    
save_or_not = yes_no_dialog(
    title='Realy?',
    text='Do you want to save your file?')

class service:

    def bottom_toolbar_main():
        return HTML(filename + '\n|Alt+Enter or Esc+Enter - Exit|')
    def bottom_toolbar_save_file():
        return HTML(filename + '\n|Want to save?|')
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
                    prompt_continuation=service.prompt_continuation, bottom_toolbar=service.bottom_toolbar_main(), auto_suggest=AutoSuggestFromHistory(),
                    )

        if ("%s" % inp) == fff:
            pass
            
        else:
            if save_or_not.run():
                if unnamed == True:
                    temp = open(save_dialog.run(), 'w', encoding='utf-8')
                    temp.writelines("%s" % inp)
                    temp.close()
                    
                else:
                    temp = open(filename, 'w', encoding='utf-8')
                    temp.writelines("%s" % inp)
                    temp.close()
                    
            else:
                pass
    except PermissionError:
        message_dialog(
            title='Permission Error',
            text='"Carbonate" does not have sufficient rights to create rights in this location\nor edit the selected file').run()

    except UnicodeDecodeError:
        message_dialog(
            title='UnicodeDecode Error',
            text='"Carbonate" cannot recognize the Unicode in the file, therefore cannot open or edit it').run()
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
