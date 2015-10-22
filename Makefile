env:
	pyvenv pyvenv
	pyvenv/bin/python -m pip install Flask
	pyvenv/bin/python -m pip install flask-wtf
	pyvenv/bin/python -m pip install flask-sqlalchemy
	pyvenv/bin/python -m pip install sqlalchemy-migrate

db:
	pyvenv/bin/python db_create.py
	pyvenv/bin/python db_migrate.py
	pyvenv/bin/python db_upgrade.py

clean_db:
	rm -rf app.db db_repository

clean: clean_db
	rm -rf pyvenv
