# Flask Boilerplate

A basic Flask application template with a clean structure and essential configurations.

## Project Structure

```
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── static/
│   └── templates/
├── run.py
├── requirements.txt
├── .render.yaml
└── README.md
```

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python run.py
```

The application will be available at `http://localhost:5000`

## Features

- Flask application factory pattern
- Blueprint-based routing
- Bootstrap 5 for styling
- Ready for deployment on Render
- Basic template structure

## Deployment

This project is configured for deployment on Render. The `.render.yaml` file contains the necessary configuration.

## License

MIT