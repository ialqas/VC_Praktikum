
import { useState } from "react";

async function findAddress(street: string, housenumber: string, postalCode: string, setResp: Function, setCoords: Function) {
    const response = await fetch('http://localhost:8080/api/address/coordinates', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({"street": street, "housenumber": housenumber, "postalCode": postalCode})
      });
    const data = await response.json();
    setResp([data["lat"], data["lon"]]);
    console.log("RESPONSE TYPES ", typeof(data["lat"]), typeof(data["lon"]));
    setCoords([data["lat"], data["lon"]]);
}

//TODO: BUTTON ZU SECOND STEP ERST CLICKABLE MACHEN WENN COORDINATES GEFUNDEN WURDEN

function AddressStep({setStep, setCoords}: {setStep: Function, setCoords: Function}) {
    const [street, setStreet] = useState("Wenckstraße");
    const [housenumber, setHousenumber] = useState("13");
    const [postalCode, setPostalCode] = useState("64295");
    const [resp, setResp]  = useState(["x", "x"]);

    //TODO USESTATE INITIAL VALUES + INPUT VALUES ANPASSEN

    return (
        <div className="flex flex-col justify-center items-center space-y-6">
            <div className="flex flex-col items-center space-x-6">
                    <p>Your picture did not contain any Geolocation, so we need your address</p>        
                    <input className="border-2 border-gray-500" type="text" placeholder="Street" onChange = {(event) => setStreet(event.target.value)}/>
                    <input className="border-2 border-gray-500" type="text" placeholder="Housenumber" onChange = {(event) => setHousenumber(event.target.value)}/>
                    <input className="border-2 border-gray-500" type="number" placeholder="Postal Code" onChange = {(event) => setPostalCode(event.target.value)}/>
            </div>
            <div className="flex gap-4">
                <button className="relative flex h-[50px] w-40 items-center justify-center overflow-hidden bg-gray-800 text-white shadow-2xl transition-all before:absolute before:h-0 before:w-0 before:rounded-full before:bg-orange-600 before:duration-500 before:ease-out hover:red-400 hover:before:h-56 hover:before:w-56" onClick={() => { findAddress(street, housenumber, postalCode, setResp, setCoords)}}>
                <span className="relative z-10">Confirm Address</span>
                </button>
            </div>
            <div className={resp.length == 0 ? "flex flex-row items-center space-x-6 hidden" : "flex flex-row items-center space-x-6"}>
                <div className={resp[0] == "x" ? "hidden" : ""}>Coordinates: {resp[0]}, {resp[1]}</div>
                <div className={resp[0] == "x" ? "" : "hidden"}><div className="text-red-600">Address not found, need manual approach</div></div>
            </div>
            <div className={resp.length == 0 ? " flex gap-4 hidden": "flex gap-4"}> 
                <div className={resp[0] == "x" ? "hidden" : ""}>
                    <button className="relative flex h-[50px] w-40 items-center justify-center overflow-hidden bg-gray-800 text-white shadow-2xl transition-all before:absolute before:h-0 before:w-0 before:rounded-full before:bg-orange-600 before:duration-500 before:ease-out hover:shadow-orange-600 hover:before:h-56 hover:before:w-56" onClick={() => { setStep(3)}}>
                        <span className="relative z-10">Next Step</span>
                    </button>
                </div>
            </div>

        </div>
    );
}

export default AddressStep;

/*

<div className="flex gap-4"> 
                <div className={resp.length == 0 ? "hidden": "flex gap-4"}> 
                    <button className="relative flex h-[50px] w-40 items-center justify-center overflow-hidden bg-gray-800 text-white shadow-2xl transition-all before:absolute before:h-0 before:w-0 before:rounded-full before:bg-orange-600 before:duration-500 before:ease-out hover:shadow-orange-600 hover:before:h-56 hover:before:w-56" onClick={() => { setStep(2)}}>
                        <span className="relative z-10">Next Step</span>
                    </button>
                </div>
            </div>

*/