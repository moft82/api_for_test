from app.db.database import db

def get_db():
    db_session = None
    try:
        db_session = db.get_session()
        yield db_session
    finally:
        if db_session:
            db_session.close()
