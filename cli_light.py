from light import Light


class CLILight(Light):
  block = ' ' * 42

  def on(self):
    print(f'\r\x1B[103m{self.block}', end='')


  def off(self):
    print(f'\r\x1B[0m{self.block}', end='')


  def finish(self):
    print('\r')
