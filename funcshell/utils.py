import cmd

class CommandShell(cmd.Cmd):
  def __init__(self, callback):
    """Setup shell."""
    cmd.Cmd.__init__(self)
    self.prompt = '> '
    self.use_rawinput = True
    self.callback = callback

  def default(self, line):
    if line == 'EOF':
      print ''
      return True
    self.callback(line)

  def do_exit(self, line):
    return True

  def help_exit(self, line): self.default(line)
  def help_help(self, line): self.default(line)
  def emptyline(self): pass
