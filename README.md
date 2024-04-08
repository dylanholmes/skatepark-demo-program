# skatepark-demo-program

### Super Simple Run

```
docker build --file Dockerfile -t test-skatepark:latest .
docker run --rm --name test-skatepark-container test-skatepark:latest "what's cooking"
```