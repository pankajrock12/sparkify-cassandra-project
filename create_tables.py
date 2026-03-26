import psycopg2, configparser
from sql_queries import create_table_queries, drop_table_queries

def main():
    try:
        print("🔹 Reading config file...")
        config = configparser.ConfigParser()
        config.read('dwh.cfg')

        print("🔹 Connecting to Redshift...")
        conn = psycopg2.connect(
            host=config.get("CLUSTER","HOST"),
            dbname=config.get("CLUSTER","DB_NAME"),
            user=config.get("CLUSTER","DB_USER"),
            password=config.get("CLUSTER","DB_PASSWORD"),
            port=config.get("CLUSTER","DB_PORT")
        )

        cur = conn.cursor()
        print("✅ Connected successfully!")

        print("\n🗑 Dropping tables...")
        for i, q in enumerate(drop_table_queries, 1):
            print(f"   Dropping table {i}...")
            cur.execute(q)
            conn.commit()

        print("✅ Drop complete!")

        print("\n📦 Creating tables...")
        for i, q in enumerate(create_table_queries, 1):
            print(f"   Creating table {i}...")
            cur.execute(q)
            conn.commit()

        print("✅ Tables created successfully!")

        conn.close()
        print("🔒 Connection closed.")

    except Exception as e:
        print("❌ ERROR OCCURRED:")
        print(e)


if __name__ == "__main__":
    main()