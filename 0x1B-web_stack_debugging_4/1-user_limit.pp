#resolves too many open files error

exec { 'change-max-open-files-hard-limit':
  command => "/bin/sed -i /etc/security/limits.conf -e 's/hard nofile [0-9]\+/hard nofile 4200/g'"
}

exec { 'change-max-open-files-soft-limit':
  command => "/bin/sed -i /etc/security/limits.conf -e 's/soft nofile [0-9]\+/soft nofile 3000/g'"
}
