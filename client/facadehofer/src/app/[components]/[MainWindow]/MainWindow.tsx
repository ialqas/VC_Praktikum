"use client";
import {useState} from 'react';
import ButtonBoard from './[ButtonBoard]/ButtonBoard';
import StepWindow from './[StepWindow]/StepWindow';

function mainWindow() {
    const [step, setStep] = useState(0);
    return (
    <div className="border-double border-8 border-cyan-500 grid flex flex-col h-[100vh] items-center justify-center">
        <div className="relative border-solid border-4 border-indigo-600 flex w-[100vh] h-[100vh] items-center justify-center">
        <StepWindow step={step} setStep={setStep} />
        </div>
        <div className="relative hidden border-solid border-4 border-indigo-600 flex w-[100vh] items-center justify-center">
        <ButtonBoard setStep={setStep} />
        </div>
    </div>
    );
    }
    
    

export default mainWindow;