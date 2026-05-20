# Section 2: Generative AI Fundamentals and BedRock

## Amazon Bedrock Overview
__Foundation Models__  
* The giant, pre-trained transformer models we are fine tuning for specific tasks, or applying to new applications
* GPT-n (OpenAI)
* Claude (Anthropic)
* DALL-E (OpenAI, Microsoft)
* LLaMa (Meta)
* DeepSeek
* Nova

__AWS Foundation Models (Base Models)__   
* Jurassic-2 (AI21labs)
  - Multilingual LLMs for text generation
  - Spanish, French, German, Portuguese, Italian, Dutch
* Claude (Anthropic)
  - LLM’s for conversations
  - Question answering
  - Workflow automation
* Stable Diffusion (stability.ai)
  - Image, art, logo, design generation
* Llama (Meta)
  - LLM
* Amazon Titan
  - Text summarization
  - Text generation
  - Q&A
  - Embeddings
    * Personalization
    * Search
* Amazon Nova Pro (LLM portfolio of models)
* Amazon Nova Reels
  - Video

__Amazon Bedrock__   
* An API for generative AI Foundation Models
  - Invoke chat, text, or image models
  - Pre-built, your own fine-tuned models, or your own models
  - Third-party models bill you through AWS via their own pricing
  - Support for RAG (Retrieval-Augmented Generation… we’ll get there)
  - Support for LLM agents
* Serverless
* Can integrate with SageMaker

__The Bedrock API Endpoints__  
* __bedrock__: Manage, deploy, train models
* __bedrock-runtime__: Perform inference (execute prompts, generate embeddings) against these models
  - Converse, ConverseStream, InvokeModel, InvokeModelWithResponseStream
* __bedrock-agent__: Manage, deploy, train LLM agents and knowledge bases
* __bedrock-agent-runtime__: Perform inference
against agents and knowledge bases
  - InvokeAgent, Retrieve, RetrieveAndGenerate


__Bedrock IAM permissions__  
* Must use with an IAM user (not root)
* User must have relevant Bedrock permissions
  - `AmazonBedrockFullAccess`
  - `AmazonBedrockReadOnly`

__Amazon Bedrock: Model Access__  
* Amazon is phasing out the need to request access to specific models
* Be sure to check pricing
  - https://aws.amazon.com/bedrock/pricing
