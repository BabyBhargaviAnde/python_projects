import subprocess
cmd="date"
returned_output=subprocess.check_output(cmd)
print('Current date is:',returned_output.decode("utf-8"))

