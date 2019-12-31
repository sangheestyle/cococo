class ModelA:
  """This is a sort of prototype implementation for our base model."""
  def __init__(self):
    pass

  def load(self):
    print("ModelA: loaded")

  def fit(self):
    print("ModelA: fitted")

  def predict(self):
    print("ModelA: predicted")


class ModelB:
  """This is a sort of prototype implementation for our base model."""
  def __init__(self):
    pass

  def load(self):
    print("ModelB: loaded")

  def fit(self):
    print("ModelB: fitted")

  def predict(self):
    print("ModelB: predicted")


ma = ModelA()
ma.load()
ma.fit()
ma.predict()

mb = ModelB()
mb.load()
mb.fit()
mb.predict()
