from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import Config

Base = declarative_base()
class DataBase:
    def __init__(self) -> None:
        config =Config()
        self._engine = create_engine(config.DB_URL, pool_recycle=500)
        self._session = sessionmaker(autocommit=False, autoflush=False, bind=self._engine)
        # self.init_app()

    # def init_app(self) -> None:
    #     self._engine = create_engine(const.DB_URL, pool_recycle=500)
    #     self._session = sessionmaker(autocommit=False, autoflush=False, bind=self._engine)


    def get_db(self):
        """
        요청마다 DB 세션 유지 함수
        :return:
        """
        db_session = None
        if self._session is None:
            raise Exception("must be called 'init_app'")
        try:
            db_session = self._session()
            yield db_session
        finally:
            db_session.close()

    @property
    def session(self):
        return self.get_db

    @property
    def engine(self):
        return self._engine
    
    def get_session(self):
        """
        Method to get a database session without using a generator.
        """
        return self._session()
    
db = DataBase()