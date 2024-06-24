import google_play_scraper
from google_play_scraper.constants.regex import Regex
from google_play_scraper.constants.request import Formats
from google_play_scraper.utils.request import post

def _fetch_review_items(
    url: str,
    app_id: str,
    sort: int,
    count: int,
    filter_score_with: Optional[int],
    pagination_token: Optional[str],
):
    dom = post(
        url,
        Formats.Reviews.build_body(
            app_id,
            sort,
            count,
            "null" if filter_score_with is None else filter_score_with,
            pagination_token,
        ),
        {"content-type": "application/x-www-form-urlencoded"},
    )

    # MOD error handling
    if "error.PlayDataError" in dom:
        return _fetch_review_items(url, app_id, sort, count, filter_score_with, pagination_token)
    # ENDMOD

    match = json.loads(Regex.REVIEWS.findall(dom)[0])

    return json.loads(match[0][2])[0], json.loads(match[0][2])[-1][-1]


