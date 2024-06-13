# Puppet file that fix stack to get 0
file { 'last line':
    ensure  => present,
    path    => '/etc/default/nginx',
    content => 'ULIMIT="-n 4096"',
}

service { 'nginx':
    ensure    => running,
    subscribe => File['/etc/default/nginx']
}
