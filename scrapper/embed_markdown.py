import boto3
import botocore
import json
import argparse

# --- Configuration ---
# Model ID for Titan Text Embeddings G1
# You might need to update this if a newer version is preferred/available
DEFAULT_MODEL_ID = "amazon.titan-embed-text-v2:0"
# Default AWS region - change if needed or provide via command line
DEFAULT_REGION = "us-east-1"
# -------------------


def get_bedrock_client(region_name):
    """Creates a Boto3 client for the Bedrock Runtime service."""
    try:
        # It's generally recommended to explicitly create a session
        session = boto3.Session(
            region_name=region_name,
            profile_name="bedrock",
        )
        bedrock_client = session.client(
            service_name="bedrock-runtime", region_name=region_name
        )
        print(f"Successfully created Bedrock client in region: {region_name}")
        return bedrock_client
    except Exception as e:
        print(f"Error creating Bedrock client: {e}")
        return None


def get_embedding(bedrock_client, text_content, model_id=DEFAULT_MODEL_ID):
    """
    Generates an embedding for the given text using the specified Bedrock model.

    Args:
        bedrock_client: The Boto3 Bedrock Runtime client.
        text_content: The string content to embed.
        model_id: The ID of the embedding model to use.

    Returns:
        A list of floats representing the embedding, or None if an error occurred.
    """
    if not text_content:
        print("Error: Input text content is empty.")
        return None

    try:
        # Prepare the payload for the model invocation
        # Titan Text Embeddings models expect this format
        body = json.dumps({"inputText": text_content})

        # Invoke the model
        print(f"Invoking model: {model_id}...")
        response = bedrock_client.invoke_model(
            body=body,
            modelId=model_id,
            accept="application/json",
            contentType="application/json",
        )
        print("Model invocation successful.")

        # Parse the response
        response_body = json.loads(response.get("body").read())

        # Extract the embedding
        embedding = response_body.get("embedding")

        if embedding:
            print(f"Successfully generated embedding of dimension: {len(embedding)}")
            return embedding
        else:
            print("Error: Could not find 'embedding' in the model response.")
            print("Response received:", response_body)
            return None

    except botocore.exceptions.ClientError as error:
        print(f"An error occurred during Bedrock API call: {error}")
        # You might want to check error.response['Error']['Code'] for specifics
        # e.g., 'AccessDeniedException' if model access isn't enabled
        if "AccessDeniedException" in str(error):
            print(
                f"Hint: Ensure you have enabled access to model '{model_id}' in the Bedrock console for region '{bedrock_client.meta.region_name}'."
            )
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def read_markdown_file(file_path):
    """Reads the content of a markdown file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        print(f"Successfully read content from: {file_path}")
        return content
    except FileNotFoundError:
        print(f"Error: Markdown file not found at {file_path}")
        return None
    except Exception as e:
        print(f"Error reading markdown file: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Generate embeddings for a Markdown file using Amazon Bedrock."
    )
    parser.add_argument("markdown_file", help="Path to the input Markdown file.")
    parser.add_argument(
        "--region",
        default=DEFAULT_REGION,
        help=f"AWS region for Bedrock (default: {DEFAULT_REGION}).",
    )
    parser.add_argument(
        "--model-id",
        default=DEFAULT_MODEL_ID,
        help=f"Bedrock Titan embedding model ID (default: {DEFAULT_MODEL_ID}).",
    )
    parser.add_argument(
        "--output-file", help="Optional path to save the embedding JSON."
    )

    args = parser.parse_args()

    # 1. Read the Markdown file
    markdown_content = read_markdown_file(args.markdown_file)
    if markdown_content is None:
        return  # Exit if file reading failed

    # 2. Get Bedrock client
    bedrock_runtime = get_bedrock_client(args.region)
    if bedrock_runtime is None:
        return  # Exit if client creation failed

    # 3. Generate embedding
    embedding_vector = get_embedding(bedrock_runtime, markdown_content, args.model_id)

    # 4. Output/Save the result
    if embedding_vector:
        print("\nEmbedding Generation Complete.")
        # Print first few elements for confirmation
        print(f"Embedding Vector (first 5 elements): {embedding_vector[:5]}...")
        print(f"Embedding Dimension: {len(embedding_vector)}")

        if args.output_file:
            try:
                output_data = {
                    "inputFile": args.markdown_file,
                    "modelId": args.model_id,
                    "embedding": embedding_vector,
                }
                with open(args.output_file, "w", encoding="utf-8") as f:
                    json.dump(output_data, f, indent=4)
                print(f"Embedding saved to: {args.output_file}")
            except Exception as e:
                print(f"Error saving embedding to file: {e}")
    else:
        print("\nEmbedding Generation Failed.")


if __name__ == "__main__":
    main()
