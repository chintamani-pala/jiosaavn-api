# JioSaavn API Wrapper

This project provides an API wrapper for JioSaavn, enabling users to search for songs and retrieve song details including lyrics and media URLs. The application is built using Flask and provides a simple interface to interact with JioSaavn's API.

## Features

- **Search Songs**: Search for songs on JioSaavn by query.
- **Get Song Details**: Retrieve detailed information about a specific song, including media URLs, lyrics, and more.
- **URL Decryption**: Decrypts the encrypted media URLs provided by JioSaavn.
- **Lyrics Fetching**: Fetches lyrics for songs if available.
- **Preview URL Generation**: Generates preview URLs for songs.

## Project Structure

The project is divided into several key components:

- **api.py**: Contains base URLs for interacting with the JioSaavn API.
- **helper.py**: Provides helper functions for formatting song data and decrypting media URLs.
- **index.py**: Main Flask application that defines the API endpoints.
- **jiosaavn.py**: Handles communication with the JioSaavn API and processes responses.
- **requirements.txt**: Lists the dependencies required for the project.

## API Endpoints

### Home

- **URL**: `/`
- **Method**: GET
- **Description**: Returns a message indicating no endpoint is available.

### Search for Songs

- **URL**: `/song/`
- **Method**: GET
- **Parameters**:
  - `query` (required): The search query.
  - `page` (optional): The page number for pagination (default is 1).
  - `lyrics` (optional): Boolean to include lyrics in the response (default is False).
  - `songdata` (optional): Boolean to include detailed song data in the response (default is True).
- **Description**: Searches for songs on JioSaavn based on the query.

### Get Song Details

- **URL**: `/song/get/`
- **Method**: GET
- **Parameters**:
  - `id` (required): The ID of the song.
  - `lyrics` (optional): Boolean to include lyrics in the response (default is False).
- **Description**: Retrieves detailed information about a specific song by its ID.

## Installation

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```
## Running the Application

To run the Flask application, use:

```bash
python index.py
```

# Search for Songs
```bash
curl http://0.0.0.0:5100/song/?query=aradhya&page=1
```
# Get Song Details by ID
```bash
curl http://0.0.0.0:5100/song/get/?id=<song_id>&lyrics=true
```


# Code Overview
## api.py
- Defines the base URLs for interacting with the JioSaavn API.

## helper.py
- Contains helper functions such as format_song for formatting song data and decrypt_url for decrypting media URLs.

## index.py
- Main Flask application that defines API endpoints and handles incoming requests.

## points.py
- Handles the logic for searching songs and retrieving song details from the JioSaavn API. Utilizes helper functions for processing responses.

## requirements.txt
- Lists the Python packages required for the project.


# Credits
## Developed by Chintamani Pala.
