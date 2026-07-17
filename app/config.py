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

# ---- 启动时安全警告 ----
import logging as _warn_log
_warn = _warn_log.getLogger("security")

if config.COOKIE_SECRET == "datafinderagentos-token":
    _warn.warning(
        "⚠️  COOKIE_SECRET 使用了默认值，会话可被伪造！"
        "请在环境变量或 .env 中设置一个随机长字符串（≥32位）。"
    )

if config.DEFAULT_ADMIN_PASSWORD == "123456":
    _warn.warning(
        "⚠️  DEFAULT_ADMIN_PASSWORD 使用了默认值 123456，"
        "请尽快在环境变量中修改管理员密码。"
    )

if not config.ENCRYPTION_KEY:
    _warn.warning(
        "⚠️  ENCRYPTION_KEY 未设置，API密钥将以明文形式存储！"
        "请在环境变量中设置 ENCRYPTION_KEY。"
    )
