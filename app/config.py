from pydantic import BaseSettings


class Settings(BaseSettings):
    mysql_user: str = ""
    mysql_password: str = ""
    mysql_server: str = ""
    mysql_port: str = ""
    mysql_db: str = "res_db"

    class Config:
        env_file = ".env"

settings = Settings()