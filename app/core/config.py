from dotenv import load_dotenv
import os

class Config():
    def __init__(self) -> None:
        # Load the common .env file
        common_env_file = os.path.join(os.path.dirname(__file__), "../.env")
        load_dotenv(common_env_file)
        
        self.APP_ENV:str = os.getenv('APP_ENV', 'development')
        self.load_environment_config()
        
        
    def load_environment_config(self):
        # Load environment-specific .env file
        env_file = os.path.join(os.path.dirname(__file__), f"../.env.{self.APP_ENV}")
        load_dotenv(env_file)
        
        # Load common settings
        self.DB_URL = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PWD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
        
        # Load environment-specific settings
        if self.APP_ENV == "testing":
            self.load_testing_config()
        elif self.APP_ENV == "production":
            self.load_production_config()
        else:
            self.load_development_config()
            
        print(f"APP_ENV : {self.APP_ENV}")
        print(f"DB_URL : {self.DB_URL}")
        
    def load_development_config(self):
        self.DEBUG = True
        
    def load_testing_config(self):
        self.DEBUG = True
        
    def load_production_config(self):
        self.DEBUG = False