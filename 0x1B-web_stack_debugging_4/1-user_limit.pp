# Puppet file that Change the OS configuration to login with holberton user and opens with no error
file { 'loginFile':
    ensure  => present,
    path    => '/etc/security/limits.conf',
    content => '#File erased'
}
