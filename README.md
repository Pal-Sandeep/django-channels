first setup venv
using pipenv shell
    pipenv install
build docker image
    docker build . -t django-channels
run the docker image
    docker run -d -p 8000:8000
    django-channels
