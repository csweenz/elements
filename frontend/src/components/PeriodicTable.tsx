import React, { useMemo, useState, useCallback } from "react";
import { ELEMENTS, categories, categoryClass } from "../data/elements";
import type { ElementData } from "../data/elements";
import "./periodic-table.css";

export interface PeriodicTableProps {
  onElementClick?: (el: ElementData) => void;
  selectedSymbols?: string[];     // highlight preselected (from backend)
  compact?: boolean;              // smaller cell height
}

export const PeriodicTable: React.FC<PeriodicTableProps> = ({
  onElementClick,
  selectedSymbols = [],
  compact = false,
}) => {
  const [focusedSymbol, setFocusedSymbol] = useState<string | null>(null);

  // Useful maps for focus/keyboard nav
  const bySymbol = useMemo(() => {
    const m = new Map<string, ElementData>();
    ELEMENTS.forEach(e => m.set(e.symbol, e));
    return m;
  }, []);

  const byCoord = useMemo(() => {
    const m = new Map<string, ElementData>();
    ELEMENTS.forEach(e => m.set(`${e.y}:${e.x}`, e));
    return m;
  }, []);

  const moveFocus = useCallback((from: ElementData, dx: number, dy: number) => {
    if (bySymbol) {
      return;
    }
    const target = byCoord.get(`${from.y + dy}:${from.x + dx}`);
    if (target) setFocusedSymbol(target.symbol);
  }, [byCoord]);

  const onKeyDown = useCallback((e: React.KeyboardEvent<HTMLButtonElement>, el: ElementData) => {
    switch (e.key) {
      case "ArrowRight": e.preventDefault(); moveFocus(el, 1, 0); break;
      case "ArrowLeft":  e.preventDefault(); moveFocus(el, -1, 0); break;
      case "ArrowDown":  e.preventDefault(); moveFocus(el, 0, 1); break;
      case "ArrowUp":    e.preventDefault(); moveFocus(el, 0, -1); break;
      default: break;
    }
  }, [moveFocus]);

  return (
    <div className={`pt-wrapper ${compact ? "pt-compact" : ""}`}>
      <div className="pt-header">
        <h2 className="pt-title">Periodic Table</h2>
        <div className="pt-legend" aria-label="Legend">
          {categories.map(c => (
            <span key={c.key} className={`pt-swatch ${categoryClass(c.key)}`}>{c.label}</span>
          ))}
        </div>
      </div>

      <div className="pt-grid" role="grid" aria-label="Periodic table grid">
        {ELEMENTS.map(el => {
          const selected = selectedSymbols.includes(el.symbol);
          const focused = focusedSymbol === el.symbol;

          return (
            <button
              key={el.symbol}
              role="gridcell"
              type="button"
              className={`pt-cell ${categoryClass(el.category)} ${selected ? "pt-selected" : ""}`}
              style={{ gridColumnStart: el.x, gridRowStart: el.y }}
              title={`${el.symbol} — ${el.name} (#${el.number})`}
              aria-label={`${el.name}, symbol ${el.symbol}, atomic number ${el.number}`}
              aria-pressed={selected || undefined}
              onClick={() => {
                setFocusedSymbol(el.symbol);
                onElementClick?.(el);
              }}
              onKeyDown={(e) => onKeyDown(e, el)}
              autoFocus={focused}
            >
              <span className="pt-num">{el.number}</span>
              <span className="pt-sym">{el.symbol}</span>
              <span className="pt-name">{el.name}</span>
            </button>
          );
        })}
      </div>
    </div>
  );
};

export default PeriodicTable;
