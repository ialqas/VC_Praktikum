"use client";
function ButtonBoard({setStep}: {setStep: Function}) {
    return (
        <div className="button-board">
                <button className="border-solid border-2 border-indigo-600 hover:bg-green-500" onClick={() => { setStep(1) }}>FirstButton</button>
                <button className="border-solid border-2 border-indigo-600 hover:bg-green-500" onClick={() => { setStep(2) }}>SecondButton</button>
                <button className="border-solid border-2 border-indigo-600 hover:bg-green-500" onClick={() => { setStep(3) }}>ThirdButton</button>
        </div>
    )
}

export default ButtonBoard;