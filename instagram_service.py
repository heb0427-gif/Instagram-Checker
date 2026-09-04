
import re
from datetime import datetime
from zoneinfo import ZoneInfo

import instaloader


loader = instaloader.Instaloader()


def get_instagram_data(url):
    if not isinstance(url, str):
        return None, None, "INVALID_URL"

    match = re.search(
        r"/(?:p|reel)/([^/?]+)",
        url
    )

    if not match:
        return None, None, "INVALID_URL"

    shortcode = match.group(1)

    try:
        post = instaloader.Post.from_shortcode(
            loader.context,
            shortcode
        )

        return (
            post.likes,
            post.comments,
            "SUCCESS"
        )

    except Exception as e:
        return (
            None,
            None,
            type(e).__name__
        )


def get_korea_time():
    return datetime.now(
        ZoneInfo("Asia/Seoul")
    ).strftime(
        "%Y-%m-%d %H:%M:%S"
    )
