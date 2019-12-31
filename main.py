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


m = ModelA()
m.load()
m.fit()
m.predict()
