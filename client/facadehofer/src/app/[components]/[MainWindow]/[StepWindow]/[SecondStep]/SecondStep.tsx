"use client";
import {useEffect, useState} from "react";
import { MapContainer , TileLayer , Marker } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import { Icon } from "leaflet";

//TODO: useEffect mit leerem Array und dann von OSM die Koordinaten aller Eckpunkte der Hauswände holen

function SecondStep({setStep, coords}: {setStep: Function, coords: string[]}) {
    const [markers, setMarkers] = useState([]);
    
    const customIcon = new Icon({
        iconUrl: "https://cdn-icons-png.flaticon.com/512/107/107831.png",
        iconSize: [38,38]
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
            console.log(data.nodes);
            setMarkers(data.nodes);
        })();
    }, []);

    
    


    return (
        <div className="flex flex-col justify-center items-center">
            <h1>Second Step, define which Hauswand you fotografiert hast</h1>
            <div className="flex flex-row items-center space-x-6 h-screen">
                <MapContainer center={[Number(coords[0]), Number(coords[1])]} zoom={20} style={{height: "800px", width: "800px"}}>
                <TileLayer attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors' maxNativeZoom={19} maxZoom={23} url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"/>
                {markers.map((marker: any) => (
                    <Marker position={marker.geocode}></Marker>
                ))
                }

                </MapContainer>
            </div>
            <div className="flex gap-4">
                <button className="relative flex h-[50px] w-40 items-center justify-center overflow-hidden bg-gray-800 text-white shadow-2xl transition-all before:absolute before:h-0 before:w-0 before:rounded-full before:bg-orange-600 before:duration-500 before:ease-out hover:shadow-orange-600 hover:before:h-56 hover:before:w-56" onClick={() => { setStep(3)}}>
                <span className="relative z-10">Next Step</span>
                </button>
            </div>
        </div>
    );
}

export default SecondStep;