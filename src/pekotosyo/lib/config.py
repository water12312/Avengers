import os
#SQLALchemyの設定

SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://{user}:{password}@{host}/pekotosyo'.format(**{
    'user':os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', 'ZBtH6myf'),
    'host': os.getenv('DB_HOST', 'localhost:5432'),
    })

SQLALCHEMY_TRACK_MODIFICATION = False

SECRETKEY = 'secret_key'
