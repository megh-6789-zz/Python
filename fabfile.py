from fabric.api import* 
def copy():
   env.hosts = ['ec2-35-161-196-60.us-west-2.compute.amazonaws.com']
   env.password = 'Downloads/megh_key.pem'
   env.user = 'ubuntu'
   run('mkdir -p /home/ubuntu/')
   put('Downloads/docs/ps.pdf','/home/ubuntu/')
def apache():
   run('sudo service httpd status')
def user():
   sudo('useradd megh')
   sudo('passwd megh')
   sudo('echo "megh ALL=(ALL) ALL" >> /etc/sudoers')
