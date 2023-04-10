# Puppet script to set up a server for deployment of web_static

# Check if the ubuntu user and group exist
exec { 'check_ubuntu_user':
  command => '/usr/bin/id -u ubuntu',
  unless  => '/usr/bin/id -u ubuntu',
}

exec { 'check_ubuntu_group':
  command => '/usr/bin/getent group ubuntu',
  unless  => '/usr/bin/getent group ubuntu',
}

# Install Nginx if it is not already installed
package { 'nginx':
  ensure => 'present',
}

# Create the necessary directories for the web_static deployment
file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/shared', '/data/web_static/releases/test']:
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Create a fake HTML file in the /data/web_static/releases/test directory
file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>",
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Create a symbolic link from /data/web_static/current to /data/web_static/releases/test
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  force  => true,
}

# Updates the Nginx configuration to serve content from /data/web_static/current at the /hbnb_static location
augeas { 'nginx_config':
  context => '/files/etc/nginx/sites-available/default',
  changes => [
    'ins location before /files/etc/nginx/sites-available/default/server/location[last()]',
    'set /files/etc/nginx/sites-available/default/server/location[last()]/path /hbnb_static/',
    'set /files/etc/nginx/sites-available/default/server/location[last()]/alias /data/web_static/current/',
    ],
}

# now we restart Nginx
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => Augeas['nginx_config'],
}

