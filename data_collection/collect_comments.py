import redditharbor.login as login
from redditharbor.dock.pipeline import collect
from redditharbor.utils import fetch
from redditharbor.utils import download


# Configure authentication
SUPABASE_URL = ""
SUPABASE_KEY = ""  # Use "service_role/secret" key, not "anon/public"
REDDIT_PUBLIC = ""
REDDIT_SECRET = ""  
REDDIT_USER_AGENT = "theproject"  # Format: <institution:project-name (u/reddit-username)>
# e.g. REDDIT_USER_AGENT = "LondonSchoolofEconomics:ICWSM-tutorial (u/reddit-username)" 


# Define database table names
DB_CONFIG = {
    "user": "test_redditor",
    "submission": "test_submission",
    "comment": "test_comment",
}

# Login and create instances of Reddit and Supabase clients
reddit_client = login.reddit(public_key=REDDIT_PUBLIC, secret_key=REDDIT_SECRET, user_agent=REDDIT_USER_AGENT)
supabase_client = login.supabase(url=SUPABASE_URL, private_key=SUPABASE_KEY)

# Initialise an instance of the `collect` class
collect = collect(reddit_client=reddit_client, supabase_client=supabase_client, db_config=DB_CONFIG)

#subreddits = ["changemyview"]
#sort_types = ["relevance"]
#query = "climate AND action "
# filter out null delta later
#collect.submission_by_keyword(subreddits, query, limit=100) #mask_pii=True)

fetch_submission = fetch.submission(supabase_client=supabase_client, db_name=DB_CONFIG["submission"])
submission_ids = fetch_submission.id(limit=None)  # Limiting to 100 submission IDs for demonstration. Set limit=None to fetch all submission IDs.

collect.comment_from_submission(submission_ids=submission_ids, level=10)  # Set level=None to collect entire comment threads


# Download the dataset test/comment table from Supabase in my path: data_collection/newDataset/test_comment.csv
download = download.comment(supabase_client, DB_CONFIG["comment"])
download.to_csv(columns="all", file_name="comment", file_path="data/newDataset")
