import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_timezone(host):
    assert 'Europe/London' in host.file('/etc/timezone').content_string


def test_ntp_servers(host):
    ntp_conf = host.file('/etc/ntp.conf').content_string
    for i in range(0, 3):
        assert '%i.amazon.pool.ntp.org' % i in ntp_conf


def test_service(host):
    assert host.service('ntp').is_enabled
    assert host.service('ntp').is_running
