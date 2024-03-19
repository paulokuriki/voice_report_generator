# RAD-GPT
RAD-GPT is a cutting-edge application tailored specifically for radiologists, designed to revolutionize the way brain MRI reports are created. 

By leveraging the advanced capabilities of speech recognition, natural language processing, and the latest in AI technology through OpenAI's GPT models, RAD-GPT aims to streamline the reporting process, making it faster, more accurate, and highly efficient. 

This README guide provides detailed information on setting up and utilizing RAD-GPT to enhance your radiological reporting.

## Features
- Speech Recognition: Captures radiologists' verbal descriptions of positive findings from MRI scans, converting spoken words into text with high accuracy.
- AI-Powered Reporting: Utilizes OpenAI's GPT models to analyze the text input and generate comprehensive brain MRI reports, focusing on delivering precise and clinically relevant opinions.
- Text-to-Speech Conversion: Converts the AI-generated reports back into audio, enabling radiologists to review the findings and the report's conclusion audibly, ensuring accuracy and comprehensibility.
- Custom Template Integration: Incorporates a customizable template system (TEMPLATE_PT) to ensure that the generated reports adhere to standard radiological reporting formats and include all necessary information fields.

## Setup
### Prerequisites
- Python 3.6 or later.
- Installation of the following Python packages: pyttsx3, speech_recognition, pydub, pyperclip, playsound, and warnings. Also, ensure you have ffmpeg installed on your system for pydub to process audio files.
- An OpenAI API key for accessing GPT models.

### Installation
Clone the Repository
Copy code

`git clone https://github.com/paulokuriki/voice_report_generator.git`

`pip install -r requirements.txt`

Configure OpenAI API Key
Set your OpenAI API key as an environment variable:

`export OPENAI_API_KEY='your_api_key_here'`

## Usage
To use RAD-GPT, run the main Python script:

`python main.py`

Begin by speaking into your microphone, describing the positive findings from a brain MRI scan.

RAD-GPT will process your speech, generate a detailed report based on your input, and finally read back the report aloud.

The generated report is also copied to the clipboard for easy pasting into medical record systems.


## Customization

You can customize the report template by editing `template.py`. This allows you to adjust the structure of the generated reports to meet specific requirements or preferences.

## Contact
For further inquiries or contributions to RAD-GPT, please feel free to reach out:

Paulo Kuriki on LinkedIn

## License
This project is licensed under the MIT License - see the LICENSE file for details.
