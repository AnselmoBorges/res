sample_dict = {
    "model": "gemma2:2b",
    "created_at": "2024-08-16T01:09:40.717598779Z",
    "message": {
        "role": "assistant",
        "content": "Saudades de quem, meu querido?  A gente nem sabe se foi a novela ou o choro do caixão! 😥🤣  Só me dá mais um café com açúcar, que eu preciso dar uma força pra continuar essa conversa... ☕💪\n\nAgora, você quer saber sobre novelas? 🤔\n\n\n",
    },
    "done_reason": "stop",
    "done": True,
    "total_duration": 28361537941,
    "load_duration": 15540999016,
    "prompt_eval_count": 158,
    "prompt_eval_duration": 1277049000,
    "eval_count": 65,
    "eval_duration": 11416392000,
}

print(sample_dict["message"]["content"])
