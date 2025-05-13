# The Batch Rag

This project is a Retrieval-Augmented Generation (RAG) system that retrieves and generates information from The Batch, a website that provides weekly news about AI. The system uses a combination of text and image data to provide relevant answers to user queries.

## Overview

The Batch is a weekly newsletter by Andrew Ng that covers the latest developments in AI and machine learning. It is a great resource for anyone interested in staying up-to-date with the latest trends and advancements in the field. This project is a simple web application that allows users to search for specific topics in the newsletter and get relevant information. The application uses a combination of web scraping, natural language processing, and machine learning to provide accurate and relevant results.

## Approach

Andrew's Letters, Data Points, ML Research, Business, Science, Culture, Hardware, and AI Careers categories are just rewrites of the Weekly Issues. Therefore, one can only scrape the Weekly Issues and not the other categories.
In this case, to quickly get the data, we will use a scrapper to scrape the data from The Batch. The scrapper will extract the relevant information from the website and store it in a structured format (e.g., JSON or Markdown). The data should be stored somewhere to then be tokenized and embed into a query solution.

### Selecting a Storage Solution

There are several factors when deciding which storage solution to use. For this project, using an SQL database was quickly discarded because

- SQL databases are great for structured data and complex queries. However, they are not well-suited for unstructured data, such as text and images. Additionally, SQL databases can be slow when it comes to searching for similar items in large datasets.
- SQL databases are not designed to handle high-dimensional data, such as embeddings, which are commonly used in machine learning applications. This makes them less suitable for applications that require fast and efficient similarity search and retrieval.

Because of the nature of the extracted Markdown data, it was decided to use a NoSQL database. That said, there are many options on the market, and it was important to consider the pros and cons of each option.

- **DynamoDB**: DynamoDB is a fully managed NoSQL database service provided by AWS. It is designed to handle large amounts of unstructured data and can scale automatically to accommodate high traffic. However, it may not provide the same level of query capabilities as SQL databases. Additionally, while it can store unstructured data, it may not be optimized for similarity search and retrieval.
- **MongoDB**: MongoDB is a popular NoSQL database that is designed to handle unstructured data. It provides flexible schema design and can scale horizontally to accommodate large datasets. However, it may not be as efficient as vector databases when it comes to similarity search and retrieval.

- **OpenSearch**: OpenSearch is an open-source search and analytics engine that is designed to handle large amounts of unstructured data. It provides powerful search capabilities and can be used for similarity search and retrieval.

- **Vector Database as a Service**: There are various services like Pinecone, Weaviate, and Qdrant that provide vector database solutions. These services are designed to handle high-dimensional data and provide efficient similarity search and retrieval capabilities. They can be easily integrated with machine learning applications and provide fast response times. That said, their cost is nothing to underestimate, and they may not be the best option for a small project like this one.

- **OpenSearch Serverless**: OpenSearch Serverless is a fully managed, serverless version of OpenSearch that allows you to run OpenSearch without managing the underlying infrastructure. It provides the same powerful search capabilities as OpenSearch and can be used for similarity search and retrieval. It is also cost-effective, as you only pay for the resources you use.

Ultimately, the decision to use OpenSearch Serverless was made because it provides a powerful search engine that can handle large amounts of unstructured data. It is also cost-effective, as you only pay for the resources you use. Additionally, it provides the same powerful search capabilities as OpenSearch and can be used for similarity search and retrieval. This makes it an ideal choice for this project, as it allows for efficient storage and retrieval of the scraped data.

### Data Ingestion and Preprocessing

To ingest and process all the data from the website, a scrapper was created to scrape the data and extract relevant information to store it in a structured format. Because of the nature of the data, all the articles were saved in Markdown format. The data is then stored in an S3 bucket for further processing.

#### Tokenization and Embedding

