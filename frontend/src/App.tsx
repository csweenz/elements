import { useState } from "react";
import PeriodicTable from "./components/PeriodicTable";
import type { ElementData } from "./data/elements";

function App() {
  const [picked, setPicked] = useState<string[]>([]);

  const handlePick = async (el: ElementData) => {
    setPicked(prev =>
      prev.includes(el.symbol) ? prev.filter(s => s !== el.symbol) : [...prev, el.symbol]
    );

    //ping Django for testing
    try {
      const res = await fetch(`/api/elements/${el.symbol}`);
       const json = await res.json();
       console.log("Backend says:", json);
    } catch (e) {
      console.error(e);
    }
  };

  return (
    <main><div id="mainscreendiv">
      <h1>Demo: Periodic Table</h1>
      <PeriodicTable onElementClick={handlePick} selectedSymbols={picked} />
    </div></main>
  );
}

export default App;
