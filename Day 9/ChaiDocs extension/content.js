// Create a button element
const botButton = document.createElement("button");
botButton.innerText = "🤖";
botButton.style.position = "fixed";
botButton.style.bottom = "20px";
botButton.style.right = "20px";
botButton.style.zIndex = "99999";
botButton.style.fontSize = "24px";
botButton.style.width = "60px";
botButton.style.height = "60px";
botButton.style.backgroundColor = "#4CAF50";
botButton.style.color = "white";
botButton.style.border = "none";
botButton.style.borderRadius = "50%";
botButton.style.cursor = "pointer";

// When clicked, open popup
botButton.onclick = () => {
  chrome.runtime.sendMessage({ action: "openPopup" });
};

document.body.appendChild(botButton);