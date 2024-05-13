import {useState} from "react";



async function requestData(setText: Function) {
    const response = await fetch("http://localhost:8080/api/second");
    const data = await response.json();
    setText(data.message);

}

function SecondStep({setStep}: {setStep: Function}) {
    const [text, setText] = useState("Not yet pressed");
    return (
        <div className="flex flex-col justify-center items-center space-y-6">
            <h1>Second Step, make API call on button press</h1>
            <div className="flex flex-row items-center space-x-6">
                <button className="relative flex h-[50px] w-40 items-center justify-center bg-emerald-400 border-double border-4 hover:bg-cyan-600" onClick={() => {requestData(setText)}}>Make API Call</button>
                <div>{text}</div>
            </div>
            <div className="flex gap-4">
                <button className="relative flex h-[50px] w-40 items-center justify-center overflow-hidden bg-gray-800 text-white shadow-2xl transition-all before:absolute before:h-0 before:w-0 before:rounded-full before:bg-orange-600 before:duration-500 before:ease-out hover:shadow-orange-600 hover:before:h-56 hover:before:w-56" onClick={() => { setStep(3)}}>
                <span className="relative z-10">Next Step</span>
                </button>
            </div>
        </div>
    );
}

export default SecondStep;