const API_BASE = "http://127.0.0.1:8000";

async function askQuestion() {
  const question = document.getElementById("question").value;

  const response = await fetch(`${API_BASE}/query`, {
    method: "POST",
    body: new URLSearchParams({
      q: question,
      k: 3
    })
  });

  const data = await response.json();

  document.getElementById("answer").innerText = data.answer;

  const sources = document.getElementById("sources");
  sources.innerHTML = "";

  data.sources.forEach((source) => {
    const card = document.createElement("div");
    card.className = "source-card";

    card.innerHTML = `
      <strong>${source.metadata.subject} - Grade ${source.metadata.grade}</strong>
      <p><strong>Lesson:</strong> ${source.metadata.lesson}</p>
      <p><strong>Score:</strong> ${source.score.toFixed(3)}</p>
      <p>${source.content}</p>
    `;

    sources.appendChild(card);
  });
}