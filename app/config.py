import os
import secrets

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


def project_root():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


class Config:
    SYSTEM_NAME = os.environ.get("SYSTEM_NAME", "智能瞭望与智能问数系统")
    SYSTEM_SHORT_NAME = os.environ.get("SYSTEM_SHORT_NAME", "DataFinderAgentOS")
    
    PORT = int(os.environ.get("PORT", 10010))
    DEBUG = os.environ.get("DEBUG", "true").lower() == "true"
    AUTORELOAD = os.environ.get("AUTORELOAD", "true").lower() == "true"
    
    COOKIE_SECRET = os.environ.get(
        "COOKIE_SECRET",
        os.environ.get("SECRET_KEY", "datafinderagentos-token")
    )
    
    DB_PATH = os.environ.get(
        "DATABASE_PATH",
        os.path.join(project_root(), "database", "finderos.db")
    )
    
    LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
    LOG_PATH = os.environ.get(
        "LOG_PATH",
        os.path.join(project_root(), "logs")
    )
    
    DEFAULT_ADMIN_USERNAME = os.environ.get("DEFAULT_ADMIN_USERNAME", "admin")
    DEFAULT_ADMIN_PASSWORD = os.environ.get("DEFAULT_ADMIN_PASSWORD", "123456")
    
    ENCRYPTION_KEY = os.environ.get("ENCRYPTION_KEY", "")


config = Config()
