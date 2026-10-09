let RunSentimentAnalysis = () => {
    const textToAnalyze = document.getElementById("textToAnalyze").value;
    const systemResponse = document.getElementById("system_response");

    if (!textToAnalyze.trim()) {
        systemResponse.textContent = "Invalid text! Please try again!";
        return;
    }

    const xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (this.readyState === 4) {
            if (this.status === 200) {
                systemResponse.textContent = this.responseText;
            } else {
                systemResponse.textContent =
                    "Unable to process the request. Please try again.";
            }
        }
    };

    xhttp.open(
        "GET",
        "/emotionDetector?textToAnalyze=" +
            encodeURIComponent(textToAnalyze),
        true
    );
    xhttp.send();
};