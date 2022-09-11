function generatecode(value) {
    let formdata = new formdata();
    formdata.append('data', value);
    fetch('http://localhost:5000/generate', {
    method: 'POST',
    body: formdata
    }).then((res) => {
        res.body.getReader().read().then((img)=> {
            let img_array = img.value;
            let stringvalue = String.fromCharCode(...img_array);
        })
    })
}