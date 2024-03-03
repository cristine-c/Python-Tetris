class Colors:
  grey = (70, 70, 70)
  red = (255, 173, 173)
  orange = (255, 214, 165)
  yellow = (253, 255, 182)
  green = (202, 255, 191)
  blue = (155, 246, 255)
  purple = (189, 178, 255)
  pink = (255, 198, 255)
  white = (255, 255, 255)
  # used for the screen background
  dark_blue = (86, 117, 185)
  
  @classmethod
  def get_cell_colors(cls):
    return [cls.grey, cls.red, cls.orange, cls.yellow, cls.green, cls.blue, cls.purple, cls.pink]