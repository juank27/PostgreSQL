from psycopg2 import connect

HOST = 'ec2-44-207-133-100.compute-1.amazonaws.com'
USER = 'qfwdpxbgjqavtf'
PASSWORD = 'eadd9d43080e6a143bad98eeffbd90c43404b4007e89e5c1ebe0e75526b1b19f'
PORT = 5432
DATABASE = 'd82if8oasjirp3'

def get_connection():
	try:
		connection = connect(
			host=HOST,
			user=USER,
			password=PASSWORD,
			port=PORT,
			dbname=DATABASE
			#database=DATABASE
		)
		return connection
	except Exception as e:
		print(e)
		return None