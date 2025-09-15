import { useState } from "react";
import PeriodicTable from "./components/PeriodicTable";
import type { ElementData } from "./data/elements";
import { getElementData } from "./api";

function App() {
  const [picked, setPicked] = useState<string[]>([]);

  const handlePick = async (el: ElementData) => {
    setPicked(prev =>
      prev.includes(el.symbol) ? prev.filter(s => s !== el.symbol) : [...prev, el.symbol]
    );

    // Fetch element data from Django backend
    try {
      const res = await getElementData(el.symbol);
      console.log("Backend says:", res);
    } catch (e) {
      console.error(e);
    }
  };

  return (
    <main>
      <div id="mainscreendiv">
        <h1>Demo: Periodic Table</h1>
        <PeriodicTable onElementClick={handlePick} selectedSymbols={picked} />
      </div>
    </main>
  );
}

export default App;