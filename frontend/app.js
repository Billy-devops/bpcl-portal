const API = "/api";
async function loadDealers() {
  const res = await fetch(`${API}/dealers`);
  const data = await res.json();

  const list = document.getElementById("dealer-list");
  list.innerHTML = "";

  data.forEach(d => {
    list.innerHTML += `<div>${d.name} - ${d.location}</div>`;
  });
}

function searchDealer() {
  let input = document.getElementById("search").value.toLowerCase();
  let items = document.querySelectorAll("#dealer-list div");

  items.forEach(i => {
    i.style.display = i.innerText.toLowerCase().includes(input) ? "" : "none";
  });
}

async function submitComplaint() {
  const dealer = document.getElementById("dealer").value;
  const issue = document.getElementById("issue").value;

  await fetch(`${API}/complaints`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ dealer, issue })
  });

  alert("Complaint submitted");
}