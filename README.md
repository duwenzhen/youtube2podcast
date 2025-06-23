# AI-Powered YouTube-to-Podcast Converter

## Overview

This project is an advanced content transformation pipeline that automatically converts any YouTube video into a polished, two-person podcast. It leverages the power of Google's Gemini models for transcription, thematic analysis, scriptwriting, and audio generation.

The system is built on a client-server architecture using the **Model Context Protocol (MCP)**, which allows the AI model (acting as a client) to intelligently call and orchestrate a series of server-side tools. This showcases a sophisticated agent-based workflow where the AI model directs the entire conversion process.

This tool is designed for developers, content creators, and AI enthusiasts interested in agentic workflows, large language models, and automated content generation. As a quantitative developer, you'll appreciate the modular, scalable, and now professionally packaged architecture using Poetry.

## Features

* **YouTube Video Transcription:** Automatically fetches the full transcript of a given YouTube video.
* **Thematic Analysis:** Uses the Gemini Flash model to analyze the transcript and classify the video's content into one of several predefined themes (e.g., "Education & How-To," "News & Current Events").
* **Dynamic Podcast Scripting:** Generates a custom, two-person dialogue script (featuring "Jane" the expert and "Joe" the curious co-host) tailored to the video's identified theme.
* **Text-to-Speech (TTS) Generation:** Converts the final podcast script into a high-quality audio file (`.wav`) using Gemini's multi-speaker TTS capabilities.
* **Model Context Protocol (MCP) Architecture:** Built on a robust client-server model where the server exposes Gemini functionalities as tools. The AI client intelligently selects and executes these tools to drive the workflow.
* **Asynchronous Operations:** Utilizes `asyncio` for efficient, non-blocking execution of API calls.
* **Dependency Management:** Uses Poetry for robust and reproducible dependency management.
* **Configuration Management:** Securely manages API keys using environment variables.

## System Architecture

The project uses a client-server architecture based on the Model Context Protocol (MCP). This allows the main application to communicate with a set of AI tools in a standardized way.

1.  **MCP Server (`gemini_mcpserver.py`):**
    * This server acts as a gateway to the Gemini API.
    * It defines and exposes several functions as "tools" that can be called remotely. These tools include:
        * `instruction_to_gemini_flash_model`: For text generation and analysis.
        * `instruction_to_gemini_youtube_model`: For fetching video transcripts.
        * `instruction_to_gemini_TTS_model`: For generating audio.

2.  **MCP Client (`gemini_mcpclient.py`):**
    * The client communicates with the Gemini Pro model.
    * It informs the model about the available tools on the MCP server.
    * When given a high-level prompt, the AI model decides which tool to call, with what arguments, to accomplish the task. The client then executes that function call.

3.  **Main Orchestrator (`main.py`):**
    * This script defines the high-level, multi-step logic for the YouTube-to-Podcast conversion.
    * It crafts a series of prompts that guide the AI client through the pipeline:
        1.  Get the transcript.
        2.  Classify the theme.
        3.  Generate the podcast script based on the theme.
        4.  Convert the script to speech.

This decoupling of logic (orchestrator) and capabilities (tools server) is a powerful pattern for building complex, agent-based AI systems.

## How It Works: The Step-by-Step Pipeline

1.  **Initialization:** The `main.py` script starts the process.
2.  **Step 1: Transcription:** It sends a prompt to the MCP client, instructing it to use the `youtube_model` tool to get the transcript of a specified YouTube URL.
3.  **Step 2: Thematic Analysis:** The transcript is then sent back to the client with a new prompt, instructing it to use the `flash_model` tool to classify the content into a theme.
4.  **Step 3: Script Generation:** The `main.py` script selects a pre-written "podcast instruction" template based on the identified theme. It formats this instruction with the transcript and sends it to the client, which again uses the `flash_model` tool to generate an engaging two-person dialogue.
5.  **Step 4: Audio Generation:** Finally, the generated podcast script is sent to the client with an instruction to use the `TTS_model` tool, which produces the final `out.wav` audio file.

## Getting Started

### Prerequisites

* Python 3.10+
* [Poetry](https://python-poetry.org/docs/#installation) for dependency management
* A Google Gemini API Key

### Installation

1.  **Clone the Repository:**
    ```
    git clone <your-repository-url>
    cd <your-repository-url>
    ```

2.  **Configure Environment Variables:**
    Create a file named `.env` in the root of your project directory and add your Gemini API key:
    ```
    GEMINI_API_KEY="your_api_key_here"
    ```

3.  **Install Dependencies:**
    Poetry will automatically create a virtual environment (as configured in `poetry.toml`) and install all the required packages from `pyproject.toml`.
    ```
    poetry install
    ```

## Usage

The entire pipeline is executed by running the `main.py` script using Poetry's `run` command. This ensures you are using the correct virtual environment.

```
poetry run python main.py
```

The script will perform all the steps, and upon completion, you will find an `out.wav` file in your project directory containing the generated podcast.

## Extensibility and Next Steps

This project provides a powerful foundation for more complex AI-driven workflows.

* **Add More Themes:** Expand the `THEMES` and `instructionByTheme` dictionaries in `main.py` to handle a wider variety of content styles.
* **Parameterize the URL:** Modify `main.py` to accept the YouTube URL as a command-line argument instead of being hardcoded.
* **Error Handling:** Implement more robust error handling for API calls and unexpected model outputs.
* **Web Interface:** Wrap the application in a web framework like Flask or FastAPI to create a user-friendly interface for converting videos.
