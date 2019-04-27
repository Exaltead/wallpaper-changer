import json
import praw
import selection


def _load_secret_config(filename: str):
    with open(filename, mode='r') as f:
        return json.load(f)


def main():
    config = _load_secret_config("keys.secret.json")
    reddit = praw.Reddit(client_id=config['client_id'],
                         client_secret=config['client_secret'],
                         user_agent=config['user_agent'])
    submission = selection.select_submission(config, reddit)
    print(submission.title)


if __name__ == "__main__":
    main()
