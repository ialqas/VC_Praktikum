import FirstStep from "./[FirstStep]/FirstStep";
import SecondStep from "./[SecondStep]/SecondStep";
import ThirdStep from "./[ThirdStep]/ThirdStep";

function stepWindow({step, setStep}: {step: number, setStep: Function}) {
    switch(step) {
        case 1: return <FirstStep setStep={setStep}/>;
        case 2: return <SecondStep setStep={setStep}/>;
        case 3: return <ThirdStep setStep={setStep}/>;
        default: return <p>Welcome to the website</p>;
        }
}   

export default stepWindow;