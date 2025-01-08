# importing and installing 
import pandas as pd



import openai
import pandas as pd
import time


# loading dataset



# Directory path where the thread files are stored
path = "../newdataset/updated_data.csv"
data = pd.read_csv(path)

# Check the dataset
print(f"Dataset loaded successfully with {len(data)} rows.")
print(data.head())


# Select the first 2000 rows but keep all columns
sample_data = data.head(2000)

# Check the sample
sample_data[['cleaned_text','cleaned_body']].head(5)




# Set up OpenAI API key
openai.api_key = "my_key"


# Function to get GPT label for a single post and comment
def get_gpt_label(post, comment):
    try:
        # Prepare the prompt
        prompt = f"""
        Analyze the semantic relationship between the following post and comment.
        Post: {post}
        Comment: {comment}
        
        Does the comment:
        +1: Agree with the post,
        -1: Disagree with the post,
         0: Neutral (neither agree nor disagree)?
        
        Respond with one number only: +1, -1, or 0.
        """
        
        # Call OpenAI GPT API
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        
        # Extract the response content
        label = response['choices'][0]['message']['content'].strip()
        return int(label)  # Convert to integer

    except Exception as e:
        print(f"Error: {e}")
        return None  # Return None if there's an error

# Process the dataset (use a sample for testing, e.g., first 2000 rows)
sample_data = data.head(2000).copy()

# Add a new column for GPT labels
sample_data['label'] = None

# Iterate through each post and comment pair
for i, row in sample_data.iterrows():
    post = row['cleaned_text']
    comment = row['cleaned_body']
    
    # Get GPT label
    label = get_gpt_label(post, comment)
    sample_data.at[i, 'label'] = label
    
    # Optional: Print progress
    if i % 10 == 0:
        print(f"Processed {i} rows...")

    # Avoid hitting API rate limits (adjust delay as needed)
    time.sleep(1.5)

# Save the labeled dataset
output_path = "labeled_sample_data.csv"
sample_data.to_csv(output_path, index=False)
print(f"Labeled dataset saved to {output_path}")

