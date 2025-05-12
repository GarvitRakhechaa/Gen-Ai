function askQuestion() {
  const input = document.getElementById("userInput");
  const question = input.value;
  if (!question) return;

  appendMessage("You", question);

  fetch("http://localhost:8000/api/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query: question })
  })
  .then(res => res.json())
  .then(data => {
    appendMessage("Bot", data.answer);
  })
  .catch(err => {
    console.error(err);
    appendMessage("Bot", "Error getting response.");
  });

  input.value = "";
}

function appendMessage(sender, message) {
  const chatbox = document.getElementById("chatbox");
  const msgDiv = document.createElement("div");
  msgDiv.innerHTML = `<strong>${sender}:</strong> ${message}`;
  chatbox.appendChild(msgDiv);
  chatbox.scrollTop = chatbox.scrollHeight;
}