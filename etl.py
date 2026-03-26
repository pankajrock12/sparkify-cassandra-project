
import psycopg2, configparser
from sql_queries import insert_table_queries

def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect(
        host=config.get("CLUSTER","HOST"),
        dbname=config.get("CLUSTER","DB_NAME"),
        user=config.get("CLUSTER","DB_USER"),
        password=config.get("CLUSTER","DB_PASSWORD"),
        port=config.get("CLUSTER","DB_PORT")
    )

    cur = conn.cursor()

    copy_events = f"""
    COPY staging_events FROM '{config.get("S3","LOG_DATA")}'
    IAM_ROLE '{config.get("IAM_ROLE","ARN")}'
    FORMAT AS JSON '{config.get("S3","LOG_JSONPATH")}';
    """

    copy_songs = f"""
    COPY staging_songs FROM '{config.get("S3","SONG_DATA")}'
    IAM_ROLE '{config.get("IAM_ROLE","ARN")}'
    FORMAT AS JSON 'auto';
    """

    cur.execute(copy_events); conn.commit()
    cur.execute(copy_songs); conn.commit()

    for q in insert_table_queries:
        cur.execute(q); conn.commit()

    conn.close()

if __name__ == "__main__":
    main()
