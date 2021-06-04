from app.db import Base, engine, get_session
from sqlalchemy import text

async def init():
    Base.metadata.create_all(bind=engine)
    # ses = await get_session()
    # stat = text("""
    # CREATE FUNCTION token_table_delete_old_rows() RETURNS trigger
    #     LANGUAGE plpgsql
    #     AS $$
    # BEGIN
    #     DELETE FROM token WHERE created_date < NOW() - INTERVAL '1 day';
    #     RETURN NEW;
    # END;
    # $$;

    # CREATE TRIGGER token_table_delete_old_rows_trigger
    #     AFTER INSERT ON 
    #     EXECUTE PROCEDURE token_table_delete_old_rows();

    # """)
    # await ses.execute(stat)
