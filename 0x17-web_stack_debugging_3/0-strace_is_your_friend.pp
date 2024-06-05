# Using strace, Puppet manifest to fix Apache 500 error
file { '/etc/apache2/sites-available/000-default.conf':
  ensure => file,
  content => "ServerName localhost\n",
}

service { 'apache2':
  ensure => running,
  enable => true,
  require => File['/etc/apache2/sites-available/000-default.conf'],
}
