
const messages = [
  "Analyzing brainwaves...",
  "Scanning memories...",
  "Calculating probabilities...",
  "Decoding thoughts..."
];


const btn = document.getElementById("readBtn");
const progressArea = document.getElementById("progressArea");
const progressBar = document.getElementById("progressBar");
const progressText = document.getElementById("progressText");
const result = document.getElementById("result");


btn.addEventListener("click", () => {
  const number = document.getElementById("numberInput").value;


  if (!number || number < 1 || number > 10) {
    alert("Please enter a number between 1 and 10!");
    return;
  }


  result.textContent = "";
  progressBar.style.width = "0%";
  progressArea.classList.remove("d-none");

  let step = 0;


  const interval = setInterval(() => {
    progressText.textContent = messages[step] || "";
    progressBar.style.width = ((step + 1) / messages.length) * 100 + "%";
    step++;


    if (step === messages.length) {
      clearInterval(interval);
      setTimeout(() => {
        progressArea.classList.add("d-none");
        result.textContent = `You're thinking of the number ${number}.`;
      }, 800);
    }
  }, 1200);
});
