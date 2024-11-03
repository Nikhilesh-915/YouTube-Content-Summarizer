YouTube Content Summarizer

A tool to fetch and summarize the latest videos from specific YouTube channels, helping users quickly capture essential information from video content without needing to watch the entire video. Ideal for users looking to save time and focus on key insights.

Problem Statement

Many users find it challenging to keep up with long YouTube videos and prefer short, readable summaries to get the main points. This application addresses that need by automatically retrieving and summarizing the latest videos from specific YouTube channels, making video content more accessible and efficient to consume.

Features

Automated Video Summarization: Retrieves transcripts of the latest videos and generates concise, easy-to-read summaries.
YouTube API Integration: Fetches video details like title, description, and transcript, enabling seamless summarization of new uploads.
Streamlit Interface: Provides an interactive and user-friendly web application where users can view summaries and watch videos.
Performance Optimization with Caching: Reduces redundant API calls for faster loading and less resource consumption.

Technology Stack

YouTube API: Fetches video data, including video titles, descriptions, and metadata.

YouTube Transcript API: Retrieves transcripts for videos, enabling text-based summarization.

Hugging Face Transformers: Utilizes a T5 model to generate concise, human-readable summaries of the transcripts.

Streamlit: Creates an interactive web interface for displaying video summaries to users.

Installation

Clone the repository
git clone (https://github.com/Nikhilesh-915/YouTube-Content-Summarizer.git)
Navigate to the project directory
cd youtube-content-summarizer
Install dependencies
pip install -r requirements.txt
Set up API keys
Add your YouTube API key to your environment variables. The application uses this to access YouTube data.

Usage

Go to cmd:
cd "YOUR_PROJECT_FOLDER_PATH"
streamlit run main.py

The application will display a list of the latest videos from predefined YouTube channels along with their summaries.
Click on a video link to watch the full content if you want more details.

Project Structure

main.py: The main script for running the Streamlit app and handling user interactions.
summarizer/: Contains the code for retrieving video transcripts and generating summaries.
utils/: Utility functions, including caching, API calls, and error handling.
requirements.txt: Lists the dependencies required for this project.

Future Enhancements

Custom Channel Selection: Allow users to input their preferred channels for personalized summaries.
Enhanced Summarization Models: Use larger or fine-tuned models to improve the quality of summaries.
Multi-Language Support: Summarize content in multiple languages, making it accessible to a wider audience.
Keyword-Based Summaries: Highlight key topics or keywords for a quick overview.



Acknowledgments

YouTube API and YouTube Transcript API for enabling video data and transcript retrieval.
Hugging Face Transformers for providing access to pre-trained summarization models.
Streamlit for enabling the quick creation of an interactive web interface.

With the YouTube Content Summarizer, stay up-to-date with your favorite channels while saving time on lengthy videos!

NOTE: YOU SHOULD CHANGE YOUTUBE ID INSIDE THE CODE ITSELF , I HAVE GIVEN FEW THAT I SEE REGULARLY. 
