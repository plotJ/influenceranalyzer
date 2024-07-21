import requests
from bs4 import BeautifulSoup
import time

def analyze_twitter_influencers(twitter_handle):
    # Base URL for the twitterscore.io site
    base_url = "https://twitterscore.io"
    
    # Construct the URL for the Twitter handle analysis
    analysis_url = f"{base_url}/twitter/{twitter_handle}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # Send a GET request to the URL
        response = requests.get(analysis_url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract relevant information
        # Note: These selectors are hypothetical and would need to be adjusted based on the actual structure of the website
        influencer_count = soup.select_one('.influencer-count').text
        total_followers = soup.select_one('.total-followers').text
        engagement_rate = soup.select_one('.engagement-rate').text
        
        # You might also want to extract a list of top influencers
        top_influencers = [influencer.text for influencer in soup.select('.top-influencer')]
        
        # Compile the results
        analysis_result = {
            "twitter_handle": twitter_handle,
            "influencer_count": influencer_count,
            "total_followers": total_followers,
            "engagement_rate": engagement_rate,
            "top_influencers": top_influencers[:5]  # Limit to top 5 for brevity
        }
        
        return analysis_result
    
    except requests.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
        return None

def main():
    twitter_handle = input("Enter the Twitter handle to analyze (without @): ")
    result = analyze_twitter_influencers(twitter_handle)
    
    if result:
        print("\nAnalysis Result:")
        for key, value in result.items():
            if key == "top_influencers":
                print(f"{key.replace('_', ' ').title()}:")
                for influencer in value:
                    print(f"  - {influencer}")
            else:
                print(f"{key.replace('_', ' ').title()}: {value}")
    else:
        print("Failed to analyze Twitter influencers.")

if __name__ == "__main__":
    main()