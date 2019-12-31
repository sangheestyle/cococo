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


class ModelBExtended(ModelB):
  def predict(self):
    print("ModelBExtended: predicting")


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


def runner(models, data):
    for model in models:
        print(f"--> Running on {model}")
        m = model()
        m.load(data)
        m.fit()
        m.predict()


data = [1, 2, 3]

models = [
  ModelA,
  ModelAExtended,
  ModelB,
  ModelBExtended,
  ModelC,
]

runner(models, data)
