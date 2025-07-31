from llama_cpp import Llama

llm = Llama(
    model_path=r'C:\Users\anura\PycharmProjects\dc_decision_support_system\project-root\backend\model\mistral-7b-instruct-v0.2.Q8_0.gguf',
    n_gpu_layers=40,
    n_ctx=2048,
    verbose=True
)

output = llm.create_chat_completion(
    messages=[{
        'role': 'system',
        'content': 'say hello'
    }],
    max_tokens=10
)

print(output['choices'][0]['message']['content'])