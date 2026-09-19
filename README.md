# MASA PixelConvert Pro

Batch image format converter supporting PNG, JPEG, WEBP, BMP, and ICO pipelines

## Technical Architecture

The application is architected with modular separation of concerns adhering to modern clean code standards:

- **Component Layering**: Isolated view layouts, state managers, and service controllers.
- **Defensive Engineering**: Robust input sanitization and exception management.
- **Modern Design Standards**: High-contrast dark-mode interface styled for optimal usability and visual polish.

## Preview

![Application Interface](screenshots/app_interface.png)

## Features

- Multi-format translation preserving color channels and alpha transparency.
- Batch processing queue with progress telemetry and size estimation.
- Configurable quality and compression ratios for optimized storage.
- Drag-and-drop file ingestion and folder batch conversion.

## Prerequisites

- Python 3.10 or higher
- Required packages:

```bash
pip install customtkinter pillow requests
```

## Execution

Launch the application via Python:

```bash
python "Image Converter using Tkinter in Python/index.py"
```

## Project Structure

```
.
├── Image Converter using Tkinter in Python
├── screenshots/
│   └── app_interface.png
├── .gitignore
├── LICENSE             # MIT License
└── README.md           # Developer documentation
```

## License

This project is licensed under the terms of the MIT License. Refer to the `LICENSE` file for details.
