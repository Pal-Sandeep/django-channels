first setup venv<br>
using pipenv shell <br>
    pipenv install<br>
build docker image <br>
    docker build . -t django-channels  <br>
run the docker image  <br>
    docker run -d -p 8000:8000  <br>
    django-channels  <br>
