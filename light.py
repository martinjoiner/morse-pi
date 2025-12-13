class Light:
  """ Abstract class to be extended for different interfaces """

  def on(self):
    """ Puts the light into whatever state represents on """
    print("On")

  def off(self):
    """ Puts the light into whatever state represents off """
    print("Off")

  def finish(self):
    """ Clean-up any leftover state from on() or off() """
    return
