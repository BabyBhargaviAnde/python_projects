import subprocess
cmd="curl --version"
returned_value=subprocess.call(cmd,shell=True)
print('returned value:',returned_value)