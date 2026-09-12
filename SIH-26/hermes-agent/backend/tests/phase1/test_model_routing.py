from server.core.model_routing import prepare_messages_for_latest_turn, resolve_requested_model


def _messages(text, *, image=False):
    content = [{"type": "text", "text": text}]
    if image:
        content.append({"type": "image_url", "image_url": {"url": "data:image/png;base64,AA=="}})
    return [{"role": "user", "content": content if image else text}]


def test_professional_aliases_resolve_to_physical_models():
    expected = {
        "indra-general": "qwen3.5-4b",
        "coder": "qwen3.5-4b",
        "maths": "qwen3.5-4b",
        "writer": "gemma-2-2b-it",
        "ocr": "qwen2-vl-ocr-2b-instruct",
    }

    for alias, target in expected.items():
        assert resolve_requested_model(alias, _messages("hello")).routed_model == target


def test_auto_route_selects_a_specialist_for_each_latest_request():
    cases = (
        (_messages("Debug this Python API"), "qwen3.5-4b"),
        (_messages("Solve the equation 3x + 7 = 22"), "qwen3.5-4b"),
        (_messages("Rewrite this email clearly"), "gemma-2-2b-it"),
        (_messages("Write a paragraph about renewable energy"), "gemma-2-2b-it"),
        (_messages("What should I work on today?"), "qwen3.5-4b"),
        (_messages("Read the logo", image=True), "qwen2-vl-ocr-2b-instruct"),
    )

    for messages, target in cases:
        assert resolve_requested_model("indra-auto", messages).routed_model == target

    conversation = [
        {"role": "user", "content": "Rewrite this email clearly"},
        {"role": "assistant", "content": "Draft"},
        {"role": "user", "content": "Now solve 3x + 7 = 22"},
    ]
    assert resolve_requested_model("indra-auto", conversation).routed_model == "qwen3.5-4b"

    vision_conversation = [
        {"role": "user", "content": [
            {"type": "text", "text": "old image"},
            {"type": "image_url", "image_url": {"url": "old"}},
        ]},
        {"role": "user", "content": [
            {"type": "text", "text": "tell me about this img"},
            {"type": "image_url", "image_url": {"url": "clipboard"}},
            {"type": "image_url", "image_url": {"url": "newest"}},
        ]},
    ]
    prepare_messages_for_latest_turn(vision_conversation)
    assert len(vision_conversation[0]["content"]) == 1
    assert vision_conversation[1]["content"][-1]["image_url"]["url"] == "newest"
