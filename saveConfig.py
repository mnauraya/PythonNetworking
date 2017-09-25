class saveConfig():
  def __saveConfig__(self, connectHandle):
      connection = connectHandle
      output = connection.send_command_expect('wr')##sends the command wr in order to save the running config to startup
      print output
