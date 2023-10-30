document.querySelector('button').addEventListener('click', function () {
    var fileInput = document.getElementById('file-input');
    var file = fileInput.files[0];
    var formData = new FormData();
    formData.append('file', file);

    fetch('http://127.0.0.1:8000/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the server
        pred=document.querySelector(".s4")
        pred.innerHTML=data.prediction
        if(pred.innerHTML==="undefined"){
            pred.innerHTML="Submit an image"
            pred.style.fontSize="30px"
        }
        else{
            console.log(data.prediction)
            pred.innerHTML=data.prediction
            pred.style.fontSize="50px"
        }
        // console.log(data)
    })
    .catch(error => console.error('Error:', error));
});
