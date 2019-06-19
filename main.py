# Import the necessary packages
from consolemenu import *
from consolemenu.items import *
from ansible_vault import Vault
import csv, os

__author__ = "ibrahim edib kokdemir"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "ibrahim edib kokdemir"
__email__ = "kokdemir@gmail.com"
__status__ = "Dev"

#*****************************/
#* CONFIG
# encrypted ansible_vault file
data_file="serverlist.vault"
# terminal client
terminal="x-terminal-emulator"
#*****************************/

if not os.path.exists(data_file):
    print("First create ansible_vault file like below, set the data_file parameter and do not forget the password!")
    print("$ ansible_vault create serverlist.vault")
    quit()


def main():
    # Create the menu
    menu = ConsoleMenu("SSH Menu")

    vault = Vault(input("Enter Vault Password: "))
    data = vault.load_raw(open(data_file).read())
    data = data.decode('utf-8')
    data = data.splitlines()

    for column in csv.DictReader(data):
        if column['ssh_port'] == "":
            column['ssh_port'] = 22
        if column['ssh_user'] == "":
            column['ssh_user'] = os.getlogin()
        command_item = CommandItem("{}".format(column['server_name']), "{} -e ssh {} -l {} -p {}"
                                   .format(terminal, column['ip_address'], column['ssh_user'], column['ssh_port']))
        menu.append_item(command_item)

    menu.show()


if __name__ == "__main__":
    main()
