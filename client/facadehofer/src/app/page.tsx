import Header from "./[components]/[header]/header";

export default function Home() {
  return (
    <div className="font-coolvetica">
      <Header />
    <div className="flex h-[100vh] items-center justify-center">
    <div className="border-solid border-4 border-indigo-600 flex h-[50vh] items-center justify-center">
      <h1>Willkommen, bitte Adresse eingeben:</h1>
      <input type="text" />
      <button>Suchen</button>
      
    </div>
    </div>
    </div>
  );
}
