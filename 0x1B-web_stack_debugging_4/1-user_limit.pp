#resolves too many open files errors

exec { 'change-os-configuration-for-holberton-user':
  command => "/bin/sed -i '/soft nofile/d; /hard nofile/d; /holberton soft nofile/d; /holberton hard nofile/d' /etc/security/limits.conf && echo -e 'holberton soft nofile 4096\nholberton hard nofile 8192' >> /etc/security/limits.conf",
}

exec { 'apply-pam-session':
  command => 'pam-auth-update --package',
  require => Exec['change-os-configuration-for-holberton-user'],
}

