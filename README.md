AntiBoredom
================

The application AntiBoredom allows you to find an activity (thanks to
the [boredAPI](https://www.boredapi.com/)) and, just for fun, gives you
a joke (thanks to the [jokeAPI](https://sv443.net/jokeapi/v2/#try-it))
which contains words from the activity found.

It has been deployed to heroku services at
<https://marbotteantiboredom.herokuapp.com>.

The original idea is from Daniel Fernando López Lozano and Erika Suarez
Valencia from the Colombian [“Instituto de investigación Alexander von
Humboldt”](http://humboldt.org.co/es/) and served as a test to
candidates for participating to a call with the institute.

# 1 How to use Antiboredom

The application antiboredom is thought as a restful API with 3 main
“GET” endpoint:

1.  the **ActJoke** *GET* endpoint take a “type_activity” argument and
    allows you to search for an activity from the selected type and a
    joke associated, containing a word from the activity description. It
    is available through
    <https://marbotteantiboredom.herokuapp.com/ActJoke/><activity_type>,
    where <activity_type> is one of:
    -   education
    -   recreational
    -   social
    -   diy
    -   charity
    -   cooking
    -   relaxation
    -   music
    -   busywork
2.  the **Export** *GET* endpoint allows you to get a csv file with the
    results previous requests to the API
    (<https://marbotteantiboredom.herokuapp.com/Export>)
3.  the **ExportComplete** is very similar to the **Export** endpoint
    but return a more comprehensive file from the log table of the
    application database
    (<https://marbotteantiboredom.herokuapp.com/ExportComplete>)

## 1.1 In a web browser

Connect to <https://marbotteantiboredom.herokuapp.com/> in order to get
some very simple explanations.

You might as well connect directly to the addresses described in the
last paragraph.

## 1.2 Bash

You may use directly the *curl* bash application to access the API:

``` bash
curl https://marbotteantiboredom.herokuapp.com/ActJoke/social
```

    ##   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
    ##                                  Dload  Upload   Total   Spent    Left  Speed
    ##   0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0  0     0    0     0    0     0      0      0 --:--:--  0:00:02 --:--:--     0  0     0    0     0    0     0      0      0 --:--:--  0:00:03 --:--:--     0  0     0    0     0    0     0      0      0 --:--:--  0:00:04 --:--:--     0100   141  100   141    0     0     34      0  0:00:04  0:00:04 --:--:--    34
    ## {"activity": "Invite some friends over for a game night", "joke": "I have a joke about Stack Overflow, but you would say it's a duplicate."}

``` bash
curl https:///marbotteantiboredom.herokuapp.com/Export | head | column -t -s, 
```

    ##   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
    ##                                  Dload  Upload   Total   Spent    Left  Speed
    ##   0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0100  5148  100  5148    0     0   5368      0 --:--:-- --:--:-- --:--:--  5362
    ## (23) Failed writing body
    ##    type        activity                                     key      joke                                                                                                                                                                                                      id                                                                                                                                                                
    ## 0  social      Have a bonfire with your close friends       8442249  Why did the JavaScript heap close shop? -> It ran out of memory.                                                                                                                                          31.0                                                                                                                                                              
    ## 1  social      Go to an escape room                         5585829  I can't believe I got fired from the calendar factory. -> All I did was take a day off.                                                                                                                   303.0                                                                                                                                                             
    ## 2  social      Go on a fishing trip with some friends       3149232  Why should you never talk to pi? -> Because it will go on forever.                                                                                                                                        318.0                                                                                                                                                             
    ## 3  social      Hold a yard sale                             1432113  "I'll never forget my Granddad's last words to me just before he died. ""Are you still holding the ladder?"""                                                                                             208.0                                                                                                                                                             
    ## 4  social      Go on a fishing trip with some friends       3149232  Why did the banana go see a doctor? -> Because it wasn't peeling well.                                                                                                                                    256.0                                                                                                                                                             
    ## 5  cooking     Prepare a dish from a foreign culture        8061754  "I bought some shoes from a drug dealer. I don't know what he laced them with                                                                                                                              but I was tripping all day!"                                                                                 204.0                                               
    ## 6  relaxation  Look at pictures and videos of cute animals  2565076  How can you tell an extroverted programmer? -> He looks at YOUR shoes when he's talking.                                                                                                                  17.0                                                                                                                                                              
    ## 7  cooking     Make homemade ice cream                      3818400  "My girlfriend's dog died                                                                                                                                                                                  so I tried to cheer her up by getting her an identical one. It just made her more upset. She screamed at me   ""What am I supposed to do with two dead dogs?"""  275.0
    ## 8  cooking     Learn a new recipe                           6553978  "Today I learned that changing random stuff until your program works is ""hacky"" and a ""bad coding practice"" but if you do it fast enough it's ""Machine Learning"" and pays 4x your current salary."  33.0

## 1.3 Python

In python the access to the API is possible through *requests*.

``` python
import requests

def getActJoke(type_act):
  api= f"https://marbotteantiboredom.herokuapp.com/ActJoke/{type_act}"
  response = requests.get(api)
  content = response.json()
  return content

getActJoke("charity")
```

    ## {'activity': 'Donate to your local food bank', 'joke': 'Why was the river rich? -> Because it had two banks.'}

## 1.4 R

In R the access to the API is possible through the packages *httr* and
*jsonlite*.

``` r
require(httr)
```

    ## Loading required package: httr

``` r
require(jsonlite)
```

    ## Loading required package: jsonlite

``` r
getActJoke <- function(type_act)
{
  api <- paste0("https://marbotteantiboredom.herokuapp.com/ActJoke/",type_act)
  res <- GET(api)
  rawToChar(res$content)
}
getActJoke("relaxation")
```

    ## [1] "{\"activity\": \"Take your dog on a walk\", \"joke\": \"The past, the present and the future walk into a bar. -> It was tense.\"}\n"

# 2 Deployment

The application has been thought to be deployed in Heroku services.

If you want to clone the repository and deploy again (with or without
modifications), you will need:

-   a heroku account
-   git
-   the heroku cli (you may do it through the heroku website)
-   python3
-   postgreSQL
-   psql

You may check in the file [runtime.txt](./runtime.txt) which version of
Python I used, and in the file [requirement.txt](./requirement.txt) the
Python extension which are necessary to install to run the application.

To clone the repository:

    git clone https://github.com/marbotte/antiBoredom.git

Login in heroku:

    heroku login

Create a local database, which you will use to push into the heroku
application database:

    createdb antiboredom

Create a
[pgpass](https://www.postgresql.org/docs/9.3/libpq-pgpass.html), in
order not to worry about your credentials to connect to the local
database:

Initialize the local postgres database with the \<initializeDb.sql>
file:

    psql antiboredom -f initializeDb.sql

Here you might want to do, for the application to interact with your
database when running locally:

    export DATABASE_URL=postgres://localhost/antiboredom

(**NOTE** I think you have to replace “export” by “set” in windows)

Create your application in Heroku and push the local repository:

    heroku create
    git push heroku main

Import the postgres addon in your heroku application

    heroku addons:create heroku-postgresql:hobby-dev

Push the local database into the database of the Heroku hosted
application

    heroku pg:push antiboredom DATABASE_URL

Deploy the heroku based application

    heroku ps:scale web=1
    heroku open

More explanation
[here](https://devcenter.heroku.com/articles/getting-started-with-python)

# 3 Exercise statements (in spanish)

Implementar un servicio web que exponga los siguientes endpoints:

1.  Un endpoint GET que recibe una palabra y retorna un objeto json con
    los atributos actividad y chiste.
2.  Un endpoint GET que permite descargar la bitácora del servicio en
    formato .csv

El primer endpoint debe cumplir con las siguientes características:

-   Hacer una petición a Bored API enviándole la palabra recibida como
    el parámetro type, tomar alguna de las palabras de la actividad
    retornada y hacer una petición a JokeAPI enviando la palabra de la
    actividad como el parámetro contains, la respuesta del endpoint es
    la actividad retornada por Bored API y el chiste retornado por
    JokeAPI
-   Si la palabra tomada de la actividad de Bored API no retorna
    resultados en JokeAPI, intentar con otra, si no retorna resultados
    con ninguna retornar “Esta es una actividad muy aburrida” como
    chiste en la respuesta del endpoint
-   Si la palabra recibida por el usuario no corresponde a un tipo
    válido para Bored API, retornar un error con un mensaje explicativo
-   Si el chiste retornado por JokeAPI es de 2 partes (type=twopart) el
    chiste de la respuesta debe contener las dos partes concatenadas con
    los caracteres “->” (sin las comillas)
-   Debe escribir en una base de datos el registro de la petición y
    almacenar los siguientes campos, de la respuesta de Bored API: type,
    activity, key; de la respuesta de JokeAPI: joke (si es de dos
    partes, concatenado también), id.

El segundo endpoint debe retornar un .csv con el contenido de la tabla
descrita en el último punto de la sección anterior

# 4 How to contribute

This application was mostly a proof of concept, and a way to participate
on a call from the Instituto Humboldt, so I do not plan to work much
more on its development, but do not use to fork and PR if you are
interested.
