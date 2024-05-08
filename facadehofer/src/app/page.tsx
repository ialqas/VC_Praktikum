import Header from "./[components]/[header]/header";

export default function Home() {
  return (
    <div className="font-coolvetica">
      <Header />
    <div>
      <h1>Willkommen, bitte Adresse eingeben:</h1>
      <input type="text" />
      <button>Suchen</button>
      
    </div>
    </div>
  );
}
