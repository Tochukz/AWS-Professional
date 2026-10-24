# Lesson 16: Hands-on with Knowledge Base

### Description

In this configuration, we deploy a Managed Knowlege Base with a S3 Data store

### Operation  
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

2. Upload data to the S3 bucket and path for the data source 
```bash
$ aws s3 cp book.tx s3://chucks-workspace-storage/data/book.txt 
```
This is the data ingestion step.  

3. Sync the data source to the newly created knowledge base to index the content for searching. 
```bash 
$ aws bedrock-agent start-ingestion-job --knowledge-base-id EA7NSEIG9K --data-source-id CODMJGLFS8
```

**Testing**
```bash
$ pip install --upgrade boto3
$ python3 agentic_retrieve.py <KnowledgeBaseId> "What are some steps to follow before deciding to become self-employed?"
``` 

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
List Base Models ARN and IDs
```bash
$ aws bedrock list-foundation-models --query "modelSummaries[].[modelArn, modelId]" --output table --region eu-west-2 --no-cli-pager
```
