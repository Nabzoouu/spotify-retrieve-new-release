# Launch Postgres Database Container
```
docker run --rm -p 5432:5432 -v $PWD/groover_database:/var/lib/postgresql/data --name postgres -e POSTGRES_PASSWORD=password postgres
```
- The default user is _postgres_

__Warning : the volume must be mount on the local and not on a mounted partition (or it will make file autorization error__

# Launch Postgres Admin Container
```
docker run -p 8888:80 --rm --name pgadmin -e 'PGADMIN_DEFAULT_EMAIL=nabil@gmail.com' -e 'PGADMIN_DEFAULT_PASSWORD=SuperSecret' dpage/pgadmin4
```
__Warning : PGADMIN_DEFAULT_EMAIL must be a valid email with @ and .com__

# Connect to the database in a container
- Right click on server
- Click on _Create > Server..._
- To find the host name of the container, type on a terminal
```
docker network inspect bridge
```
- Find the right container by name, the host should look like _172.17.0.4/16_
- The default user is _postgres_
- The default password should be specified as an environment variable when the container is launched

# Organisation of the database

![Diagram of database](./diagram_of_database.png)