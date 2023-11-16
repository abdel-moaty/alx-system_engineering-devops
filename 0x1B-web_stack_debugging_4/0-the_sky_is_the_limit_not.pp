# Dynamically sets the file descriptor limit in the Nginx configuration file
exec { 'file descriptor limit':
  command  => 'sed -i "5s/[0-9]\+/$(ulimit -n)/" /etc/default/nginx && service nginx restart',
  onlyif   => 'test -e /etc/default/nginx',
  provider => shell,
}
