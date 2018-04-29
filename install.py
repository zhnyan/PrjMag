import os
import sys

package_list = sys.argv[1]
def install(package_list):
    # update pip
    os.system('python -m pip install --upgrade pip')
    # install packages
    os.system('pip install -r ' + package_list + ' --timeout 300')
    # configure jupyter
    os.system('jupyter contrib nbextension install --user')

if __name__ == '__main__':
    install( package_list )
