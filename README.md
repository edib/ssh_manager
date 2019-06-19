# ssh manager
========================

A simple Python menu-based ssh manager system integrated with ansible-vault.

Note: This script only works in local terminal.

## Installation
* Python 3.x
* Python console-menu
* Python ansible_vault

```
pip3 install console-menu ansible_vault

# install ansible for ubuntu
apt install ansible

```
### After Installation

```
git clone {REPO_URL}
cd ssh_manager
ansible-vault create serverlist.vault

```

* `serverlist.vault` file content will be like `serverlist.example`
* Change the `data_file` variable in `main.py` accordingly.

### Run the app

```
python3 main.py
```
### Thanks to
* [console-menu](https://github.com/aegirhall/console-menu)
* [ansible-vault](https://docs.ansible.com/ansible/latest/user_guide/vault.html)
