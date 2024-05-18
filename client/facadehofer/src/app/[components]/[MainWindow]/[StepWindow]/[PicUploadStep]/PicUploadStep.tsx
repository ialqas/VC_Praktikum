import { useState , useEffect } from 'react';
import PicUploader from './[PicUploader]/PicUploader';


function PicUploadStep({setStep, coords, setCoords, setPicture}: {setStep: Function, coords: string[], setCoords: Function, setPicture: Function}) {

    return (
        <div>
            <div className="flex flex-col justify-center space-y-6">
                <p>PUSTEPUpload Photo here</p>
            </div>
            <div className="flex flex-gap-4 justify-center space-y-6">
                <PicUploader setStep={setStep} coords={coords} setCoords={setCoords} setPicture={setPicture}/>
                <button className="relative flex h-[50px] w-40 items-center justify-center overflow-hidden bg-gray-800 text-white shadow-2xl transition-all before:absolute before:h-0 before:w-0 before:rounded-full before:bg-orange-600 before:duration-500 before:ease-out hover:shadow-orange-600 hover:before:h-56 hover:before:w-56" onClick={() => {coords[0] == "x" || coords[1] == "x" ? setStep(2) : setStep(3)}}>
                        <span className="relative z-10">Next Step</span>
                    </button>
            </div>
        </div>
    );
}

export default PicUploadStep;