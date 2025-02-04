document.getElementById("culminarPeriodoForm").addEventListener('submit', function(event){
    console.log("OK")
    event.preventDefault();
    const formData = new FormData(this);
    const url = document.getElementById("urlCulminarPeriodo").value;
    fetch(`${url}`,{
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data =>{
            if(data.success){
                alert(data.message);
                const modal = new bootstrap.Modal(document.getElementById("culminarPeriodo"));
                modal.hide();
                this.reset();
                window.location.reload();
            }
            else {
                alert(data.message);
            }
        })
    .catch(error => {
        console.error('Error:', error);
    })
})