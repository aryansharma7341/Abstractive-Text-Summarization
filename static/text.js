function summarize() {
    var inputText = document.getElementById("inputText").value.trim();
    var warningDiv = document.getElementById("warning");

    if (inputText === "") {
        warningDiv.style.display = "block";
        return;
    }

    warningDiv.style.display = "none";

    // Perform summarization (replace this with your summarization logic)
    var summarizedText = "{{ result }}";

    var summaryDiv = document.getElementById("summary");
    var summaryContent = document.getElementById("summary-content");
    
    summaryContent.innerText = summarizedText;
    summaryDiv.style.display = "block";
}

function copyToClipboard() {
    var textToCopy = document.getElementById("summary-content").innerText;
    navigator.clipboard.writeText(textToCopy).then(function() {
        alert("Text copied to clipboard");
    }, function() {
        alert("Failed to copy text to clipboard");
    });
}
