let dragArea = document.querySelector(".drag-area");
let dragText = document.querySelector(".header");
let btn = document.querySelector(".btns");
let input = document.querySelector("input");

let file;

btn.onclick = () => {
  input.click();
}

function processzip(folder){
  var zip = new JSZip();
  var img = zip.folder(folder);
  zip.generateAsync({type:"blob"})
    .then(function(contents) {
      console.log(contents)
      return zip.files[0]
  });
}

input.addEventListener("change", function (){
    dragText.textContent = "Uploaded sucessfully!";
  dragArea.classList.remove("cus")
  dragArea.classList.add("cos")
  dragArea.classList.remove("cust")
  let folder = this.files[0];
  if (folder.type == "application/zip") {
    console.log(folder)
  let fileReader = new FileReader();
  fileReader.onload = ()=>{
    let fileURL = fileReader.result;
    console.log(fileURL)
    uploadfile(fileURL);
  };
  fileReader.readAsDataURL(folder);
  }
  else {
    dragText.textContent = "Unsupported format";
    dragArea.classList.remove("cus")
    dragArea.classList.remove("cos")
    dragArea.classList.add("cust")
  }
})
dragArea.addEventListener("dragover", (e) => {
  e.preventDefault();
  dragText.textContent = "Release to Upload";
  dragArea.classList.remove("cos")
  dragArea.classList.add("cus")
})
dragArea.addEventListener("dragleave", (e) => {
  dragText.textContent = "Drag & Drop zip file";
  dragArea.classList.remove("cos")
  dragArea.classList.remove("cus")
  dragArea.classList.remove("cust")
})
dragArea.addEventListener("drop", (e) => {
  e.preventDefault();
  dragText.textContent = "Uploaded sucessfully!";
  dragArea.classList.remove("cus")
  dragArea.classList.add("cos")
  dragArea.classList.remove("cust")
  let folder = e.dataTransfer.files[0];
  if (folder.type == "application/zip") {
    console.log(folder)
  let fileReader = new FileReader();
  fileReader.onload = ()=>{
    let fileURL = fileReader.result;
    console.log(fileURL)
    uploadfile(fileURL);
  };
  fileReader.readAsDataURL(folder);
  }
  else {
    dragText.textContent = "Unsupported format";
    dragArea.classList.remove("cus")
    dragArea.classList.remove("cos")
    dragArea.classList.add("cust")
  }
})

function uploadfile(file) {
  $.ajax({
      method: "POST",
      url: "/",
      data: {
        'file': file,
         // csrfmiddlewaretoken: token,
      },
      // datatype: "dataType",
      success: function (response) {
        Swal.fire(
          response.heading,
          response.message,
          response.status
        )
      },
      error: function (e) {
        Swal.fire(
         'Error',
          e.statusText,
          'warning'
        )
      }
    })
}
