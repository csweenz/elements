import { useState } from "react";
import PeriodicTable from "./components/PeriodicTable";
import type { ElementData } from "./data/elements";
import { getElementData, type ElementDetails } from "./api";
import ElementPanel from "./components/ElementPanel";

export default function App() {
  const [picked, setPicked] = useState<string[]>([]);
  const [panelOpen, setPanelOpen] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [details, setDetails] = useState<ElementDetails | null>(null);

  const handlePick = async (el: ElementData) => {
    // TODO toggle highlight in the grid
    setPicked(prev =>
      prev.includes(el.symbol) ? prev.filter(s => s !== el.symbol) : [...prev, el.symbol]
    );

    // open panel and fetch details
    setPanelOpen(true);
    setLoading(true);
    setError(null);
    try {
      const res = await getElementData(el.symbol);
      setDetails(res);
    } catch (e: any) {
      setError(e?.message ?? "Failed to load");
      setDetails(null);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main>
      <div id="mainscreendiv">
        <h1>Demo: Periodic Table</h1>
        <PeriodicTable onElementClick={handlePick} selectedSymbols={picked} />
      </div>

      <ElementPanel
        open={panelOpen}
        loading={loading}
        error={error}
        data={details}
        onClose={() => setPanelOpen(false)}
      />
    </main>
  );
}