import re


def select_submission(config, reddit):
    resolution = config['resolution']

    selected_submission = None
    for subreddit in config['subreddits']:
        valid_submissions = _load_wallpaper_submissions(
            reddit, subreddit, resolution)
        if len(valid_submissions) == 0:
            continue
        for submission in valid_submissions:
            if _validate_url(submission):
                return submission

    return None


def _validate_url(submission):
    # Match only direct reddit images for now, that way it is bit safer
    # since it should avoid downloading completely random stuff from the internet.
    matching = re.match(r'https://i\.redd\.it/[\d\w]*\.jpg', submission.url)
    if not matching:
        print(f"Invalid url {submission.url}")
    return matching


def _load_wallpaper_submissions(reddit, subreddit_name: str, resolution: (int, int)):
    subreddit = reddit.subreddit(subreddit_name)
    return [x for x in subreddit.top('day', limit=24) if _is_good_resolution(x.title, resolution)]


def _is_good_resolution(title: str, resolution: (int, int)):
    matching = re.search(
        f"{resolution[0]}(px)?\\s?.\\s?{resolution[1]}(px)?", title) is not None
    if not matching:
        print(f"Discarding \"{title}\" not matching resolution")
    else:
        print(f"Found \"{title}\" with matching resolution")
    return matching
