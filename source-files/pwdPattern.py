import subprocess

def testPattern():
    p = subprocess.Popen("./pattern/pipal-master/passpat.rb --layout uk outputFiles/patternPass.txt",
                                 stdout= subprocess.PIPE, shell=True)
    result = p.communicate().__str__().split('\\n')
    result = result[1:]
    result = result[:-1]

    return result