import os

from dotenv import load_dotenv
from sqlalchemy.engine import URL

load_dotenv() # load env var from .env for the function
def get_db_url() -> URL:
    return URL.create(
        drivername="mysql+pymysql",
        username=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        host=os.environ.get("DB_HOST", "localhost"),
        port=int(os.environ.get("DB_PORT", "3306")),
        database=os.environ["DB_NAME"],
        query={"charset": "utf8mb4"}
    )
