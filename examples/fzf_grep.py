# Tested with ranger 1.9.3

from __future__ import (absolute_import, division, print_function)


from ranger.api.commands import Command



class fzf_grep(Command):
    """:fzf_grep *pattern*

    Search pattern and open fzf with matches. After select one, opens file on pattern-line in nvim.
    """
    def execute(self):

        import subprocess
        pattern = self.rest(1)
        get_string = 'rg -j 50 --color "auto" -n -e "{word}" | fzf'.format(word=pattern)
        fzf = self.fm.execute_command(get_string, universal_newlines=True, stdout=subprocess.PIPE)
        stdout, _ = fzf.communicate()
        parse = stdout.split(":")
        command = ["st", "-e", "nvim", parse[0], "+" + str(parse[1]), "&>/dev/null"]
        subprocess.run(command)
