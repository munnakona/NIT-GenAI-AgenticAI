# Hello Gradio

A simple web application built with Gradio that demonstrates a basic greeting interface with adjustable intensity.

## Features

- Input a name and select intensity level
- Get a personalized greeting with exclamation marks based on intensity
- Clean and intuitive web interface
- REST API endpoint available for programmatic access

## Installation

1. Make sure you have Python installed (version 3.7 or higher)
2. Install the required dependencies:

```bash
pip install gradio
```

## Usage

1. Run the application:

```bash
python hello_gradio.py
```

2. Open your web browser and navigate to the local URL provided (usually `http://127.0.0.1:7860`)
3. Enter a name in the text field and adjust the intensity slider
4. Click submit to see your personalized greeting!

## API Usage

The application exposes a REST API endpoint that can be used programmatically:

- **Endpoint**: `/predict`
- **Method**: POST
- **Parameters**:
  - `name` (string): The name to greet
  - `intensity` (number): Intensity level (0-10)
- **Response**: JSON with the greeting message

Example API call:

```bash
curl -X POST "http://127.0.0.1:7860/predict" \
     -H "Content-Type: application/json" \
     -d '{"data": ["John", 5]}'
```

## Requirements

- Python 3.7+
- Gradio

## Contributing

Feel free to fork this repository and submit pull requests with improvements!

## License

This project is open source and available under the MIT License.
