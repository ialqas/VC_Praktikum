import Image from "next/image";
import logo from "./logo_fraunhofer.png";

const Header = () => (
    <header>
    <div className="bg-gradient-to-r from-indigo-500 h-20 p-10 flex justify-items-center">
        <div className="flex items-center">
        <Image src={logo} alt="Logo" width={100} height={50} />
        </div>
        <div className="flex items-center">
        <h1 className="text-white text-3xl font-bold">Facadehofer Fassadenberechnung</h1>
        </div>
    </div>
    </header>
);

export default Header;