from typing import Dict, List
from pathlib import Path
import yaml
from pydantic import BaseModel

from app.paths import SERVICE_CONFIG_PATH

class RateLimitConfig(BaseModel):
    default: str
    auth: str
    health: str
    exclude_paths: List[str]
    custom_paths: Dict[str, str]

class CORSConfig(BaseModel):
    allow_origins: List[str]
    allow_credentials: bool
    allow_methods: List[str]
    allow_headers: List[str]

class Config(BaseModel):
    rate_limits: RateLimitConfig
    cors: CORSConfig

    @classmethod
    def from_yaml(cls, file_path: str | Path | None = None) -> 'Config':
        """
        Load configuration from YAML file.
        
        Args:
            file_path: Path to config file. If not provided, will use SERVICE_CONFIG_PATH.
        
        Returns:
            Config: Loaded configuration
        """
        config_path = Path(file_path) if file_path else SERVICE_CONFIG_PATH
        
        if not config_path.exists():
            raise FileNotFoundError(f"Configuration file not found at {config_path}")
        
        with open(config_path, "r") as f:
            config_dict = yaml.safe_load(f)
        
        return cls.model_validate(config_dict) 