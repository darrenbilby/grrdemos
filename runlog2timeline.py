def RunLog2Timeline(client_id, directories, base_dir='/grrfuse'):
  import subprocess
  client_id = client_id.Basename()
  hostname = console_utils.ClientIdToHostname(client_id)
  filename = '/tmp/plaso/%s.plaso' % hostname
  #os.makedirs(os.path.dirname(filename))
  for dir_path in directories:
    path = os.path.join(base_dir, client_id, dir_path)
    if os.path.exists(path):
      #command = "/usr/bin/log2timeline.py -p --single_thread %s %s" % (filename, path)
      command = "/usr/bin/log2timeline.py --workers=5 -p %s %s" % (filename, path)
      print 'Running: ', command
      subprocess.check_call(command.split())
  if os.path.exists(filename):
    import_command = "/usr/bin/psort.py -a -o timesketch --name '%s Timeline' %s" % (hostname, filename)
    print 'Running: ', import_command
    subprocess.check_call(import_command.split())
DIRS = [r'fs/os/C:/Windows/System32/winevt/Logs']
#, r'fs/os/C:/Windows/System32']
for c in SearchClients('.'):
  RunLog2Timeline(c[0].urn, DIRS)
