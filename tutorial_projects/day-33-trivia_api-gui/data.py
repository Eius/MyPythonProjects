import requests


def get_random_questions():
    parameters = {
        "amount": 10,
        "type": "boolean",
        "category": 27
    }
    req = requests.get("https://opentdb.com/api.php", params=parameters)
    questions = req.json()["results"]
    return questions
