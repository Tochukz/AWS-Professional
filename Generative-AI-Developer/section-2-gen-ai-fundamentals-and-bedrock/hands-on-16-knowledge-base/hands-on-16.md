# Lesson 16: Hands-on with Knowledge Base

### Description

Here we create an underlying Vector Store for AWS Knowledge Base and query it from within the Knowlege Base feature.  

**How it works**  

### Operation

**Deployment**
Lint the templates

```bash
$ cfn-lint KnowledgeBase.yaml
```

To get the foundation model ARNs 
```bash
$ aws bedrock list-foundation-models --query "modelSummaries[].[modelArn]" --output text > embedded-models.md
```
Select one foundation model arn to use for your `EmbeddingModelArn` parameter.   

**After Deployment**  
Create the index on the OpenSearchServerless  vector store 
```bash


```

1. Upload data to the S3 bucket and path for the data source 
```bash

$ aws s3 cp s3://knowledge-base-storage-09-24/base-data
```

2. Sync the data source to the newly created knowledge base to index the content for searching. 
```bash 
$ aws bedrock-agent start-ingestion-job \
  --knowledge-base-id <KnowledgeBaseId> \
  --data-source-id <DataSourceId>
```

**Testing**
After deployment, use the RetrieveAndGenerate API to perform RAG queries:
```bash
$ aws bedrock-agent-runtime retrieve-and-generate \
  --knowledge-base-id <KnowledgeBaseId> \
  --model-arn "arn:aws:bedrock:eu-west-2::foundation-model/anthropic.claude-v2" \
  --retrieval-configuration '{"vectorSearchConfiguration": {"numberOfResults": 5}}' \
  --text "Your query here"
```
Note that the RetrieveAndGenerate API requires a generation model (separate from the embedding model) to synthesize answers from the retrieved content 

**Cleanup**


**Learn More**  
A knowlege Base can be created with either
1. __A Vector Store__:  for maximum flexibility. You get to select your embedding model  
2. __Structured Data Store__: e.g database and tables. It enables semantic search within existing system   
3. __Kendra GenAI Index__: (AWS Managed) Use for document understanding   

[Create a service role for Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-permissions.html)

**Useful Commands**
List Base Models ARN and IDS
```bash
$ aws bedrock list-foundation-models --query "modelSummaries[].[modelArn, modelId]" --output table --region eu-west-2 --no-cli-pager
```
