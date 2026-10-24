"""Query a managed knowledge base with AgenticRetrieveStream and print the generated answer.

Usage: python3 agentic_retrieve.py <knowledge-base-id> ["<question>"]
"""
import sys

import boto3

KNOWLEDGE_BASE_ID = sys.argv[1]
question = sys.argv[2] if len(sys.argv) > 2 else "What are some steps to follow before deciding to become self-employed?"

# Uses the default CLI region/profile, same as the aws commands in hands-on-16a.md
client = boto3.client("bedrock-agent-runtime")

response = client.agentic_retrieve_stream(
    messages=[{"role": "user", "content": {"text": question}}],
    retrievers=[{"configuration": {"knowledgeBase": {"knowledgeBaseId": KNOWLEDGE_BASE_ID}}}],
    # MANAGED lets Bedrock pick the model; use CUSTOM + foundationModelConfiguration to pick your own
    agenticRetrieveConfiguration={"foundationModelType": "MANAGED"},
    generateResponse=True,
)

for event in response["stream"]:
    if "traceEvent" in event:
        attrs = event["traceEvent"].get("attributes", {})
        print(f"[trace] {attrs.get('step', '')} {attrs.get('status', '')} {attrs.get('message', '')}".rstrip())
    elif "result" in event:
        generated = event["result"].get("generatedResponse", {})
        print("\nAnswer:\n" + generated.get("answer", ""))
        for i, citation in enumerate(generated.get("citations", []), 1):
            print(f"\n[{i}] {citation}")
    else:
        print(event)
