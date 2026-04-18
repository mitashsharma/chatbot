async function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();

    if (message === "") return;

    addMessage(message, "user-message");
    input.value = "";

    addTyping();

    try {
        const response = await fetch("/get_response", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        });

        const data = await response.json();
        removeTyping();
        addMessage(data.response, "bot-message");
    } catch (error) {
        removeTyping();
        addMessage("⚠ Server error. Please try again.", "bot-message");
    }
}

function sendQuick(text) {
    document.getElementById("user-input").value = text;
    sendMessage();
}

function addMessage(text, className) {
    const chatBox = document.getElementById("chat-box");
    const msg = document.createElement("div");
    msg.className = className;
    msg.innerHTML = text;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function addTyping() {
    const chatBox = document.getElementById("chat-box");
    const typing = document.createElement("div");
    typing.className = "bot-message typing";
    typing.id = "typing-indicator";
    typing.innerHTML = "Typing...";
    chatBox.appendChild(typing);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function removeTyping() {
    const typing = document.getElementById("typing-indicator");
    if (typing) typing.remove();
}

document.addEventListener("DOMContentLoaded", function () {
    const input = document.getElementById("user-input");
    if (input) {
        input.addEventListener("keypress", function (e) {
            if (e.key === "Enter") {
                sendMessage();
            }
        });
    }
});
