const quizTypeSelect = document.getElementById("quizType");
const subTopicsContainer = document.getElementById("subTopics");

quizTypeSelect.addEventListener("change", (event) => {
  const selectedValue = event.target.value;

  subTopicsContainer.innerHTML = ""; // Clear previous sub-topics

  if (selectedValue === "coding") {
    const codingLanguages = document.createElement("select");
    codingLanguages.id = "codingLanguages";

    const languageOptions = [
      { value: "c", text: "C" },
      { value: "python", text: "Python" },
      { value: "cpp", text: "C++" },
      { value: "java", text: "Java" },
    ];

    languageOptions.forEach((option) => {
      const languageOption = document.createElement("option");
      languageOption.value = option.value;
      languageOption.text = option.text;
      codingLanguages.appendChild(languageOption);
    });

    subTopicsContainer.appendChild(codingLanguages);
  } else if (selectedValue === "aktu") {
    // Create input box for AKTU subjects
    const aktuSubjectsInput = document.createElement("input");
    aktuSubjectsInput.type = "text";
    aktuSubjectsInput.placeholder = "Enter AKTU Subject";
    subTopicsContainer.appendChild(aktuSubjectsInput);
  } else if (selectedValue === "gk") {
    const gkSubTopics = document.createElement("select");
    gkSubTopics.id = "gkSubTopics";

    const gkOptions = [
      { value: "currentAffairs", text: "Current Affairs" },
      { value: "history", text: "History" },
      { value: "geography", text: "Geography" },
    ];

    gkOptions.forEach((option) => {
      const gkOption = document.createElement("option");
      gkOption.value = option.value;
      gkOption.text = option.text;
      gkSubTopics.appendChild(gkOption);
    });

    subTopicsContainer.appendChild(gkSubTopics);
  }
});


function openDialog(button) {
    const dialog = button.closest('div').querySelector('dialog');
    dialog.showModal();
  }