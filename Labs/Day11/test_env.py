def test_environment(env):
    print("Environment:", env)
    assert env in ["dev", "qa", "prod"]
