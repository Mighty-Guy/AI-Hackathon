let mediaRecorder;
      let chunks = [];

      const startBtn = document.getElementById('start-btn');
      const stopBtn = document.getElementById('stop-btn');

      navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
          mediaRecorder = new MediaRecorder(stream);
          startBtn.disabled = false;

          mediaRecorder.addEventListener('dataavailable', event => {
            chunks.push(event.data);
          });

          mediaRecorder.addEventListener('stop', () => {
            const blob = new Blob(chunks, { type: 'audio/webm' });
            chunks = [];

            const formData = new FormData();
            formData.append('audio', blob, 'recording.webm');

            fetch('/save-audio', {
              method: 'POST',
              body: formData
            })
            .then(response => {
              if (response.ok) {
                console.log('Audio saved successfully');
                const audioPlayer = document.createElement('audio');
                audioPlayer.src = URL.createObjectURL(blob);
                audioPlayer.controls = true;
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