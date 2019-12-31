def basic_runner(models, data):
    for model in models:
        print(f"--> Running on {model}")
        m = model()
        m.load(data)
        m.fit()
        m.predict()
