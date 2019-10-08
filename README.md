vivid-role-linux-jenkins-agent-configure
=========

A role to configure a vm to be a Jenkins agent

Role Variables

--------------
`variable_name: default`

```yaml
---
# jenkins master
master_username: admin
master_password: admin
master_host: "{{ ansible_host }}"
master_port: 8080
master_url: "http://{{ master_host }}:{{ master_port }}"

# general agent
agent_function: generic
agent_agent_name: "{{ agent_function }}-agent"
agent_executors_num: 1

# jenkins linux agent
agent_linux_host: "{{ ansible_host }}"
agent_linux_ssh_port: 22
agent_linux_home: /opt/jenkins
agent_linux_jenkins_cred_id: ci_agent
agent_linux_jenkins_username: jenkins
agent_linux_jenkins_password: J3nk1ns
agent_linux_jenkins_public_key: ""
agent_linux_user_group: jenkins
agent_linux_labels:
  - linux
  - "{{ agent_function }}"
agent_linux_selinux_ports: "{{ master_port }},49187,\
{{ agent_linux_ssh_port }}"

connect_agent_to_master: true

configure_ansible: true

ansible_agent_install_docker: true
ansible_agent_install_molecule: true

```

Example Playbook
----------------

```yaml
---
- name: Converge
  hosts: all
  # Roles assumes default vars from role.
  vars:
    connect_agent_to_master: true
    configure_ansible: true
    configure_packer: true
    ansible_agent_install_molecule: true
    ansible_agent_install_docker: false
  roles:
    - role: ansible_role_configure_agent

```

This will connect the agent to the master, it will configure it to be an ansible agent and a packer agent. Molecule will be installed but docker will not.

License
-------

MIT
