from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)
API_ID: int
API_HASH: str


SLEEP_TIME: list[int] = [3600, 7200]
START_DELAY: list[int] = [5, 25]

USE_RANDOM_DELAY_IN_RUN: bool = True
RANDOM_DELAY_IN_RUN: list[int] = [30, 60]


AUTO_TASK: bool = True
CLAIM_REWARD: bool = True
WATCH_ADS: bool = True
AUTO_UPGRADE: bool = True
PAINT_REWARD_MAX: int = 7
ENERGY_LIMIT_MAX: int = 6
RECHARGE_SPEED_MAX: int = 7
AUTO_DRAW: bool = True
ENTER_CODE: bool = True
CODE: list[str] = [happy_halloween]
CUSTOM_TOURNAMENT_TEMPLATE: bool = True
TOURNAMENT_TEMPLATE_ID: str = ""
NIGHT_MODE: bool = True
NIGHT_TIME: list[int] = [0, 7]
USE_PROXY: bool = True



JOIN_TG_CHANNELS: bool = False
USE_REF: bool = True
REF_ID: str = 'f7751345041'


settings = Settings()
