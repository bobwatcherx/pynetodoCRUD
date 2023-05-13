import pynecone as pc

class YtappConfig(pc.Config):
    pass

config = YtappConfig(
    app_name="ytapp",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
