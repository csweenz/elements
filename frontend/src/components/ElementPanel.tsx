import "./element-panel.css";
import type { ElementDetails } from "../api";

type Props = {
  open: boolean;
  loading?: boolean;
  error?: string | null;
  data?: ElementDetails | null;
  onClose: () => void;
};

export default function ElementPanel({ open, loading, error, data, onClose }: Props) {
  if (!open) return null;

  // Close on ESC
  function onKeyDown(e: React.KeyboardEvent<HTMLDivElement>) {
    if (e.key === "Escape") onClose();
  }

  const ts = data?.last_ts ? new Date(data.last_ts).toLocaleString() : "—";

  return (
    <div className="elpanel-overlay" onClick={onClose} role="presentation">
      <div
        className="elpanel"
        role="dialog"
        aria-modal="true"
        aria-labelledby="elpanel-title"
        onClick={(e) => e.stopPropagation()}
        onKeyDown={onKeyDown}
        tabIndex={-1}
      >
        <button className="elpanel-close" onClick={onClose} aria-label="Close">×</button>

        {loading ? (
          <div className="elpanel-body"><p>Loading…</p></div>
        ) : error ? (
          <div className="elpanel-body error"><p>{error}</p></div>
        ) : data ? (
          <div className="elpanel-body">
            <h2 id="elpanel-title">
              {data.name} <span className="muted">({data.symbol})</span>
            </h2>
            <dl className="kv">
              <dt>Atomic #</dt><dd>{data.atomic_number}</dd>
              <dt>Last timestamp</dt><dd>{ts}</dd>
            </dl>
          </div>
        ) : (
          <div className="elpanel-body"><p>No data.</p></div>
        )}
      </div>
    </div>
  );
}
