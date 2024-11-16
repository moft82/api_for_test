from app.db.database import db

def get_db():
    """
    Dependency that provides a database session for the duration of the request.
    """
    db_session = None
    try:
        db_session = db.get_session()
        yield db_session
    finally:
        if db_session:
            db_session.close()
