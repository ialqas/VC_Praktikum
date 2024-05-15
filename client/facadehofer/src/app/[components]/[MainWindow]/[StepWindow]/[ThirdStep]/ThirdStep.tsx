import { useState } from 'react';

async function requestData(name: string, number: number, setResp: Function) {
    const response = await fetch("http://localhost:8080/api/third?name=" + name + "&number=" + number);
    const data = await response.json();
    setResp([data.name, data.number]);

}

function ThirdStep({setStep, selectedMarkers}: {setStep: Function, selectedMarkers: string[][]}) {
    const [name, setName] = useState("");
    const [number, setNumber] = useState(0);
    const [resp, setResp]  = useState([]);
    return (
            <div className="flex flex-col justify-center space-y-6">
                <p>Your coordinates are {selectedMarkers[0]} and {selectedMarkers[1]}</p>
                <p>Next step: Use Oli's Python script to calculate the distance between these coordinates</p>
            </div>
    );
}

export default ThirdStep;

/*
<h1>Third Step, give Info to the API: Tell me your name and a number of your choice</h1>
                <div className="flex flex-row items-center space-x-6">
                    <input className="border-2 border-gray-500" type="text" placeholder="Name" onChange = {(event) => setName(event.target.value)}/>
                    <input className="border-2 border-gray-500" type="number" placeholder="Number" onChange = {(event) => setNumber(event.target.valueAsNumber)}/>
                </div>
                <div className={resp.length == 0 ? "flex flex-row items-center space-x-6 hidden" : "flex flex-row items-center space-x-6"}>
                    <div>Good Evening {resp[0]}, here is your doubled number: {resp[1]}. Amazing, right?</div>
                </div> 


                <div className="flex flex-row items-center">
                    <button className="relative flex h-[50px] w-40 items-center justify-center bg-emerald-400 border-double border-4 hover:bg-cyan-600" onClick={() => {requestData(name, number, setResp)}}>Make API Call</button>
                    <div></div>
                </div>
                <div className="flex gap-4">
                    <button className="relative flex h-[50px] w-40 items-center justify-center overflow-hidden bg-gray-800 text-white shadow-2xl transition-all before:absolute before:h-0 before:w-0 before:rounded-full before:bg-orange-600 before:duration-500 before:ease-out hover:shadow-orange-600 hover:before:h-56 hover:before:w-56" onClick={() => { setStep(4)}}>
                    <span className="relative z-10">Next Step</span>
                    </button>
                </div>
                */