let mediaRecorder;
let chunks = [];

const startBtn = document.getElementById('start-btn');
const stopBtn = document.getElementById('stop-btn');

this.updateChat = function () {
    console.log('test')
    $(document).ready(function() {
    // AJAX-Anfrage an den Flask-Server senden
    $.ajax({
      url: "/chat/user/newest", // URL des Flask-Endpunkts, der die Liste zurückgibt
      type: "GET",
      dataType: "json", // Datenformat, das vom Server zurückgegeben wird (JSON in diesem Beispiel)
      success: function(response) {
        // Funktion, die ausgeführt wird, wenn die AJAX-Anfrage erfolgreich ist
        console.log(response)

        // Aktualisieren des Inhalts des Divs mit der generierten HTML-Liste
        $("#chat-update").append("<div class=\"col-9 offset-3 text-right mt-2 p-2 w-75 border align-items-end bg-muted\"\n" +
            "                     style=\"text-align: right; width: 75%\">\n" +
            "                    <p class=\"text-right \">" + response.text + "</p>\n" +
            "                </div>");
      }
    });
  });

    $(document).ready(function() {
    // AJAX-Anfrage an den Flask-Server senden
    $.ajax({
      url: "/chat/gpt/newest", // URL des Flask-Endpunkts, der die Liste zurückgibt
      type: "GET",
      dataType: "json", // Datenformat, das vom Server zurückgegeben wird (JSON in diesem Beispiel)
      success: function(response) {
        // Funktion, die ausgeführt wird, wenn die AJAX-Anfrage erfolgreich ist
        console.log(response)

        // Aktualisieren des Inhalts des Divs mit der generierten HTML-Liste
        $("#chat-update").append("<div class=\"col-9 text-left mt-2 p-2 bg-secondary\">"+
                    "<div>" + response.text + "</div>" +
                "</div>");
      }
    });
  });
};
navigator.mediaDevices.getUserMedia({audio: true})
    .then(stream => {
        mediaRecorder = new MediaRecorder(stream);
        startBtn.disabled = false;

        mediaRecorder.addEventListener('dataavailable', event => {
            chunks.push(event.data);
        });

        mediaRecorder.addEventListener('stop', () => {
            const blob = new Blob(chunks, {type: 'audio/webm'});
            chunks = [];

            const formData = new FormData();
            formData.append('audio', blob, 'recording.webm');

            fetch('/save-audio', {
                method: 'POST',
                body: formData
            })
                .then(response => {
                    if (response.ok) {
                        this.updateChat();


                        const audioPlayer = new Audio('/audio/The best text ever');
                        // audioPlayer.src = URL.createObjectURL(blob);
                        audioPlayer.controls = true;
                        audioPlayer.autoplay = true;
                        audioPlayer.hidden = true;
                        document.body.appendChild(audioPlayer);
                    } else {
                        console.error('Failed to save audio');
                    }
                });
        });
    })
    .catch(error => {
        console.error('Failed to get user media:', error);
    });

startBtn.addEventListener('click', () => {
    startBtn.disabled = true;
    stopBtn.disabled = false;
    chunks = [];
    mediaRecorder.start();
});

stopBtn.addEventListener('click', () => {
    stopBtn.disabled = true;
    mediaRecorder.stop();
});

