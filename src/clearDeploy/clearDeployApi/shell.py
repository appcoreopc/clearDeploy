from shutil import which

class ShellManager:
    def execCommand(self):
        path = which('terraform')
        if path != None:
            return True
        return False
