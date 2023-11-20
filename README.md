# backend for blue-guam

## Setup

ensure you write a `.env` file with the following environment variables set
```sh
MARIADB_ROOT_PASSWORD=your_mariadb_root_pw
SQL_LOGIN=your_mariadb_user
SQL_PASSWORD=your_mariadb_user_pw
# blueguam.com for example. This defaults to localhost when running in development mode
HOST=the_host_name
# This is the prefix path. this should be left as /api so that the api is accessible at HOST/api
VIRTUAL_PATH=/api
```

## Usage

### Development
`uvicorn api.main:app --reload`  
access the api at `localhost:8000/api`. `localhost:8000/api/places` for example

### Development with DB
This is the prefered method of working on the api.  

Command: `docker compose up --force-recreate --build`  
access the api at `localhost:8000/api` or at `<HOST>/api` (assuming the nginx network has been started up from the frontend repo using `make start-network` from within that repo's directory)

See [DB](#db) section for info about the DB spun up this way

### Production
In order to run this in production mode, ensure that the nginx network is running first by going to the frontend repo directory and running `make start-network`. `HOST` in the `.env` file can be `localhost` if just testing that this builds in production mode, or the actual hostname of the machine. If trying to get the whole project running in production mode from your computer, you can use [ngrok](https://ngrok.com/) to host your localhost on a domain.  

Command: `docker compose -f docker-compose.production.yml up -d --force-recreate --build`  
`--force-recreate` ensures that the service is rebuilt if it's already running  
`--build` rebuilds it if necessary. useful for if `.env` values change  
`-d` runs it in detached mode (in the background)  
To see the logs of these detached containers, run `docker compose -f docker-compose.production.yml logs -f`. The second `-f` will follow the logs as they are written  

`docker compose -f docker-compose.production.yml down` to spin down the containers

#### DB
note, this spins up the db container also. 

If you need to start off with a fresh db
1. spin down the containers `docker compose down`
2. remove the db container `docker rm blue-guam-db`
3. so that we can remove the db volume `docker volume rm blue-backend_db`

If you want a mariaDB shell, you will need open one via connecting to the container.
`docker exec -it blue-guam-db mariadb -u<username> -p`


## notes:
trying to track:
    activity title

    description+/notes

    where = google maps link -> leaflet lat, long

    what time = what days, what hour range, (thinking of also whether or not the event is one off or recurring)
    
    author name and contact (phone number)
