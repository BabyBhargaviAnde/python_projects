import os
cmd="curl --version"
returned_value=os.system(cmd)
print('returned value:',returned_value)