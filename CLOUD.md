# Cloud Services Setup to Run the Project

This document provides instructions on how to set up the necessary cloud services to run the project. The project is designed to scrape data from The Batch, a website that provides weekly news about AI, and store the data in a vector database for further processing and analysis.

## Prerequisites

- An AWS account
- Knowledge of AWS services, including S3, Bedrock, IAM, and OpenSearch Serverless.
- Basic understanding of Python and web scraping.

## Steps

1. Ensure you have the AWS CLI installed and configured with your AWS credentials. You can do this by running the following command in your terminal:
   ```bash
   aws configure
   ```
   Follow the prompts to enter your AWS Access Key ID, Secret Access Key, region, and output format.
   Also, ensure that the account has SSO enabled and the required permissions to access the services you will be using.
2. Create an S3 bucket to store the scraped data. You can do this using the AWS Management Console or the AWS CLI. For example, to create a bucket named `the-batch-markdown`, run:

   ```bash
   aws s3api create-bucket --bucket the-batch-markdown --region us-east-1
   ```

3. Prepare the scrapper script to scrape the data from The Batch. The script should be able to extract relevant information from the website and store it in a structured format (e.g., JSON or Markdown). For this, follow the instructions in the [Scrapper README](/scrapper/README.md).
   Assume this project only works in US`us-east-1`.
4. Set up the Vector Database using AWS Bedrock. This will allow you to store and query the scraped data efficiently.

   - Go to the AWS Management Console and navigate to AWS OpenSearch Serverless' dashboard.
   - Create a new OpenSearch Serverless collection.
   - Choose the appropriate settings for your collection, such as the name, region, and instance type.
     - Select the collection type as "Vector search".
     - Since this is a demo, you can disable redundacy (active replicas) to save costs.
     - For security, you can implement your own solution or leave it as "Easy Create" for now.
     - Submit the form to create the collection.
   - Once the collection is created, go to the collection's Indexes tab. There, you can create a new vector Index. We will be using KNN (k-nearest neighbors) for the vector search.
     - Once you have created the index, return to the collection's overview page and take note of the ARN.

5. Set up Amazon Bedrock to use a knowledge base

   - Go to the AWS Management Console and navigate to Amazon Bedrock.
   - Go to Knowledge Bases and create a new knowledge base.
   - As the data source, select S3. Click next.
   - To configure the data source, select the S3 bucket you created earlier (`the-batch-markdown`) and specify the path to the data files (root by default).
   - Choose the chunking strategy for the data. You can select "Auto" for automatic chunking or specify a custom chunk size. The example deployed uses fixed-size chunking with a size of 1050 tokens with 20% overlap.
   - Configure the embeddings model to use for the knowledge base. For this example, we will use the `Titan Text Embedings V2` model.
   - When selecting the vector database, select the OpenSearch Serverless collection you created earlier. Do this by selecting `Choose a vector store yhou have created` and selecting `Vector engine for Amazon OpenSearch Serverless`.
   - After you have done so, paste the ARN of the OpenSearch Serverless collection you created earlier.
   - In the Index field mapping, add the vector field name you created earlier. For this example, we will `vector`.
   - Fill in the metadata field mapping as well. For this example, we will use `text` and `text-metadata` as the metadata fields for the Text Field Name and the Bedrock-managed Metadata Field Name.
   - Finally, review the configuration and create the knowledge base.
     When it has finished, you can select the Data Source in the knowledge base, click Sync, and test it with the `Test` button.

6. Create the Bedrock Flow

   - Go to the AWS Management Console and navigate to Amazon Bedrock.
   - Go to Flows and create a new flow.

     - When prompeted for service role names, yhou can either create a new role or use an existing one. If you choose to create a new role, make sure to attach the necessary permissions for the flow to access the knowledge base and vector database.

   - At this point, you will be presented with the Flow editor. You can add steps to the flow to process the data and generate responses. By default, you will have the Flow Input, the Prompt, and the Flow Output nodes. - In the Prompt node, click it and edit the prompt in the left column. Make sure you have at least two variables in text (declaring them by enclosing them in {{curly_braces}}).
     The prompt used for the deployed example is

     ```text
     Human: You are a reporter AI system. You provide provide answers to questions by using fact based information published in an online site called The Batch.

       Use the following pieces of information to provide a concise answer to the question enclosed in <question> tags.
       Always include jpg links related to the user question.
       If you don't know the answer, just say that you don't know, don't try to make up an answer.

     <question>
     {{question}}
     </question>

     The response should be specific and use statistics or numbers when possible.

     Context: {{context}}

     A:
     ```

   - Connect the Knowledge base to your flow. Connect the `Flow Input` node to the `Input` entry in the Knowledge Base, and the Output to the Prompt's Input Question.

     - This will allow the flow to retrieve data from the knowledge base based on the user's query and pass such information to the LLM.

   - Try out your configuration.

If you have made it this far, congratulations! You have successfully set up a Bedrock flow that uses a knowledge base to provide answers to user queries. You can now use this flow to build applications that leverage the power of AI and machine learning.
