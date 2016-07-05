# NTP

Master: [![Build Status](https://travis-ci.org/sansible/ntp.svg?branch=master)](https://travis-ci.org/sansible/ntp)  
Develop: [![Build Status](https://travis-ci.org/sansible/ntp.svg?branch=develop)](https://travis-ci.org/sansible/ntp)

* [ansible.cfg](#ansible-cfg)
* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Examples](#examples)

This roles installs and configures NTP, it will also set the timezone.




## ansible.cfg

This role is designed to work with merge "hash_behaviour". Make sure your
ansible.cfg contains these settings

```INI
[defaults]
hash_behaviour = merge
```




## Installation and Dependencies

This role has no dependencies.

To install run `ansible-galaxy install sansible.ntp` or add
this to your `roles.yml`

```YAML
- src: sansible.ntp
  version: v1.0
```

and run `ansible-galaxy install -p ./roles -r roles.yml`




## Tags

This role uses two tags: **build**, **configure**

* `build` - Install NTP
* `configure` - Configures timezone and enable NTP




## Examples

Simple example for enabling NTP and setting timezone to Europe/London

```YAML
- name: Install and setup NTP
  hosts: sandbox

  roles:
    - name: sansible.ntp
      ntp:
        timezone: Europe/London
```

Example of using a different set of NTP servers (AWS servers are used by default):

```YAML
- name: Install and setup NTP
  hosts: sandbox

  roles:
    - name: sansible.ntp
      ntp:
        servers:
          - 0.ubuntu.pool.ntp.org
          - 1.ubuntu.pool.ntp.org
          - 2.ubuntu.pool.ntp.org
          - 3.ubuntu.pool.ntp.org
```
