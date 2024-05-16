"use client";
import {useEffect, useState} from "react";
import { MapContainer , TileLayer , Marker } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import { Icon } from "leaflet";

//TODO: useEffect mit leerem Array und dann von OSM die Koordinaten aller Eckpunkte der Hauswände holen

function SecondStep({setStep, coords, selectedMarkers, setSelectedMarkers}: {setStep: Function, coords: string[], selectedMarkers: string[][], setSelectedMarkers: Function}) {
    const [markers, setMarkers] = useState([]);
    const [errorMessage, setErrorMessage] = useState("");
    
    const customIcon = new Icon({
        iconUrl: "https://uxwing.com/wp-content/themes/uxwing/download/signs-and-symbols/red-circle-icon.png",
        iconSize: [18, 18]
    });

    const customIconClicked = new Icon({
        iconUrl: "https://uxwing.com/wp-content/themes/uxwing/download/signs-and-symbols/green-circle-icon.png",
        iconSize: [18, 18]
    });


    useEffect(() => {
        (async () => {
            const response = await fetch("http://localhost:8080/api/address/nearbynodes", {
                method: "POST",
                headers: {
                    "Accept": "application/json",
                    "Content-Type": "application/json"                  
                },
                body: JSON.stringify({"lat": coords[0], "lon": coords[1]})           
            });
            const data = await response.json();
            setMarkers(data.nodes);
        })();
    }, []);

    const markersValid = selectedMarkers.length === 2;

    return (
        <div className="flex flex-col items-center">
            <h1>Second Step, define which Hauswand you fotografiert hast</h1>
            <div className="flex flex-row items-center space-x-6">
                <MapContainer center={[Number(coords[0]), Number(coords[1])]} zoom={20} style={{height: "600px", width: "800px"}}>
                <TileLayer attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors' maxNativeZoom={19} maxZoom={23} url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"/>
                {markers.map((marker: any, index: number) => {
                    return <Marker position={marker.geocode} key={index} icon={selectedMarkers.includes(marker.geocode) ? customIconClicked : customIcon} eventHandlers={{
                        click: (e) => {
                            if(selectedMarkers.includes(marker.geocode)) { //marker selected
                                setSelectedMarkers(selectedMarkers.filter((item) => item.toString() !== marker.geocode.toString())); //remove marker from selectedMarkers
                            } else { //marker not selected
                                if(selectedMarkers.length < 2) { //less than 2 markers selected
                                    setSelectedMarkers([...selectedMarkers, marker.geocode]); //add marker to selectedMarkers
                                } else { //2 markers selected
                                    setErrorMessage("You can only select 2 markers");
                                    const timer = setTimeout(() => {
                                        setErrorMessage("");
                                    }, 3000);
                                }
                            }
                        }  
                    }}></Marker>
                })
                }

                </MapContainer>
            </div>
            {errorMessage != "" ? <p>{errorMessage}</p> : ""}
            <div className="flex gap-4">
                {markersValid ?
                <button className="relative flex h-[50px] w-40 items-center justify-center overflow-hidden bg-gray-800 text-white shadow-2xl transition-all before:absolute before:h-0 before:w-0 before:rounded-full before:bg-orange-600 before:duration-500 before:ease-out hover:shadow-orange-600 hover:before:h-56 hover:before:w-56" onClick={() => { setStep(3)}}>
                <span className="relative z-10">Finalise Markers</span>
                </button>
                : <button disabled={true} className="relative flex h-[50px] w-40 items-center justify-center overflow-hidden bg-gray-400 cursor-not-allowed opacity-60 shadow-2xl" onClick={() => { setStep(3)}}>
                <span className="relative z-10">Finalise Markers</span>
                </button>
                }
                
            </div>
        </div>
    );
}

export default SecondStep;