Embedding is the process of converting text data into a numerical representation that can be easily processed by vector databases by searching similar results in a multimiensional dimension.
The embedding process involves converting the text data into a numerical representation that can be easily processed by machine learning algorithms. This is done by using a pre-trained model that has been trained on a large dataset of text data. The resulting embeddings are then stored in the vector database for later retrieval.
Once the data is stored in the S3 bucket, it is then tokenized and embedded into a vector database. This allows for efficient retrieval of relevant information based on user queries. The embedding model used for this project is the `Titan Text Embedings V2` model, which is designed to handle high-dimensional data and provide efficient similarity search and retrieval capabilities.

## Challenges

### Finding cost-effective solutions

As this project is purposed to be designed on a small scale, products that offered free or low cost solutions were prioritized, although compromising some performance.

- Render was used to host the frontend and backend applications, as it provides a free tier for small projects. However, it may not be as performant as other hosting solutions, and the backend service shuts down after 15 minutes of inactivity. This can lead to longer response times for users who access the application after a period of inactivity.
- AWS Bedrock was used to create the knowledge base and vector database. While it provides a powerful solution for storing and retrieving data, it locks the project behind AWS. However, it is a good option for projects that require high performance and scalability.
- OpenSearch Serverless was used to create the vector database. While it provides a powerful solution for storing and retrieving data, it may not be as performant as other vector databases. Moreover, it is not part of the free tier, and the cost can add up quickly if the project is not managed properly. That said, the AWS environment allows for easy integration with other AWS services, such as S3 and Bedrock, which is beneficial for the project development speed.

Other services that were considered but discarded:

- **Vercel**: Vercel is a popular hosting platform for frontend applications. It provides a free tier for small projects, but it is not designed to handle backend applications.
- **Railway**: Railway is an excellent hosting platform for backend applications. However, for our use case, the free tier was not sufficient to handle vector databases and embeddings.
- **Supabase**: Supabase is a popular open-source alternative to Firebase. It provides a free tier for small projects, but it does not offer any vector database solution.
- **Pinecone**: Pinecone is a vector database that provides a free tier for small projects. However, their integration with AWS is not as seamless as OpenSearch Serverless and Bedrock Flow.

### Image processing inside the articles

The images inside the articles are not downloaded as separate entities, but rather, were referenced from their original URL inside the Markdown file. This is done to save space and avoid redundancy, while still providing access to the images when needed. Querying them becomes possible as well as they are tied to the news text that come with them.

## Conclusions

The Batch RAG project is a simple web application that allows users to search for specific topics in the newsletter and get relevant information. The application uses a combination of web scraping, natural language processing, and machine learning to provide accurate and relevant results. The project is designed to be cost-effective and easy to use, making it a great option for anyone interested in staying up-to-date with the latest trends and advancements in the field of AI.
The project is still in its early stages, and there are many opportunities for improvement. The current implementation provides a solid foundation for building a more advanced RAG system that can handle larger datasets and provide more accurate results. The use of OpenSearch Serverless and AWS Bedrock allows for easy integration with other AWS services, making it a great option for future development.

## Future Work

Because new articles are published weekly, the system should be able to update itself with new articles. This can be done by scheduling the scrapper to run weekly and update the vector database with new articles. Additionally, the system can be improved by adding more features, such as sentiment analysis, topic modeling, and user feedback.

One critical feature missing is to continue the conversation with subsequent questions from the user, keeping the previous context in mind. This can be done by using a session-based approach, where the system keeps track of the user's previous queries and responses. This allows for a more natural conversation flow and provides users with more relevant information based on their previous interactions.

Other features that can be added to the system include:

- **Sentiment Analysis**: This can be done by using pre-trained models that can analyze the sentiment of the text data and provide insights into the overall sentiment of the articles.
- **Topic Modeling**: This can be done by using pre-trained models that can analyze the text data and provide insights into the topics covered in the articles.
- **User Feedback**: This can be done by allowing users to provide feedback on the results returned by the system. This feedback can be used to improve the system's performance and provide more accurate results.
