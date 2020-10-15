if [ $FLASK_ENV = "production" ]
then
    service cron start 
    python /app/server/store_new_release.py
    python /app/server/app.py
else
    echo "Server running in development mode."
    echo  "Launch cd /app/server && flask init_test_db to set up the database with fake data"
    echo  "Launch cd /app/server && flask drop_db to reinitialise the database"
    echo  "Launch python /app/server/app.py to start the server"
    /bin/bash
fi