# React + TypeScript + Vite

This is the frontend side of the project to display a chatbot that interacts with the backend. The frontend and backend uses REST to communicate.

In this case, no external libraries are used to handle communication between the frontend and the backend.

Choose your favorite deployment platform that supports Bun and Vite to deploy this frontend project.

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

## Installation

Clone the repository or deploy it to your favorite deployment platform that supports Bun and Vite.


### Environment variables

For this project, the only environment variable needed to successfully run the chatbot is the backend URL. 
Declaring using the `VITE_BACKEND_URL` environment variable name. See more in the [.env.example](.env.example) file.


## Usage

An example deployment of this project can be found at [this link](https://the-batch-rag.onrender.com/).

## Routes

There is only route available, which is the root (`/`).

### How to interact

Write a question regarding [The Batch](https://www.deeplearning.ai/the-batch/) news. The question will be sent to the backend and a Markdown answer will be generated. Said answer will be displayed back in the frontend. 

### Handling images

Because the backend returns Markdown text, that means that the original URLs to the images displayed in the backend are sent back and rendered in the frontend. This means that the images are not stored locally, but rather depend on the external server that is storing them.