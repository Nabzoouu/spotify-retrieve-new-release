# Documentation
- on SQLAlchemy

https://www.youtube.com/watch?v=4gRMV-wZTQs

# Launch Postgres Database Container
```
docker run --rm -p 5432:5432 -v $PWD/groover_database:/var/lib/postgresql/data --name postgres -e POSTGRES_PASSWORD=password postgres
```
- The default user is _postgres_

__Warning : the volume must be mount on the local and not on a mounted partition (or it will make file autorization error__

- Ici, la db est situé a /Bureau/Programmation

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
Here, you have 2 options :

1st : using the container host
- Find the right container by name, the host should look like _172.17.0.4_ (it is the ip adress of the network inside the container)
- Use 5432 for the port (because it is the port used by postgres image inside the container)
- The default user is _postgres_
- The default password should be specified as an environment variable when the container is launched

2nd : using the host port
- Find the host container ip using the command ```iftable``` or in _Settings > Detail (next to the switch button) > IPv4 Adress)_ (cf : https://techwiser.com/find-ip-address/) 
- Use the mapped port for the port (the one you choosed in the -p parameters, the one which is on the left of the colon)
- The default user is _postgres_
- The default password should be specified as an environment variable when the container is launched

# Organisation of the database

![Diagram of database](./diagram_of_database.png)
