# Lesson 16: Hands-on with Knowledge Base

### Description

Here we create an underlying Vector Store for AWS Knowledge Base and query it from within the Knowlege Base feature.  

**How it works**  

### Operation
**Before Deployment**  
To get the foundation model ARNs or Models IDs
```bash
$ aws bedrock list-foundation-models --query "modelSummaries[].[modelArn]" --output text > embedded-models.md
```
Select one foundation model ID to use for your `EmbeddingModelId` parameter.  A default is already provided in the template.  

**Deployment**  
Lint the templates

```bash
$ cfn-lint ManagedKnowledgeBase.yaml
```
Deploy the stack

```bash
$ aws cloudformation deploy --template-file ManagedKnowledgeBase.yaml  --stack-name ManagedKnowledgeBase --capabilities CAPABILITY_NAMED_IAM
```

**After Deployment**  
1. Get the stack outputs
```bash
$ aws cloudformation describe-stacks --stack-name ManagedKnowledgeBase --query "Stacks[0].Outputs" --no-cli-pager
```
Get the `KnowledgeBaseId` and the `DataSourceId` from the stack outputs

1. Create the index on the OpenSearchServerless vector store
```bash

```

2. Upload data to the S3 bucket and path for the data source
```bash
$ aws s3 cp book.tx s3://chucks-workspace-storage/data/book.txt
```
This is the data ingestion step.  

3. Sync the data source to the newly created knowledge base to index the content for searching.
```bash
$ aws bedrock-agent start-ingestion-job --knowledge-base-id 12GAJXHSAQ --data-source-id QZCVSAU9GS
```

**Testing**
After deployment, use the RetrieveAndGenerate API to perform RAG queries:
```bash
$ aws bedrock-agent-runtime retrieve-and-generate \
  --knowledge-base-id 12GAJXHSAQ \
  --model-arn "arn:aws:bedrock:eu-west-2::foundation-model/anthropic.claude-v2" \
  --retrieval-configuration file://retrival-config.json
  --text "Your query here"
```
Note that the RetrieveAndGenerate API requires a generation model (separate from the embedding model) to synthesize answers from the retrieved content.   
The the above comment the generation model is represented by the value of the `model-arn` parameter.  

**Testing in AWS Console**  
It may be more useful and convinient to test using the BedRock Console.  
1. Go to the BedRock console
2. Go to Knowledge Bases (KB) menu, select the newly created knowlege base
3. Click on the Test button
4. For _Retrieval and response generation_ select the _Agentic retrieval with answer generation_ option
5. A model must also be selectedd to the response generation
6. Enter a prompt in the preview text box: "What are some steps to follow before deciding to become self-employed?"
7. click the Run button
8. Explore the references in the output by clicking on the reference link to see the chucks they were generated from.
9. Also explore the _Source chunks_ and _Trace details_.   

**Cleanup**  
To delete the stacks

```bash
$ aws cloudformation delete-stack --stack-name ManagedKnowledgeBase
```

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
