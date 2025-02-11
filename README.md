# Twitter Webhook Implementation

This repository contains a basic implementation of a Twitter webhook using Flask and Tweepy.  
The webhook listens for mentions and processes tweet creation events.

## Prerequisites

- Docker & Docker Compose installed
- Python 3.11.8 (if running outside Docker)
- A Twitter Enterprise Account with API keys and tokens
- An API Gateway as a service like `ngrok` or publicly accessible URL to register the webhook

## Setup Instructions

### 1. Clone the Repository

```sh
git clone <repository-url>
cd <repository-folder>
```

### 2. Create a `.env` File

You need to create a `.env` file inside the `app` directory with the following content:

```ini
API_KEY=your_api_key
API_KEY_SECRET=your_api_key_secret
ACCESS_TOKEN=your_access_token
ACCESS_TOKEN_SECRET=your_access_token_secret
WEBHOOK_ENV=development
WEBHOOK_URL=https://your-ngrok-url/webhook/twitter
```

> **Note:** The `.env` file is included in `.gitignore`, so your credentials will not be committed.

### 3. Build and Run the Project with Docker

Run the following command to start the application using Docker Compose:

```sh
docker-compose up --build
```

This will:
- Build the Docker image
- Start the Flask app in a container
- Expose the application on port **4500** (mapped to container port **80**)

Once running, the service will be available at:

```
http://localhost:4500
```

### 4. Register the Webhook with Twitter

Make a `POST` request to register the webhook with your Twitter developer account:

```sh
curl -X POST http://localhost:4500/webhook/register
```

If successful, you will see a response:

```json
{"message": "Webhook registered successfully!"}
```

## API Endpoints

### `POST /webhook/twitter`
Receives Twitter events when your account is mentioned in a tweet.

### `POST /webhook/register`
Registers the webhook URL with Twitter's Account Activity API.

### `GET /status`
Returns a simple JSON response to check if the service is running.

```json
{"message": "Service is running"}
```

## Stopping the Service

To stop the running containers, use:

```sh
docker-compose down
```

## License
This project is licensed under the MIT License.

