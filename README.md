# Twitter Influencer Analyzer using twitterscore.io

## About
This Python script is designed to analyze Twitter accounts for influencer metrics using the twitterscore.io platform. It demonstrates web scraping techniques to extract influencer-related information about Twitter accounts, providing insights into their social media impact and reach.

## Features
- Analyzes Twitter accounts using twitterscore.io
- Extracts key influencer metrics including influencer count, total followers, and engagement rate
- Identifies and lists top influencers associated with the account
- Provides a structured output of the influencer analysis

## Technologies Used
- Python 3
- Requests library for making HTTP requests
- BeautifulSoup4 for web scraping and HTML parsing

## How It Works
1. The script takes a Twitter handle as input.
2. It sends a request to twitterscore.io with the Twitter handle.
3. The HTML response is parsed to extract relevant influencer information.
4. The script compiles the extracted data into a structured format.
5. Results are presented in an easily readable format for further analysis.

## Prerequisites
- Python 3.7+
- Internet connection to access twitterscore.io

## Installation and Usage
1. Clone this repository
2. Install required libraries:
   pip install requests beautifulsoup4
3. Run the script:
   python twitter_influencer_analyzer.py
4. When prompted, enter the Twitter handle you wish to analyze (without the @ symbol)

## Sample Output
Analysis Result:
Twitter Handle: example_account
Influencer Count: 5,000
Total Followers: 1,000,000
Engagement Rate: 2.5%
Top Influencers:
  - @influencer1
  - @influencer2
  - @influencer3
  - @influencer4
  - @influencer5

## Limitations
- This script relies on the structure of twitterscore.io remaining consistent. Changes to their website may require updates to the scraping logic.
- The accuracy of the analysis depends on the data provided by twitterscore.io.
- Web scraping may be against the terms of service of some websites. Always ensure you have permission to scrape data.

## Future Enhancements
- Implement error handling for network issues or changes in website structure
- Add support for batch analysis of multiple Twitter accounts
- Integrate with Twitter API for more comprehensive data analysis
- Develop a user interface for easier interaction and data visualization
- Implement data export features (e.g., CSV, JSON)

## Ethical Considerations
This tool is designed for educational and research purposes. Users should respect the terms of service of twitterscore.io and use the data responsibly. Be mindful of privacy concerns when analyzing public figures or individuals.

## Contribution
Contributions to this project are welcome! Feel free to fork the repository and submit pull requests with improvements or additional features.

## License
This project is open source and available under the [MIT License](LICENSE).

---

Created by Josh Plotkin
