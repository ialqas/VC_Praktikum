

function calculationStep({setStep, picture, houseWidth}: {setStep: Function, picture: String, houseWidth: number}) {

    return (
        <div className="flex flex-col justify-center items-center">
            <h1>Calculation Step</h1>
            <p>{houseWidth}</p>
            <p>{picture}</p>
        </div>
    )
}

export default calculationStep;