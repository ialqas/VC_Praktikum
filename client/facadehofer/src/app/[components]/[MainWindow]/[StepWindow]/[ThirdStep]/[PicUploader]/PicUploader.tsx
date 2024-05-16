import React,{ useState } from "react";


function PicUploader({houseWidth}: {houseWidth: number}) {
    const [picture, setPicture] = useState<File | null>(null);
    const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        if(e.target.files) {
        setPicture(e.target.files[0]);
        console.log("handled upload", e.target.files[0])
        }
    };

    const handleUpload = async () => {
        if(picture) {
            const reader = new FileReader();
            reader.onloadend = async function() {
                if(reader.result) {
                    var base64String = String(reader.result);
                    const response = await fetch("http://localhost:8080/api/picture/receive", {
                    method: "POST",
                    headers: {
                        "Accept": "application/json",
                        "Content-Type": "application/json"                  
                    },
                    body: JSON.stringify({"picture": {base64String}, "houseWidth": {houseWidth}})
                    });
                    const data = await response.json();
                    //TODO: DO SOMETHING WITH RETURNED DATA (prob add returned values to var or state)
                }
                
            }
            var read = reader.readAsDataURL(picture);
            
        }
    };

    return (
        <div className="flex flex-col items-center justify-center">
            <input type="file" onChange={e => (handleFileChange(e))}/>
            <button className="border-solid border-2 border-indigo-600 rounded-lg hover:bg-green-300" onClick={handleUpload}>Use Picture</button>
        </div>
    )
}

export default PicUploader;