import re


def add_score(username: str, score: int):
    # Check if user not already in the text file

    users = open(f"temp/users.txt", "r")
    if username not in users.read():
        users.close()
        users = open(f"temp/users.txt", "a")
        users.write(f"{username}\n")

    won = "win"
    if score < 0:
        won = "lose"

    current = open(f"temp/{username}.txt", "a")
    current.write(f"points:{score},{won}\n")
    current.close()


add_score("Maha", 10000)


def check_score(username: str):
    pattern = r"points:(?P<pts>-*[0-9]+),(?P<res>[a-z]+)"
    try:
        current = open(f"temp/{username}.txt", "r")
        total_score = 0
        for line in current.readlines():
            matches = re.finditer(pattern, line)
            for match in matches:
                total_score += int(match["pts"])
        if total_score < 0:
            current.close()
            current = open(f"temp/{username}.txt", "w")
            current.write("")
            current.close()
            return "Your Score Has Reset"
        return total_score
    except FileNotFoundError:
        return "Not A Valid Username"


print(check_score("Maha"))


def get_points(len_hidden_word: int, missing_letter: int):
    if missing_letter > 0:
        return missing_letter * -20
    else:
        return len_hidden_word * 10


print(get_points(10, 2))