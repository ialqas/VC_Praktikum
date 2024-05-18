import React,{ useEffect, useState } from "react";
import * as ExifReader from "exifreader";

async function getExif(file: File) {
    try {
    const exifData = await ExifReader.load(file);

    const latitude = exifData?.["GPSLatitude"]?.description;
    const longitude = exifData?.["GPSLongitude"]?.description;

    
    if(latitude && longitude) {
        console.log("GETEXIF HERE", latitude, longitude);
        return [String(latitude), String(longitude)];
    } else {
        return ["x","x"];
    }
    } catch (error) {
        console.log(error);
        return ["x","x"];
    }
}

function PicUploader({setStep, coords, setCoords, setPicture}: {setStep: Function, coords: string[], setCoords: Function, setPicture: Function}) {
    const [file, setFile] = useState<File | null>(null);
    const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        if(e.target.files) {
        setFile(e.target.files[0]);
    }
    };

    useEffect(() => {
        if(file) {
            const getExifData = async () => {
                var results = await getExif(file);
                console.log("IN USEFFECT, JUST USED GETEXIF", results)
                console.log("TYPES:" , typeof(results[0]), typeof(results[1]));
                setCoords([results[0], results[1]]);
                console.log("AFTER SETCOORDS", coords)
            };
            getExifData();
            const reader = new FileReader();
            reader.onloadend = async function() {
                if(reader.result) {
                    var base64String = String(reader.result);
                    setPicture(base64String);
                } 
            }
            reader.readAsDataURL(file);
        }
    }, [file]);

    return (
        <div className="flex flex-col items-center justify-center">
            <input type="file" id="file" onChange={e => (handleFileChange(e))}/>
        </div>
    )
}

export default PicUploader;