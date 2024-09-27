# img2text
building an image to text system

# Image to Text Application

This is a Streamlit web application that takes an image and a text prompt as input, and uses Google's Generative AI model (`gemini-1.5-flash`) to generate content based on the input. The app can either take just the image or combine both the image and the text prompt to produce a response.

## Features

- Upload an image (jpg, jpeg, png formats)
- Option to provide a text prompt
- Generate content using Google's Generative AI (`gemini-1.5-flash`)
- Display the uploaded image and the generated response on the page

## Requirements

To run the app, you need to have the following installed:

- Python 3.x
- Streamlit
- Pillow (Python Imaging Library)
- `python-dotenv` for managing environment variables
- `google-generativeai` library for the Generative AI model

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/image-to-text-app.git
    cd image-to-text-app
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    - Create a `.env` file in the root directory.
    - Add your Google API key to the `.env` file:
    ```env
    GOOGLE-API-KEY=your-google-api-key-here
    ```

5. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

## Usage

1. Launch the app and upload an image file (jpg, jpeg, or png).
2. Optionally, provide a text prompt to give additional context.
3. Click the **Submit** button to generate content based on the image and the prompt.
4. The AI-generated response will be displayed on the page.

## Dependencies

- **Streamlit**: For creating the web interface
- **Pillow (PIL)**: For handling image upload and display
- **python-dotenv**: For managing environment variables like the Google API key
- **google-generativeai**: For accessing Google's Generative AI model

## API Configuration

Ensure that your Google API key has the correct permissions to access the generative model. You will need to configure the environment with the API key using a `.env` file as described above.

## License

This project is licensed under the MIT License. Feel free to modify and use the code as per your needs.

