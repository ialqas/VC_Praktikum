import AddressStep from "./[AddressStep]/AddressStep";
import PicUploadStep from "./[PicUploadStep]/PicUploadStep";
import MapStep from "./[MapStep]/MapStep";
import CalculationStep from "./[CalculationStep]/CalculationStep";
import { use, useState } from "react";

function stepWindow({step, setStep}: {step: number, setStep: Function}) {
    const [coords, setCoords] = useState(["", ""]);
    const [selectedMarkers, setSelectedMarkers] = useState([]);
    const [houseWidth, setHouseWidth] = useState(0);
    const [picture, setPicture] = useState("");
    switch(step) {
        case 1: return <PicUploadStep setStep={setStep} coords={coords} setCoords={setCoords} setPicture={setPicture}/>;
        case 2: return <AddressStep setStep={setStep} coords={coords} setCoords={setCoords}/>;
        case 3: return <MapStep setStep={setStep} coords={coords} selectedMarkers={selectedMarkers} setSelectedMarkers={setSelectedMarkers} setHouseWidth={setHouseWidth}/>;
        case 4: return <CalculationStep setStep={setStep} picture={picture} houseWidth={houseWidth}/>;
        case 5: return <p>Done</p>;
        default: return (
        <div className="flex flex-col justify-center items-center space-y-6">
         <p>Welcome to the website</p>
         <div className="flex gap-4">
                <button className="relative flex h-[50px] w-40 items-center justify-center overflow-hidden bg-gray-800 text-white shadow-2xl transition-all before:absolute before:h-0 before:w-0 before:rounded-full before:bg-orange-600 before:duration-500 before:ease-out hover:shadow-orange-600 hover:before:h-56 hover:before:w-56" onClick={() => { setStep(1)}}>
                <span className="relative z-10">Get Started</span>
                </button>
            </div>
        </div>
        );
        }
}   

export default stepWindow;