# Configure holberton user file limits
exec { 'configure-holberton-file-limits':
  command  => "sed -E -i 's/^holberton (hard|soft) nofile [45]/holberton \\1 nofile 88888/' /etc/security/limits.conf",
  path     => ['/usr/bin', '/usr/sbin', '/bin'],
  onlyif   => 'test -e /etc/security/limits.conf',
  provider => shell,
}
