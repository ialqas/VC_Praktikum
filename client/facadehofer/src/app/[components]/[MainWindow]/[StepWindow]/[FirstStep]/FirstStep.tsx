
import { useState } from "react";


function FirstStep({setStep}: {setStep: Function}) {
    const [city, setCity] = useState("");
    const [street, setStreet] = useState("");
    const [housenumber, setHousenumber] = useState("");
    const [postalCode, setPostalCode] = useState("");

    return (
        <div className="flex flex-col justify-center items-center space-y-6">
            <div className="flex flex-row items-center space-x-6">
                    <input className="border-2 border-gray-500" type="text" placeholder="City" onChange = {(event) => setCity(event.target.value)}/>
                    <input className="border-2 border-gray-500" type="text" placeholder="Street" onChange = {(event) => setStreet(event.target.value)}/>
                    <input className="border-2 border-gray-500" type="text" placeholder="Housenumber" onChange = {(event) => setHousenumber(event.target.value)}/>
                    <input className="border-2 border-gray-500" type="text" placeholder="Postal Code" onChange = {(event) => setPostalCode(event.target.value)}/>
                </div>
                <div className="flex gap-4">
                <button className="relative flex h-[50px] w-40 items-center justify-center overflow-hidden bg-gray-800 text-white shadow-2xl transition-all before:absolute before:h-0 before:w-0 before:rounded-full before:bg-orange-600 before:duration-500 before:ease-out hover:red-400 hover:before:h-56 hover:before:w-56" onClick={() => { setStep(2)}}>
                <span className="relative z-10">Confirm Address</span>
                </button>
            </div>
            <div className="flex gap-4">
                <button className="relative flex h-[50px] w-40 items-center justify-center overflow-hidden bg-gray-800 text-white shadow-2xl transition-all before:absolute before:h-0 before:w-0 before:rounded-full before:bg-orange-600 before:duration-500 before:ease-out hover:shadow-orange-600 hover:before:h-56 hover:before:w-56" onClick={() => { setStep(2)}}>
                <span className="relative z-10">Next Step</span>
                </button>
            </div>

        </div>
    );
}

export default FirstStep;