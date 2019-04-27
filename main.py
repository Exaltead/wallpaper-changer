import json
import re
import praw


def load_secret_config(filename: str):
    with open(filename, mode='r') as f:
        return json.load(f)


def load_wallpaper_submissions(reddit: praw.Reddit, subreddit_name: str, resolution: (int, int)):
    subreddit = reddit.subreddit(subreddit_name)
    return [x for x in subreddit.top('day', limit=24) if is_good_resolution(x.title, resolution)]


def is_good_resolution(title: str, resolution: (int, int)):
    matching = re.search(
        f"{resolution[0]}(px)?\\s?.\\s?{resolution[1]}(px)?", title) is not None
    if not matching:
        print(f"Discarding \"{title}\" not matching resolution")
    else:
        print(f"Found \"{title}\" with matching resolution")
    return matching


def main():
    config = load_secret_config("keys.secret.json")
    reddit = praw.Reddit(client_id=config['client_id'],
                         client_secret=config['client_secret'],
                         user_agent=config['user_agent'])
    valid_submissions = load_wallpaper_submissions(
        reddit, 'wallpapers', (1920, 1080))
    print(valid_submissions)


if __name__ == "__main__":
    main()
