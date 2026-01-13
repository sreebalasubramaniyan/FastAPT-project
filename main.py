# to run an api we need to import uvicorn
import uvicorn

if __name__ == "__main__":
    # app
    # host - domain we run our api(0.0.0 means available local host, we can access it and one who knows the private key also can acces this )
    # port - 8000 access /hello-world
    # reload - everytime we  update the file the server will restart
    uvicorn.run(app="app.app:app",host="127.0.0.1",port=8000,reload=True)

    # 127.0.0.1/docs - /docs its an endpoint
        # go and execute and see, the response from our API app that we created
    # 127.0.0.1/redoc - similar version of above endpoint
    # or we can also use http://localhost:8000/hello-world

