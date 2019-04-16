"""
q06.py

Build a website using user input and astronomy picture of the day.
"""


# Joshua Shin
# A01056181
# April 9th 2019


import requests
import json


def request_astronomy_picture_of_the_day_src() -> str:
    """
    Return the source of Astronomy Picture of the Day.

    RETURN source of Astronomy Picture of the Day
    """
    url = "https://api.nasa.gov/planetary/apod?api_key=M4115FENjIimy6fhvlebJgYsf4TbCr7eQ75dyenI"
    res = requests.get(url)
    while res.status_code != requests.codes.ok:
        pass
    return json.loads(res.text)["hdurl"]


def website():
    """
    Build a website with the given name and description and the Astronomy Picture of the Day.

    POST-CONDITION index.html is created with name, description and Astronomy Picture of the Day
    """
    with open("index.html", "w") as file_object:
        name = input("Name: ")
        description = input("Description: ")
        content = """
        <!doctype html>
        <html lang="en">
            <head>
                <meta charset="utf-8">
                <title>Introduction</title>
                <meta name="description" content="%s's webpage">
                <meta name="author" content="%s">
                <link rel="stylesheet" href="css/styles.css?v=1.0">
            </head>
            <body>
                <img src="%s" alt="Astronomy Picture of the Day">
                <center>
                    <h1>%s</h1>
                </center>
                %s
            </body>
        </html>   
        """
        file_object.write(content % (name, name, request_astronomy_picture_of_the_day_src(), name, description) + '\n')


def main():
    website()


if __name__ == "__main__":
    main()
