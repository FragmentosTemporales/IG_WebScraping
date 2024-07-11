from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    navegador : str
    dir_descargas : str = r'C:\Users\Usuario\OneDrive - Dominion Global\Escritorio\AutoBI\app\downloads'

    user_ig : str
    pw_ig : str

    class Config:
        env_file = '.env'

settings = Settings()