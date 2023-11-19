from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from configs.database import database_secrets


url = f"mysql+pymysql://{database_secrets['user']}:{database_secrets['password']}@mysql:3306/main_db"

engine = create_engine(url)

if not database_exists(engine.url):
    create_database(engine.url)
    print("Database was successfully created.")
else:
    print("Skiping database creation, it already exists.")