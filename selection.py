import re


def select_submission(config, reddit):
    resolution = config['resolution']

    selected_submission = None
    bests = []

    for subreddit in config['subreddits']:
        valid_submissions = _load_wallpaper_submissions(
            reddit, subreddit, resolution)

        if len(valid_submissions) == 0:
            continue

        for submission in valid_submissions:
            if _validate_url(submission):
                bests.append(submission)
                break

    if len(bests) == 0:
        return None
    best = max(bests, key=lambda x: x.score)
    return best


def _validate_url(submission):
    matches_reddit = re.match(
        r'https://i\.redd\.it/[\d\w]*\.jpg', submission.url)
    matches_imgur = re.match(
        r'https://i\.imgur\.com/[\d\w]*\.jpg', submission.url)
    return matches_reddit or matches_imgur


def _load_wallpaper_submissions(reddit, subreddit_name: str, resolution: (int, int)):
    subreddit = reddit.subreddit(subreddit_name)
    return [x for x in subreddit.top('day', limit=24) if _is_good_resolution(x.title, resolution)]


def _is_good_resolution(title: str, resolution: (int, int)):
    return re.search(
        f"{resolution[0]}(px)?\\s?.\\s?{resolution[1]}(px)?", title) is not None
