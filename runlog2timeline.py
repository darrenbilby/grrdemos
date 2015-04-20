def RunLog2Timeline(client_id, directories, base_dir='/grrfuse/fs/os'):
  import subprocess
  client_id = client_id.Basename()
  hostname = console_utils.ClientIdToHostname(client_id)
  filename = '/tmp/plaso/%s.plaso' % hostname
  for dir_path in directories:
    path = os.path.join(base_dir, client_id, dir_path)
    if os.path.exists(path):
      command = "/usr/bin/log2timeline.py -p %s %s" % (filename, path)
      print 'Running: ', command
      subprocess.check_call(command.split())
  if os.path.exists(filename):
    import_command = "/usr/bin/psort.py -a -o timesketch --name '%s Timeline' %s" % (hostname, filename)
    print 'Running: ', import_command
    subprocess.check_call(import_command, shell=True)

DIRS = [r'C:/Windows/System32/winevt/Logs', 'C:/Windows', '/var/log', '/bin', '/sbin', '/usr/sbin']

for c in SearchClients('.'):
  RunLog2Timeline(c[0].urn, DIRS)
