# Voice Based Email Application for Visually Impaired Person

## Overview

The Voice Based Email Application for Visually Impaired Person is designed to provide an accessible email system for visually impaired individuals. By leveraging advanced speech recognition and text-to-speech technologies, the application enables users to send, read, and manage emails using voice commands, thus eliminating the need for traditional keyboard and visual interfaces.

## Features

- **Voice Commands**: Users can compose, read, and manage emails using simple voice commands.
- **Text-to-Speech**: Emails and system instructions are read aloud, aiding visually impaired users.
- **Speech-to-Text**: Converts spoken words into text for composing emails.
- **User Authentication**: Secure login using face recognition and voice input.
- **Interactive GUI**: A user-friendly graphical interface that supports voice-based feedback.

## System Architecture

The application comprises several key components:

- **User Selection Module**: Allows users to select options such as composing an email or checking the inbox.
- **Accessibility Options**: Provides both text-based and voice-based message handling.
- **Interactive GUI Framework**: An interactive graphical user interface with voice-based feedback to guide users through various operations.
- **Mouse Click Based Accessibility**: For users who may prefer to use a mouse for certain interactions.

## Data Flow

1. **Voice Input**: The user provides input through voice commands.
2. **Speech Recognition**: The system uses Google Speech API to convert voice to text.
3. **Processing**: The system processes the text input to determine the appropriate action.
4. **Voice Output**: The system generates a voice response to guide the user through the next steps.

## System Requirements

### Hardware

- **Processor**: Intel i5
- **Memory**: 8 GB RAM
- **Storage**: 120 GB Hard Disk
- **Monitor**: 15’’ LED
- **Input Devices**: Keyboard and Mouse

### Software

- **Operating System**: Windows 7 and above
- **Programming Language**: Python 3.6
- **Tools**: Anaconda (for package management and environment setup)

## Functional Requirements

- **Desktop Application**: Developed using Tkinter for the graphical user interface.
- **User Registration and Login**: Using voice input and secure face recognition.
- **Voice Command Recognition**: System accurately recognizes and processes voice commands.
- **Voice Interaction**: Generates voice responses to interact with the user.

## Non-Functional Requirements

- **Self-Contained Program**: The application can be easily moved between different computers.
- **High Availability**: The system should achieve 100% availability.
- **Scalability**: Supports additional users and scales as needed.
- **Maintainability**: Optimized for ease of maintenance with proper documentation and coding standards.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-repo/voice-email-app.git
    cd voice-email-app
    ```

2. **Create a Virtual Environment**:
    ```bash
    conda create --name vemail python=3.6
    conda activate vemail
    ```

3. **Install Dependencies**:
    ```bash
    conda install --file requirements.txt
    ```

4. **Run the Application**:
    ```bash
    python main.py
    ```

## Usage

### Registration
Users must first register by providing voice commands and a face scan for authentication. The system will guide the user through the registration process using voice prompts.

### Login
Once registered, users can log in using their voice and face recognition. The system will confirm the user's identity before granting access to the email functionalities.

### Compose Mail
Users can compose emails by dictating the content through voice commands. The speech-to-text technology will convert the spoken words into text, which will be used to create the email.

### Read Inbox
Users can listen to their emails being read aloud by the system. The application will read out the sender, subject, and body of the email, and users can navigate through their inbox using voice commands.

## Project Structure

- `main.py`: The main entry point of the application.
- `requirements.txt`: Lists all the dependencies required to run the application.
- `README.md`: This file, providing an overview and usage instructions.
- `docs/`: Documentation and additional resources.
- `src/`: Source code for the application, including modules for GUI, voice processing, and email handling.
- `tests/`: Unit tests and integration tests for the application.

## Contributors

- **Chandan S** (1GA18CS044)
- **Dhamini BV** (1GA18CS051)
- **Dhanush R** (1GA18CS052)

## Acknowledgments

We would like to express our gratitude to the following individuals and institutions for their support and guidance throughout this project:

- **Mr. Rudramurthy V.C**, Assistant Professor, Department of CSE, GAT, Bengaluru
- **Dr. Bhagyashri R Hanji**, Professor & HOD, Department of CSE, GAT, Bengaluru
- **Dr. Rana Pratap Reddy**, Principal, GAT, Bengaluru
- All staff members of the Department of Computer Science and Engineering, GAT, Bengaluru
- Our parents, friends, and everyone who directly or indirectly contributed to the success of this project

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
"""
