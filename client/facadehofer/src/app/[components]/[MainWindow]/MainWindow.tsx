"use client";
import {useState} from 'react';
import ButtonBoard from './[ButtonBoard]/ButtonBoard';
import StepWindow from './[StepWindow]/StepWindow';

function mainWindow() {
    const [step, setStep] = useState(1);
    return (
    <div className="border-double border-8 border-cyan-500 grid flex h-[80vh] items-center justify-center">
        <div className="relative col-start-1 row-start-1 border-solid border-4 border-indigo-600 flex w-[100vh] h-[100%] items-center justify-center">
        <StepWindow step={step} setStep={setStep} />
        </div>
        <div className="relative col-start-1 row-start-2 border-solid border-4 border-indigo-600 flex w-[100vh] h-[100%] items-center justify-center">
        <ButtonBoard setStep={setStep} />
        </div>
    </div>
    );
    }
    
    

export default mainWindow;