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


class ModelAExtended(ModelA):
  def fit(self):
    print("ModelAExtended: fitted")


class ModelB(FMRIModelBase):
  """This is a sort of prototype implementation for our base model."""
  def __init__(self):
    pass

  def fit(self):
    print("ModelB: fitted")

  def predict(self):
    print("ModelB: predicted")


class ModelC(FMRIModelBase):
  """This is a sort of prototype implementation for our base model."""
  def __init__(self):
    pass

  def load(self, data):
    print("ModelC: loaded")

  def fit(self):
    print("ModelC: fitted")

  def predict(self):
    print("ModelC: predicted")


data = [1, 2, 3]

ma = ModelA()
ma.load(data)
ma.fit()
ma.predict()

ma_extended = ModelAExtended()
ma_extended.load(data)
ma_extended.fit()
ma_extended.predict()

mb = ModelB()
mb.load(data)
mb.fit()
mb.predict()

mc = ModelC()
mc.load(data)
mc.fit()
mc.predict()
