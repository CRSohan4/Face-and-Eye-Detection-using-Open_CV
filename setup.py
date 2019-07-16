import subprocess
import sys
import time

time.sleep(2)
print('Checking environment...')
time.sleep(3)
print('Checking required package...')
reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

time.sleep(1)

if 'opencv-python' in installed_packages:
    print('Requirement satisfied.')
else:
    print('Please install opencv-python and try running this script again.')
    print('To install opencv-python run the below code')
    print('pip install opencv-python')
