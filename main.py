from abc import ABC, abstractmethod


class FMRIModelBase(ABC):

    def load(self, data):
      print(f"Model: {len(data)} items are loaded.")
    
    @abstractmethod
    def fit(self):
      pass

    @abstractmethod
    def predict(self):
      pass

class ModelA(FMRIModelBase):
  """This is a sort of prototype implementation for our base model."""
  def __init__(self):
    pass

  def fit(self):
    print("ModelA: fitted")

  def predict(self):
    print("ModelA: predicted")


class ModelB(FMRIModelBase):
  """This is a sort of prototype implementation for our base model."""
  def __init__(self):
    pass

  def fit(self):
    print("ModelB: fitted")

  def predict(self):
    print("ModelB: predicted")



data = [1, 2, 3]

ma = ModelA()
ma.load(data)
ma.fit()
ma.predict()

mb = ModelB()
mb.load(data)
mb.fit()
mb.predict()

# mc = ModelC()
# mc.load()
# mc.fit()
# mc.predict()
