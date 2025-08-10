def matmul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    C = [[0.0] * len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            C[i][j] = sum(
                [a_i * b_j for a_i, b_j in zip(A[i], [b_row[j] for b_row in B])]
            )
    return C


def main():
    # 0. load text
    with open("data/tinymoliere.txt", "r") as f:
        text = f.read()

    # 1. tokenize

    # -- done before --
    unique_tokens = sorted(set(text))

    token_to_id = {token: i for i, token in enumerate(sorted(unique_tokens))}
    id_to_token = {i: token for token, i in token_to_id.items()}

    def tokenize(text: str) -> list[int]:
        return [token_to_id[token] for token in text]

    def untokenize(token_ids: list[int]) -> str:
        return "".join(id_to_token[id] for id in token_ids)

    # -- at runtime --
    sample_text = "Il faut avouer que je suis le plus malheureux"
    input_tokens = tokenize(sample_text[:-1])  # we try to predict the next token (x)
    label = tokenize(sample_text[-1])  # the next token (x)

    # 2. embed

    # dim of embedding vectors 128
    embed_dim = 16
    embedding = [[0.0] * embed_dim for _ in range(len(unique_tokens))]
    input_embed = [
        embedding[token_id] for token_id in input_tokens
    ]  # seq_len x embed_dim

    breakpoint()

    # 3. (positional embedding)

    # 4. self-attention

    # for each tokens we project into Query, Key, Value:
    attn_dim = 16

    # initialize the weights
    query_w = [[0.0] * embed_dim for _ in range(attn_dim)]
    key_w = [[0.0] * embed_dim for _ in range(attn_dim)]
    value_w = [[0.0] * embed_dim for _ in range(attn_dim)]

    # project for each sequence elements:
    queries = [
        sum([emb * q_w for emb, q_w in zip(embed_vector, query_w)])
        for embed_vector in input_embed
    ]  # seq_len x attn_dim
    keys = [
        sum([emb * k_w for emb, k_w in zip(embed_vector, key_w)])
        for embed_vector in input_embed
    ]  # seq_len x attn_dim
    values = [
        sum([emb * v_w for emb, v_w in zip(embed_vector, value_w)])
        for embed_vector in input_embed
    ]  # seq_len x attn_dim

    # softmax(query * key) * value

    # 5. feed-forward

    # 6. output layer

    # 7. softmax

    # 8. loss calculation

    # 9. backpropagation

    # 10. optimization


if __name__ == "__main__":
    main()
