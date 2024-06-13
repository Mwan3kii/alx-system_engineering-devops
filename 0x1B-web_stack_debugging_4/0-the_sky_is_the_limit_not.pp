# File that fix stack to get 0
file { 'last line':
    ensure  => present,
    path    => '/etc/default/nginx',
    content => 'ULIMIT="-n 4096"',
}

service { 'nginx to use':
    ensure    => running,
    subscribe => File['/etc/default/nginx']
}
