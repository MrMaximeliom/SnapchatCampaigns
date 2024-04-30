document.addEventListener("DOMContentLoaded", (event) => {
  var data = document.getElementById('alert-data') ? JSON.parse(document.getElementById('alert-data').textContent) : null;
  if(data){
Swal.fire({
  title: data.title,
  text: data.message,
  icon: data.icon
});
  }
});