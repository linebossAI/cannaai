from flask import Flask, jsonify, request, render_template_string

from services.ai_assistant import get_response

app = Flask(__name__)


HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>CannabisAI</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #101412;
            color: #f4f7f5;
        }

        .layout {
            display: flex;
            min-height: 100vh;
        }

        .sidebar {
            width: 240px;
            background: #171c19;
            border-right: 1px solid #29312d;
            padding: 24px;
        }

        .logo {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 8px;
        }

        .subtitle {
            color: #8f9b94;
            font-size: 13px;
            margin-bottom: 30px;
        }

        .nav {
            display: block;
            width: 100%;
            padding: 12px;
            margin: 7px 0;
            border: 0;
            border-radius: 10px;
            background: transparent;
            color: #dce3df;
            text-align: left;
            cursor: pointer;
            font-size: 14px;
        }

        .nav:hover {
            background: #242c27;
        }

        .main {
            flex: 1;
            display: flex;
            flex-direction: column;
        }

        .header {
            padding: 22px 28px;
            border-bottom: 1px solid #29312d;
            font-size: 18px;
            font-weight: bold;
        }

        .chat {
            flex: 1;
            padding: 35px;
            max-width: 900px;
            width: 100%;
            margin: auto;
        }

        .welcome {
            margin-top: 70px;
            margin-bottom: 30px;
        }

        .welcome h1 {
            font-size: 38px;
            margin-bottom: 10px;
        }

        .welcome p {
            color: #9aa69f;
        }

        .message {
            white-space: pre-line;
            background: #1b221e;
            border: 1px solid #29312d;
            border-radius: 14px;
            padding: 18px;
            margin: 20px 0;
        }

        .input-area {
            display: flex;
            gap: 10px;
            margin-top: 30px;
        }

        input {
            flex: 1;
            padding: 15px;
            border-radius: 12px;
            border: 1px solid #39443e;
            background: #171c19;
            color: white;
            outline: none;
        }

        button.send {
            padding: 15px 22px;
            border: 0;
            border-radius: 12px;
            cursor: pointer;
            font-weight: bold;
        }

        @media (max-width: 700px) {
            .sidebar {
                display: none;
            }

            .chat {
                padding: 20px;
            }

            .welcome h1 {
                font-size: 30px;
            }
        }
    </style>
</head>

<body>

<div class="layout">

    <aside class="sidebar">
        <div class="logo">🌿 CannabisAI</div>
        <div class="subtitle">Business Assistant</div>

        <button class="nav" onclick="ask('Show me our products')">
            🌿 Products
        </button>

        <button class="nav" onclick="ask('What is low in inventory?')">
            📦 Inventory
        </button>

        <button class="nav" onclick="ask('Give me a marketing idea')">
            📣 Marketing
        </button>

        <button class="nav" onclick="ask('Check compliance')">
            ⚠️ Compliance
        </button>

        <button class="nav" onclick="ask('What can you help the business with?')">
            📈 Business
        </button>
    </aside>

    <main class="main">

        <div class="header">
            CannabisAI
        </div>

        <section class="chat">

            <div class="welcome">
                <h1>What's the move?</h1>
                <p>
                    Your AI business assistant for products,
                    inventory, marketing, and operations.
                </p>
            </div>

            <div id="messages"></div>

            <div class="input-area">
                <input
                    id="message"
                    placeholder="Ask CannabisAI..."
                    onkeydown="if(event.key === 'Enter') sendMessage()"
                >

                <button class="send" onclick="sendMessage()">
                    Send
                </button>
            </div>

        </section>

    </main>

</div>

<script>
async function sendMessage() {
    const input = document.getElementById("message");
    const message = input.value.trim();

    if (!message) return;

    await ask(message);

    input.value = "";
    input.focus();
}


async function ask(message) {
    const messages = document.getElementById("messages");

    messages.innerHTML += `
        <div class="message">
            <strong>You</strong><br>
            ${escapeHtml(message)}
        </div>
    `;

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        const data = await response.json();

        messages.innerHTML += `
            <div class="message">
                <strong>🌿 CannabisAI</strong><br>
                ${escapeHtml(data.response)}
            </div>
        `;

    } catch (error) {
        messages.innerHTML += `
            <div class="message">
                <strong>⚠️ Error</strong><br>
                CannabisAI could not process that request.
            </div>
        `;
    }

    window.scrollTo(0, document.body.scrollHeight);
}


function escapeHtml(text) {
    const div = document.createElement("div");
    div.innerText = text;
    return div.innerHTML;
}
</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}

    message = data.get("message", "")

    return jsonify({
        "response": get_response(message)
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "online",
        "service": "CannabisAI"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
