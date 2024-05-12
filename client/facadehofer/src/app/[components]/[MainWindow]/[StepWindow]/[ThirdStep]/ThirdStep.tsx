function ThirdStep({setStep}: {setStep: Function}) {
    return (
        <div>
            <h1>Third Step</h1>
            <div className="flex gap-4">
                <button className="relative flex h-[50px] w-40 items-center justify-center overflow-hidden bg-gray-800 text-white shadow-2xl transition-all before:absolute before:h-0 before:w-0 before:rounded-full before:bg-orange-600 before:duration-500 before:ease-out hover:shadow-orange-600 hover:before:h-56 hover:before:w-56" onClick={() => { setStep(4)}}>
                <span className="relative z-10">Next Step</span>
                </button>
            </div>
        </div>
    );
}

export default ThirdStep;