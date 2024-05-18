

function calculationStep({setStep, picture, houseWidth}: {setStep: Function, picture: String, houseWidth: number}) {

    return (
        <div>
            <h1>Calculation Step</h1>
            <p>{houseWidth}</p>
        </div>
    )
}

export default calculationStep;