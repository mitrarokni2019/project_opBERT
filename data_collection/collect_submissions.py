import redditharbor.login as login
from redditharbor.dock.pipeline import collect
from redditharbor.utils import fetch
from datetime import datetime  # Add this import to fix the error
from redditharbor.utils import download

# Configure authentication
SUPABASE_URL = ""
SUPABASE_KEY = ""  # Use "service_role/secret" key, not "anon/public"
REDDIT_PUBLIC = ""
REDDIT_SECRET = ""  
REDDIT_USER_AGENT = "projectge"  # Format: <institution:project-name (u/reddit-username)>
# e.g. REDDIT_USER_AGENT = "LondonSchoolofEconomics:ICWSM-tutorial (u/reddit-username)" 

# Define database table names
DB_CONFIG = { 
    "user": "test_redditor",
    "submission": "test_submission",
    "comment": "test_comment"
}

# Login and create instances of Reddit and Supabase clients
reddit_client = login.reddit(public_key=REDDIT_PUBLIC, secret_key=REDDIT_SECRET, user_agent=REDDIT_USER_AGENT)
supabase_client = login.supabase(url=SUPABASE_URL, private_key=SUPABASE_KEY)

# Initialise an instance of the `collect` class
collect = collect(reddit_client=reddit_client, supabase_client=supabase_client, db_config=DB_CONFIG)

#Define the keywords list correctly
climate_change_keys = ["climate change", "global warming", "carbon emissions", "IPCC", "COP conference", "fossil fuels", "Paris Agreement", "climate action", "climate crisis", 
                       "climate science", "climate policy", "climate justice", "climate adaptation", "climate mitigation", "climate emergency", 
                       "climate report", "climate conference", "climate agreement", "climate solution", "climate target", "climate goal", "climate impact",
                       "climate effect", "climate research", "climate data", "climate technology",
                       "climate model", "climate finance", "climate investment", "climate risk", 
                       "climate resilience", "climate vulnerability", "climate awareness", "climate education", "climate communication", "climate advocacy",
                       "climate activism", "climate protest", "climate strike", "climate movement", "climate organization", "climate NGO", 
                       "climate campaign","climate cooperation", "climate governance", 
                       "climate accountability", "climate monitoring", "climate evaluation", "climate assessment", 
                       "climate reporting", "climate compliance", "climate regulation", "climate legislation","carbon emission"]


# Define the sort types for submissions
sort_types_forms = ["top","hot","new", "relevance"]

'''
# Define a function to filter submissions based on creation date (between 2022-2024)
def is_within_date_range(submission):
    created_at = submission.get('created_at')
    if created_at:
        year = created_at.year
        return 2022 <= year <= 2024
    return False
    
    
def is_within_date_range(submission_data):
    created_utc = submission_data.created_utc
    created_date = datetime.utcfromtimestamp(created_utc)
    return 2022 <= created_date.year <= 2024

# Iterate through each keyword and collect submissions
subreddits = ["changemyview"]
#sort_types = ["top"]

'''


subreddits = ["changemyview"]
for keyword in climate_change_keys:
    for sort in sort_types_forms:
        print(f"Collecting submissions for keyword: {keyword} and sort type: {sort}")
        query = keyword
        collect.submission_by_keyword(subreddits=subreddits, query=query, limit=100)  # mask_pii=True can be used if needed
        


'''


        # Fetch submission data
        fetch_submission = fetch.submission(supabase_client=supabase_client, db_name=DB_CONFIG["submission"])
        submission_ids = fetch_submission.id(limit=100)  # Fetch submission IDs from the last query
        
        for submission_id in submission_ids:
            # Use reddit_client to fetch the submission data from Reddit
            submission_data = reddit_client.submission(id=submission_id)
            
            if is_within_date_range(submission_data):
                print(f"Submission {submission_id} is within the date range (2022-2024).")
                # Process and store the submission if within date range
            else:
                print(f"Submission {submission_id} is NOT within the date range (2022-2024). Skipping.")



for keyword in climate_change_keys:
    for sort in sort_types_forms:
        print(f"Collecting submissions for keyword: {keyword} and sort type: {sort}")
        sort_types= sort
        query = keyword
        collect.submission_by_keyword(subreddits=subreddits, query=query,limit=100)  # mask_pii=True can be used if needed
        
        
        
        # Fetch the collected submissions and filter them based on the creation date
        fetch_submission = fetch.submission(supabase_client=supabase_client, db_name=DB_CONFIG["submission"])
        submission_ids = fetch_submission.id(limit=100)  # Fetch submission IDs from the last query
        
        for submission_id in submission_ids:
            submission_data = fetch_submission.by_id(submission_id=submission_id)
            if is_within_date_range(submission_data):
                # The submission is within the 2022-2024 range, so it can be processed or stored
                print(f"Submission {submission_id} is within the date range (2022-2024).")
                # You can continue processing or storing the submission
            else:
                print(f"Submission {submission_id} is NOT within the date range (2022-2024). Skipping.")
'''



#query = "COP"
# filter out null delta later
#collect.submission_by_keyword(subreddits, query, limit=100) #mask_pii=True)



# Downloading the test_submission table in to path: data/newDataset/test_submission.csv
download = download.submission(supabase_client, DB_CONFIG["submission"])
download.to_csv(columns="all", file_name="submission", file_path="data/newDataset")












