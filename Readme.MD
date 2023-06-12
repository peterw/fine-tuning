# Twitter Comment Reply App

This application is a demo of an AI model fine-tuned to generate reply for comments on a particular Twitter post in the style of @pwang_szn. 

## Description

This project uses Streamlit for the web interface, the OpenAI API, and an AI model trained to act like a Twitter influencer in the AI tech space. Given a comment on a post, it generates a reply.

The demo tweet for this application is: "Been doing 15 hr days for the past 3 weeks. Happy to just take a day off and enjoy Spring in NYC :)". You can provide a comment for this tweet, and the application will generate a suitable reply.

## Getting Started

### Prerequisites

You will need:

- Python 3.6 and above
- Streamlit
- OpenAI Python client

### Installation

1. Clone the repository

    git clone <repository-link>
2. Navigate into the project directory and install the required dependencies
    
        pip install -r requirements.txt
3. Run the application
    
            streamlit run main.py
You should now be able to view the app at `localhost:8501`.

### Usage

Enter a comment in the text input field labeled "Enter the Comment:". Click "Enter", and the application will generate a reply, which will be displayed in the "Response:" section.

## Environment Variables

The following environment variable is required for the application to run correctly:

- `OPENAI_API_KEY` - This should be set to your OpenAI API key.

## License

This project is licensed under the terms of the MIT license.

## Contact

If you encounter any issues or have any questions about the project, please file an issue on the project's GitHub page.
