# browbeat
Browbeat InfraRed Plugin


## Installation

1. Install [infrared](https://github.com/redhat-openstack/infrared)
2. Install browbeat infrared plugin

```
infrared plugin add https://github.com/rhos-infra/browbeat.git
```
3. Run the plugin

```
infrared browbeat -h
```

## Usage

To install and run browbeat on your TripleO cloud

1) clone the browbeat to home directory and export the roles path, for example
cd ~/
git clone https://opendev.org/x/browbeat
export ANSIBLE_ROLES_PATH=<home directory>/browbeat/ansible/install/roles

```
infrared browbeat --install yes --config-file <filename> -e @<ansible_vars_file>
```

If you want to install and run workloads along with monitoring and visuzalization

```
infrared browbeat --install yes --config-file <filename> --monitor yes --visualize yes -e @<ansible_vars_file>
```
If browbeat is already installed, you can skip the --install flag or set it to no to skip the installation.

Passing the extra argument -e @<ansible_vars_file> is mandatory or the plugin will fail. A sample file is provided [here](vars/all.yml)

## Tests

To run Ansible linting tests, run the following command

```
tox -e ansible-lint

```
## Contributions

Contributions are made with pull requests :)
