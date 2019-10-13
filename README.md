# Shipment system homework for Kuehne-Nagel by Felix Porcelli

## Project setup

On a termianl, type:

```
yarn install

pip install pipenv

pipenv install

pipenv shell
```

### Compiles and hot-reloads for development
Tyepe, on one terminal:
```
yarn dev
```
And, on other:
```
py ./api/manage.py runserver
```

After this, just go to your preference browser and access the [localhost:8080](http://localhost:8080/)

### Compiles and minifies for production
```
yarn build
```

### Run your tests
With pipenv setup, just run:
```
py ./api/manage.py test shipment
```

## A bit about the project

Here you can find a web system for shipment control based on Vue and Django Rest API architecture.

All the requests from the homework were implemented. On the frontend, you can find the above characteristics on:

- *List*: on the List section. You just need to go to the page to see it.
- *Retrieve*: on home section there's a card where you can type the track code and all important informations will be displayed on the screen (note that you need to previous know a code).
- *Create*: on the Register section of the website. Just fill in all information and click on the register button.
- *Update*: inside List section, just click on the modify button, change what you need and hit the save button.
- *Delete*: inside List again, identify the shipment you want to delet and press the delete button referent to it.