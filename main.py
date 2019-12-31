from cococo.models import ModelA, ModelAExtended, ModelB, ModelBExtended, ModelC
from cococo.runners import basic_runner

if __name__ == "__main__":
  data = [1, 2, 3]

  models = [
    ModelA,
    ModelAExtended,
    ModelB,
    ModelBExtended,
    ModelC,
  ]

  basic_runner(models, data)
