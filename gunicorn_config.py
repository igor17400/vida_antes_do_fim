import os
from dotenv import load_dotenv

cwd = os.getcwd()
dotenv_path = os.path.join(cwd, os.getenv('ENVIRONMENT_FILE', '.env.development'))
load_dotenv(dotenv_path=dotenv_path, override=True)

APP_HOST = os.environ.get('HOST')
APP_PORT = int(os.environ.get('PORT'))

bind = f'{APP_HOST}:{APP_PORT}'
workers = 2
