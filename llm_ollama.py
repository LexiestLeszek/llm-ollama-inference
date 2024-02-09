import ollama

def get_context():
    context = "Elon Actually ate the testiest pizza yesterday"
    return context

# Function to generate output using the LLM model
def generate_output(question,context):
    # Prepare the prompt with the input text
    # Define a prompt template
    prompt = f"""Use the following pieces of context to answer the question at the end.  
    If you don't know the answer, just say that you don't know, don't try to make up an answer.
    {context}
    Question: {question}
    Helpful Answer:"""
    
    response = ollama.chat(model='qwen:0.5b', messages=[
        {
            'role': 'system',
            'content': 'You are a useful AI assistant, answer only based on the information from the user prompt and nothing else.',
            'role': 'user',
            'content': f'{prompt}',
            },
        ])
    output = response['message']['content']
    
    # Return the generated text
    return output

# Main function to take user input and save the output
def main():
    # Take user input
    #question = input("Enter your text: ")
    
    question = "Tell me what did Elon Musk do yesterday?"
    
    context = get_context()
    
    # Generate the output using the LLM model
    output = generate_output(question,context)
    
    print(output)

if __name__ == "__main__":
    main()
