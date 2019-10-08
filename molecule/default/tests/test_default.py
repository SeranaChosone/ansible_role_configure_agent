import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_jenkins_workspace_exists(host):
    f = host.file('/opt/jenkins')

    assert f.exists
    assert f.user == 'jenkins'
    assert f.group == 'jenkins'


def test_ansible_installed(host):
    ans = host.package('ansible')

    assert ans.is_installed


def test_python_installed(host):
    py = host.package('python')

    assert py.is_installed


def test_venv_installed(host):
    venv = host.ansible("command", "virtualenv --version", check=False)["rc"]
    # rc is the return code from the command.
    # If it is 0 it means it successfully run

    assert venv == 0


def test_pip_installed(host):
    pip = host.ansible("command", "pip --version", check=False)["rc"]
    # rc is the return code from the command.
    # If it is 0 it means it successfully run

    assert pip == 0


def test_packer_installed(host):
    pac = host.ansible("command",
                       "/usr/local/bin/packer --version",
                       check=False)["rc"]
    # rc is the return code from the command.
    # If it is 0 it means it successfully run

    assert pac == 0
